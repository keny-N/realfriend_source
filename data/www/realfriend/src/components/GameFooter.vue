<template>
    <footer class="gamefooter" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
      <FavoGauge :favo-gauge-data="favoGaugeData"></FavoGauge>
      <Agesage :agesage-data="agesageData"></Agesage>
    </footer>
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
          agesageData: 0,
          backgroundImageSrc: require("@/assets/renga.jpeg")
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
  .gamefooter{
    width: ;
  }


</style>
