<template>
    <div id="statusmsg" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
      <ul v-for=" list in statusList">
        <div id=textmsg>
          {{list.Msg}}
        </div>
      </ul>
    </div>


</template>

<script>
    export default {
        name: 'StatusMsg',
        props: {
            receiveMsg: 0
        },
        data() {
            return {
                statusList: [],
                storage: "0",
                backgroundImageSrc: require("@/assets/status_back.png")
            }
        },
        methods: {
            statusMsgAdd: function () {                                     /* データを受け取ってメッセージを登録する機能です */
                let now = new Date();                                       /*時刻を表示する処理です*/
                let hour = ("0" + now.getHours()).slice(-2);                  /*時刻を表示する処理です*/
                let min = ("0" + now.getMinutes()).slice(-2);                 /*時刻を表示する処理です*/
                let time = hour + ":" + min + "       　　　　";              /*時刻を表示する処理です*/
                /*0.5から-0.5の範囲で帰って来る際に好感度判定をします。*/
              if (Number(this.receiveMsg) < 0) {
                    this.storage = time + "好感度が下がりました"
                } else if (Number(this.receiveMsg) > 0) {
                    this.storage = time + "好感度が上がりました"
                } else {
                    this.storage = time + "好感度に変化はありませんでした"
                    console.log(this.receiveMsg)
                }
                //this.storage=this.receiveMsg
                this.statusList.push({
                    Msg: this.storage            /*リストの最後に最新の好感度情報を追加する処理です*/
                })
            },

        },
        updated() {
            /*スクロールの位置を一番下に下げる処理です*/
            let element = document.getElementById("statusmsg");
            element.scrollTop = element.scrollHeight;
            return (element)
        },

    }

</script>

<style scoped>
  ul{
    padding-left:0px;
  }
  #statusmsg {
    /*場所に関してです*/
    /*スクロールに関してだとおもいます*/
    height: 30vh;
    overflow: hidden;
    overflow-y: scroll;
    overflow-x: scroll;
    background-origin: content-box;
    background: center;
    width: 100%;
    background-size: 100% 109%;
    opacity: 0.5;
  }
  #statusmsg::-webkit-scrollbar {  /* スクロールのやつが表示されるので非表示にしてます。 */
    display:none;
  }

  #textmsg {
    /*文字の下の下線です*/
    width: 90%;
    border-bottom: solid 1px #ffffff;
    color: white;
    margin: auto;
    text-align: left;
    margin-top:1em;
    font-size: 100%;
  }
</style>
