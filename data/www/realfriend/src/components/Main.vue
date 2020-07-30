<template>
  <div class="main" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <GameHeader></GameHeader>
    <FriendList class="list-position"></FriendList>
    <FriendInsert></FriendInsert>
    <Log class="Log"></Log>
    <News></News>
    <button v-on:click="userProfileDisplay">変更ページ</button>
    <!--    <button v-on:click="aIncre">{{$store.state.aCount}}</button>-->
    <!--    <button v-on:click="bIncre">{{$store.state.bCount}}</button>-->
    <!--    <button v-on:click="cIncre">{{$store.state.cCount}}</button>-->
    <!--    <button v-on:click="dIncre">{{$store.state.dCount}}</button>-->
  </div>
</template>

<script>
  import GameHeader from '@/components/GameHeader'
  import Log from "@/components/LogDisplayTransition"
  import FriendList from "@/components/FriendList"
  import FriendInsert from "@/components/FriendInsert"

  export default {
    name: "Main",
    components: {GameHeader, Log, FriendList, FriendInsert},
    data() {
      return {
        backgroundImageSrc: require("@/assets/main_back.jpg"),
        user_id: this.$route.params.userId
      }
    },
    methods: {
      userProfileDisplay() {
        let textUrl = '/user/' + this.user_id + '/success'
        this.$router.push({path: textUrl, params: {userId: this.userid}})
      },
      //カウンターテスト用
      aIncre() {
        this.$store.dispatch("increment", "a")
      },
      bIncre() {
        this.$store.dispatch("increment", "b")
      },
      cIncre() {
        this.$store.dispatch("increment", "c")
      },
      dIncre() {
        this.$store.dispatch("increment", "d")
      }
    },

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
