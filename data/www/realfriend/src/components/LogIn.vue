<template>
  <div>
    <!-- アカウント登録の時-->
    <SignUp ref="signup" @change="logInPage"></SignUp>
    <!-- ログインの時　-->
    <h1>{{changmsg}}</h1> <!-- 成功メッセージ　-->
    <p>
      <msg1>ユーザーIDを入力してください</msg1>
      <msg2>※必須</msg2>
      <br>
      <input type="text" id="userId" value="" placeholder="ユーザID"></p>
    <h2>{{resultid}}</h2>
    <p>
      <msg1>パスワードを入力してください</msg1>
      <msg2>※必須</msg2>
      <br>
      <input type="password" id="userPassword" value="" placeholder="パスワード"></p>
    <h2>{{resultpass}}</h2>

    <button v-on:click="dataCheck">サインイン</button>
    <button v-on:click="dataDelete">取り消し</button>
    <button v-on:click="addAccountPage">アカウント新規登録</button>


    <!-- 配列受け取り確認よう
        <div id="list">
          <ul v-for=" list in getApiArray">
            <div id=textmsg>
              {{list.Msg}}
            </div>
          </ul>
        </div>
        -->
  </div>


</template>

<script>
  import SignUp from "@/components/SignUp";

  export default {
    name: "LogIn",
    components: {
      SignUp:SignUp,
    },
    data() {
      return {
        changemsg: '',      /*登録成功メッセージ表示用*/
        resultid: '',       /*エラーコメント表示用*/
        resultpass: '',     /*エラーコメント表示用*/
        userid: null,       /*ユーザID受け取り用*/
        userpass: null,     /*ユーザパス受け取り用*/
        accountaad: false,  /*画面切り替えよう*/
        getApiArray:[],
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
        this.getApiArray = []

        /*テキストボックスから受け取り*/
        this.userid = document.getElementById("userId").value
        this.userpass = document.getElementById("userPassword").value

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
        document.getElementById("userId").value = ''
        document.getElementById("userPassword").value = ''
        this.message = '入力してください'

      },
      login() {
        let me = this

        this.axios.post(this.apiUrl, {
          user_id: String(this.userid),
          user_pass: String(this.userpass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            for (let getcount = 0; getcount < response.data.friends.length; getcount++) {
              me.getApiArray.push({Msg: response.data.friends[getcount]})
            }
            console.log(response)
            me.upLoad()
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },

      /*データ受け渡ししたいけど。。。*/
      upLoad() {
        /*今はルーティングでメイン画面*/
        this.$emit('changeuser', {id:this.userid , ary:this.getApiArray})
        //this.$router.replace({ path: '/a', props: { id: this.userid }})
      },
      /*画面切り替え　SignUpから触る*/
      logInPage(msg) {
        this.accountaad = false
        this.changmsg = msg
      },
      /*画面切り替え　LogInから触る*/
      addAccountPage() {
        this.$refs.signup.openModal()
        this.accountaad = true
      }

    },
    updated() {

    }
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
