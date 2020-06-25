<template>
  <header class="gameheader">
    <router-link to="/">
      <button type="button" class="btn btn-primary btn-sm">メイン</button>
    </router-link>
    <router-link to="/game">
      <button type="button" class="btn btn-primary btn-sm">ゲーム</button>
    </router-link>
  </header>
</template>

<script>
    export default {
        name: "GameHeader"
    }
</script>

<style scoped>
  .gameheader{
    background-color: #0b2e13;
  }

</style>
