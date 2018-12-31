import * as types from './mutation-types'
export const UserLogin = function({ commit }, token) {
    commit(types.SET_TOKEN, token)
}
export const UserLogout = function({ commit }) {
    commit(types.SET_TOKEN)
}
export const UserName = function({ commit }, username) {
    commit(types.SET_USERNAME, username)
}