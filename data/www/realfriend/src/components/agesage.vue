<template>
  <div class="agesage">
    <!--lamdba側から送られてくる好感判定で判断する。 -->
    <img v-show="point==1" src="../assets/143eab27e07514ea.svg">
    <img v-show="point==0" src="../assets/logo.png">
    <img v-show="point==-1" src="../assets/realogo.png">
  </div>
</template>

<script>
    export default {
        name: "agesage",
      props:{
        point:{
          type:Number
        }
      }
    }
</script>

<style scoped>
.agesage{
  float: left;
  width:35%;
}
  img{
    width: 30%;
  }
</style>
