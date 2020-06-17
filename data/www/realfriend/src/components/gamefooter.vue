<template>
    <div class="gamefooter">
      <imgchange :favo="data"></imgchange>
      <agesage :point="data1"></agesage>
    </div>
</template>

<script>
  import agesage from "@/components/agesage";
  import imgchange from "@/components/imgchange";
  import Imgchange from "./imgchange";
  import Agesage from "./agesage";
    export default {
        name: "footer",
      components: {Agesage, Imgchange},
      comments:{
        agesage:agesage,
        imgchange:imgchange
      },
      props:{
          data:{
            type:Number
          },
        data1:{
          type:Number
        }
      }
    }
</script>

<style scoped>


</style>
