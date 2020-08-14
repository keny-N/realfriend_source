<template>
  <div class="login" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    {{message}}
    <!-- アカウント登録の時-->
    <SignUp ref="signup"></SignUp>
    <!-- ログインの時　-->
    <div class="input-text1">
    <h1>{{changmsg}}</h1> <!-- 成功メッセージ　-->
    <form>
      <p>
        <msg1>ユーザーIDを入力してください</msg1>
        <msg2>※必須</msg2>
        <br>
        <input  type="text" ref="userThisId" placeholder="ユーザID" required="required"></p>
      <h2>{{resultid}}</h2>
      <p>
        <msg1>パスワードを入力してください</msg1>
        <msg2>※必須</msg2>
        <br>
        <input type="password" ref="userThisPass" placeholder="パスワード" required="required"></p>
      <h2>{{resultpass}}</h2>

      <msg3 class="sign-button" v-on:click="dataCheck">sign in</msg3>
    </form>
    <br>
    <msg3 class="account-button" v-on:click="addAccountPage">sign up</msg3>
    </div>
  </div>


</template>

<script>
  import SignUp from "@/components/SignUp"

  export default {
    name: "LogIn",
    components: {
      SignUp: SignUp,
    },
    data() {
      return {
        resultid: '',       /*エラーコメント表示用*/
        resultpass: '',     /*エラーコメント表示用*/
        userid: '',       /*ユーザID受け取り用*/
        userpass: null,     /*ユーザパス受け取り用*/
        message:'',
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
        backgroundImageSrc: require("@/assets/op.png"),
      }
    },
    methods: {
      dataCheck: function () {
        /*初期化*/
        this.resultuser = ''
        this.resultid = ''
        this.resultpass = ''
        this.changmsg = ''
        this.message='',

        /*受け取り*/
        this.userid = this.$refs.userThisId.value
        this.userpass = this.$refs.userThisPass.value


        /*正規表現パターン
        let paternid = new RegExp(/^([a-zA-Z0-9]{1,7})$/)
        let paternpass = new RegExp(/^([a-zA-Z0-9]{1,30})$/)*/

        /*if 内のコメントアウトは基本的に正規表現*/
        /*現在は入っているかだけの確認*/
        if (this.userid == ''　/*false == paternid.test(this.userid)*/) {
          this.resultid = "ユーザidが不正"
          if (this.userpass == ''　/*false == paternpass.test(this.userpass)*/) {
            this.resultpass = "ユーザpassが不正"
          }
        } else {
          if (this.userpass == ''/*false == paternpass.test(this.userpass)*/) {
            this.resultpass = "ユーザpassが不正"
          } else {
            /*すべて入っている場合*/
            this.login()
          }
        }

      },
      login() {
        let me = this
        this.axios.post(this.apiUrl, {
          user_id: String(this.userid),
          user_pass: String(this.userpass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            me.loginSuccess()
          } else {
            me.message = 'IDもしくはパスワードが間違っています'
          }
        }).catch(function (error) {
          console.log(error)
        })
      },

      loginSuccess() {
        this.$router.replace({path: '/', query: {id: this.userid}})
      },
      /*SignUpのモーダルを開く*/
      addAccountPage() {
        this.$refs.signup.openSignUpModal()
      }

    },
  }
</script>

<style scoped>
  h2 {
    color: red;
    font-size:2.5vmin;
  }

  msg2 {
    color: red;
    line-height: 7;
    margin-top: 7px;
    margin-bottom: 5px;
  }
  msg1{
    line-height: 7;
    margin-top: 7px;
    margin-bottom: 5px;
  }
  msg3{
    line-height: 3;
    margin-top: 7px;
    margin-bottom: 5px;
  }
  .login{
    background: no-repeat center;
    background-size: cover;
    /*mainのサイズをちょうど画面と同じにする。*/
    height: 100vh;
  }
  .input-text1{
    box-sizing: content-box;
    position: absolute;
    right:5%;
    /*小さくした場合にはみ出すので現在は大きい画面の対しての配置をイメージしている*/
    top:15%;
    font-size:2.5vmin;
  }

</style>

