<template>

  <div class="user-change-success" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <ReturnMenu></ReturnMenu>
    <h2>認証ページ</h2>
    <div class="user-name-position">{{userName}}さん</div>
      <p>
        <msg1>パスワードを入力してください</msg1>
        <br>
        <input class="pass-position" type="password" ref="userThisPass" placeholder="パスワード" >
      </p>
      <div class="change-check-position" v-on:click="changeCheck">認証</div>
    <div class="errMsg-position">{{errMsg}}</div>
  </div>

</template>

<script>
  import http from "../../static/axios/axios"
  import ReturnMenu from "@/components/ReturnMenu"

  export default {
    name: "UserChangeSuccess",
    components: {ReturnMenu},
    data() {
      return {
        userId: '',
        userpass: '',
        userName: '',
        errMsg: '',
        successUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
        url: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
        backgroundImageSrc: require("@/assets/test1.png"),
      }
    },
    created() {
      http.get(this.url, {
        headers: {
          Authorization: this.$store.getters['token/tokenGet']
        }
      }).then((response) => {
        console.log(response.data)
        this.userName = response.data.user[1]
        this.userId = response.data.user[0]
      }).catch((error) => {
        console.log(error.response.status)
      })
    },
    methods: {
      changeCheck() {
        let me = this
        this.userPass = this.$refs.userThisPass.value
        if(this.userPass === ''){
          this.errMsg = '入力してください'
        }else {
          this.axios.post(this.successUrl, {
            user_id: String(this.userId),
            user_pass: String(this.userPass),
          }).then(function (response) {
            me.$store.dispatch('token/setToken',response.data.token)
            me.$router.push('/profile')
          }).catch(function (error) {
            me.errMsg = 'IDもしくはパスワードが間違っています'
            console.log(error)
          })
        }
      },
      // getUserApi() {
      //   let me = this
      //   this.axios.get(this.getUrl, {}).then(function (response) {
      //     if (response.data.isSuccess == true) {
      //       me.userName = response.data.user[1]
      //     } else {
      //       console.log(response.data.error)
      //     }
      //   }).catch(function (error) {
      //     console.log(error)
      //   })
      // },
    },

  }
</script>

<style scoped>
  h2{
    position: relative;
    top: 3vh;
  }
  msg1{
    font-size: 3vmin;
    position: relative;
    top: 20vh;
  }
  .user-change-success{
    height: 100vh;
    margin: 0 auto;
    background-size: 5%;
    animation: bgiLoop 8s linear infinite;
  }
  @keyframes bgiLoop {
    0% { background-position: 0 0;}
    100% { background-position: -15% 15%;}
  }
  .pass-position{
    position: relative;
    top: 25vh;
    font-size: 3vmin;
  }
  .change-check-position{
    position: relative;
    top: 50vh;
    font-size: 3vmin;
  }
  .errMsg-position{
    position: absolute;
  }
  .user-name-position{
    font-size: 3vmin;
    position: relative;
    top: 10vh;
  }
  .change-check-position:hover {
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
</style>
