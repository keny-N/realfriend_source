<template>
  <div>
<!--    <LogOut ref="logOut"></LogOut>-->
    <div>
      <p>
        <msg1>ユーザーID：</msg1>
        {{userId}}
        <br>
      </p>
      <br>

<!--      <UserChangeName></UserChangeName>-->
<!--      <UserChangePass></UserChangePass>-->

      <button v-on:click="backMainVue">戻る</button>
      <button v-on:click="logOutOpen">ログアウト</button>
      <!--      <button v-on:click="deleteUser">アカウントを削除する</button>-->
    </div>
  </div>
</template>


<script>
  import UserChangeName from "@/components/UserChangeName"
  import UserChangePass from "@/components/UserChangePass"
  import LogOut from "@/components/LogOut"
  import http from "../../static/axios/axios"

  export default {
    name: "UserProfile",
    components: {
      UserChangePass: UserChangePass,
      UserChangeName: UserChangeName,
      LogOut:LogOut,
    },
    data() {
      return {
        userId: '',       /*ユーザID受け取り用*/
        successFlg: this.$route.params.successFlg,
        url: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users'
      }
    },
    created() {
      http.get(this.url, {
        headers:{
          Authorization:this.$store.getters['token/tokenGet']
        }
      }).then((response) => {
        console.log(response.data)
        this.userId = response.data.user[0]
      }).catch((error) => {
        console.log(error.response.status)
      })
    },
    methods: {

      // deleteUser() {
      //   let me = this
      //   if (this.succsesflg) {
      //     this.axios.delete(this.Url, {
      //       user_id: String(this.userid),
      //     }).then(function (response) {
      //       if (response.data.isSuccess == true) {
      //         alert('削除に成功しました')
      //         me.$router.push({path: '/Login'})
      //         console.log(response)
      //       } else {
      //         console.log(response.data.error)
      //         me.changemessage = '登録に失敗しました'
      //       }
      //     }).catch(function (error) {
      //       console.log(error)
      //       me.changemessage = '登録に失敗しました'
      //     })
      //   }
      //
      // },
      logOutOpen(){
        this.$refs.logOut.openLogOutModal()
      },
      backMainVue() {
        this.$router.push('/main')
      },
    }
    ,
    destroyed() {
      this.$route.params.successFlg = false
    }
  }

</script>

<style scoped>

</style>
