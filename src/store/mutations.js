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
    },
    [types.SET_PLAYING_STATE](state, flag){
        state.playing = flag 
    },
    [types.SET_FULL_SCREEN](state, flag){
        state.fullScreen = flag 
    },
    [types.SET_PLAYLIST](state, flag){
        state.playlist = list
    },
    [types.SET_SEQUENCE_LIST](state, flag){
        state.sequenceList = list 
    },
    [types.SET_PLAY_MODE](state, flag){
        state.mode = mode
    },
    [types.SET_CURRENT_INDEX](state, index){
        state.currentIndex = index
    }
}
export default mutations