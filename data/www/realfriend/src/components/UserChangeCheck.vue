<template>
  <transition name="modal" appear>
    <div class="modal-overlay" v-if="modal" @click.self="closeSignUpModal">
      <div class="modal-window">
        <div class="modal-content">
          <slot/>
          <div>
            {{userid}}
            <form>
              <p>
                <msg1>パスワードを入力してください</msg1>
                <br>
                <input type="password" ref="userThisPass" placeholder="パスワード" required="required">
              </p>
              <button v-on:click="changeCheck">ok</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: "UserChangeCheck",
    data() {
      return {
        userid: '',
        userpass: '',
        modal:false,
        apiUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login',
      }
    },
    methods: {
      changeCheck() {
        let me = this
        this.userpass = this.$refs.userThisPass.value
        this.axios.post(this.apiUrl, {
          user_id: String(this.userid),
          user_pass: String(this.userpass),
        }).then(function (response) {
          if (response.data.isSuccess == true) {
            console.log('a')
            me.modal = false
            me.$emit('succses')
          } else {
            console.log('b')
            me.message = 'IDもしくはパスワードが間違っています'
          }
        }).catch(function (error) {
          console.log('c')
          console.log(error)
        })
      },
      openSignUpModal() {
        this.modal = true
      },

      closeSignUpModal() {
        this.modal = false
        this.success = false
      },
    },
    created() {
      this.userid = window.location.href.slice(window.location.href.indexOf('=') + 1)
    }
  }
</script>

<style scoped>

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
