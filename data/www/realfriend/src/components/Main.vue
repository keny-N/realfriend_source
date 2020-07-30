<template>
  <div class="main" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <GameHeader></GameHeader>
    <FriendList class="listposition"></FriendList>
    <FriendInsert></FriendInsert>
    <News></News>
    <button v-on:click="userProfileDisplay">変更ページ</button>
  </div>
</template>

<script>
  import GameHeader from '@/components/GameHeader'
  import News from "@/components/News"
  import FriendList from "@/components/FriendList"
  import FriendInsert from "@/components/FriendInsert"

  export default {
    name: "Main",
    components: {GameHeader, News, FriendList, FriendInsert},
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
      }

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

  .listposition {
    margin: 50vh auto 0;
    transform: translateY(-50%);
  }
</style>
