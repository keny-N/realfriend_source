<template>
  <!-- 動的ルーティングの実装をしなければならない-->
  <div class="menu" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <Log class="log"></Log>
    <MainTransition class="main"></MainTransition>
  </div>
</template>

<script>
    import Log from "@/components/LogDisplayTransition"
    import MainTransition from "@/components/MainTransition"

    export default {
        name: "Menu",
      components:{Log,MainTransition},
      data() {
        return {
          backgroundImageSrc: require("@/assets/op.png")
        }
      },
    }
</script>

<style scoped>
  .menu {
    background: no-repeat center;
    background-size: cover;
    /*mainのサイズをちょうど画面と同じにする。*/
    height: 100vh;
  }
  .log{
    position: absolute;
    bottom: 8%;
    right: 10%;
    font-size: 6vmin;
  }
  .main{
    position: absolute;
    bottom: 20%;
    right: 10%;
    font-size: 6vmin;
  }
</style>
