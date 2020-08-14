<template>
  <router-link to="/menu">
    <!--本来ならcssでFontsizeを変更すべきところだがとりあえず-->
    <input type="image" src="/static/return.png" class="image-size purupuru">
  </router-link>
</template>

<script>
    export default {
        name: "ReturnMenu"
    }
</script>

<style scoped>
  .image-size{
    width: 5%;
    position:absolute;
    left: 5%;
  }
  .purupuru {
    animation: purupuru 0.1s infinite;
  }
  @keyframes purupuru {
    0% {
      transform: translate(0px, 0px)
    }
    50% {
      transform: translate(0px, 1px) rotateZ(1deg)
    }
  }


</style>
