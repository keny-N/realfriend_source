<template>
  <div class="agesage">
    <!--lamdba側から送られてくる好感判定で判断する。 -->
    <!--数値に変更があったので反映してます -->
    <img v-show="agesageData<=10 && agesageData>0" src="../assets/smile.png">
    <img v-show="agesageData==0" src="../assets/normal.png">
    <img v-show="agesageData>=-10 && agesageData<0" src="../assets/shock.png">
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
