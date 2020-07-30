<template>

  <div>
    {{username}}さん
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
        userid: this.$route.params.userId,
        userpass: '',
        username:'',
        modal: false,
        errMsg: '',
        successUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
        getUrl:'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
      }
    },
    methods: {
      changeCheck() {
        let me = this
        this.userpass = this.$refs.userThisPass.value
        this.axios.post(this.successUrl, {
          user_id: String(this.userid),
          user_pass: String(this.userpass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            let textUrl = '/user/' + me.userid + '/profile'
            me.$router.push({path: textUrl,params:{userId:me.userid}})
          } else {
            me.errMsg = 'IDもしくはパスワードが間違っています'
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
      getUserApi() {
        let me = this
        this.getUrl = this.getUrl+'/'+this.userid
        this.axios.get(this.getUrl, {
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            me.username = response.data.user[1]
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
    },
    created() {
      this.getUrl = this.getUrl+'/'+this.userid
      this.getUserApi()
    }
  }
</script>

<style scoped>
</style>
