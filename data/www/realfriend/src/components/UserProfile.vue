<template>
  <div>
    <UserChangeCheck ref="UserChangeCheck" @succses="userChangeSuccses"></UserChangeCheck>
    <div>
      <h2>{{changemessage}}</h2>

      <p>
        <msg1>ユーザーID：</msg1>
        {{userid}}
        <br>
      </p>
      <br>

      <UserChangeName ref="userchangename" @getuser="getUserApi" @open="openUserChangeCheck" :user_name="username"
                      :api_url="Url"></UserChangeName>
      <UserChangePass ref="userchangepass" @open="openUserChangeCheck" :api_url="Url"></UserChangePass>


      <button v-on:click="backMainVue">戻る</button>
      <button v-on:click="deleteUser">アカウントを削除する</button>
    </div>
  </div>
</template>


<script>
  import UserChangeCheck from "@/components/UserChangeCheck"
  import UserChangeName from "@/components/UserChangeName"
  import UserChangePass from "@/components/UserChangePass"

  export default {
    name: "UserProfile",
    components: {
      UserChangePass: UserChangePass,
      UserChangeName: UserChangeName,
      UserChangeCheck: UserChangeCheck
    },
    data() {
      return {
        userid: '',       /*ユーザID受け取り用*/
        useroldpass: null,     /*ユーザパス受け取り用*/
        usernewpass: null,
        changemessage: '',
        username: '',
        succsesflg: false,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
        Url: '',
      }
    },
    methods: {

      getUserApi() {
        let me = this
        this.axios.get(this.Url, {}).then(function (response) {
          if (response.data.isSuccess == true) {
            me.username = response.data.user[1]
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },

      deleteUser() {
        let me = this
        this.openUserChangeCheck()
        if (this.succsesflg) {
          this.axios.delete(this.Url, {
            user_id: String(this.userid),
          }).then(function (response) {
            if (response.data.isSuccess == true) {
              alert('削除に成功しました')
              me.$router.push({path: '/Login'})
              console.log(response)
            } else {
              console.log(response.data.error)
              me.changemessage = '登録に失敗しました'
            }
          }).catch(function (error) {
            console.log(error)
            me.changemessage = '登録に失敗しました'
          })
        }

      },
      backMainVue() {
        this.$router.replace({path: '/', query: {id: this.userid}})
      },
      userChangeSuccses() {
        this.succsesflg = true
        if (this.$refs.userchangename.nameflg) {
          this.$refs.userchangename.succses_flg = true
          this.$refs.userchangename.updateUserNameApi()
        } else if (this.$refs.userchangepass.passflg) {
          this.$refs.userchangepass.succses_flg = true
          this.$refs.userchangepass.updateUserPassApi()
        }
      },
      openUserChangeCheck() {
        this.$refs.UserChangeCheck.openUserChangeModal()
      }
    }
    ,
    created() {
      this.userid = window.location.href.slice(window.location.href.indexOf('=') + 1)
      this.Url = this.apiUrl + '/' + this.userid
      this.getUserApi()
    }
  }

</script>

<style scoped>

</style>
