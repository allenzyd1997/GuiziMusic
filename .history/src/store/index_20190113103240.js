import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import login from './login'
import play from './play'
export default new Vuex.Store({
  modules: {
    login,
    play
  }
})