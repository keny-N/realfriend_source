<template>

  <div class="dis">

    <table>
      <tr>
        <td class="odd">{{ msg1 }}</td>
      </tr>
      <tr>
        <td class="even">{{ msg2 }}</td>
      </tr>
      <tr>
        <td class="odd">{{ msg3 }}</td>
      </tr>
      <tr>
        <td class="even">{{ msg4 }}</td>
      </tr>
    </table>

    <!-- このボタンは撮影ボタン等の開始させる処理に置き換えられると思います　-->
    <button v-on:click="dataReceive">おして</button>
    　
  </div>

</template>


<script>
  export default {
    name: 'favoriteDisplay',

    data() {
      return {

        msg1: "１つ目の通知",
        msg2: "２つ目の通知",
        msg3: "３つ目の通知",
        msg4: "４つ目の通知",
        storage: "一時的な保存場所だよ"

      }
    },

    methods: {
      dataReceive: function (/*favoriteFlg*/) {                     /* データを受け取ってメッセージを登録する機能です */
        let random = Math.round(Math.random() * 3);              /* 受け取りができないので単体テスト用の乱数生成です */
        let receiveData = random　                                 　/*  本来はここにfavoriteFlgを受け取り挿入します */

        /* receiveData > 0 && receiveData <= 0.5 のように細かく処理を書くことになると思う */
        if (receiveData === 1) {
          this.storage = "好感度が下がりました"
        } else if (receiveData === 3) {
          this.storage = "好感度が上がりました"
        } else {
          this.storage = "好感度に変化はありませんでした"
        }

        this.favoriteDisplay(); /* 表示を更新させる関数を呼びます */
        /* 将来的に今の好感度の表示処理などのために一応分離しておきました */

      },

      favoriteDisplay: function () { /* メッセージを一つずつ上にあげ最後に新しいデータを挿入する機能です */
        this.msg1 = this.msg2
        this.msg2 = this.msg3
        this.msg3 = this.msg4
        this.msg4 = this.storage

      }

    }

  }
</script>


<style scoped>

  table {
    /*どの環境からでも位置を調整するためにabsolute + % です*/
    width: 100%;
    position: absolute;
    bottom: 10%;
  }

  /* カメラ映像の上にあるので見やすくするために背景色　＋　文字白です */
  td.odd {
    font-weight: normal;
    color: #ffffff;
    background-color: #696969;
  }

  td.even {
    font-weight: normal;
    color: #ffffff;
    background-color: #a9a9a9;
  }
</style>
