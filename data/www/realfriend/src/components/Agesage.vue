<template>
  <div class="agesage">
    <!--lamdba側から送られてくる好感判定で判断する。 -->
    <!--数値に変更があったので反映してます -->
    <img v-show="agesageData>0" src="../assets/smile.png">
    <img v-show="agesageData==0" src="../assets/normal.png">
    <img v-show="agesageData<0" src="../assets/shock.png">
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
  position: absolute;
  right: 5vh;
  width: 25%;
}
  img{
    width: 30%;
  }
</style>
