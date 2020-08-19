<template>
  <div class="profile" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
<!--    <LogOut ref="logOut"></LogOut>-->
    <ReturnMenu></ReturnMenu>
    <div>
      <p class="userId-position">
        <msg1>ユーザーID：</msg1>
        {{userId}}
        <br>
      </p>
      <br>

      <UserChangeName class="name-position"></UserChangeName>
      <UserChangePass class="pass-position"></UserChangePass>
      <button v-on:click="logOutOpen" class="logout-position">ログアウト</button>
      <!--      <button v-on:click="deleteUser">アカウントを削除する</button>-->
    </div>
  </div>
</template>


<script>
  import UserChangeName from "@/components/UserChangeName"
  import UserChangePass from "@/components/UserChangePass"
  import LogOut from "@/components/LogOut"
  import ReturnMenu from "@/components/ReturnMenu"
  import http from "../../static/axios/axios"

  export default {
    name: "UserProfile",
    components: {
      UserChangePass: UserChangePass,
      UserChangeName: UserChangeName,
      LogOut:LogOut,
      ReturnMenu:ReturnMenu,
    },
    data() {
      return {
        userId: '',       /*ユーザID受け取り用*/
        successFlg: this.$route.params.successFlg,
        url: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
        backgroundImageSrc: require("@/assets/test1.png")
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
        // メイン画面出なくメニュー画面への遷移に変更、異常はないか
        // this.$router.push('/main')
        this.$router.push({name: 'Menu', params: {userId: this.userId}})
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
  .logout-position{
    position: absolute;
    bottom: 10%;
    right: 20%;
  }
  .name-position{
    font-size: 4vh;
  }
  .pass-position{
    font-size: 4vh;
  }
  .userId-position{
    font-size: 4vh;
  }

</style>
