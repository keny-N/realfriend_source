<template>
    <div class="main">
        <GameHeader></GameHeader>
        <img src="../assets/realogo.png">
        <h1>メイン画面</h1>
    </div>
</template>

<script>
    import GameHeader from '@/components/GameHeader'
    export default {
        name: "Main",
        components: { GameHeader },
    };
</script>

<style scoped>

</style>
