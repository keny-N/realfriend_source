<template>
  <div class="agesage">
    <!--lamdba側から送られてくる好感判定で判断する。 -->
    <!--ここに張っている画像はテスト用 -->
    <img v-show="agesageData==1" src="../assets/favo_plus_test.svg">
    <img v-show="agesageData==0" src="../assets/logo.png">
    <img v-show="agesageData==-1" src="../assets/realogo.png">
  </div>
</template>

<script>
    export default {
        name: "Agesage",
      props:{
        agesageData:{
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
