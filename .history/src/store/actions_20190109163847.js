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

export const selectPlay = function({commit, state}, {list, index}){
	commit(types.SET_SEQUENCE_LIST, list)
	commit(types.SET_PLAYLIST, list)
	commit(types.SET_CURRENT_INDEX, index)
	commit(types.SET_FULL_SCREEN, true)	
	commit(types.SET_PLAYING_STATE, true)
}