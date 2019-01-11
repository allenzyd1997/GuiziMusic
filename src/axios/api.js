import axios from 'axios'

axios.defaults.baseURL = 'localhost:8090'

export const requseLogin = params => {
    return axios.post('/user/login', params)
}

export const requseRegister = params => {
    return axios.post('/user/register', params)
}

export const listAlbum = params => {
    return axios.post('/api/albuminfo/loadPage', params)
}

export const listSongList = params => {
	return axios.post('/api/listinfo/loadPage')
}