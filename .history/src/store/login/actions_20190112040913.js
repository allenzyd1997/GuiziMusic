const actions = {
	UserLogin: ({ commit }, data) => {
		commit('LOGIN', data)
	},
	UserLogout: ({ commit }) => {
		commit('LOGOUT')
	},
	UserName: ({ commit }, data) => {
		commit('USERNAME', data)
	},
	LoginVisible: ({commit}, data) => {
		commit('LOGIN_VISIBLE', data)
	}
}
export default actions

