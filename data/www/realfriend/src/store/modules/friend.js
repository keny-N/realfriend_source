export default {
  namespaced: true,  //モジュールを名前空間に分ける
  state: {
    friendFlag: false,
    friendName: null
  },
  getters: {
    getFriendFlag: state => {
      return state.friendFlag
    },
    getFriendName: state => {
      return state.friendName
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
    },
    insertFriendName(state, payload) {
      state.friendName = payload
      console.log("insertFriendName")
    },
  },
  actions: {
    flagSwitch: ({commit}) => {
      setTimeout(() => {
        commit('flagSwitch')
      }, 100)
    },
    insertFriendName: ({commit}, payload) => {
      setTimeout(() => {
        commit('insertFriendName', payload)
      }, 100)
    }
  }
}
