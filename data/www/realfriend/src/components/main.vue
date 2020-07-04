<template>
  <div>
    <div v-if="login == true">
      <LogIn @changeuser="changeUser"></LogIn>
    </div>
    <div v-if="login == false">
      <div class="main" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
        <GameHeader></GameHeader>
        <FriendList class="listposition"></FriendList>
        <News></News>
      </div>
    </div>
  </div>
</template>

<script>
  import GameHeader from '@/components/GameHeader'
  import News from "@/components/News";
  import FriendList from "@/components/FriendList";
  import LogIn from "@/components/LogIn";

  export default {
    name: "Main",
    components: {LogIn, GameHeader, News, FriendList},
    data() {
      return {
        backgroundImageSrc: require("@/assets/main_back.jpg"),
        user_id: null,
        friends_array: [],
        login: true,
      }
    },
    methods: {
      changeUser(id) {
        this.user_id = id.id
        this.friends_array = id.ary
        this.login = false
      }
    }
  };
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
