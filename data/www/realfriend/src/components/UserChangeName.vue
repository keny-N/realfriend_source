<template>
  <div>
    <p>
      <br>
    </p>
      <input type="text" ref="userThisName" value="" required="required" placeholde="新しいユーザ名を入力してください" size="35">
      <br>
      <button v-on:click="updateUserNameApi">変更</button>
    {{errNameMsg}}
  </div>
</template>

<script>
  export default {
    name: "UserChangeName",
    data() {
      return {
        errNameMsg: '',
        userId: this.$route.params.userId,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users'
      }
    },
    methods: {
      updateUserNameApi() {
        let me = this
        this.userName = this.$refs.userThisName.value
        this.axios.put(this.apiUrl, {
          user_name: String(this.userName),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            me.getUserApi()
            me.$refs.userThisName.value = ''
          } else {
            me.errNameMsg = '失敗しました'
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })


      },
      getUserApi() {
        let me = this
        this.axios.get(this.apiUrl, {}).then(function (response) {
          if (response.data.isSuccess == true) {
            me.userName = response.data.user[1]
            let plcMsg = "ユーザ名：" + me.userName
            me.$refs.userThisName.placeholder = plcMsg
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
    },
    created() {
      this.apiUrl = this.apiUrl + '/' + this.userId
      this.getUserApi()
    }
  }
</script>

<style scoped>

</style>
