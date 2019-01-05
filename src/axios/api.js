import axios from 'axios'

axios.defaults.baseURL = 'localhost:8080'

export const requseLogin = params => {
    return axios.post('/user/login', params)
}