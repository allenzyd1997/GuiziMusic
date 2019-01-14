import axios from 'axios'
import MockAdapter from 'axios-mock-adapter'
import Mock from 'mockjs'
import {users} from './data/user'

export default {
    init() {
        let mock = new MockAdapter(axios)

        mock.onGet('/success').reply(200, {
            msg: 'success'
        });

        mock.onGet('/error').reply(500, {
            msg: 'failure'
        })

        mock.onPost('/user/login').reply(config => {
            let { username, password } = JSON.parse(config.data)

            return new Promise((resolve, reject) => {
                let user = null;
                setTimeout(() => {
                    let hasUser = users.some(person => {
                        if (person.username === username && person.password === password) {
                            user = JSON.parse(JSON.stringify(person))
                            user.password = undefined
                            return true 
                        } else {
                            return false
                        }
                    })
                    if (hasUser) {
                        resolve([200, {code: 200, msg: '登陆成功', user}])
                    } else {
                        resolve([200, {code: 500, msg: '账号错误'}])
                    }
                }, 500)
            })
        })

        mock.onPost('/user/register').reply(config => {
            let { username, password } = JSON.parse(config.data)
            
            return new Promise((resolve, reject) => {
                let user = null;
                setTimeout(() => {
                    let hasUser = users.some(person => {
                        if (person.username === username) {
                            return true
                        } else {
                            return false
                        }                           
                    }) 
                    if (hasUser) {
                        resolve([200, {code: 500, msg: '账号已被注册'}])
                    } else {
                        resolve([200, {code: 200, msg: '注册成功'}])
                    }
                })
            })
        })

        // mock.onPost('/api/albuminfo/loadPage').reply(req => {
        //     return new Promise((resolve, reject) => {
                
        //         let data = req.data ? JSON.parse(req.data) : {
        //             size: 20
        //         }
        //         let result = {
        //             rows: [],
        //             total: 10000
        //         }
        //         for (let i = 0; i < data.size; i++) {
        //             let item = Mock.mock({
        //                 image: Mock.Random.image('240x240', '#ffcc33', '#FFF', 'jpg'),
        //                 album_name: Mock.Random.ctitle(5),
        //                 artist_name: Mock.Random.cname(),
        //                 publish_time: Mock.Random.date('yyyy-MM-dd')
        //             })
        //             result.rows.push(item)
        //         }
        //         setTimeout(() => {
        //             resolve([200, result])
        //         })
        //     })
        // })

        // //加载歌手页面
        // mock.onPost('/api/artistinfo/loadPage').reply(req => {
        //     return new Promise((resolve, reject) => {
        //         let result = {
        //             rec_rows: [],
        //             rows: []
        //         }
        //         for (let i = 0; i < 10; i++) {
        //             let item = Mock.mock({
        //                 image: Mock.Random.image('140x140', '#ffcc33', '#FFF', 'jpg'),
        //                 artist_name: Mock.Random.cname(),
        //             })
        //             result.rec_rows.push(item)
        //         }     
        //         for (let i = 0; i < 50; i++) {
        //             let item = Mock.mock({
        //                 artist_name: Mock.Random.cname(),
        //             })
        //             result.rows.push(item)                    
        //         }
        //         setTimeout(() => {
        //             resolve([200, result])
        //         })           
        //     })
        // })

        // //搜索框搜索
        

        // mock.onPost('/api/listinfo/loadPage').reply(req => {
        //     return new Promise((resolve, reject) => {
        //         console.log(req.data)
        //         let data = req.data ? JSON.parse(req.data) : {
        //             size: 20
        //         }
        //         let result = {
        //             rows: [],
        //         }
        //         for (let i = 0; i < data.size; i++) {
        //             let item = Mock.mock({
        //                 image: Mock.Random.image('240x240', '#00000', '#FFF', 'jpg'),
        //                 list_name: Mock.Random.ctitle(5),
        //                 list_creater: Mock.Random.cname(),
        //                 list_amount: Mock.Random.natural(0, 2000)
        //             })
        //             result.rows.push(item)
        //         }
        //         setTimeout(() => {
        //             resolve([200, result])
        //         })
        //     })
        // })

        // mock.onPost('/api/playSong/loadPage').reply(req => {
        //     return new Promise((resolve, reject) => {
        //         let data = req.data ? JSON.parse(req.data) : {
        //             size: 20
        //         }
        //         let result = {
        //             rows: [],
        //             total: 1000
        //         }
        //         for (let i = 0; i < data.size; i++) {
        //             let song = Mock.mock({
        //                 song_name: Mock.Random.ctitle(3),
        //                 singer: Mock.Random.cname(),
        //                 duration: Mock.Random.time('mm:ss'),
        //                 url: "../../../static/music/火箭少女101-Light.mp3",
        //             })
        //             result.rows.push(song)
        //         }
        //         setTimeout(() => {
        //             resolve([200, result])
        //         })
        //     })
        // })
    }
}