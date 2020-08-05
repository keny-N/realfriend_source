<template>
  <div class="news-body">
    <InformationList :data-list="updateInformation"></InformationList>
    <InformationList :data-list="logInformation"></InformationList>
  </div>
</template>

<script>
  import InformationList from "@/components/LogDisplayList"
  import http from "../axios/axios"

  export default {
    name: "LogDisplayBody",
    components: {InformationList},
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
        apiError: false
      }
    },

    methods: {
      apiGet: async function (url, data) {
        const token = this.$store.getters['token/tokenGet']
        http.interceptors.request.use((config) => {
          config.headers.Authorization = token
          return config
        })
        console.log(token)
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
            // console.log(this.apiError)
            // console.log(this.logInformation)
        }


    }
</script>

<style scoped>
  .news-body {
    width: 70vh;
    height: 100%;
    margin: 0 auto;
  }
</style>
