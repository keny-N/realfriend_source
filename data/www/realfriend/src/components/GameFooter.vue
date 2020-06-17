<template>
    <div class="gamefooter">
      <FavoGauge :favo-gauge-data="favoGaugeData"></FavoGauge>
      <Agesage :agesage-data="agesageData"></Agesage>
    </div>
</template>

<script>
  import Agesage from "@/components/Agesage";
  import FavoGauge from "@/components/FavoGauge";
    export default {
        name: "GameFooter",
      components:{Agesage,FavoGauge},
      comments:{
        Agesage:Agesage,
        FavoGauge:FavoGauge
      },
      data() {
        return {
          favoGaugeData: 0,
          agesageData: 0
        }
      },
      props:{
          favoGaugeData:{
            type:Number
          },
        agesageData:{
          type:Number
        }
      }
    }
</script>

<style scoped>


</style>
