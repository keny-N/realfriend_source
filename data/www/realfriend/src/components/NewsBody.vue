<template>
  <div class="news-body">
    <h1>ニュース画面</h1>
    <ListMT></ListMT>
    <ListMT></ListMT>
  </div>
</template>

<script>
  import ListMT from "@/components/NewsListMatsuo";

  export default {
      name: "NewsBody",
      components: {ListMT}
  }
</script>

<style scoped>
  .news-body{
    height: 100%;
    width: 50%;
    margin: 0 auto;
  }
</style>
