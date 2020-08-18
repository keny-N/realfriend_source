<template>
  <div>
    <p>
      <br>
    </p>
      <input type="password" ref="newThisPass" placeholder="新しいパスワードを入力してください"
             size="35"><br>
      <input type="password" ref="checkThisPass" placeholder="もう一度入力してください" size="35"><br>
    {{errPassMsg}}
      <button v-on:click="checkPass">変更</button>
  </div>
</template>

<script>
  import http from "../../static/axios/axios"

  export default {
    name: "UserChangePass",
    data() {
      return {
        passUrl: '',
        errPassMsg: '',
        userId: this.$route.params.userId,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users/pass'
      }
    },
    props: {
      api_url: ''
    },
    methods: {
      updateUserPassApi() {
        let me = this
        http.put(this.apiUrl, {
          user_pass: String(me.$refs.newThisPass.value),
        }).then(function (response) {
           me.errPassMsg = '成功'
            me.$refs.newThisPass.value = ''
            me.$refs.checkThisPass.value = ''
        }).catch(function (error) {
          console.log(error)
        })
      },
      checkPass() {
        if(this.$refs.newThisPass.value === '' || this.$refs.checkThisPass.value ==='') {
          this.errPassMsg = '入力してください'
          console.log('a')
        }else{
          if (this.$refs.newThisPass.value === this.$refs.checkThisPass.value) {
            this.updateUserPassApi()
          } else {
            this.errPassMsg = '確認用と同じものが指定されていません'
          }
        }
      },
    },
  }
</script>

<style scoped>

</style>
