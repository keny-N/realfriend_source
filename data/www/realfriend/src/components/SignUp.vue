<template>
  <div>
    <!--    <SignUpModal @close="closeModal" v-if="modal">-->
    <!--      <p>-->
    <!--        <msg1>ユーザー名を入力してください</msg1>-->
    <!--        <msg2>※必須</msg2>-->
    <!--        <br>-->
    <!--        <input type="text" id="userName" value="" placeholder="ユーザ名">-->
    <!--      </p>-->
    <!--      <h2>{{resultid}}</h2>-->
    <!--      <p>-->
    <!--        <msg1>ユーザーIDを入力してください</msg1>-->
    <!--        <msg2>※必須</msg2>-->
    <!--        <br>-->
    <!--        <input type="text" id="userId" value="" placeholder="ユーザID"></p>-->
    <!--      <h2>{{resultid}}</h2>-->
    <!--      <p>-->
    <!--        <msg1>パスワードを入力してください</msg1>-->
    <!--        <msg2>※必須</msg2>-->
    <!--        <br>-->
    <!--        <input type="password" id="userPassword" value="" placeholder="パスワード"></p>-->
    <!--      <h2>{{resultpass}}</h2>-->

    <!--      <button v-on:click="dataConfirmation">登録</button>-->
    <!--      <br>-->
    <!--      <button v-on:click="dataDelete">取り消し</button>-->
    <!--      <h1>{{message}}</h1>-->

    <!--      <a v-on:click="back" id="link">ゲーム画面に戻る</a>-->
    <!--    </SignUpModal>-->

    <div class="example-modal-window">
      <!-- コンポーネント MyModal -->
      <SignUpModal @close="closeModal" v-if="modal">
        <!-- default スロットコンテンツ -->
        <p>
          <msg1>ユーザー名を入力してください</msg1>
          <msg2>※必須</msg2>
          <br>
          <input type="text" id="userName" value="" placeholder="ユーザ名">
        </p>
        <h2>{{resultid}}</h2>
        <p>
          <msg1>ユーザーIDを入力してください</msg1>
          <msg2>※必須</msg2>
          <br>
          <input type="text" id="userId" value="" placeholder="ユーザID"></p>
        <h2>{{resultid}}</h2>
        <p>
          <msg1>パスワードを入力してください</msg1>
          <msg2>※必須</msg2>
          <br>
          <input type="password" id="userPassword" value="" placeholder="パスワード"></p>
        <h2>{{resultpass}}</h2>
        <!-- /default -->
        <!-- footer スロットコンテンツ -->
        <template slot="footer">
          <button v-on:click="dataConfirmation">登録</button>
          <br>
          <button v-on:click="dataDelete">取り消し</button>
          <h1>{{message}}</h1>

          <a v-on:click="back" id="link">ゲーム画面に戻る</a>
        </template>
        <!-- /footer -->
      </SignUpModal>
    </div>

  </div>

</template>

<script>
  import SignUpModal from '@/components/SignUpModal';
  export default {
    name: "SignUp",
    components: { SignUpModal },
    data() {
      return {
        message: '必要情報を入力してください',
        resultuser: '',       /*エラー表示用*/
        resultid: '',         /*エラー表示用*/
        resultpass: '',       /*エラー表示用*/
        username: null,       /*受け取り用*/
        userid: null,         /*受け取り用*/
        userpass: null,       /*受け取り用*/
        modal: false,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
        //apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login'
      }
    },
    methods: {
      dataConfirmation: function () {

        /*msg初期化*/
        this.message = ''
        this.resultuser = ''
        this.resultid = ''
        this.resultpass = ''

        /*テキストボックスから受け取り*/
        this.username = document.getElementById("userName").value
        this.userid = document.getElementById("userId").value
        this.userpass = document.getElementById("userPassword").value

        /*正規表現パターン*/
        // let paternid = new RegExp(/^([a-zA-Z0-9]{1,7})$/)
        // let paternpass = new RegExp(/^([a-zA-Z0-9]{1,30})$/)

        /*入力値のチェック*/
        if (this.username == '') {
          this.resultuser = "ユーザ名が不正です"
          if (this.userid == '' /*false == paternid.test(this.userid)*/) {
            this.resultid = "ユーザidが不正です"
            if (this.userpass == '' /*false == paternpass.test(this.userpass)*/) {
              this.resultpass = "ユーザpassが不正です"
            }
          } else {
            if (this.userpass == '' /*false == paternpass.test(this.userpass)*/) {
              this.resultpass = "ユーザpassが不正です"
            }
          }
        } else {
          if (this.userid == '' /*false == paternid.test(this.userid)*/) {
            this.resultid = "ユーザidが不正です"
            if (this.userpass == '' /*false == paternpass.test(this.userpass)*/) {
              this.resultpass = "ユーザpassが不正です"
            }

          } else {
            if (this.userpass == '' /*false == paternpass.test(this.userpass)*/) {
              this.resultpass = "ユーザpassが不正です"
            } else {
              this.userAdd()
            }
          }
        }
      },
      /*API*/
      userAdd() {
        let me = this
        this.axios.post(this.apiUrl, {
          user_name: String(this.username),
          user_id: String(this.userid),
          user_pass: String(this.userpass),
        }).then(function (response) {
          if (response.data.isSuccess) {
            me.upLoad()
          } else {
            me.msg = response.data.error
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
      upLoad() {
        alert('登録が完了しました!続けてログインしてください')
        this.$emit('change', '登録が完了しました')
      },
      back() {
        this.$emit('change', '')
      },
      /*データクリア用*/
      dataDelete: function () {
        document.getElementById("userName").value = ''
        document.getElementById("userId").value = ''
        document.getElementById("userPassword").value = ''
        this.message = '必要情報を入力してください'

      },
      openModal() {
        this.modal = true
        console.log(this.modal)
      },
      closeModal() {
        this.modal = false
      },

    },
    updated() {

    }
  }
</script>

<style scoped>
  h2 {
    color: red;
  }

  msg2 {
    color: red;
  }

  #link {
    color: blue;
    text-decoration: underline
  }
</style>
