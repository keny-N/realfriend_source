import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
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
    }
  },
  actions: {
    increment: ({commit}, payload) => {
      setTimeout(() => {
        commit('increment', payload)
      }, 1000)
    }
  },
  modules: {}
})
