export default {
  namespaced: true,  //モジュールを名前空間に分ける
  state: {
    friendFlag: false
  },
  getters: {
    getFriendFlag: state => {
      return state.friendFlag
    }
  },
  mutations: {
    flagSwitch(state) {
      if (state.friendFlag) {
        state.friendFlag = false
      } else {
        state.friendFlag = true
      }
      console.log("ミューテションflagSwitch")
    }
  },
  actions: {
    flagSwitch: ({commit}) => {
      setTimeout(() => {
        commit('flagSwitch')
      }, 100)
    }
  }
}
