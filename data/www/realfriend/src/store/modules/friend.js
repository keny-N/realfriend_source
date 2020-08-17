export default {
  namespaced: true,  //モジュールを名前空間に分ける
  state: {
    insertFlag:false
  },
  getters:{
    insertFlagGet:(state) => {
      return state.insertFlag
    }
  },
  mutations: {
    insertFlagSet:(state, flag) => {
      state.insertFlag = flag
    }
  },
  actions: {
    insertFlagSet:({commit}, flag) => {
      commit('insertFlagSet', flag)
    }
  }
}
