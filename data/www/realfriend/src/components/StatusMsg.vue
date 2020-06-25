<template>
  <div>
    <div id="status" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
      <ul v-for=" list in statuslist">
        <div id=textmsg>
          {{list.Msg}}
        </div>
      </ul>
    </div>
  </div>

</template>

<script>
    export default {
        name: 'StatusMsg2',
        data() {
            return {
                statuslist: [],
                storage: "0",
                backgroundImageSrc: require("@/assets/status_back.png")
            }
        },
        methods: {
            dataReceive: function (/*favoriteFlg*/) {                     /* データを受け取ってメッセージを登録する機能です */
                let random = Math.round(Math.random() * 3);              /* 受け取りができないので単体テスト用の乱数生成です */
                let receiveData = random　                                 　/*  本来はここにfavoriteFlgを受け取り挿入します */
                let now = new Date();                                       /*時刻を表示する処理です*/
                let hour = ("0" + now.getHours()).slice(-2);                  /*時刻を表示する処理です*/
                let min = ("0" + now.getMinutes()).slice(-2);                 /*時刻を表示する処理です*/
                let time = hour + ":" + min + "       　　　　";              /*時刻を表示する処理です*/

                /* receiveData > 0 && receiveData <= 0.5 のように細かく処理を書くことになると思う */
                if (receiveData === 1) {
                    this.storage = time + "好感度が下がりました　　　"
                } else if (receiveData === 3) {
                    this.storage = time + "好感度が上がりました　　　"
                } else {
                    this.storage = time + "好感度に変化はありませんでした"
                }

                this.statuslist.push({
                    Msg: this.storage            /*リストの最後に最新の好感度情報を追加する処理です*/
                })
            },

        },
        updated() {
            /*スクロールの位置を一番下に下げる処理です*/
            let element = document.getElementById("status");
            element.scrollTop = element.scrollHeight;
            return (element)
        }
    }

</script>

<style scoped>
  ul{
    padding-left:0px;
  }
  #status {
    /*場所に関してです*/
    /*スクロールに関してだとおもいます*/
    height: 190px;
    overflow: hidden;
    overflow-y: scroll;
    overflow-x: scroll;
    background-origin: content-box;
    background: no-repeat;
    width: 100%;
    background-size: 100% 100%;;
  }

  #textmsg {
    /*文字の下の下線です*/
    width: 90%;
    border-bottom: solid 1px #ffffff;
    color: white;
    margin: auto;
    text-align: left;
  }
</style>
