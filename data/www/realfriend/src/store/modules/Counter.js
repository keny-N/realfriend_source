export default {
  namespaced: true,  //モジュールを名前空間に分ける
  state: {
    aCount: 0,
    bCount: 0,
    cCount: 0,
    dCount: 0
  },
  mutations: {
    increment(state, payload) {
      if (payload == "a") {
        state.aCount++
      } else if (payload == "b") {
        state.bCount++
      } else if (payload == "c") {
        state.cCount++
      } else if (payload == "d") {
        state.dCount++
      }
      state.aCount++
    },
    resetCounter(state) {
      state.aCount = 0
      state.bCount = 0
      state.cCount = 0
      state.dCount = 0
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
