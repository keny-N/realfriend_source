<template>
  <div id="app">
    <transition mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
    import http from "../static/axios/axios"

    export default {
        name: 'App',
        beforeCreate() {
            //vueインスタンス生成時
            this.$store.dispatch("token/localStorageLoad")
        },
        created() {
            window.addEventListener("beforeunload", this.confirmSave)
        },
        destroyed() {
            window.removeEventListener("beforeunload", this.confirmSave)
            // thislog(http.request.headers.Authorization)
        },
        methods: {


            confirmSave(event) {
                this.counterSave()
                event.returnValue = "編集中のものは保存されませんが、よろしいですか？"
            },
            counterSave() {
                let me = this
                //ユーザー動向のカウンター値をDBに保存する
                this.axios.post('https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/counter', {
                    login_count: this.$store.state.counter.loginCount,
                    autoLogin_count: this.$store.state.counter.autoLoginCount,
                    camera_count: this.$store.state.counter.cameraCount,
                    news_count: this.$store.state.counter.newsCount
                }).then(function (response) {
                    me.$store.dispatch("resetCounter")
                    console.log(response)
                }).catch(function (error) {
                    console.log(error)
                })
            }
        }
    }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background-image: url("assets/log.png");
  }
  .v-enter {
    transform: translate(0, 0);
  }
  .v-enter-to {
  }
  .v-enter-active {
    transition: all 1s 0s ease;
  }
  .v-leave {
    transform: translate(0, 0);
  }
  .v-leave-to {
    transform: translate(100%, 0);
  }
  .v-leave-active {
    transition: all .5s 0s ease;
  }
</style>
