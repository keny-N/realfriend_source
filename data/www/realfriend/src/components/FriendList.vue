<template>
  <div class="friendinsert">
    <ul>
      <!--itemsの件数文回している-->
      <li v-for="friend in friends" class="rounded border border-dark">
        <img class="friendimg rounded" :src=friend[3]>
        <div>
          {{ friend[2]}}
          <router-link v-bind:to="{name:'GameBody',params:{friendid:friend[0]}}">
            <button type="button" class="btn btn-primary btn-sm botan">攻略</button>
          </router-link>
        </div>
        <div>
          好感度：{{friend[4]}}
          <!--ボタンが押された時にfriendIdを送っている。きっと消える-->
          <button v-on:click="deleteFriend(friend[0])">さくじょおおおお</button>
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
  export default {
    name: "FriendList",
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
      deleteFriend(value) {
        this.axios.delete(this.deleteUrl + Number(value)
        ).then(function (response) {
          if (response.data.isSuccess) {
            console.log(response)
          }
        }).catch(function (error) {
          console.log(error)
        })
      },
      showFriend() {
        let self = this
        //ログイン画面から遷移する際に動的ルーティングで送られてくる
        let userid = this.$route.params.userid
        console.log('get送信します')
        //this.axios.get(this.getUrl+Number(userid))
        this.axios.get(this.getUrl)
          .then(function (response) {
            if (response.data.isSuccess) {
              console.log(response.data)
              self.friends = response.data.friends
            } else {
              self.msg = "エラーリスト表示"
            }
          }).catch(function (error) {
          console.log(error)
          self.msg = "エラーリスト表示"
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
  }

  .friendimg {
    float: left;
    /*リストでの背景に入らないため画像サイズを調整している。項目が増えると変更する必要あり*/
    max-width: 55px; /* 最大幅 */
    max-height: 48px;
    width: 30%;
    object-fit: cover;
  }

  .botan {
    float: right;
  }

  .friendinsert {
    overflow: scroll;
    height: 80vh;
  }

</style>
