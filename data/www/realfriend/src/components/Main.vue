<template>
  <div class="main" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <GameHeader></GameHeader>
    <FriendList class="listposition"></FriendList>
    <FriendInsert></FriendInsert>
    <Log class="Log"></Log>
  </div>
</template>

<script>
  import GameHeader from '@/components/GameHeader';
  import Log from "@/components/LogDisplayTransition";
  import FriendList from "@/components/FriendList";
  import FriendInsert from "@/components/FriendInsert";

  export default {
    name: "Main",
    components: {GameHeader, Log,FriendList,FriendInsert},
    data () {
      return {
        backgroundImageSrc: require("@/assets/main_back.jpg")
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
