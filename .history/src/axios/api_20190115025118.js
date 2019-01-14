import axios from 'axios'
import store from '../store'
import router from '../router'

axios.defaults.baseURL = 'http://localhost:8080'

const API_PROXY = 'https://bird.ioliu.cn/v1/?url='

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
    return axios.post('/api/login/findid?username='+params.username+'&password='+params.password)
}

export const requseRegister = params => {
    return axios.post('/api/login/addUser?username='+params.username+'&password='+params.password)
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

export const findSongBySongList = params => {
    return axios.get('/api/songinfo/findsonginfoBysonglist_id?songlist_id='+params)
}

export const playSongList = params => {

}

//首字母查询
export const listSingerByFirstName = params => {
    return axios.get('/api/artistinfo/firsthanzicode_page?firsthanzicode='+params.name+'&currentPage='+params.page+'&pageSize='+params.size)
}

//根据album_id查询专辑所包歌曲
export const findSongByAlbum = params => {
    return axios.get('/api/songinfo/findsonginfoByalbum_id?album_id='+params)
}

//根据歌手id查找歌手信息
export const findSingerById = id => {
    return axios.get('/api/artistinfo/singer_id?singer_id='+id)
}

//根据歌手id查找歌曲
export const findSongBySingerId = params => {
    return axios.get('/api/songinfo/findsonginfoBysinger_id_page?singer_id='+params.id+'&currentPage='+params.page+'&pageSize='+params.pageSize)
}

//根据歌手区域
export const findSongByArea = params => {
    return axios.get('/api/artistinfo/singer_area_page?singer_label='+params.area+'&currentPage='+params.page+'&pageSize='+params.size)
}

//根据歌手性别
export const findSongBySex = params => {
    return axios.get('/api/artistinfo/singer_sex_page?singer_label='+params.sex+'&currentPage='+params.page+'&pageSize='+params.size)
}

export const getLyric = id => {
    return axios.get('https://api.bzqll.com/music/netease/lrc?key=579621905&'+id)
}

export const getRank = id => {
    return axios.get(API_PROXY + 'https://music.163.com/api/playlist/detail?id=' + id)
}

export const getPopularSinger = params => {
    return axios.get('/api/artistinfo/findpopuler')
}

export const getSongById = id => {
    return axios.get('/api/songinfo/findsonginfoBysong_id?song_id=' + id)
}

export const getSongByLabel = params => {
    return axios.get('/api/songlist/findbysonglist_label_page?currentPage='+params.currentPage+'&pageSize='+params.pageSize+'&songlist_label='+params.label)
}

//获得歌单
export const getSongListByUser = id => {
    return axios.get('/api/songlist/findbyuser_id?user_id=' + id)
}

//创建歌单 
export const createSonglist = params => {
    return axios.get('/api/songlist/addSonglist?songlist_id='+params.songlist_id+'&user_id='+params.user_id+'&songlist_name='+params.songlist_name+'&songlist_time='+params.songlist_time)
}

//删除歌单
export const deleteSonglist = id => {
    return axios.get('/api/songlist/deleteSonglist?songlist_id=' + id)
}

//歌单表增加歌曲
export const addSongToList = params => {
    return axios.get('/api/songlist/addSongintoSonglist?songlist_id=' + params.songlist_id + '&song_id=' + params.song_id)
}

//通知
export const getNotice = params => {
    return axios.geet('/api/notification/findNotification_page?currentPage=' + params.currentPage + '&pageSize=' + params.pageSize)
}