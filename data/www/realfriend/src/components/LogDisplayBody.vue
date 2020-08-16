<template>
  <div class="news-body" :style="{ 'background-image': 'url(' + backgroundImageSrc + ')' }">
    <ReturnMenu class="return-position"></ReturnMenu>
    <InformationList :data-list="updateInformation" class="update-position"></InformationList>
    <InformationList :data-list="logInformation"></InformationList>
  </div>
</template>

<script>
  import InformationList from "@/components/LogDisplayList"
  import http from "../../static/axios/axios"
  import ReturnMenu from "@/components/ReturnMenu"

  export default {
    name: "LogDisplayBody",
    components: {InformationList,ReturnMenu},
    data() {
      return {
        updateInformation: {
          title: "更新情報", body: [{title: "全米が驚愕", body: "あほくさ"}]
        },
        logInformation: {
          title: "ログ情報", body: [{title: "07/07/02/21", body: "削除完了"}]
        },
        USER_ID: "1",
        BASE_URL: "https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend",
        apiError: false,
        backgroundImageSrc: require("@/assets/test1.png")
      }
    },

    methods: {
      apiGet: async function (url, data) {
        const token = this.$store.getters['token/tokenGet']
        http.interceptors.request.use((config) => {
          config.headers.Authorization = token
          return config
        })
        // console.log(token)
        await http.get(url)
          .then(response =>
            response.data.logs.forEach(tmpData=> {
              data.body.push({title:tmpData[1], body:tmpData[0]})
            })
          )
          .catch(error => {
            this.apiError = true
            // console.log(error.response.status)
          })

      },

      dataGet: async function () {
        const LOG_URL = this.BASE_URL + "/users/log"
        // await Promis.all([this.updateGet,this.logGet])
        // await Promis.all([this.logGet()])
        await this.apiGet(LOG_URL, this.logInformation)
      },
    },

        async mounted() {
            await this.dataGet()
            if (this.apiError === true) {
                alert("エラーが発生しました。再度実行してください。")
            }
        }
    }
</script>

<style scoped>
  .news-body {
    height: 100vh;
    margin: 0 auto;
    background-size: 5%;
    animation: bgiLoop 8s linear infinite;
  }
  @keyframes bgiLoop {
    0% { background-position: 0 0;}
    100% { background-position: -15% 15%;}
  }
  .update-position{
  }

</style>
