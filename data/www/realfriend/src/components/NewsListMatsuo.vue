<template>
  <li @click="newsClick()">{{ NewsData.title }}</li>
</template>

<script>
  export default {
    name: "ListMT",
    props: {
      NewsData: {
        type: Object,
        required: true,
        defalut: "ニュースなし"
      }
    },
    methods: {
      newsClick: function () {
        this.$emit("selectNews", this.NewsData.id, this.NewsData.title, this.NewsData.body)
        // console.log(this.NewsData)
      }
    }
  }
</script>

<style scoped>
  li {
    list-style: none;
    margin-left: -20px;
  }
</style>
