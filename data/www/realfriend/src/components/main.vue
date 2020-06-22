<template>
  <div class="main">
    <GameHeader></GameHeader>
    <img src="../assets/realogo.png">
    <h1>メイン画面</h1>
    <FriendList></FriendList>
    <News></News>
  </div>
</template>

<script>
    import GameHeader from '@/components/GameHeader'
    import News from "@/components/News";
    import FriendList from "@/components/FriendList";

    export default {
        name: "Main",
        components: {GameHeader, News,FriendList},
    };
</script>

<style scoped>

</style>
