<template>
  <div class="main" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <GameHeader></GameHeader>
    <FriendList class="listposition"></FriendList>
    <Log class="Log"></Log>
  </div>
</template>

<script>
  import GameHeader from '@/components/GameHeader';
  import Log from "@/components/LogDisplayTransition";
  import FriendList from "@/components/FriendList";

  export default {
    name: "Main",
    components: {GameHeader, Log,FriendList},
    data () {
      return {
        backgroundImageSrc: require("@/assets/main_back.jpg")
      }
    }
  };
</script>

<style scoped>
  .main{
    background: no-repeat center;
    background-size: cover;
    /*mainのサイズをちょうど画面と同じにする。*/
    height: 100vh;
  }
  .listposition{
    margin: 50vh auto 0;
    transform: translateY(-50%);
  }
  /*.news{*/

  /*}*/

</style>
