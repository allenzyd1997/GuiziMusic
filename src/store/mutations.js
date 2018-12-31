import * as types from './mutation-types'
const mutations = {
    [types.SET_TOKEN](state, token) {
        if (token !== '') {
            state.token = token
            window.sessionStorage.setItem('token', token)
        } else {
            state.token = null
            window.sessionStorage.removeItem('token')
        }
    },
    [types.SET_USERNAME](state, username) {
        state.token = username
        window.sessionStorage.setItem('username', username)
    }
}
export default mutations