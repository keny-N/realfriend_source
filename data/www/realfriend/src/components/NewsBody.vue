<template>
  <div class="news-body">

    <h1>ニュース画面</h1>
    <ol>
      <ListMT v-for="news in newsData" :news="newsData.id" :news-data="news" @selectNews="selectNews"></ListMT>
    </ol>
<!--    <p v-if="choosingNewsFlag">{{ choosingNewsId }}</p>-->
<!--    <button @click="releaseNews">初期化</button>-->

    <transition name="fade"><!-- transitionは不要なら外してOK -->
      <div v-if="choosingNewsFlag">
        <div class="modal" @click="choosingNewsFlag=false">
        <NewsModal>
          <template v-slot:header>
            <h4 class="modal-title">{{choosingNewsTitle}}</h4>
            <button type="button" class="close" @click="choosingNewsFlag=false"></button>
          </template>
          <template v-slot:body>
            <p>{{choosingNewsBody}}</p>
          </template>
          <template v-slot:exit-button>
            <button type="button" class="btn btn-primary" @click="choosingNewsFlag=false">確認</button>
          </template>
        </NewsModal>
        </div>
        <div class="modal-backdrop show"></div>
      </div>
    </transition>

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
           {id:1,title: "観測停止のピンチから一転　岩手の電波望遠鏡、運用続く",body: "難しい"},
           {id:2,title: "観測停止のピンチから一転　岩手の電波望遠鏡、運用続く",body: "簡単"}
        ],
        choosingNewsId:0,
        choosingNewsFlag:false,
        choosingNewsTitle: "",
        choosingNewsBody: "",
      }
    },

    methods:{
      selectNews: function(Id,Title,Body) {
        // console.log(Id)
        this.choosingNewsId = Id
        this.choosingNewsFlag = true
        this.choosingNewsTitle = Title
        this.choosingNewsBody = Body
      },

      releaseNews: function () {
        this.choosingNewsId= 0
        this.choosingNewsFlag = false
        this.choosingNewsTitle= ""
        this.choosingNewsBody = ""
      }
    },
  }
</script>

<style scoped>
  .news-body {
    height: 100%;
    width: 50%;
    margin: 0 auto;
  }


  ul, li {
    width: 100%;
  }

/* 表示/非表示はvueで制御するので最初から表示状態にする */
 .modal {
  display: block;
}

/* vueのtransitionを使わないなら不要 */
.fade-enter-active, .fade-leave-active {
  transition: opacity .15s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
