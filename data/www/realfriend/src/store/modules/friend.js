export default {
  namespaced: true,  //モジュールを名前空間に分ける
  state: {
    friendFlag: false,
    friendName: null,
    friendGauge: 0,
    forCount: 0
  },
  getters: {
    getFriendFlag: state => {
      return state.friendFlag
    },
    getFriendName: state => {
      return state.friendName
    },
    getFriendGauge: state => {
      return state.friendGauge
    },
    getForCount: state => {
      return state.forCount
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
    insertFriendName(state, {friendName, Gauge}) {
      state.friendName = friendName
      state.friendGauge = Gauge
      console.log("insertFriendName")
      console.log(state.friendName, state.friendGauge)
    },
    updateFriendGauge(state, payload) {
      state.friendGauge += payload
      console.log(state.friendGauge)
      console.log("updateFavo")
    },
    insertForCount(state) {
      state.forCount = Math.floor(state.friendGauge / 200)
      if (state.forCount < 0) {
        state.forCount = 0
      }
      console.log(state.forCount)
      console.log("insertforCount")
    }
  },
  actions: {
    flagSwitch: ({commit}) => {
      setTimeout(() => {
        commit('flagSwitch')
      }, 100)
    },
    insertFriendName: ({commit}, {friendName, Gauge}) => {
      setTimeout(() => {
        commit('insertFriendName', {friendName, Gauge})
      }, 100)
    },
    updateFriendGauge: ({commit}, payload) => {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          commit('updateFriendGauge', payload)
          resolve()
        }, 50)
      })

    },
    insertForCount: ({commit}) => {
      return new Promise(((resolve, reject) => {
        setTimeout(() => {
          commit('insertForCount')
          resolve()
        }, 50)
      }))
    }
  }
}
