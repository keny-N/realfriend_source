<template>
  <div>
    <button v-on:click="dataConfirmation">サインイン</button>
    <button v-on:click="deleteData">取り消し</button>
    <p>
      <input type="text" id="userId" value="" placeholder="ユーザID"></p>
    <p>
      <input type="password" id="userPassword" value="" placeholder="パスワード"></p>
    <h1>{{message}}</h1>
    <h2>{{resultid}}</h2>
    <h2>{{resultpass}}</h2>
  </div>
</template>

<script>
  export default {
    name: "SignIn",
    data() {
      return {
        message: '入力してください',
        postUrl: 'aaa',
        resultid:'',
        resultpass:'',
        userid: null,
        userpass: null,
        apiUrl:'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login'
      }
    },
    methods: {
      dataConfirmation: function () {

        const crypto = require('crypto')

        /*msg初期化*/
        this.message = ''
        this.resultuser = ''
        this.resultid = ''
        this.resultpass = ''

        /*テキストボックスから受け取り*/
        this.userid = document.getElementById("userId").value
        this.userpass = document.getElementById("userPassword").value

        /*正規表現パターン*/
        let paternid = new RegExp(/^([a-zA-Z0-9]{1,7})$/)
        let paternpass = new RegExp(/^([a-zA-Z0-9]{1,30})$/)

        if (false == paternid.test(this.userid)) {
          this.resultid = "ユーザidが不正"
          if (false == paternpass.test(this.userpass)) {
            this.resultpass = "ユーザpassが不正"
          }

        } else {
          if (false == paternpass.test(this.userpass)) {
            this.resultpass = "ユーザpassが不正"
          } else {
            this.message = this.message = crypto.createHash('sha256').update(this.userpass).digest('hex')
          }
        }

      },
      deleteData: function () {
        document.getElementById("userId").value = ''
        document.getElementById("userPassword").value = ''
        this.message = '入力してください'

      },
      pushData: function () {
        this.axios.post(this.postUrl, {
          id: this.userid,
          pass: this.userpass,
        })


      },
      signinApi(){
        this.axios.post(this.apiUrl, {
          id:String(this.userid),
          password:String(this.userpass)
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
      }
    },
    updated() {

    }
  }
</script>

<style scoped>
  h2{
    color: red;
  }
</style>
