<template>
  <div>
    <div id = "statusmsg">
      <ul v-for=" list in statusList">
        <div id = textmsg>
           {{list.Msg}}
        </div>
      </ul>
    </div>
  </div>

</template>

<script>
  export default {
    name:'StatusMsg',
    props:{
      receiveMsg:{
        type:Number,
        default:999
      }
    },
    data(){
      return{
        statusList:[],
        storage:"0",
      }
    },
    methods:{
      statusMsgAdd:function() {                                     /* データを受け取ってメッセージを登録する機能です */
        let now = new Date();                                       /*時刻を表示する処理です*/
        let hour = ("0"+now.getHours()).slice(-2);                  /*時刻を表示する処理です*/
        let min = ("0"+now.getMinutes()).slice(-2);                 /*時刻を表示する処理です*/
        let time = hour + ":" + min + "       　　　　";              /*時刻を表示する処理です*/

        /*0.5から-0.5の範囲で帰って来る際に好感度判定をします。*/
        if (this.receiveMsg > 0.5 || this.receiveMsg < -0.5) {
          this.storage = time + "エラーです"
        }
        else if (this.receiveMsg < 0) {
          this.storage = time +"好感度が下がりました"
        } else if (this.receiveMsg > 0) {
          this.storage = time +"好感度が上がりました"
        } else {
          this.storage = time +"好感度に変化はありませんでした"
        }

        this.statusList.push({
          Msg:this.storage            /*リストの最後に最新の好感度情報を追加する処理です*/
        })
      },

    },
    updated() {
      /*スクロールの位置を一番下に下げる処理です*/
      let element = document.getElementById("statusmsg");
      element.scrollTop = element.scrollHeight;
      return(element)
    },

  }

</script>

<style scoped>
  #statusmsg {
    /*場所に関してです*/
    width: 60%;
    position: absolute;
    left :20%;
    bottom: 10%;
    /*スクロールに関してだとおもいます*/
    height: 200px;
    overflow: hidden;
    overflow-y: scroll;
    overflow-x: scroll;
    background: #f83ce3;
    background-origin: content-box;
  }

  #textmsg {
    /*文字の下の下線です*/
    width: 350px;
    border-bottom: solid 1px #87CEFA;
  }
</style>
