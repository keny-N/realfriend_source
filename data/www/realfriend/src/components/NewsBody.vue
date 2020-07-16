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
            <template v-slot:footer>
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
  import ListMT from "@/components/NewsListMatsuo"
  import NewsModal from "@/components/NewsModal"

  export default {
    name: "NewsBody",
    components: {ListMT, NewsModal},
    data() {
      return {
        newsData: [
          {
            id: 1,
            title: "「はやぶさ2」地球帰還は12月6日",
            body: "昨年11月に小惑星「リュウグウ」を出発した探査機「はやぶさ2」は現在、地球まで9200万kmのところまで戻ってきている。太陽からの距離は約2億kmで、地球を外側から追いかける方向に飛行中で、残る航程は約3.2億kmだ。" +
              " これまで「はやぶさ2」の地球帰還は今年11～12月と発表されていたが、本日の記者発表会でその日付が12月6日（日）と発表された。JAXAでは宇宙物体のオーストラリアへの着陸許可を申請中で、許可取得に向けてJAXAとオーストラリア宇宙庁が協力して作業を実施中だ。" +
              "「はやぶさ2」は今後、9月中旬ごろまでイオンエンジン航行を続け、10月からは化学推進系を用いた軌道微調整を数回行う。そして地球帰還時に、リュウグウのサンプルが入っているとみられるカプセルを分離する。カプセル分離後、「はやぶさ2」は別の天体を目指して飛行を続ける予定だ。"
          },
          {id: 2, title: "観測停止のピンチから一転　岩手の電波望遠鏡、運用続く", body: "簡単"}
        ],
        choosingNewsFlag: false,
        choosingNewsTitle: "",
        choosingNewsBody: "",
      }
    },

    methods: {
      selectNews: function (Id, Title, Body) {
        // console.log(Id)
        this.choosingNewsId = Id
        this.choosingNewsFlag = true
        this.choosingNewsTitle = Title
        this.choosingNewsBody = Body
      },

      releaseNews: function () {
        this.choosingNewsId = 0
        this.choosingNewsFlag = false
        this.choosingNewsTitle = ""
        this.choosingNewsBody = ""
      },
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
