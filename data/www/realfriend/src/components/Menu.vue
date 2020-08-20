<template>
  <!-- 動的ルーティングの実装をしなければならない-->
  <div class="menu" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <Log class="log"></Log>
    <MainTransition class="main"></MainTransition>
    <ChangeSuccessTransition class="profile"></ChangeSuccessTransition>
  </div>
</template>

<script>
    import Log from "@/components/LogDisplayTransition"
    import MainTransition from "@/components/MainTransition"
    import ChangeSuccessTransition from "@/components/ChangeSuccessTransition"

    export default {
        name: "Menu",
      components:{Log,MainTransition,ChangeSuccessTransition},
      data() {
        return {
          backgroundImageSrc: require("@/assets/op2.png")
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
    bottom: 20%;
    right: 10%;
    font-size: 6vmin;
    text-decoration: none;
  }
  .main{
    position: absolute;
    bottom: 32%;
    right: 10%;
    font-size: 6vmin;
    text-decoration: none;
  }
  .profile{
    position: absolute;
    bottom: 8%;
    right: 10%;
    font-size: 6vmin;
    text-decoration: none;
  }
  .log:hover {
    animation: shake 2s infinite;
  }
  .main:hover{
    animation: shake 2s infinite;
  }
  .profile:hover{
    animation: shake 2s infinite;
  }
  @keyframes shake {
    0% {
      transform: translate(2px, 0px);
    }
    5% {
      transform: translate(-2px, 0px);
    }
    10% {
      transform: translate(2px, 0px);
    }
    15% {
      transform: translate(-2px, 0px);
    }
    20% {
      transform: translate(2px, 0px);
    }
    25% {
      transform: translate(-2px, 0px);
    }
    30% {
      transform: translate(0px, 0px);
    }
  }
</style>
