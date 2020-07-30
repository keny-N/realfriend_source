<template>

  <div>
    {{userName}}さん
    <h1>認証ページです</h1>
    <form>
      <p>
        <msg1>パスワードを入力してください</msg1>
        <br>
        <input type="password" ref="userThisPass" placeholder="パスワード" required="required">
      </p>
      <button v-on:click="changeCheck">ok</button>
    </form>
    {{errMsg}}
  </div>

</template>

<script>
  export default {
    name: "UserChangeSuccess",
    data() {
      return {
        userId: this.$route.params.userId,
        userpass: '',
        userName: '',
        errMsg: '',
        successUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
        getUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
      }
    },
    methods: {
      changeCheck() {
        let me = this
        this.userPass = this.$refs.userThisPass.value
        this.axios.post(this.successUrl, {
          user_id: String(this.userId),
          user_pass: String(this.userPass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            let textUrl = '/user/' + me.userId + '/profile'
            me.$router.push({path: textUrl, params: {userId: me.userId}})
          } else {
            me.errMsg = 'IDもしくはパスワードが間違っています'
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
      getUserApi() {
        let me = this
        this.axios.get(this.getUrl, {}).then(function (response) {
          if (response.data.isSuccess == true) {
            me.userName = response.data.user[1]
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
    },
    created() {
      this.getUrl = this.getUrl + '/' + this.userId
      this.getUserApi()
    }
  }
</script>

<style scoped>
</style>
