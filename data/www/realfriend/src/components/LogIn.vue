<template>
  <div>
    <!-- アカウント登録の時-->
    <SignUp ref="signup" @change="logInPage"></SignUp>
    <!-- ログインの時　-->
    <h1>{{changmsg}}</h1> <!-- 成功メッセージ　-->
    <form>
      <p>
        <msg1>ユーザーIDを入力してください</msg1>
        <msg2>※必須</msg2>
        <br>
        <input type="text" ref="userThisId" value="" placeholder="ユーザID" required="required"></p>
      <h2>{{resultid}}</h2>
      <p>
        <msg1>パスワードを入力してください</msg1>
        <msg2>※必須</msg2>
        <br>
        <input type="password" ref="userThisPass" value="" placeholder="パスワード" required="required"></p>
      <h2>{{resultpass}}</h2>

      <button v-on:click="dataCheck">サインイン</button>
      <button v-on:click="dataDelete">取り消し</button>
    </form>
    <br>
    <button v-on:click="addAccountPage">アカウント新規登録</button>

  </div>


</template>

<script>
  import SignUp from "@/components/SignUp";

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
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
      }
    },
    methods: {
      dataCheck: function () {
        /*初期化*/
        this.resultuser = ''
        this.resultid = ''
        this.resultpass = ''
        this.changmsg = ''

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
      dataDelete: function () {
        this.$refs.userThisId.value = ''
        this.$refs.userThisPass.value = ''
        this.resultid = ''
        this.resultpass = ''
        this.message = '入力してください'

      },
      login() {
        let me = this
        this.axios.post(this.apiUrl, {
          user_id: String(this.userid),
          user_pass: String(this.userpass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            me.upLoad()
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },

      upLoad() {
        this.$router.replace({path: '/', query: {id: this.userid}})
      },
      /*SignUpのモーダルを開く*/
      addAccountPage() {
        this.$refs.signup.openModal()
        this.accountaad = true
      }

    },
  }
</script>

<style scoped>
  h2 {
    color: red;
  }

  msg2 {
    color: red;
  }
</style>

