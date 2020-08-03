<template>
  <div class="friend-list">
    <ul>
      <!--itemsの件数文回している-->
      <li v-for="friend in friends" class="rounded border border-dark">
        <img class="friend-img rounded" :src=friend[3]>
        <div>
          {{ friend[2]}}
          <router-link v-bind:to="{name:'GameBody',params:{friendId:friend[0]}}">
            <button type="button" class="btn btn-primary btn-sm c-button">攻略</button>
          </router-link>
        </div>
        <div>
          好感度：{{friend[4]}}
          <!--ボタンが押された時にfriendIdを送っている。きっと消える-->
          <FriendDelete v-bind:friend-id=friend[0] v-bind:friend-img=friend[3]
                        v-bind:friend-name=friend[2]></FriendDelete>
          <FriendEdit v-bind:friend-id=friend[0] v-bind:image-data=friend[3] v-bind:friend-name=friend[2]></FriendEdit>
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
  import http from "@/axios/axios"

  export default {
    name: "FriendList",
    components: {FriendEdit, FriendDelete},
    data: function () {
      return {
        //getUrlでは適当なユーザーのフレンドを一覧として取得するためのURL、ログインとの連携を試していないのでユーザーID１を固定している
        getUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/all/1',
        //deleteUrlでは削除したいフレンドのIDを指定することでデータベースから削除されるURL
        deleteUrl: 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one/',
        friends: [],
      }
    },
    mounted() {
      this.showFriend()
    },
    methods: {
      //フレンド削除のやつきっと消える
      // deleteFriend(value) {
      //   this.axios.delete(this.deleteUrl + Number(value)
      //   ).then(function (response) {
      //     if (response.data.isSuccess) {
      //       console.log(response)
      //     }
      //   }).catch(function (error) {
      //     console.log(error)
      //   })
      // },
      showFriend() {
        let me = this
        //ログイン画面から遷移する際に動的ルーティングで送られてくる時用
        let userId = this.$route.params.userid
        console.log('get送信します')
        //動的ルーティングで取得した際の書き方
        //this.axios.get(this.getUrl+Number(userid))
        // http.get(this.getUrl)
        //   .then(function (response) {
        //     if (response.data.isSuccess) {
        //       console.log(response.data)
        //       me.friends = response.data.friends
        //     } else {
        //       me.msg = "エラーリスト表示"
        //     }
        //   })
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
  }

  .friend-img {
    float: left;
    /*リストでの背景に入らないため画像サイズを調整している。項目が増えると変更する必要あり*/
    max-width: 55px; /* 最大幅 */
    max-height: 48px;
    width: 30%;
    object-fit: cover;
  }

  .c-button {
    float: right;
  }

  .friend-list {
    overflow: scroll;
    height: 80vh;
  }

</style>
