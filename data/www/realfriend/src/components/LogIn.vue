<template>
  <div>
    <h2>{{resultid}}</h2>
    <h2>{{resultpass}}</h2>
    <p>
      <input type="text" id="userId" value="" placeholder="ユーザID"></p>
    <p>
      <input type="text" id="userPassword" value="" placeholder="パスワード"></p>
    <button v-on:click="dataConfirmation">サインイン</button>
    <button v-on:click="deleteData">取り消し</button>
    <h1>{{msg}}</h1>


    <div id="list">
      <ul v-for=" list in getApiArray">
        <div id=textmsg>
          {{list.Msg}}
        </div>
      </ul>
    </div>
  </div>


</template>

<script>
  export default {
    name: "LogIn",
    data() {
      return {
        msg: '入力してください',
        resultid: '', /*エラーコメント表示用*/
        resultpass: '',　/*エラーコメント表示用*/
        userid: null,
        userpass: null,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
      }
    },
    methods: {
      dataConfirmation: function () {

        /*初期化*/
        this.msg = ''
        this.resultuser = ''
        this.resultid = ''
        this.resultpass = ''
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
      deleteData: function () {
        document.getElementById("userId").value = ''
        document.getElementById("userPassword").value = ''
        this.message = '入力してください'

      },
      login() {
        let me = this
        this.axios.post(this.apiUrl, {
          user_id: String(this.userid),
          user_pass: String(this.userpass)
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            console.log(response)
            for (let getcount = 0; getcount < response.data.friends.length; getcount++) {
              me.getApiArray.push({Msg: response.data.friends[getcount]})
            }
            me.upLoad()
          } else {
            console.log(response)
            me.msg = response.data.error
          }
        }).catch(function (error) {
          console.log()
          console.log(error)
        })
      },
      /*データ受け渡ししたいけど。。。*/
      upLoad() {
        this.$router.push({path: '/'})
        //this.$router.replace({ path: '/a', props: { id: this.userid }})
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
</style>
