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
    //设置播放状态
    SET_PLAYING_STATE: (state, flag) => {
        state.playing = flag
    },

    SET_PLAYLIST: (state, list) => {
        state.playlist = list
    },

    SET_SEQUENCE_LIST: (state, list) => {
        state.sequenceList = list
    },

    SET_PLAY_MODE: (state, mode) => {
        state.mode = mode
    },

    SET_CURRENT_INDEX: (state, index) => {
        state.currentIndex = index
    },

    SET_PLAY_HISTORY: (state, history) => {
        state.playHistory = history
    }
}
export default mutations