<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="closeLogOutModal" v-if="modal">
      <div class="modal-window">
        <div class="modal-content">
          <slot/>
          <!-- コンポーネント MyModal -->
          <!-- default スロットコンテンツ -->
          <div>
            <h1>ログアウトしますか？？</h1>
            <button v-on:click="logOut">ログアウト</button>
            <button v-on:click="closeLogOutModal">キャンセル</button>

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
    name: "LogOut",
    data() {
      return {
        userId: this.$route.params.userId,
        modal:false,
      }
    },
    methods: {
      logOut(){
        this.$router.push({path: '/login'})
      },
      openLogOutModal() {
        this.modal = true
      },

      closeLogOutModal() {
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
