<template>
  <div>
    {{message}}
    <!-- アカウント登録の時-->
    <SignUp ref="signUp"></SignUp>
    <!-- ログインの時　-->
      <p>
        <msg1>ユーザーIDを入力してください</msg1>
        <msg2>※必須</msg2>
        <br>
        <input type="text" ref="userThisId" placeholder="ユーザID" ></p>
      <h2>{{resultId}}</h2>
      <p>
        <msg1>パスワードを入力してください</msg1>
        <msg2>※必須</msg2>
        <br>
        <input type="password" ref="userThisPass" placeholder="パスワード" ></p>
      <h2>{{resultPass}}</h2>

      <button v-on:click="dataCheck">サインイン</button>

    <br>
    <button v-on:click="addAccountPage">アカウント新規登録</button>

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
        resultId: '',       /*エラーコメント表示用*/
        resultPass: '',     /*エラーコメント表示用*/
        userId: '',       /*ユーザID受け取り用*/
        userPass: null,     /*ユーザパス受け取り用*/
        message: '',
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
      }
    },
    methods: {
      dataCheck: function () {
        /*初期化*/
        this.resultId = ''
        this.resultPass = ''
        this.message = ''

        /*受け取り*/
        this.userId = this.$refs.userThisId.value
        this.userPass = this.$refs.userThisPass.value

        /*正規表現パターン
        let paternid = new RegExp(/^([a-zA-Z0-9]{1,7})$/)
        let paternpass = new RegExp(/^([a-zA-Z0-9]{1,30})$/)*/

        /*if 内のコメントアウトは基本的に正規表現*/
        /*現在は入っているかだけの確認*/
        if (this.userId == ''　/*false == paternid.test(this.userid)*/) {
          this.resultId = "入力してください"
          if (this.userPass == ''　/*false == paternpass.test(this.userpass)*/) {
            this.resultPass = "入力してください"
          }
        } else {
          if (this.userPass == ''/*false == paternpass.test(this.userpass)*/) {
            this.resultPass = "入力してください"
          } else {
            /*すべて入っている場合*/
            this.login()
          }
        }

      },
      login() {
        let me = this
        this.axios.post(this.apiUrl, {
          user_id: String(this.userId),
          user_pass: String(this.userPass),
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
        this.$router.push({name: 'Main', params: {userId: this.userId}})
      },
      /*SignUpのモーダルを開く*/
      addAccountPage() {
        this.$refs.signUp.openSignUpModal()
      }

    },
  }
</script>

<style scoped>
  h2 {
    color: red
  }

  msg2 {
    color: red
  }
</style>

