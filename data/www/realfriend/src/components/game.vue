<template>
    <div class="game">
        <hdr></hdr>
        <h1>ゲーム画面</h1>
      <input type="number" v-model="data">
      <input type="number" v-model="data1">
      <gamefooter :data="data" :data1="data1"></gamefooter>

    </div>
</template>

<script>
    import hdr from '@/components/hdr'
    import gamefooter from "@/components/gamefooter"
    export default {
        name: "Game",
        components: {
          gamefooter:gamefooter,
          hdr:hdr,
        },
      data(){
          return{
            data:0,
            data1:0
          }
      }
    };
</script>

<style scoped>

</style>
