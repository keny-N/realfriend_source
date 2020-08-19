<template>
  <div class="friend-delete">
    <input type="image" src="/static/消しゴム.png" class="image-size" v-on:click="openModal">
    <div class="overlay" v-show="showContent">
      <div class="content">
        <h4>本当に削除しますか？</h4>
        <div class="card-body">
          <div>
            <img v-on:src="friendImg">
          </div>
        </div>
        <div>フレンド名前：{{friendName}}</div>
        <div class="float-left float-left-position font-design" v-on:click="deleteFriend">削除</div>
        <div class="float-right float-right-position font-design" v-on:click="closeModal">取り消し</div>
      </div>
    </div>
  </div>
</template>

<script>

    import http from "../../static/axios/axios"

    export default {
        name: "FriendDelete",
        props: ['friendId', 'friendImg', 'friendName'],
        data() {
            return {
                showContent: false, //モーダルを非表示している
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
                let friendId = Number(this.friendId)
                let me = this


                console.log('delete送信します')

                http.interceptors.request.use(request => {
                    request.headers.Authorization = this.$store.getters['token/tokenGet']
                    return request
                })
                console.log(friendId)
                http.delete(this.deleteUrl + friendId, {data: {'friend_name': this.friendName}})
                    .then(function (response) {
                        console.log(response)
                        me.showContent = false
                        me.$store.dispatch('friend/flagSwitch')
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
  .float-right-position{
    position: relative;
    right: 10%;
  }
  .float-left-position{
    position: relative;
    left: 10%;
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
