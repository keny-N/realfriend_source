<template>
  <div class="imagchange">
    <!-- nが1から４になるまで繰り返す。-->
    <ul v-for="n of 4">
      <!--favoの値によって表示する画像を判断する -->
      <li v-show="favo>=n">
        <img src="../assets/ハートのマーク.png">
      </li>
      <li v-show="favo<n">
        <img src="../assets/ハートのマーク2.png">
      </li>
    </ul>


  </div>

</template>

<script>
    export default {
      name: "imgchange",
      props: {
        favo: {
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
    width: 50%;
  }
</style>
