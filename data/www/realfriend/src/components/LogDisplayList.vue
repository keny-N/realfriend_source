<template>
  <div>
    <h1>{{dataList.title}}</h1>
    <div class="news-list overflow-auto">
      <ol>
        <li v-for="data in dataList.body" :key="data.title">{{data.title}}:{{data.body}}</li>
      </ol>
    </div>
  </div>
</template>

<script>
  export default {
    name: "LogDisplay",
    props: {
      dataList: {
        type: Object
      }
    }
  }

</script>

<style scoped>
  li {
    list-style: none;
    margin-left: -20px;
  }
  div:first-child{
    height: 30vh;
    margin-bottom: 5vh;
  }
  h1{
    height: 5vh;
  }
  .news-list{
    border: #1b1e21 solid 1px;
    height: 25vh;
  }
</style>
