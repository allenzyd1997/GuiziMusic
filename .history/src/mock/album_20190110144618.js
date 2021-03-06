import Mock from 'mockjs'
import MockAdapter from 'axios-mock-adapter/types';

let adapters = []
adapters.push(
    (MockAdapter) => MockAdapter.onPost('/api/albuminfo/loadPage').reply(req => {
        let promise = new Promisse((resolve, reject) => {
            let data = req.data ? JSON.parse(req.data) : {
                size: 20
            }
            let result = {
                rows: [],
                total: 10000
            }
            for (let i = 0; i < data.size; i++) {
                let item = Mock.mock({
                    image: Mock.Random.image('240x240', '#ffcc33', '#FFF', 'jpg'),
                    
                })
            }
        })
    })
)