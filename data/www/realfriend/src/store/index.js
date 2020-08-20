import Vue from 'vue'
import Vuex from 'vuex'

import counter from '@/store/modules/Counter'
import token from '@/store/modules/Token'
import friend from '@/store/modules/friend'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    counter,
    token,
    friend
  },
})
