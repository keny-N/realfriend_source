<template>
  <div class="camera">
    <!--    <button v-on:click="faceApi">POST送信</button>-->
    <!--    <button v-on:click="empath">empath送信</button>-->
    <div>
      <video ref="video" id="video" width="500" height="500" autoplay muted class="camerasize"></video>
      <canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
      <div>
        <button v-on:click="recStart">Start</button>
        <button ref="stop" v-on:click="recStop">Stop</button>
      </div>
    </div>
  </div>
</template>

<script>


    export default {
        name: "camera",
        data() {
            return {
                video: {},
                canvas: {},
                // chunks: [],
                localStream: null,
                // mediaRecorder: null,
                timer: null,
                image: null,  //画像を保存しておく場所
                msg: '',      //APIからの返り値をメッセージとして保存する
                audio_sample_rate: 11025,
                audio_sample_rate_old: null,
                scriptProcessor: null,
                audioContext: null,
                audioData: [],
                bufferSize: 1024,
                wav: null,
                postUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/emotionjudgement'
            }
        },
        mounted() {
            //マウント後に起動
        },
        destroyed() {
            //インスタンス削除時に実行
            //Webカメラマイクの停止
            this.localStream.getTracks().forEach(track => track.stop())
        },
        methods: {
            emotionJudgement() {
                let me = this
                //faceApiに顔データを送信
                console.log('POST送信します')
                console.log(this.image)
                console.log(this.wav)
                this.axios.post(this.postUrl, {
                    image: String(this.image),
                    voice: this.wav
                }).then(function (response) {
                    if (response.data.isSuccess) {
                        console.log(response)
                        me.msg = response.data.result
                    } else {
                        me.msg = response.data.result
                        console.log(response)
                    }
                }).catch(function (error) {
                    console.log(error)
                    me.msg = "catch_error"
                })
            },
            empath(wav) {
                console.log("empath起動")
                console.log(wav)
                this.axios.post('https://23gjh3gnd7.execute-api.ap-northeast-1.amazonaws.com/empath/mastuo_lamda_test', {
                    wav: String(wav)
                }).then(function (response) {
                    console.log(response)
                }).catch(function (error) {
                    console.log(error)
                })

            },
            capture() {
                //カメラが写っている範囲を指定し、その領域を画像として切り取る
                this.canvas = this.$refs.canvas
                this.canvas.getContext("2d").drawImage(this.video, 0, 0, 640, 480)

                //画像データをbase64にエンコード
                this.image = this.canvas.toDataURL("image/jpeg")
                this.image = this.image.substr(23)


                this.exportWAV()

                //感情測定APIを実行[empath|faceapi]
                this.emotionJudgement()


                //親コンポーネント(GameBodyのupdateMSGを実行する)
                this.$emit('updateMsg', this.msg)
            },
            // saveAudio() {
            //     // this.$refs.download.href =
            //     this.exportWAV()
            //     // this.$refs.download.download = 'test.wav'
            //     this.audioContext.close().then(function () {
            //         // this.stopButton.setAttribute('disabled', 'disabled')
            //     })
            // },
            exportWAV() {
                let me = this

                let encodeWAV = function (samples, sampleRate) {
                    let buffer = new ArrayBuffer(44 + samples.length * 2)
                    let view = new DataView(buffer)

                    let writeString = function (view, offset, string) {
                        for (let i = 0; i < string.length; i++) {
                            view.setUint8(offset + i, string.charCodeAt(i))
                        }
                    }

                    let floatTo16BitPCM = function (output, offset, input) {
                        for (let i = 0; i < input.length; i++, offset += 2) {
                            let s = Math.max(-1, Math.min(1, input[i]))
                            output.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7fff, true)
                        }
                    }

                    writeString(view, 0, 'RIFF') // RIFFヘッダ
                    view.setUint32(4, 32 + samples.length * 2, true) // これ以降のファイルサイズ
                    writeString(view, 8, 'WAVE') // WAVEヘッダ
                    writeString(view, 12, 'fmt ') // fmtチャンク
                    view.setUint32(16, 16, true) // fmtチャンクのバイト数
                    view.setUint16(20, 1, true) // フォーマットID
                    view.setUint16(22, 1, true) // チャンネル数
                    view.setUint32(24, sampleRate, true) // サンプリングレート
                    view.setUint32(28, sampleRate * 2, true) // データ速度
                    view.setUint16(32, 2, true) // ブロックサイズ
                    view.setUint16(34, 16, true) // サンプルあたりのビット数
                    writeString(view, 36, 'data')// dataチャンク
                    view.setUint32(40, samples.length * 2, true) // 波形データのバイト数
                    floatTo16BitPCM(view, 44, samples) // 波形データ


                    return view
                }

                let mergeBuffers = function (audioData) {
                    let sampleLength = 0
                    for (let i = 0; i < audioData.length; i++) {
                        sampleLength += audioData[i].length
                    }
                    let samples = new Float32Array(sampleLength)
                    let sampleIdx = 0
                    for (let i = 0; i < audioData.length; i++) {
                        for (let j = 0; j < audioData[i].length; j++) {
                            samples[sampleIdx] = audioData[i][j]
                            sampleIdx++
                        }
                    }

                    return samples
                }

                let dataview = encodeWAV(mergeBuffers(this.audioData), this.audio_sample_rate)
                let audioBlob = new Blob([dataview], {type: 'audio/wav'})
                console.log(dataview)
                console.log(audioBlob)
                let reader = new FileReader()
                reader.readAsDataURL(audioBlob)

                reader.onload = function () {
                    me.wav = reader.result.substr(22)
                }

                this.audioData = []
                // let myURL = window.URL || window.webkitURL
                // let url = myURL.createObjectURL(audioBlob)
                // return url
            },
            onAudioProcess(e) {
                //オーディオ入力
                let input = e.inputBuffer.getChannelData(0)

                input = this.interpolateArray(input, input.length * (this.audio_sample_rate / this.audio_sample_rate_old))
                this.bufferSize = input.length * (this.audio_sample_rate / this.audio_sample_rate_old) * 3

                let bufferData = new Float32Array(this.bufferSize)
                for (let i = 0; i < this.bufferSize; i++) {
                    bufferData[i] = input[i]
                }
                this.audioData.push(bufferData)
            },
            interpolateArray(data, fitCount) {
                let linearInterpolate = function (before, after, atPoint) {
                    return before + (after - before) * atPoint
                }
                let newData = new Array()
                let springFactor = new Number((data.length - 1) / (fitCount - 1))
                newData[0] = data[0] // for new allocation
                for (let i = 1; i < fitCount - 1; i++) {
                    let tmp = i * springFactor
                    let before = new Number(Math.floor(tmp)).toFixed()
                    let after = new Number(Math.ceil(tmp)).toFixed()
                    let atPoint = tmp - before
                    newData[i] = linearInterpolate(data[before], data[after], atPoint)
                }
                newData[fitCount - 1] = data[data.length - 1] // for new allocation
                return newData
            },
            recStart() {
                //カメラマイクをONにし、録音を始める
                this.video = this.$refs.video
                if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                    navigator.mediaDevices.getUserMedia({audio: true, video: true}).then(stream => {
                        //カメラを起動させる
                        this.video.srcObject = stream
                        this.video.play()
                        //マイクを起動させる
                        this.localStream = stream
                        this.audioContext = new AudioContext()
                        this.audio_sample_rate_old = this.audioContext.sampleRate
                        this.scriptProcessor = this.audioContext.createScriptProcessor(this.bufferSize, 1, 1)
                        let mediastreamsource = this.audioContext.createMediaStreamSource(stream)
                        mediastreamsource.connect(this.scriptProcessor)
                        this.scriptProcessor.onaudioprocess = this.onAudioProcess
                        // １秒間隔で画像を切り取る
                        this.timer = setInterval(this.capture, 4900)
                        this.scriptProcessor.connect(this.audioContext.destination)
                        console.log('record start?')

                        //１０秒後に録音を停止する
                        setTimeout(this.recStop, 10000)
                    })
                } else {
                    console.log("getUserMedia not support")
                }
            },
            recStop() {
                //画像を切り取る処理を停止させる
                clearInterval(this.timer)
                console.log('saved wav')
                this.localStream.getTracks().forEach(track => track.stop())
            },

        }
    }
</script>

<style scoped>
  #video {
    background-color: #000000;
  }

  #canvas {
    display: none;
  }

  li {
    display: inline;
    padding: 5px;
  }

  .camerasize {
    width: 100%;
  }

</style>
