import {playMode} from 'common/js/config'

const state = {
    playing: false,
    fullScreen: false,
    playlist: [],
    sequenceList: [],
    mode: playMode.sequence,
    currentIndex: -1,
    playHistory: loadPlay(),
}
export default state