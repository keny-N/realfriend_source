<template>
  <router-link v-bind:to="{name:'ChangeSuccess',params:{userId:this.userId}}">
    <!--本来ならcssでFontsizeを変更すべきところだがとりあえず-->
    UserProfile
    <!--
    <button type="button" class="btn btn-primary btn-sm">更新情報</button>
    -->
  </router-link>
</template>

<script>
    export default {
        name: "ChangeSuccessTransition"
    }
</script>

<style scoped>

</style>
