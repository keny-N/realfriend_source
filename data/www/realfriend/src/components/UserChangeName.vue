<template>
  <div>
    <p>
      <msg1>ユーザー名：</msg1>
      {{user_name}}
      <button v-on:click="nameFlagchange">変更</button>
      <br>
    </p>
    <div v-if="nameflg == true">
      <form>
        <input type="text" ref="userThisName" value="" required="required">
        <button v-on:click="openNModal">送信</button>
      </form>
      {{errNameMsg}}
    </div>
  </div>
</template>

<script>
  export default {
    name: "UserChangeName",
    data() {
      return {
        nameflg: false,
        succses_flg:false,
        errNameMsg:'',
      }
    },
    props: {
      user_name: '',
      api_url:''
    },
    methods: {
      updateUserNameApi() {
        let me = this
        this.username = this.$refs.userThisName.value
        if(this.succses_flg == true) {
          this.axios.put(this.api_url, {
            user_id: String(this.userid),
            user_name: String(this.username),
          }).then(function (response) {
            if (response.data.isSuccess == true) {
              me.getUserApi()
              me.nameflg = false
            } else {
              me.errNameMsg = '失敗しました'
              console.log(response.data.error)
            }
          }).catch(function (error) {
            console.log(error)
          })
        }

      },
      openNModal(){
        this.$emit('open')
      },
      getUserApi() {
        let me = this
        this.axios.get(this.api_url, {
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            me.user_name = response.data.user[1]
          } else {
            console.log(response.data.error)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
      nameFlagchange() {
        if (this.nameflg) {
          this.nameflg = false
        } else {
          this.nameflg = true
        }
      },
    }
  }
</script>

<style scoped>

</style>
