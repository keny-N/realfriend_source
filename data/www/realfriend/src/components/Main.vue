<template>
  <div class="main" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <GameHeader></GameHeader>
    <FriendList class="list-position"></FriendList>
    <FriendInsert></FriendInsert>
    <Log class="Log"></Log>
    <News></News>
    <button v-on:click="userProfileDisplay">変更ページ</button>
    <!--    <button v-on:click="aIncre">{{aCount}}</button>-->
    <!--    <button v-on:click="bIncre">{{bCount}}</button>-->
    <!--    <button v-on:click="cIncre">{{cCount}}</button>-->
    <!--    <button v-on:click="dIncre">{{dCount}}</button>-->
  </div>
</template>

<script>
    import GameHeader from '@/components/GameHeader'
    import Log from "@/components/LogDisplayTransition"
    import FriendList from "@/components/FriendList"
    import FriendInsert from "@/components/FriendInsert"
    import {mapState} from "vuex"

    export default {
        name: "Main",
        components: {GameHeader, Log, FriendList, FriendInsert},
        data() {
            return {
                // backgroundImageSrc: require("@/assets/main_back.jpg")
                userId: this.$route.params.userId
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
            userProfileDisplay() {
                this.$router.push({name: 'ChangeSuccess', params: {userId: this.userId}})
            },
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
    margin: 50vh auto 0;
    transform: translateY(-50%);
  }
</style>
