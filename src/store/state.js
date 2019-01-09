import {playMode} from 'common/js/config'

const state = {
    token: window.sessionStorage.getItem('token'),
    username: '',
    singer:{},
    playing:false,
    fullScreen: false,
    playlist:[],
    sequenceList:[],
    mode: playMode.sequence,
    currentIndex: -1,
}
export default state