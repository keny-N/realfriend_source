<template>
  <div class="friend-list">
    <ul>
      <!--itemsの件数文回している-->
      <li v-for="friend in friends" class="rounded border border-dark">
        <router-link v-bind:to="{name:'GameBody',params:{friendId:friend[0]}}" class="rink">
        <img class="friend-img rounded" :src=friend[2]>
          {{ friend[1]}}
        </router-link>
          <FriendDelete class="float-right yureru-j" v-bind:friend-id=friend[0] v-bind:friend-img=friend[2] v-bind:friend-name=friend[1]></FriendDelete>
        <div class="position">
          <router-link v-bind:to="{name:'GameBody',params:{friendId:friend[0]}}" class="rink">
          好感度：{{friend[3]}}
          </router-link>
          <FriendEdit class="float-right yureru-j" v-bind:friend-id=friend[0] v-bind:image-data=friend[2] v-bind:friend-name=friend[1]></FriendEdit>
        </div>
      </li>
    </ul>
    <!--itemsが増えた際にリストに追加させているかのテスト用 何をのせるのか不明のためとりあえずの項目名
    名前: <input v-model="addName"><br />
    住所: <input v-model="addJusyo"><br />
    <button v-on:click="add">add</button><br />
    -->
  </div>
</template>

<script>
  import FriendEdit from "@/components/FriendEdit"
  import FriendDelete from "@/components/FriendDelete"
  import http from "../../static/axios/axios"

  export default {
    name: "FriendList",
    components: {FriendEdit, FriendDelete},
    data: function () {
      return {
        //getUrlでは適当なユーザーのフレンドを一覧として取得するためのURL、ログインとの連携を試していないのでユーザーID１を固定している
        getUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/all',
        //deleteUrlでは削除したいフレンドのIDを指定することでデータベースから削除されるURL
        deleteUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one/',
        friends: [],
      }
    },
    mounted() {
      this.showFriend()
      // console.log(http.request.headers)
    },
    methods: {
      //フレンド削除のやつきっと消える
      deleteFriend(value) {
        http.interceptors.request.use(config => {
          config.headers.Authorization = this.$store.getters['token/tokenGet']
          return config
        })
        http.delete(this.deleteUrl + Number(value)
        ).then(function (response) {
          console.log(response)
        }).catch(function (error) {
          console.log(error)
        })
      },
      showFriend() {
        let me = this
        //ログイン画面から遷移する際に動的ルーティングで送られてくる時用
        // let userId = this.$route.params.userid
        // console.log('get送信します')
        // 動的ルーティングで取得した際の書き方
        // http.get(this.getUrl+Number(userid))
        http.interceptors.request.use(config => {
          config.headers.Authorization = this.$store.getters['token/tokenGet']
          return config
        })
        http.get(this.getUrl)
          .then(function (response) {
              console.log(response.data)
              me.friends = response.data.friends
          })
      }
    }
  }
</script>

<style scoped>
  ul {
    list-style: none;
    padding-left: 0px;

  }

  /*上下の間隔と背景に影をつけている。*/
  li {
    background: white;
    box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.3);
    padding: 10px 20px;
    margin: auto;
    margin-bottom: 20px;
    width: 70%;
    max-width: 600px;
    height: 80px;
  }

  .friend-img {
    float: left;
    /*リストでの背景に入らないため画像サイズを調整している。項目が増えると変更する必要あり*/
    max-width: 55px; /* 最大幅 */
    max-height: 48px;
    width: 30%;
    object-fit: cover;
  }
  .rink{
    text-decoration: none;
  }
  .friend-list {
    overflow: scroll;
    height: 80vh;
  }
  .position{
    margin-top:10px;
  }
  .yureru-j {
    animation: yureru-j 2s infinite;
  }
  @keyframes yureru-j {
    0% {
      transform: translate(0px, 2px);
    }
    5% {
      transform: translate(0px, -2px);
    }
    10% {
      transform: translate(0px, 2px);
    }
    15% {
      transform: translate(0px, -2px);
    }
    20% {
      transform: translate(0px, 2px);
    }
    25% {
      transform: translate(0px, -2px);
    }
    30% {
      transform: translate(0px, 0px);
    }
  }

</style>
