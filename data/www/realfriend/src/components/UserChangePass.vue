<template>
  <div>
    <p>
      <br>
    </p>
      <input type="password" ref="newThisPass" value="" required="required" placeholder="新しいパスワードを入力してください"
             size="35"><br>
      <input type="password" ref="checkThisPass" value="" required="required" placeholder="もう一度入力してください" size="35"><br>
      <button v-on:click="checkPass">変更</button>
    {{errPassMsg}}
  </div>
</template>

<script>
  export default {
    name: "UserChangePass",
    data() {
      return {
        passUrl: '',
        errPassMsg: '',
        userId: this.$route.params.userId,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users'
      }
    },
    props: {
      api_url: ''
    },
    methods: {
      updateUserPassApi() {
        let me = this
        me.userNewPass = this.$refs.newThisPass.value
        me.passUrl = me.apiUrl + '/pass'
        this.axios.put(this.passUrl, {
          user_pass: String(me.userNewPass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            me.errPassMsg = '成功'
            me.$refs.newThisPass.value = ''
            me.$refs.checkThisPass.value = ''
          } else {
            console.log(response)
            me.errPassMsg = '失敗'
          }
        }).catch(function (error) {
          console.log(error)
        })


      },
      checkPass() {
        if (this.$refs.newThisPass.value == this.$refs.checkThisPass.value) {
          this.updateUserPassApi()
        } else {
          this.errPassMsg = '確認用と同じものが指定されていません'
        }
      },

    },
    created() {
      this.apiUrl = this.apiUrl + '/' + this.userId
    }
  }
</script>

<style scoped>

</style>
