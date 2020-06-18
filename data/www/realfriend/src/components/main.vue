<template>
  <div class="main">
    <GameHeader></GameHeader>
    <img src="../assets/realogo.png">
    <h1>メイン画面</h1>
    <News></News>
  </div>
</template>

<script>
    import GameHeader from '@/components/GameHeader'
    import News from "@/components/News";

    export default {
        name: "Main",
        components: {GameHeader, News},
    };
</script>

<style scoped>

</style>
