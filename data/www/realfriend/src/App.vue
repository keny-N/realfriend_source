<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
    export default {
        name: 'App',
        created() {
            window.addEventListener("beforeunload", this.confirmSave)
        },
        destroyed() {
            window.removeEventListener("beforeunload", this.confirmSave)
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
                    A: this.$store.state.aCount,
                    B: this.$store.state.bCount,
                    C: this.$store.state.cCount,
                    D: this.$store.state.dCount
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

  }
</style>
