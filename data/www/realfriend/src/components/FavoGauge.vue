<template>
  <div >
    <!-- nが1から４になるまで繰り返す。-->
    <ul v-for="n of 5">
      <!--favoの値によって表示する画像を判断する -->
      <li v-show="favoGaugeData>=n">
        <img src="../assets/満ハートのマーク.png">
      </li>
      <li v-show="favoGaugeData<n">
        <img src="../assets/空ハートのマーク.png">
      </li>
    </ul>
  </div>
</template>

<script>
    export default {
      name: "FavoGauge",
      props: {
        favoGaugeData: {
          type:Number
        }
      },

    }
</script>

<style scoped>
  ul{
    list-style: none;
  }
li{
  float: left;
  width:15%;
}
  img{
    width: 10vh;
  }
</style>
