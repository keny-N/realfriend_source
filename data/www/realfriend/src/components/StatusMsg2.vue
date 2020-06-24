<template>
  <div>
    <div id = "status">
      <ul v-for=" list in statuslist">
        <div id = textmsg>
          {{list.Msg}}
        </div>
      </ul>
    </div>
    <div id = "button">
      <button v-on:click="dataReceive">おして</button>
    </div>
  </div>

</template>

<script>
  export default {
    name:'StatusScrollList',
    data(){
      return{
        statuslist:[],
        storage:"0",
      }
    },
    methods:{
      dataReceive: function (/*favoriteFlg*/) {                     /* データを受け取ってメッセージを登録する機能です */
        let random = Math.round(Math.random() * 3);              /* 受け取りができないので単体テスト用の乱数生成です */
        let receiveData = random　                                 　/*  本来はここにfavoriteFlgを受け取り挿入します */
        let now = new Date();
        let Hour = ("0"+now.getHours()).slice(-2);
        let min = ("0"+now.getMinutes()).slice(-2);
        let time = Hour + ":" + min + "       　　　　";

        /* receiveData > 0 && receiveData <= 0.5 のように細かく処理を書くことになると思う */
        if (receiveData === 1) {
          this.storage = time +"好感度が下がりました　　　"
        } else if (receiveData === 3) {
          this.storage = time +"好感度が上がりました　　　"
        } else {
          this.storage = time +"好感度に変化はありませんでした"
        }

        this.statuslist.unshift({
          Msg:this.storage
        })

      },
    }
  }

</script>

<style scoped>
  #status{
    width: 60%;
    position: absolute;
    left :20%;
    bottom: 10%;
    height: 200px;
    overflow: hidden;
    overflow-y:scroll;
    text-align: left;
    background: #f83ce3;
  }
  #textmsg{
    width:350px;
    border-bottom: solid  1px #87CEFA;
  }
</style>
