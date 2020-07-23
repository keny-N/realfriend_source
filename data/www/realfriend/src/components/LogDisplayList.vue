<template>
  <h1>{{title}}</h1>
  <h2>{{bodyData}}</h2>

  <ol>
    <li v-for="data in bodyData" :key="data">{{data.title}}:{{data.body}}</li>
  </ol>
</template>

<script>
  export default {
    name: "LogDisplay",
    props: {
      title: {
        type: String,
      },
      bodyData:{
        type:Object,
      },
    },
  }

</script>

<style scoped>
  li {
    list-style: none;
    margin-left: -20px;
  }
</style>
