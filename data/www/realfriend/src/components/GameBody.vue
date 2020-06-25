<template>
  <div class="gamebody">
    <GameHeader></GameHeader>
    <h1>ゲーム画面</h1>
    <p>{{fromFaceapiMsg}}</p>
    <camera @updateMsg="updateFaceapiMsg"></camera>
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
    import Camera from "@/components/Camera";

    export default {
        name: "GameBody",
        components: {
            GameHeader: GameHeader,
            GameFooter: GameFooter,
            FavoGauge: FavoGauge,
            Camera: Camera
        },
        data() {
            return {
                favoGaugeData: 0,
                agesageData: 0,
                fromFaceapiMsg: "あ"
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

</style>
