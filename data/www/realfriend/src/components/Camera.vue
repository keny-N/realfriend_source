<template>
  <div class="camera">
    <h2>カメラ機能テスト</h2>
    <button v-on:click="faceApi">POST送信</button>
    <div>
      <video ref="video" id="video" width="500" height="500" autoplay muted></video>
      <canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
      <div>
        <button v-on:click="recStart">Start</button>
      </div>
      <div>
        <button color="info" id="snap" v-on:click="capture">シーン切り取り</button>
      </div>
      <!--      <ul>-->
      <!--        <li class="capture" v-for="c in captures" v-bind:key="c.d">-->
      <!--          <img v-bind:src="c" height="50">-->
      <!--        </li>-->
      <!--      </ul>-->
      <!--      <audio id="player" controls></audio>-->
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
                captures: [],   //画像を保存しておく
                // chunks: [],
                localStream: null,
                mediaRecorder: null,
                timer: null,
                image: null,
                // player: this.$refs.player.src,
                postUrl: 'https://6ou7h94f7f.execute-api.ap-northeast-1.amazonaws.com/realfriend_api/realfriend/emotionjudgment'
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
                //faceApiに顔データを送信
                this.axios.post(this.postUrl, {
                    images: String(this.image)
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
                this.captures.push(this.canvas.toDataURL("image/jpeg").substr(23))
                console.log(this.captures)
                this.image = this.canvas.toDataURL("image/jpeg")
                // console.log(this.image)
                // console.log("aaa")
                this.image = this.image.substr(23)
                // console.log(this.image)
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

                        //１秒間隔で画像を切り取る
                        // this.timer = setInterval(this.capture, 1000)
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
                this.mediaRecorder.ondataavailable = function (e) {
                    // this.chunks.push(e.data)
                }
                console.log(this.chunks)
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
</style>
