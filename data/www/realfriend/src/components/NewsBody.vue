<template>
  <div class="news-body">
    <h1>ニュース画面</h1>
    <ol>
      <ListMT v-for="news in newsData" :news="newsData.id" :news-data="news" @selectNews="selectNews"></ListMT>
    </ol>
<!--    <p v-if="choosingNewsFlag">{{ choosingNewsId }}</p>-->
<!--    <button @click="releaseNews">初期化</button>-->

    <div class="p-modal" :class="{'is-open': choosingNewsFlag}">
<!--        {{choosingNewsText}}-->
      <p>こんにちは</p>
    </div>

<!--    <NewsModal v-if="choosingNewsFlag" :news-data="newsData.id(choosingNewsId)" @releaseNews="releaseNews" >-->
<!--     &lt;!&ndash; default スロットコンテンツ &ndash;&gt;-->
<!--      <p v-for="news in newsData" :news="newsData.id" v-if="news === choosingNewsId">-->
<!--        {{ news.title }}-->
<!--      <p>-->
<!--      <div><input v-model="message"></div>-->

<!--    </NewsModal>-->
  </div>

</template>

<script>
  import ListMT from "@/components/NewsListMatsuo";
  import NewsModal from "@/components/NewsModal";

  export default {
    name: "NewsBody",
    components: {ListMT,NewsModal},
    data() {
      return {
        newsData: [
           {id:1,title: "観測停止のピンチから一転　岩手の電波望遠鏡、運用続く"},
           {id:2,title: "観測停止のピンチから一転　岩手の電波望遠鏡、運用続く"}
        ],
        choosingNewsId:0,
        choosingNewsFlag:false,
        // choosingNewsText : this.newsData.title.filter(x => this.newsData.id === this.choosingNewsId)
      }
    },

    methods:{
      selectNews: function(Id) {
        // console.log(Id)
        this.choosingNewsId = Id
        this.choosingNewsFlag = true
        // console.log(this.choosingNewsText)
      },

      releaseNews: function () {
        this.choosingNewsId= 0
        this.choosingNewsFlag = false
      }
    }
  }
</script>

<style scoped>
  .news-body {
    height: 100%;
    width: 50%;
    margin: 0 auto;
  }

  .overflow-auto {
    width: 100%;
    height: 30vh;
    margin: auto auto;
    overflow-x: visible;
  }

  ul, li {
    width: 100%;
  }

  .p-modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  overflow-y: auto;
  visibility: hidden;
  opacity: 0;
  z-index: -1;

  }

  .p-modal.is-open{
    visibility: visible;
    opacity: 1;
    z-index: 100;
}
</style>
