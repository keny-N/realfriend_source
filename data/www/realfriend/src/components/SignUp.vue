<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="closeSignUpModal" v-if="modal">
      <div class="modal-window">
        <div class="modal-content">
          <slot/>
          <!-- コンポーネント MyModal -->
          <!-- default スロットコンテンツ -->
          <div v-if="success == false">
            <form>
              <p>
                <msg1>ユーザー名を入力してください</msg1>
                <msg2>※必須</msg2>
                <br>

                <input type="text" ref="userThisName" value="" placeholder="ユーザ名" required="required">
              </p>
              <h2>{{resultuser}}</h2>
              <p>
                <msg1>ユーザーIDを入力してください</msg1>
                <msg2>※必須</msg2>
                <br>
                <input type="text" ref="userThisId" value="" placeholder="ユーザID" required="required"></p>
              <h2>{{resultid}}</h2>
              <p>
                <msg1>パスワードを入力してください</msg1>
                <msg2>※必須</msg2>
                <br>
                <input type="password" ref="userThisPass" value="" placeholder="パスワード" required="required"></p>
              <h2>{{resultpass}}</h2>
              <button v-on:click="dataConfirmation">登録</button>
              <button v-on:click="dataDelete">取り消し</button>

            </form>
            <h1>{{message}}</h1>
          </div>
          <div v-if="success">
            <p>登録が完了しました！再度ログインしてください</p>
            <button v-on:click="closeSignUpModal">閉じる</button>
          </div>
          <!-- /default -->
          <!-- footer スロットコンテンツ -->

          <!-- /footer -->

        </div>
      </div>
    </div>
  </transition>

</template>

<script>

  export default {
    name: "SignUp",
    data() {
      return {
        message: '必要情報を入力してください',
        resultuser: '',       /*エラー表示用*/
        resultid: '',         /*エラー表示用*/
        resultpass: '',       /*エラー表示用*/
        username: null,       /*受け取り用*/
        userid: null,         /*受け取り用*/
        userpass: null,       /*受け取り用*/
        modal: false,         /*モーダル展開*/
        success: false,       /*登録用or登録完了切り替え*/
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users',
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
        this.username = this.$refs.userThisName.value
        this.userid = this.$refs.userThisId.value
        this.userpass = this.$refs.userThisPass.value

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
            me.success = true
          } else {
            me.msg = response.data.error
          }
        }).catch(function (error) {
          console.log(error)
        })
      },

      /*データクリア用*/
      dataDelete: function () {
        this.$refs.userThisName.value = ''
        this.$refs.userThisId.value = ''
        this.$refs.userThisPass.value = ''
        this.resultuser = ''
        this.resultid = ''
        this.resultpass = ''
        this.message = '必要情報を入力してください'
      },

      openSignUpModal() {
        this.modal = true
      },

      closeSignUpModal() {
        this.modal = false
        this.success = false
      },
    },

  }
</script>

<style scoped>
  h2 {
    color: red;
  }

  msg2 {
    color: red;
  }

  .link {
    color: blue;
    text-decoration: underline
  }

  .modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 30;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
  }

  .modal-content {
    padding: 10px 20px;
  }

  .modal-window {
    background: #fff;
    border-radius: 4px;
    overflow: hidden;
  }

  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }

  modal-enter {
    opacity: 0;
  }

  modal-window {
    opacity: 0;
    transform: translateY(-20px);
  }

</style>
