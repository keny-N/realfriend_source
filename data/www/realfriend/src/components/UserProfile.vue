<template>
  <div>
    <div>
      <h2>{{changemessage}}</h2>

      <p>
        <msg1>ユーザーID：</msg1>
        {{userid}}
        <br>
      </p>
      <br>

      <UserChangeName ref="userchangename"></UserChangeName>
      <UserChangePass ref="userchangepass"></UserChangePass>


      <button v-on:click="backMainVue">戻る</button>
<!--      <button v-on:click="deleteUser">アカウントを削除する</button>-->
    </div>
  </div>
</template>


<script>
  import UserChangeName from "@/components/UserChangeName"
  import UserChangePass from "@/components/UserChangePass"

  export default {
    name: "UserProfile",
    components: {
      UserChangePass: UserChangePass,
      UserChangeName: UserChangeName,
    },
    data() {
      return {
        userid: this.$route.params.userId,       /*ユーザID受け取り用*/
        useroldpass: null,     /*ユーザパス受け取り用*/
        usernewpass: null,
        changemessage: '',
        username: '',
        succsesflg: false,
        Url: '',
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
      backMainVue() {
        let textUrl = '/main/' + this.userid
        this.$router.push({path: textUrl, params: {userId: this.userid}})
      },
    }
    ,
  }

</script>

<style scoped>

</style>
