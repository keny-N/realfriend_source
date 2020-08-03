import vue from 'vue'
import Axios from "axios"
import router from "../router"
import Store from "../store"


const http = Axios.create({
  withCredentials: true
})

http.interceptors.response.use(function (response) {
}, function (error,) {
  // 認証エラー時の処理
  console.log(error)
  if (error.status !== 200) {
    router.push('/login')
    // システムエラー時の処理
  }
  // } else if (error.response.status === 500) {
  //   Vue.toasted.clear()
  //   Vue.toasted.error(error.response.data.message)
  // }
  return Promise.reject(error)
})


export default http
