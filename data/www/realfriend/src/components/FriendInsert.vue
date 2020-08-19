<template>
  <div class="friend-insert">
    <input type="image" src="/static/friendinset.png" class="image-size" v-on:click="openModal">
    <div class="overlay" v-show="showContent">
      <div class="content">
        <h4>フレンド登録</h4>
<!--        <div class="card-body">-->
<!--          <div class="trim">-->
<!--            <img v-bind:src="imageData" v-if="imageData">-->
<!--          </div>-->
<!--          <h4 class="card-title">画像を選んでください。</h4>-->
<!--          <input type="file" accept="image/*" @change="onImgRegister($event)">-->
<!--        </div>-->
        <div>フレンド名前：<input v-model="friendName"></div>
        <div class="float-left font-design float-left-position" v-on:click="registerFriend">REGISTER</div>
        <div class="float-right font-design float-right-position" v-on:click="closeModal">CANCEL</div>
      </div>
    </div>
  </div>
</template>

<script>
import http from "../../static/axios/axios"

export default {
  name: "FriendInsert",
  data() {
    return {
      showContent: false, //モーダルを非表示している
      imageData: '',//画像
      friendName: '',//フレンドの名前
      postUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one',//フレンド登録URL
    }
  },
  methods: {
    openModal: function () {
      this.showContent = true
    },
    closeModal: function () {
      this.showContent = false
    },
    onImgRegister(e) {
      const files = e.target.files

      if (files.length > 0) {
        const file = files[0]
        const reader = new FileReader()
        reader.onload = (e) => {
          this.imageData = e.target.result
        }
        reader.readAsDataURL(file)
      }
    },
    registerFriend() {
      //   ２０文字以内かつ一文字以上でない時に実行される。画像用の条件式も書かないと行けない
      // if (this.friendName.length > 20 || this.friendName.length < 1) {
      // }

      let name = this.friendName
      let me = this

      console.log('post送信します')

      http.interceptors.request.use(request => {
        request.headers.Authorization = this.$store.getters['token/tokenGet']
        return request
      })

      http.post(this.postUrl, {
        friend_name: name,
        //現在はパスが確定していないためパスっぽい文字を入れているだけです。
        friend_img: 'matuo/apex'
      }).then(function (response) {
        console.log(response)
        me.showContent = false
        //フレンド表示更新
        me.$store.dispatch('friend/flagSwitch')
      }).catch(function (error) {
        console.log(error)
        me.showContent = true
      })
      //メイン画面を更新する処理
      console.log('以下')
    },

  },
}
</script>

<style scoped>
.overlay {
  /*　要素を重ねた時の順番　*/
  z-index: 1;

  /*　画面全体を覆う設定　*/
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);

  /*　画面の中央に要素を表示させる設定　*/
  display: flex;
  align-items: center;
  justify-content: center;

}

  .content {
    z-index: 2;
    width: 50%;
    padding: 1em;
    background: #fec7d7;
    border-radius:30px;
  }
  .trim{
    height: 150px;  /* トリミングしたい高さ */
    overflow: hidden;
    position: relative;
  }
  .trim img {
    position: absolute;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
  }
  .float-right-position{
    position: relative;
    right: 10%;
  }
  .float-left-position{
    position: relative;
    left: 10%;
  }
  .image-size{
    width: 7vmin;
    position: fixed;
    right: 10%;
    bottom: 15%;
  }
  .font-design:hover {
    animation: shake 2s infinite;
  }
  @keyframes shake {
    0% {
      transform: translate(2px, 0px);
    }
    5% {
      transform: translate(-2px, 0px);
    }
    10% {
      transform: translate(2px, 0px);
    }
    15% {
      transform: translate(-2px, 0px);
    }
    20% {
      transform: translate(2px, 0px);
    }
    25% {
      transform: translate(-2px, 0px);
    }
    30% {
      transform: translate(0px, 0px);
    }
  }
  .font-design{
    font-family: Impact;
    color: white;
  }
</style>

