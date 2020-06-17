<template>
  <div class="camera">
    <h2>カメラ機能テスト</h2>
    <button v-on:click="testAxios">TEST</button>
    <div>
      <video ref="video" id="video" width="500" height="500" autoplay></video>
      <div>
        <button color="info" id="snap" v-on:click="capture">Snap Photo</button>
      </div>
      <canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
      <ul>
        <li class="capture" v-for="c in captures" v-bind:key="c.d">
          <img v-bind:src="c" height="50">
        </li>
      </ul>
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
                captures: [],
                postUrl: 'https://discordapp.com/api/webhooks/719394613278015548/qVo2SWvbtzDWUG-XgTs25Oz1GNHlp8QRYLSH3Uh6LOBIRn2VaMjxN7q7Dj_EblvnkPgS'
                // audioData: [],
                // localMediaStream: null,
                // localScriptProcessor: null
            }
        },
        mounted() {
            this.video = this.$refs.video
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({audio: true, video: true}).then(stream => {
                    this.video.srcObject = stream
                    this.video.play()

                })
            }
        },
        destroyed() {

        },
        methods: {
            testAxios() {
                console.log(this.captures)
                this.axios.post(this.postUrl, {
                    content: 'aa'
                    // images: this.capture()
                }).then(function (response) {
                    console.log(response)

                }).catch(function (error) {
                    console.log(error)
                })
            },
            capture() {
                this.canvas = this.$refs.canvas
                this.canvas.getContext("2d").drawImage(this.video, 0, 0, 640, 480)
                this.captures.push(this.canvas.toDataURL("image/jpeg"))
                console.log(this.captures)
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
