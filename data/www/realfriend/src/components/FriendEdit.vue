<template>
  <div class="friend-edit">
    <input type="image" src="/static/enpitu.png" class="image-size" v-on:click="openModal">
    <div class="overlay" v-show="showContent">
      <div class="content">
        <h4>フレンド編集</h4>
        <div class="card-body">
          <div>
            <img v-on:src="imageDataEdit" v-if="imageDataEdit">
          </div>
          <h4 class="card-title">画像を選んでください。</h4>
          <input type="file" accept="image/*" @change="onImgRegister($event)" v-model="ImageDataEdit">
        </div>
        <div>フレンド名前：<input v-model="friendNameEdit"></div>
        <button class="float-left" v-on:click="editFriend">変更</button>
        <button class="float-right" v-on:click="closeModal">取り消し</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "FriendEdit",
    props: ['friendId', 'imageData', 'friendName'],
    data() {
      return {
        showContent: false, //モーダルを非表示している
        imageDataEdit: '',//画像
        friendNameEdit: this.friendName,//フレンドの名前
        friendIdEdit: this.friendId,
        Url: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one/'//フレンド編集
      }
    },
    methods: {
      openModal: function () {
        this.showContent = true
      },
      closeModal: function () {
        this.showContent = false
      },
      onImgRegister(e) {
        const files = e.target.files
        let me = this

        if (files.length > 0) {

          const file = files[0]
          const reader = new FileReader()
          reader.onload = (e) => {
            me.imageDataEdit = e.target.result
          }
          reader.readAsDataURL(file)
        }
      },
      editFriend() {
        //今後文字数の制限が必要となると思うので、画像保存時ようの条件式を書かないといけない。
        //if (this.friendName.length > 20 || this.friendName.length < 1) {
        //}

        let name = this.friendNameEdit
        //画像は何も送られてこないためコメントアウトしています。
        // let imgpath=this.friendImg
        //　動的ルーティングでのuseridを取得するため、子コンポーネントなので取得できているかは不明
        //let user_id =Number(this.$route.params.userid)
        let friendId = Number(this.friendIdEdit)
        let putUrl = this.Url + friendId
        //if文のなかだとthisがスコープの都合で参照できないためmeに入れている。
        let me = this

        console.log('put送信します')
        this.axios.put(putUrl, {
          //ログとして表示する際に使用するためユーザーIDを送る
          //ログインの動的ルーティングが確認できないので1を入れてます。
          user_id: '1',
          friend_name: name,
          //現在はパスが確定していないためパスっぽい文字を入れているだけです。
          friend_img: '/jk/matuo'
        }).then(function (response) {
          if (response.data.isSuccess) {
            console.log(response)
            //ifのなかでthisは使えない
            me.closeModal()
            me.$router.go({path: me.$router.currentRoute.path, force: true})
          }
        }).catch(function (error) {
          console.log(error)
          //ifのなかでthisは使えない
          me.openModal()
        })
        //メイン画面を更新する処理
        //this.$router.go({path: this.$router.currentRoute.path, force: true})
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
    border-radius:30px;
  }
  .image-size{
    width: 3vmin;
  }
  .yureru-s {
    animation: yureru-s 2s infinite;
  }
  @keyframes yureru-s {
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
