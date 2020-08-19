<template>
  <div>
    <p>
      <br>
      <input type="text" ref="userThisName" size="35"></p>
    <br>
    {{ errMsg }}
    <button v-on:click="updateUserNameApi">変更</button>
    {{ errNameMsg }}
  </div>
</template>

<script>
import http from "../../static/axios/axios"

export default {
  name: "UserChangeName",
  data() {
    return {
      errNameMsg: '',
      userId: this.$route.params.userId,
      errMsg: '',
      apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users'
    }
  },
  methods: {
    updateUserNameApi() {
      let me = this
      this.userName = this.$refs.userThisName.value
      if (this.userName === '') {
        this.errMsg = '入力してください'
      } else {
        http.put(this.apiUrl, {
          user_name: String(this.userName),
        },{
         headers:{
           Authorization:this.$store.getters['token/tokenGet']
         }
        }).then(function (response) {
          me.getUserApi()
          me.$refs.userThisName.value = ''
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    getUserApi() {
      let me = this
      http.get(this.apiUrl).then(function (response) {
        me.userName = response.data.user[1]
        me.$refs.userThisName.placeholder = "ユーザ名：" + me.userName
      }).catch(function (error) {
        console.log(error)
      })
    },
  },
  created() {
    // this.apiUrl = this.apiUrl + '/' + this.userId
    this.getUserApi()
  }
}
</script>

<style scoped>

</style>
