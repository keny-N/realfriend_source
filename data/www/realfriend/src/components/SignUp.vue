@ -0,0 +1,103 @@
<template>
  <div>
    <button v-on:click="dataConfirmation">登録</button>
    <button v-on:click="deleteData">取り消し</button>
    <p>
      <input type="text" id="userName" value="" placeholder="ユーザネーム"></p>
    <p>
      <input type="text" id="userId" value="" placeholder="ユーザID"></p>
    <p>
      <input type="text" id="userPassword" value="" placeholder="パスワード"></p>
    <h1>{{message}}</h1>
    <h2>{{resultuser}}</h2>
    <h2>{{resultid}}</h2>
    <h2>{{resultpass}}</h2>
  </div>
</template>

<script>
  export default {
    name: "SignUp",
    data() {
      return {
        message: '入力してください',
        postUrl: 'aaa',
        resultuser:'',
        resultid:'',
        resultpass:'',
        username: null,
        userid: null,
        userpass: null,
      }
    },
    methods: {
      dataConfirmation: function () {
        /*msg初期化*/
        this.message=''
        this.resultuser = ''
        this.resultid =''
        this.resultpass=''

        /*テキストボックスから受け取り*/
        this.username = document.getElementById("userName").value
        this.userid = document.getElementById("userId").value
        this.userpass = document.getElementById("userPassword").value

        /*正規表現パターン*/
        let paternid = new RegExp(/^([a-zA-Z0-9]{1,7})$/)
        let paternpass = new RegExp(/^([a-zA-Z0-9]{1,30})$/)

        if (this.username == '') {
          this.resultuser = "ユーザ名が空です"
          if (false == paternid.test(this.userid)) {
            this.resultid = "ユーザidが空"
            if (false == paternpass.test(this.userpass) ){
              this.resultpass = "ユーザpassが空です"
            }
          }else{
            if (this.userpass == '') {
              this.resultpass = "ユーザpassが空"
            }
          }
        } else {
          if (false == paternid.test(this.userid)) {
            this.resultid = "ユーザidが空"
            if (false == paternpass.test(this.userpass)) {
              this.resultpass = "ユーザpassが空"
            }

          }else{
            if (false == paternpass.test(this.userpass)) {
              this.resultpass = "ユーザpassが空"
            }else{
              this.message = 'ok'
            }
          }
        }
      },
      deleteData: function () {
        document.getElementById("userName").value =''
        document.getElementById("userId").value =''
        document.getElementById("userPassword").value = ''
        this.message =  '入力してください'

      },
      pushData: function () {
        this.axios.post(this.postUrl, {
          id: this.userid,
          name: this.username,
          pass: this.userpass,
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
