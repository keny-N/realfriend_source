<template>
  <div>
    <p>
      <msg1>パスワード：＊＊＊＊＊＊</msg1>
      <button v-on:click="passFlagchange">変更</button>
      <br>
    </p>
    <div v-if="passflg == true">
      <form>
        新しいパスワードを入力してください：
        <input type="password" ref="newThisPass" value="" required="required"><br>
        新しいパスワードをもう一度入力してください：
        <input type="password" ref="checkThisPass" value="" required="required"><br>
        <button v-on:click="openPModal">送信</button>
      </form>
      {{errPassMsg}}
    </div>
  </div>
</template>

<script>
  export default {
    name: "UserChangePass",
    data() {
      return {
        passflg: false,
        succses_flg: false,
        pass_url: '',
        openUModal: "",
        errPassMsg: '',
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
          me.pass_url = me.api_url + '/pass'
          this.axios.put(this.pass_url, {
            user_pass: String(me.usernewpass),
          }).then(function (response) {
            if (response.data.isSuccess == true) {
              me.passflg = false
            } else {
              me.errPassMsg = '失敗'
            }
          }).catch(function (error) {
            console.log(error)
          })
        }

      },
      openPModal() {
        if (this.$refs.newThisPass.value == this.$refs.checkThisPass.value) {
          this.$emit('open')
        } else {
          this.errPassMsg = '確認用と同じものが指定されていません'
        }
      },
      passFlagchange() {
        if (this.passflg) {
          this.passflg = false
        } else {
          this.passflg = true
        }
      },
    }
  }
</script>

<style scoped>

</style>
