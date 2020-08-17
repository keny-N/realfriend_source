export default {
  namespaced: true,  //モジュールを名前空間に分ける
  state: {
    loginCount: 0,
    autoLoginCount: 0,
    cameraCount: 0,
    newsCount: 0
  },
  mutations: {
    increment(state, payload) {
      if (payload == "login") {
        state.loginCount++
      } else if (payload == "autoLogin") {
        state.autoLoginCount++
      } else if (payload == "camera") {
        state.cameraCount++
      } else if (payload == "news") {
        state.newsCount++
      }
    },
    resetCounter(state) {
      state.loginCount = 0
      state.autoLoginCount = 0
      state.cameraCount = 0
      state.newsCount = 0
    }
  },
  actions: {
    increment: ({commit}, payload) => {
      setTimeout(() => {
        commit('increment', payload)
      }, 1000)
    },
    resetCounter: ({commit}) => {
      setTimeout(() => {
        commit('resetCounter')
      }, 100)
    }
  }
}
