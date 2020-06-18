<template>
    <div class="gamebody">
      <GameHeader></GameHeader>
        <h1>ゲーム画面</h1>
      <input type="number" v-model="favoGaugeData">
      <input type="number" v-model="agesageData">
      <!-- input v-modelで宣言した値を入れている-->
      <GameFooter :favo-gauge-data="favoGaugeData" :agesage-data="agesageData"></GameFooter>

    </div>
</template>

<script>
    import GameHeader from "@/components/GameHeader";
    import GameFooter from "@/components/GameFooter"
    import FavoGauge from "@/components/FavoGauge";
    export default {
        name: "GameBody",
        components: {
          GameHeader:GameHeader,
          GameFooter:GameFooter,
          FavoGauge:FavoGauge
        },
      data(){
          return{
            favoGaugeData:0,
            agesageData:0
          }
      }
    };
</script>

<style scoped>

</style>
