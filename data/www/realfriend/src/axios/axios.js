import vue from 'vue'
import Axios from "axios"
import router from "../router"
import Store from "../store"


const http = Axios.create({
  // withCredentials: true
})

http.interceptors.response.use(function (response) {
  return response
  }, function (error,) {
  // 認証エラー時の処理
  console.log(error)
  if (error.status !== 200) {
    router.push('/login')
    Store.dispatch("token/setError", true)
    Store.dispatch("token/setLogin", true)
    console.log("error!!!")
    // システムエラー時の処理
  }
  return Promise.reject(error)
})


export default http
