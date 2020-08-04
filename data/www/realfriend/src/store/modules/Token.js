import Axios from "axios"
import http from "../../axios/axios"

export default {
  namespaced: true,  //モジュールを名前空間に分ける
  state: {
    token: "私はToken.jsのstateのtokenです！",
    firstFlag: true,
    tokenError: false,
    loginScreenJudgment: false,
    axios: http
  },

  getters: {
    tokenGet: (state) => {
      return state.token
    },
    firstFlagGet: (state) => state.firstFlag,
    tokenErrorGet: (state) => state.tokenError,
    loginGet: (state) => {
      return state.loginScreenJudgment
    },
  },
  mutations: {
    setFirstFlag: (state, flag) => {
      state.firstFlag = flag
    },
    setError: (state, flag) => {
      state.tokenError = flag
    },
    setLogin: (state, flag) => {
      state.loginScreenJudgment = flag
    },
    setAxiosToken: (state) => {
      state.axios.interceptors.request.use((config => {
        config.headers.Authorization = state.token
        return config
      }))
    },
    localStorageSave: (state) => {
      //ローカルストレージにstateのトークンを保存する処理
      // Json文字列に変換しLocalStorageへ保存
      localStorage.setItem('token', JSON.stringify(state.token))
    },
    localStorageLoad: (state) => {
      //ローカルストレージのトークンをstateのトークンに保存する処理
      if (localStorage.getItem('token')) {
        console.log("tokenをstateに保存します")
        // LocalStorageから取得したJson文字列をパース
        const token = JSON.parse(localStorage.getItem('token'))
        // stateを置き換えます。
        state.token = token
      }
    }
  },
  actions: {
    setFirstFlag: ({commit}, flag) => {
      commit('setFirstFlag', flag)
    },
    setError: ({commit}, flag) => {
      commit('setError', flag)
    },
    setLogin: ({commit}, flag) => {
      commit('setLogin', flag)
    },
    setAxiosToken: ({commit}) => {
      commit('setAxiosToken')
    },
    localStorageSave: ({commit}) => {
      commit('localStorageSave')
    },
    localStorageLoad: ({commit}) => {
      commit('localStorageLoad')
    }
  }
}
