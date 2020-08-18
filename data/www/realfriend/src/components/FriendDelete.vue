<template>
  <div class="friend-delete">
    <input type="image" src="/static/消しゴム.png" class="image-size" v-on:click="openModal">
    <div class="overlay" v-show="showContent">
      <div class="content">
        <h4>本当に削除しますか？</h4>
        <div class="card-body">
          <div>
            <img v-on:src="friendNameDelete">
          </div>
        </div>
        <div>フレンド名前：{{friendNameDelete}}</div>
        <div class="float-left font-design" v-on:click="deleteFriend">DELETE</div>
        <div class="float-right font-design" v-on:click="closeModal">CANCEL</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "FriendDelete",
    props: ['friendId', 'friendImg', 'friendName'],
    data() {
      return {
        showContent: false, //モーダルを非表示している
        imageDataDelete: this.friendImg,//画像
        friendNameDelete: this.friendName,//フレンドの名前
        friendIdDelete: this.friendId,
        deleteUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one/'//フレンド削除URL
      }
    },
    methods: {
      openModal: function () {
        this.showContent = true
      },
      closeModal: function () {
        this.showContent = false
      },
      deleteFriend() {
        //   ２０文字以内かつ一文字以上でない時に実行される。画像用の条件式も書かないと行けない
        // if (this.friendName.length > 20 || this.friendName.length < 1) {
        // }
        //画像は何も送られてこないためコメントアウトしています。
        // let imgpath=this.friendImg
        let friendId = Number(this.friendIdDelete)
        let me = this


        console.log('delete送信します')
        this.axios.delete(this.deleteUrl + friendId
        ).then(function (response) {
          if (response.data.isSuccess) {
            console.log(response)
            me.showContent = false
            me.$router.go({path: me.$router.currentRoute.path, force: true})
          }
        }).catch(function (error) {
          console.log(error)
          me.showContent = true
        })
        //メイン画面を更新する処理
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
  .font-design{
    font-family: Impact;
    color: white;
  }

  .content {
    z-index: 2;
    width: 50%;
    padding: 1em;
    background: #fec7d7;
    border-radius:30px;
  }
  .image-size{
    width: 3vmin;
  }
  .font-design:hover {
    animation: shake 2s infinite;
  }
  @keyframes shake {
    0% {
      transform: translate(2px, 0px);
    }
    5% {
      transform: translate(-2px, 0px);
    }
    10% {
      transform: translate(2px, 0px);
    }
    15% {
      transform: translate(-2px, 0px);
    }
    20% {
      transform: translate(2px, 0px);
    }
    25% {
      transform: translate(-2px, 0px);
    }
    30% {
      transform: translate(0px, 0px);
    }
  }
</style>
