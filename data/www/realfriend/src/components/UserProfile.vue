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

      <p>
        <msg1>ユーザー名：</msg1>
        {{username}}
        <button v-on:click="nameFlagchange">変更</button>
        <br>
      </p>
      <div v-if="nameflg == true && succsesflg == true">
        <form>
          <input type="text" ref="userThisName" value="" required="required">
          <button v-on:click="updateUserNameApi">送信</button>
        </form>
      </div>

      <br>
      <p>
        <msg1>パスワード：＊＊＊＊＊＊</msg1>
        <button v-on:click="passFlagchange">変更</button>
        <br>
      </p>
      <div v-if="passflg == true && succsesflg == true">
        <form>
          元のパスワードを入力してください：
          <input type="password" ref="oldThisPass" value="" required="required"><br>
          新しいパスワードを入力してください：
          <input type="password" ref="newThisPass" value="" required="required"><br>
          新しいパスワードをもう一度入力してください：
          <input type="password" ref="checkThisPass" value="" required="required"><br>
          <button v-on:click="updateUserPassApi">送信</button>
        </form>
      </div>

      <button v-on:click="backMainVue">戻る</button>
      <button v-on:click="deleteUser">アカウントを削除する</button>
    </div>
  </div>
</template>


<script>
  import UserChangeCheck from "@/components/UserChangeCheck"

  export default {
    name: "UserProfile",
    components: {
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
        nameflg: false,
        passflg: false,
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
            me.openUserChangeCheck()
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },

      updateUserNameApi() {
        let me = this
        this.username = this.$refs.userThisName.value
        this.axios.put(this.Url, {
          user_id: String(this.userid),
          user_name: String(this.username),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            me.getUserApi()
            me.nameflg = false
            me.changemessage = '成功！'
            console.log(response)
          } else {
            console.log(response.data.error)
            me.changemessage = '登録に失敗しました'
          }
        }).catch(function (error) {
          console.log(error)
          me.changemessage = '登録に失敗しました'
        })

      },

      updateUserPassApi() {
        let me = this
        if (this.$refs.oldThisPass.value == this.$refs.newThisPass.value) {
          me.changemessage = '同じパスワードが指定されています'
        } else if (this.$refs.newThisPass.value == this.$refs.checkThisPass.value) {
          me.useroldpass = this.$refs.oldThisPass.value
          me.usernewpass = this.$refs.newThisPass.value
          me.Url = me.apiUrl + '/' + me.userid + '/pass'
          this.axios.put(this.Url, {
            old_pass: String(me.useroldpass),
            new_pass: String(me.usernewpass),
          }).then(function (response) {
            if (response.data.isSuccess == true) {
              me.Url = me.apiUrl + '/' + me.userid
              me.passflg = false
              me.changemessage = '成功！'
            } else {
              me.changemessage = '失敗'
            }
          }).catch(function (error) {
            console.log(error)
          })
        }
      },

      deleteUser() {
        let me = this
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

      },
      nameFlagchange() {
        if (this.nameflg) {
          this.nameflg = false
        } else {
          this.nameflg = true
        }
      },
      passFlagchange() {
        if (this.passflg) {
          this.passflg = false
        } else {
          this.passflg = true
        }
      },
      backMainVue() {
        this.$router.replace({path: '/', query: {id: this.userid}})
      },
      userChangeSuccses() {
        this.succsesflg = true
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
