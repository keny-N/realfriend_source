<template>
    <footer>
      <!--本来であれば下のバックグラウンドが処理されるべきだが、div内にコンポーネントされているためfooterとして認識されていない
      文字などでなく画像のためfavogaugeのulが高さを認識しない。
      そのため次にコンポーネントを呼び出しているGameBody内で画像を設定している。
      <div class="gamefooter" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
      -->
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
          backgroundImageSrc: require("@/assets/game_footer.jpg")
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

  /*本来であれば下のバックグラウンドが処理されるべきだが、div内にコンポーネントされているためfooterとして認識されていない */
  .gamefooter{
    background-size: cover;
  }

</style>
