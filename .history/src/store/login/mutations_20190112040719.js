const mutations = {

    //更改token的值
    LOGIN: (state, data) => {
        state.user = data
        window.sessionStorage.setItem('user', data)
    },
    //登出的时候要清楚token
    LOGOUT: (state) => {
        state.user = null
        window.sessionStorage.removeItem('user')
    },
    //把用户名存起来
    USERNAME: (state, data) => {
        state.username = data
        window.sessionStorage.setItem('username', data)
    },

    LOGIN_VISIBLE: (state, bool) {{
        state.loginVisible = bool
    }}
}
export default mutations