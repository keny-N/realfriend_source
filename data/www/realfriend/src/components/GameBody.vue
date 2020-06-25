<template>
  <!--本来であればgamefooterで処理されるべきだが、div内にコンポーネントされているためfooterとして認識されていない
      文字などでなく画像のためfavogaugeのulが高さを認識しない。
      そのためコンポーネントとして呼び出しているGameBody内で画像を設定している。-->
  <div class="gamebody" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <GameHeader></GameHeader>
    <camera @updateMsg="updateFaceapiMsg"></camera>
    <!-- input v-modelで宣言した値を入れている-->
    <GameFooter :favo-gauge-data="favoGaugeData" :agesage-data="agesageData"></GameFooter>
  </div>
</template>

<script>
    import GameHeader from "@/components/GameHeader";
    import GameFooter from "@/components/GameFooter"
    import FavoGauge from "@/components/FavoGauge";
    import Camera from "@/components/Camera";
    import StatusMsg from "@/components/StatusMsg";

    export default {
        name: "GameBody",
        components: {
            GameHeader: GameHeader,
            GameFooter: GameFooter,
            FavoGauge: FavoGauge,
            Camera: Camera,
            StatusMsg: StatusMsg
        },
        data() {
            return {
                favoGaugeData: 0,
                agesageData: 0,
                fromFaceapiMsg: "あ",
                backgroundImageSrc: require("@/assets/game_footer.jpg")
            }
        },
        methods: {
            updateFaceapiMsg(msg) {
                this.fromFaceapiMsg = msg
            }
        }
    };
</script>

<style scoped>
  .gamebody{
    /*gamebodyのサイズをちょうど画面と同じにする。*/
    height:100vh;
    background-size: cover;
  }

</style>
