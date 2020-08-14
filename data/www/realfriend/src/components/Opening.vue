<template>
  <div class="opening" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <LoginTransition class="login"></LoginTransition>
  </div>
</template>

<script>
  import LoginTransition from "@/components/LoginTransition"
    export default {
        name: "Opening",
      components:{LoginTransition},
      data() {
        return {
          backgroundImageSrc: require("@/assets/op.png")
        }
      },
    }
</script>

<style scoped>
  .opening {
    background: no-repeat center;
    background-size: cover;
    /*mainのサイズをちょうど画面と同じにする。*/
    height: 100vh;
  }
  .login{
    position: absolute;
    bottom: 100px;
    right: 100px;
  }
</style>
