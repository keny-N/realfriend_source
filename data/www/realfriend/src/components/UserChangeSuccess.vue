<template>

  <div>
    {{userName}}さん
    <h1>認証ページです</h1>
      <p>
        <msg1>パスワードを入力してください</msg1>
        <br>
        <input type="password" ref="userThisPass" placeholder="パスワード" >
      </p>
      <button v-on:click="changeCheck">ok</button>
    {{errMsg}}
  </div>

</template>

<script>
  import http from "../../static/axios/axios"

  export default {
    name: "UserChangeSuccess",
    data() {
      return {
        userId: '',
        userpass: '',
        userName: '',
        errMsg: '',
        successUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
        url: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
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
</style>
