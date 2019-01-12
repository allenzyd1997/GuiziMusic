import {playMode} from 'common/js/config'
import {shuffle} from 'common/js/util'

export const selectPlay = function ({commit, state}, {list, index}) {
    commit('SET_SEQUENCE_LIST', list)
    if (state.mode == playMode.random) {
        let randomList = shuffle(list)
        commit('SET_PLAYLIST', list)
        index = findIndex(randomList, list[index])
    } else {
        commit('SET_PLAYLIST', list)
    } 
    commit('SET_CURRENT_INDEX', index)
    commit('SET_PLAYING_STATE', true)
}