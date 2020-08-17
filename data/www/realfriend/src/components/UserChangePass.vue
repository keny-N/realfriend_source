<template>
  <div>
    <p>
      <br>
    </p>
      <input class="old-pass" type="password" ref="newThisPass" placeholder="新しいパスワードを入力してください"
             size="35"><br>
      <input class="new-pass" type="password" ref="checkThisPass" placeholder="もう一度入力してください" size="35"><br>
    {{errPassMsg}}
      <button v-on:click="checkPass" class="edit-position">変更</button>
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
        if(this.$refs.newThisPass.value == '' || this.$refs.checkThisPass.value =='') {
          this.errPassMsg = '入力してください'
          console.log('a')
        }else{
          if (this.$refs.newThisPass.value == this.$refs.checkThisPass.value) {
            this.updateUserPassApi()
          } else {
            this.errPassMsg = '確認用と同じものが指定されていません'
          }
        }
      },

    },
    created() {
      this.apiUrl = this.apiUrl + '/' + this.userId
    }
  }
</script>

<style scoped>
  .old-pass{
    margin-bottom: 10px;
  }
  .new-pass{
    margin-bottom: 4%;
  }
  .edit-position{
    margin-top: 10px;
  }

</style>
