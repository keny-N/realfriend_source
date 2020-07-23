<template>
  <div class="news-body">
    <InformationList :title="UpdateInformationTitle" :body-data="UpdateInformationBody"></InformationList>
<!--    <InformationList :title="title" :body-data="LogInformation"></InformationList>-->
  </div>
</template>

<script>
  import InformationList from "@/components/LogDisplayList"

  export default {
    name: "LogDisplayBody",
    components: {InformationList},
    data() {
      return {
        UpdateInformationTitle: "アップデート情報",
        UpdateInformationBody: [{title:"全米が驚愕",body:"あほくさ"}],
        LogInformation: {
          title: "ログ情報", body: [{title: "07/07/02/21", body: "削除完了"}]
        },
      }
    },

    methods: {},
  }
</script>

<style scoped>

</style>
