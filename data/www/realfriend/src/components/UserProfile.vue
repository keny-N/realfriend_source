<template>
  <div>
    <div v-if="succsesflg == false">
      <UserChangeCheck @succses="userChangeSuccses"></UserChangeCheck>
    </div>
    <div v-if="succsesflg == true">
      <h2>{{changemessage}}</h2>

      <p>
        <msg1>ユーザーID：</msg1>
        {{getUserId}}
        <br>
      </p>
      <br>

      <p>
        <msg1>ユーザー名：</msg1>
        {{getUserName}}
        <button v-on:click="nameFlagchange">変更</button>
        <br>
      </p>
      <div v-if="nameflg">
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
      <div v-if="passflg">
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
        resultid: '',       /*エラーコメント表示用*/
        resultpass: '',     /*エラーコメント表示用*/
        userid: '',       /*ユーザID受け取り用*/
        useroldpass: null,     /*ユーザパス受け取り用*/
        usernewpass: null,
        changemessage: '',
        username: '',
        getUserName: null,
        nameflg: false,
        idflg: false,
        passflg: false,
        modal: false,
        succsesflg: false,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
        Url: '',
      }
    },
    methods: {

      getUserApi() {
        // this.$refs.userUpdata.openModal()
        let me = this
        this.axios.get(this.Url, {}).then(function (response) {
          if (response.data.isSuccess == true) {
            me.getUserName = response.data.user[1]
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
          user_id: String(this.getUserId),
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
      // updateUserIdApi() {
      //   let me = this
      //   this.userid = this.$refs.userThisId.value
      //   this.axios.put(this.Url, {
      //     user_id: String(this.userid),
      //     user_name: String(this.getUserName),
      //   }).then(function (response) {
      //     if (response.data.isSuccess == true) {
      //       me.getUserId = me.userid
      //       me.idflg = false
      //       console.log(response)
      //       me.Url = me.apiUrl + '/' + me.getUserId
      //       me.replaceUrl()
      //     } else {
      //       console.log(response.data.error)
      //       me.changemessage = '登録に失敗しました'
      //     }
      //   }).catch(function (error) {
      //     console.log(error)
      //     me.changemessage = '登録に失敗しました'
      //   })
      //
      // },
      updateUserPassApi() {
        let me = this
        if (this.$refs.oldThisPass.value == this.$refs.newThisPass.value) {
          me.message = '同じパスワードが指定されています'
        } else if (this.$refs.newThisPass.value == this.$refs.checkThisPass.value) {
          me.useroldpass = this.$refs.oldThisPass.value
          me.usernewpass = this.$refs.newThisPass.value
          me.Url = me.apiUrl + '/' + me.getUserId + '/pass'
          this.axios.put(this.Url, {
            old_pass: String(me.useroldpass),
            new_pass: String(me.usernewpass),
          }).then(function (response) {
            if (response.data.isSuccess == true) {
              me.Url = me.apiUrl + '/' + me.getUserId
              me.passflg = false
              me.changemessage = '成功！'
            } else {
              me.changemessage = '失敗。。。'
            }
          }).catch(function (error) {
            console.log(error)
          })
        }
      },

      nameFlagchange() {
        if (this.nameflg) {
          this.nameflg = false
        } else {
          this.nameflg = true
        }
      },
      // idFlagchange() {
      //   if (this.idflg) {
      //     this.idflg = false
      //   } else {
      //     this.idflg = true
      //   }
      // },
      passFlagchange() {
        if (this.passflg) {
          this.passflg = false
        } else {
          this.passflg = true
        }
      },

      openModal() {
        this.modal = true
      },

      closeModal() {
        this.modal = false
        this.success = false
      },
      replaceUrl() {
        console.log(this.getUserId)
        this.$router.replace({path: '/u', query: {id: this.userid}})
        this.changemessage = '成功！'
      },
      userUpdataPage() {
        console.log('b')
      },
      userChangeSuccses() {
        this.succsesflg = true
        console.log(this.succsesflg)
      }
    },
    created() {
      this.getUserId = window.location.href.slice(window.location.href.indexOf('=') + 1)
      this.Url = this.apiUrl + '/' + this.getUserId
      // this.$refs.userUpdata.openModal()
      this.getUserApi()
    }
  }

</script>

<style scoped>

</style>
