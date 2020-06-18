<template>
  <div class="game">
    <hdr></hdr>
    <h1>ゲーム画面</h1>
    <Camera></Camera>
  </div>
</template>

<script>
    import hdr from '@/components/hdr'
    import Camera from '@/components/Camera'

    export default {
        name: "Game",
        components: {hdr, Camera}
    };
</script>

<style scoped>

</style>
