<template>
  <!-- 動的ルーティングの実装をしなければならない-->
  <div class="menu" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <Log class="log"></Log>
    <MainTransition class="main"></MainTransition>
    <ChangeSuccessTransition class="profile"></ChangeSuccessTransition>
    <router-link v-bind:to="{name:'ChangeSuccess',params:{userId:this.userId}}">
      userPro
    </router-link>
    <div v-on:click="userProfileDisplay">UserProfile</div>
  </div>
</template>

<script>
    import Log from "@/components/LogDisplayTransition"
    import MainTransition from "@/components/MainTransition"
    import ChangeSuccessTransition from "@/components/ChangeSuccessTransition"

    export default {
        name: "Menu",
      components:{Log,MainTransition,ChangeSuccessTransition},
      data() {
        return {
          backgroundImageSrc: require("@/assets/op.png")
        }
      },
      methods: {
        userProfileDisplay() {
          this.$router.push({name: 'ChangeSuccess', params: {userId: this.userId}})
        },
      }
    }
</script>

<style scoped>
  .menu {
    background: no-repeat center;
    background-size: cover;
    /*mainのサイズをちょうど画面と同じにする。*/
    height: 100vh;
  }
  .log{
    position: absolute;
    bottom: 20%;
    right: 10%;
    font-size: 6vmin;
  }
  .main{
    position: absolute;
    bottom: 32%;
    right: 10%;
    font-size: 6vmin;
  }
  .profile{
    position: absolute;
    bottom: 8%;
    right: 10%;
    font-size: 6vmin;
  }
</style>
