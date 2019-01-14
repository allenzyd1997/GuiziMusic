import axios from 'axios'
import store from '../store'
import router from '../router'

axios.defaults.baseURL = 'http://localhost:8080'

var instance = axios.create({
    timeout: 5000,
    headers: { 'Content-Type': 'application/json;charset=UTF-8' },
})

// instance.interceptors.request.use(
//     config => {
//         if (store.state.to) {

//         }
//     }
// )

export const requseLogin = params => {
    return axios.post('/user/login', params)
}

export const requseRegister = params => {
    return axios.post('/user/register', params)
}

//专辑
export const listAlbum = params => {
    return axios.get('/api/albuminfo/findalbuminfoall_page?currentPage='+params.currentPage+'&pageSize='+params.pageSize)
}

//歌手
export const listSinger = params => {
    return axios.get('/api/artistinfo/findsingerall_page?currentPage='+params.currentPage+'&pageSize='+params.pageSize)
}

//歌单
export const listSongList = params => {
    if (params.songlist_label != '') {
        return axios.get('/api/songlist/findbysonglist_label_page?currentPage='+params.currentPage+'&pageSize='+params.pageSize+'&songlist_label='+params.songlist_label)
    } else {
        return axios.get('/api/songlist/findbysonglist_label_page?currentPage='+params.currentPage+'&pageSize='+params.pageSize+'&songlist_label')
    }

}

export const playSongList = params => {

}

//首字母查询
export const listSingerByFirstName = params => {
    return axios.get('/api/artistinfo/firsthanzicode?firsthanzicode='+params.character)
}

//根据album_id查询专辑所包歌曲
export const findSongByAlbum = params => {
    return axios.get('/api/songinfo/findsonginfoByalbum_id?album_id='+params.album_id)
}
