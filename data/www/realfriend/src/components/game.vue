<template>
  <div class="game">
    <hdr></hdr>
    <h1>ゲーム画面</h1>
    <camera></camera>
  </div>
</template>

<script>
    import hdr from '@/components/hdr'
    import camera from '@/components/camera'

    export default {
        name: "Game",
        components: {hdr, camera}
    };
</script>

<style scoped>

</style>
