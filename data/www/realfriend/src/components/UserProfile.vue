<template>
  <div class="profile" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <LogOut ref="logOut"></LogOut>
    <divc>
      <p class="userId-position">
        <msg1>ユーザーID：</msg1>
        {{userId}}
        <br>
      </p>
      <br>

      <UserChangeName class="name-position"></UserChangeName>
      <UserChangePass class="pass-position"></UserChangePass>

      <button v-on:click="backMainVue" class="return-position">戻る</button>
      <button v-on:click="logOutOpen" class="logout-position">ログアウト</button>
      <!--      <button v-on:click="deleteUser">アカウントを削除する</button>-->
    </div>
  </div>
</template>


<script>
  import UserChangeName from "@/components/UserChangeName"
  import UserChangePass from "@/components/UserChangePass"
  import LogOut from "@/components/LogOut"

  export default {
    name: "UserProfile",
    components: {
      UserChangePass: UserChangePass,
      UserChangeName: UserChangeName,
      LogOut:LogOut,
    },
    data() {
      return {
        userId: this.$route.params.userId,       /*ユーザID受け取り用*/
        successFlg: this.$route.params.successFlg,
        backgroundImageSrc: require("@/assets/test1.png")
      }
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
        this.$router.push({name: 'Main', params: {userId: this.userId}})
      },
    }
    ,
    destroyed() {
      this.$route.params.successFlg = false
    }
  }

</script>

<style scoped>
  .profile{
    height: 100vh;
    background-size: 5%;
    animation: bgiLoop 8s linear infinite;
  }
  @keyframes bgiLoop {
    0% { background-position: 0 0;}
    100% { background-position: -15% 15%;}
  }
  .return-position{
    position:fixed;
  }
  .logout-position{
    position: fixed;
  }
  .name-position{
    font-size: 5vh;
  }
  .pass-position{
    font-size: 5vh;
  }
  .userId-position{
    font-size: 5vh;
  }

</style>
