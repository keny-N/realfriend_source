<template>
  <div class="news-body">
    <InformationList :data-list="updateInformation"></InformationList>
    <InformationList :data-list="logInformation"></InformationList>
  </div>
</template>

<script>
  import InformationList from "@/components/LogDisplayList"

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
        await this.axios.get(url)
          .then(response =>
            response.data.logs.forEach(tmpData=> {
              // console.log(tmpData)
              data.body.push({title:tmpData[1], body:tmpData[0]})
            })
          )
          .catch(error => {
            this.apiError = true
            console.log(error.response.status)
          })
        // console.log(data)
      },
      // updateGet: async function() {
      //   const URL = ""
      //   await $.axios.get(URL)
      //     .then(response => (this.UpdateInformation = response))
      //     .catch(error => alert('エラーが発生したためリロードしてくださいｋ'))
      //
      // },
      // logGet: async function () {
      //   await this.axios.get(this.LOG_URL)
      //     .then(response => response)
      //     .catch(error =>{
      //       this.apiError = true
      //       console.log(error.response.status)
      //     })
      dataGet: async function () {
        const LOG_URL = this.BASE_URL + "/users/" + this.USER_ID + "/log"
        // await Promis.all([this.updateGet,this.logGet])
        // await Promis.all([this.logGet()])
        await this.apiGet(LOG_URL, this.logInformation)


      },
    },

    async mounted() {
      // this.axios.get(this.LOG_URL).then(response=>console.log(response)).catch(error=>console.log(error.response.status))
      // console.log(1111111111111111111)
      await this.dataGet()
      if (this.apiError === true) {
        alert("エラーが発生しました。再度実行してください。")
      }
      console.log(this.apiError)
      console.log(this.logInformation)
      // console.log(this.apiError,222222222222)
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
