<template>
  <div>
    <p>
      <br>
    </p>
    <form>
      <input type="password" ref="newThisPass" value="" required="required" placeholder="新しいパスワードを入力してください" size="35"><br>
      <input type="password" ref="checkThisPass" value="" required="required" placeholder="もう一度入力してください" size="35"><br>
      <button v-on:click="checkPass">変更</button>
    </form>
    {{errPassMsg}}
  </div>
</template>

<script>
  export default {
    name: "UserChangePass",
    data() {
      return {
        succses_flg: true,
        pass_url: '',
        errPassMsg: '',
        userid:this.$route.params.userId,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users'
      }
    },
    props: {
      api_url: ''
    },
    methods: {
      updateUserPassApi() {
        let me = this
        if (this.succses_flg) {
          me.usernewpass = this.$refs.newThisPass.value
          me.pass_url = me.apiUrl + '/pass'
          console.log(me.pass_url)
          this.axios.put(this.pass_url, {
            user_pass: String(me.usernewpass),
          }).then(function (response) {
            if (response.data.isSuccess == true) {
              me.errPassMsg = '成功'
              me.$refs.newThisPass.value =''
              me.$refs.checkThisPass.value =''
            } else {
              console.log(response)
              me.errPassMsg = '失敗'
            }
          }).catch(function (error) {
            console.log(error)
          })
        }

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
      this.apiUrl = this.apiUrl+'/'+this.userid
    }
  }
</script>

<style scoped>

</style>
