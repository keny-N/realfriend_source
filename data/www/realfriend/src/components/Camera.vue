<template>
  <div class="camera">
    <!--    <button v-on:click="faceApi">POST送信</button>-->
    <!--    <button v-on:click="empath">empath送信</button>-->
    <div>
      <video ref="video" id="video" width="500" height="500" autoplay muted class="camerasize"></video>
      <canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
      <div>
        <button v-on:click="recStart">Start</button>
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
                chunks: [],
                localStream: null,
                mediaRecorder: null,
                timer: null,
                image: null,  //画像を保存しておく場所
                audio: null,
                msg: '',
                // player: this.$refs.player.src,
                postUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend_api/realfriend/emotionjudgement'
                // audioData: [],
                // localMediaStream: null,
                // localScriptProcessor: null
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
            faceApi() {
                var me = this
                //faceApiに顔データを送信
                console.log('POST送信します')
                this.axios.post(this.postUrl, {
                    images: String(this.image)
                }).then(function (response) {
                    if (response.data.error == 0) {
                        console.log(response)
                        me.msg = response.data.result
                    } else {
                        me.msg = "エラー"
                    }
                }).catch(function (error) {
                    console.log(error)
                    me.msg = "エラー"
                })
            },
            // empath(wav) {
            //     console.log("empath起動")
            //     this.axios.post('https://23gjh3gnd7.execute-api.ap-northeast-1.amazonaws.com/empath/mastuo_lamda_test', {
            //         wav: this.audio
            //     }).then(function (response) {
            //         console.log((response))
            //     }).catch(function (error) {
            //         console.log(error)
            //     })
            //
            // },
            capture() {
                //カメラが写っている範囲を指定し、その領域を画像として切り取る
                this.canvas = this.$refs.canvas
                this.canvas.getContext("2d").drawImage(this.video, 0, 0, 640, 480)
                this.image = this.canvas.toDataURL("image/jpeg")
                this.image = this.image.substr(23)
                console.log(this.image)
                //faceapiの返り値をmsgに代入
                this.faceApi()
                console.log(this.msg)
                //親コンポーネント(GameBodyのupdateMSGを実行する)
                this.$emit('updateMsg', this.msg)
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
                        this.mediaRecorder = new MediaRecorder(stream)
                        this.mediaRecorder.start()
                        // １秒間隔で画像を切り取る
                        this.timer = setInterval(this.capture, 5000)
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
                //カメラマイクをOFFにし、音声データを取得する
                this.mediaRecorder.stop()
                // this.mediaRecorder.addEventListener('dataavailable', e => {
                //
                //     this.chunks.push(e.data)
                //     this.$refs.player.src = URL.createObjectURL(e.data)
                //     this.$refs.download.href = URL.createObjectURL(e.data)
                //     this.$refs.download.download = 'matuo.wav'
                // })

                // this.mediaRecorder.ondataavailable = function (e) {
                //     document.getElementById('player').src = URL.createObjectURL(e.data);
                // }
                //撮影終了後指定のイメージを表示させる
                //6/18時点では未実装のちに背景等をだす
                // this.canvas.getContext("2d").drawImage(this.video, 0, 0, 640, 480)
                this.localStream.getTracks().forEach(track => track.stop())
            }
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
  .camerasize{
    width: 100%;
  }
</style>
