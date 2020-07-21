<template>
  <div class="frienddelete">
    <button v-on:click="openModal">削除</button>
    <div class="overlay" v-show="showContent">
      <div class="content">
        <h4>本当に削除しますか？</h4>
        <div class="card-body">
          <div>
            <img v-on:src="FriendName">
          </div>
        </div>
        <div>フレンド名前：{{FriendName}}</div>
        <button class="float-left" v-on:click="deleteFrined">削除</button>
        <button class="float-right" v-on:click="closeModal">取り消し</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "FriendDelete",
    props:['friendId','FriendImg','FriendName'],
    data() {
      return {
        showContent: false, //モーダルを非表示している
        imageData: '',//画像
        friendName: '',//フレンドの名前
        deleteUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one/'//フレンド削除
      }
    },
    methods: {
      openModal: function () {
        this.showContent = true
      },
      closeModal: function () {
        this.showContent = false
      },
      deleteFrined() {
        if (this.friendName.length > 20 || this.friendName.length < 1) {
          //２０文字以内かつ一文字以上でない時に実行される。
        }

        //画像は何も送られてこないためコメントアウトしています。
        // let imgpath=this.FriendImg
        let friend_id =Number(this.friendId)
        //faceApiに顔データを送信
        console.log('put送信します')
        this.axios.delete(this.deleteUrl+friend_id
        ).then(function (response) {
          if (response.data.isSuccess) {
            console.log(response)
            this.showContent = false
          }
        }).catch(function (error) {
          console.log(error)
          this.showContent = true
        })
        //メイン画面を更新する処理
        this.$router.go({path: this.$router.currentRoute.path, force: true})
        console.log('以下')
      }
    },
  }
</script>

<style scoped>
  .overlay {
    /*　要素を重ねた時の順番　*/
    z-index: 1;

    /*　画面全体を覆う設定　*/
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5);

    /*　画面の中央に要素を表示させる設定　*/
    display: flex;
    align-items: center;
    justify-content: center;

  }

  .content {
    z-index: 2;
    width: 50%;
    padding: 1em;
    background: #fff;
  }
</style>
