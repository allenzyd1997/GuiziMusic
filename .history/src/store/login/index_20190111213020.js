import * as actions from './actions'
import state from './state'
import mutations from './mutations'
import getters from './getters'
import createLogger from 'vuex/dist/logger'
Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
    namespaced: true,
    state, 
    mutations,
    actions,
    getters,
    strict: debug,
    plugins: debug ? [createLogger()] : []
})