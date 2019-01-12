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

export const listAlbum = params => {
    return axios.post('/api/albuminfo/loadPage', params)
}


export const listSinger = params => {
    return axios.get('/api/artistinfo/findsingerall_page', params)
}
export const listSongList = params => {
	return axios.post('/api/listinfo/loadPage')

}


