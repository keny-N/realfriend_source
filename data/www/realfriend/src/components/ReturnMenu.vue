<template>
  <router-link v-bind:to="{name:'Menu',params:{userId:this.userId}}">
    <!--本来ならcssでFontsizeを変更すべきところだがとりあえず-->
    <input type="image" src="/static/return.png" class="image-size">
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
  .image-size:hover {
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
