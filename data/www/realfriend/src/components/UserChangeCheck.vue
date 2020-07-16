<template>
  <div>
    {{userid}}
    <form>
      <p>
        <msg1>パスワードを入力してください</msg1>
        <br>
        <input type="password" ref="userThisPass" placeholder="パスワード" required="required">
      </p>
      <button v-on:click="changeCheck">ok</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: "UserChangeCheck",
    data() {
      return {
        userid: '',
        userpass: '',
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
      }
    },
    methods: {
      changeCheck() {
        let me = this
        this.userpass = this.$refs.userThisPass.value
        this.axios.post(this.apiUrl, {
          user_id: String(this.userid),
          user_pass: String(this.userpass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            console.log('a')
            me.$emit('succses')
          } else {
            console.log('b')
            me.message = 'IDもしくはパスワードが間違っています'
          }
        }).catch(function (error) {
          console.log('c')
          console.log(error)
        })
      },
    },
    created() {
      this.userid = window.location.href.slice(window.location.href.indexOf('=') + 1)
    }
  }
</script>

<style scoped>

</style>
