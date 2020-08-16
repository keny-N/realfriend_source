<template>
  <div class="main" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <ReturnMenu></ReturnMenu>
    <FriendList class="list-position"></FriendList>
    <FriendInsert></FriendInsert>
    <!--    <button v-on:click="aIncre">{{aCount}}</button>-->
    <!--    <button v-on:click="bIncre">{{bCount}}</button>-->
    <!--    <button v-on:click="cIncre">{{cCount}}</button>-->
    <!--    <button v-on:click="dIncre">{{dCount}}</button>-->
  </div>
</template>

<script>
    import Log from "@/components/LogDisplayTransition"
    import FriendList from "@/components/FriendList"
    import FriendInsert from "@/components/FriendInsert"
    import ReturnMenu from "@/components/ReturnMenu"
    import {mapState} from "vuex"

    export default {
        name: "Main",
        components: {Log, FriendList, FriendInsert,ReturnMenu},
        data() {
            return {
                backgroundImageSrc: require("@/assets/main_back.jpg")
            }
        },
        computed: {
            // ...mapState({
            //     aCount: state => state.counter.aCount,
            //     bCount: state => state.counter.bCount,
            //     cCount: state => state.counter.cCount,
            //     dCount: state => state.counter.dCount,
            // })
        },

      methods: {
            //カウンターテスト用
            // aIncre() {
            //     this.$store.dispatch("counter/increment", "a")
            // },
            // bIncre() {
            //     this.$store.dispatch("counter/increment", "b")
            // },
            // cIncre() {
            //     this.$store.dispatch("counter/increment", "c")
            // },
            // dIncre() {
            //     this.$store.dispatch("counter/increment", "d")
            // }
        }
    }
</script>

<style scoped>
  .main {
    background: no-repeat center;
    background-size: cover;
    /*mainのサイズをちょうど画面と同じにする。*/
    height: 100vh;
  }

  .list-position {
    position: relative;
    top: 10%;
  }
</style>

