<template>
    <div class="singer-detail">
        <div class="main">
            <div class="singer_data">
                <span class="data_cover">
                    <img :src="singerInfo.img_url" class="data_photo">
                </span>
                <div class="data_cont">
                    <div class="data_name">
                        <h1 class="data_name_txt" title="G.E.M.邓紫棋">{{singerInfo.singer_name}}</h1> 
                    </div>
                    <ul class="data_statistic">
                        <li class="data_statistic_item">
                            <a href=""><span>单曲</span><strong>0</strong></a>
                        </li>
                        <li class="data_statistic_item">
                            <a href=""><span>专辑</span><strong>0</strong></a>
                        </li>                        
                    </ul>
                    <div class="data_actions">
                        <el-button @click="sequence" class="btn">播放歌手热门歌曲</el-button>
                        <el-button>关注</el-button>
                    </div>
                </div>
            </div>
            <div class="js_tab">
                <div class="part">
                    <div class="part_hd">
                        <h2 class="part_tit">热门歌曲</h2>
                        <a href="" class="js_goto_tab">全部</a>
                    </div>
                    <div class="songlist">
                        <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%"  :row-style="setRowStyle"
                        >
                        

                            <el-table-column label="歌曲" width="200" prop="song">
                                <template scope="scope">
                                    <img :src="scope.row.pic_url" width="60px" height="60px"><span>{{scope.row.song_name}}</span>
                                </template>
                            </el-table-column> 
                            <el-table-column width="400px">
                                <template scope="scope">
                                    <div class="icon-menu" style="transform: scale(0.7)">
                                        <a href="javascript:;" title="播放" @click="play">
                                            <i class="icon_button icon_play_opacity"></i>
                                        </a>
                                        <a href="javascript:;" title="添加到歌单" @click="add">
                                            <i class="icon_button icon_add_opacity"></i>
                                        </a>
                                        <a href="javascript:;" title="下载" @click="download">
                                            <i class="icon_button icon_upload_opacity"></i>
                                        </a>                   
                                    </div>
                                </template>                            
                            </el-table-column>
                            <el-table-column label="歌手" width="200" prop="singer_name">
                                
                            </el-table-column>
                            <el-table-column label="时长" width="200" prop="format(duration/1000/60)">

                            </el-table-column>
                        </el-table> 
				<div id="album_foot" class="album_foot">
					<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">
					</el-pagination>
				</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import IconMenu from '@/base/icon-menu/icon-menu'
import {findSingerById, findSongBySingerId, listAlbum, findSongByAlbum, getLyric, findSongById} from '@/axios/api'
import {format, formatUnixtimestamp} from '@/common/js/util'
import {createSong} from '@/common/js/song'
import {mapGetters, mapActions} from 'vuex'
export default {
    data() {
        return {
            tableData: [],
            page: 1,
            size: 20,
            total: 0,
            singerInfo: {},
            songs: [],
            params: {}
        }
    },
    mounted() {
        this.getSingerInfo()
        this.getSongInfo()
    },
    methods: {
        getSingerInfo() {
            findSingerById(this.$route.query.singerid).then(res => {
                if (!res.data) 
                    return 
                console.log('11111111')
                console.log(res.data)
                this.singerInfo = res.data
            }).catch(err => {
                console.log(err)
            })
        },
        getSongInfo() {
            console.log('0000000000')
            this.params = {
                id: this.$route.query.singerid,
                page: this.page,
                pageSize: this.size
            }
            findSongBySingerId(this.params).then(res => {
                if (!res.data) {
                    console.log('3333333333')
                    return 
                }
                this.page++
                this.total = res.data.total
                console.log('22222')
                console.log(res)                    
                this.songs = res.data
                this.tableData = this.songs
            }).catch(err => {
                console.log(err)
            })
            
        },
        setRowStyle() {

        },
        handleCurrentChange(val) {
            this.page = val
            this.getSongInfo()
        },
        sequence(params) {
            console.log('444444444')
            console.log(params)
            findSongById(params).then(res => {
                if (!res.data)
                    return 
                this.songs = this.normalizeSongs(res.data)
                this.page++				
                this.sequencePlay({
                    list: this.songs
                
                })
            }).catch(err => {
                console.log(err)
            })

            // 跳转到播放页面
            // let routeUrl = this.$router.resolve({
            // 	path: "/player"
            // })
            // window.open(routeUrl .href, '_blank')
            this.$router.push({path: '/player'})	
        },
        play() {
            this.sequence()
        },
        download() {

        },
        add() {

        },
        //随机播放
        random(params) {
            findSongByAlbum(params).then(res => {
                if (!res.data)
                    return 
                this.songs = this.normalizeSongs(res.data)
                this.page++				
                this.randomPlay({
                    list: this.songs
                
                })
            }).catch(err => {
                console.log(err)
            })

            // 跳转到播放页面
            // let routeUrl = this.$router.resolve({
            // 	path: "/player"
            // })
            // window.open(routeUrl .href, '_blank')
            this.$router.push({path: '/player'})
        },
        normalizeSongs(list) {
            let ret = []
            list.forEach((item) => {
                let musicData = item
                console.log(musicData)
                console.log('musicData')
                
                if (musicData.song_id && musicData.album_id) {
                    ret.push(createSong(musicData))
                }
            })
            return ret
        },
        ...mapActions({	
            randomPlay: 'play/randomPlay',
            sequencePlay: 'play/sequencePlay'
        }),
    },
    computed: {
        ...mapGetters({
            sequenceList: 'play/sequenceList'
        })
    },
    components: {
        IconMenu
    }
}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .main
        margin: 0 154px
        .singer_data
            position: relative
            height: 250px
            padding-left: 305px
            margin-top: 40px
            margin-bottom: 35px
            .data_cover
                position: absolute 
                left: 0
                top: 0
                width: 250px
                height: 250px
                .data_photo
                    border-radius: 999px
                    width: 100%
                    height: 100%
            .data_cont
                padding-top: 31px
                .data_name
                    line-height: 50px
                    height: 50px
                    .data_name_txt
                        float: left 
                        font-size: 38px
                        font-weight: 400
                        white-space: nowrap 
                        overflow: hidden
                        text-overflow: ellipsis 
                        margin-top: -25.460px
                        margin-bottom: -25.460px
                .data_desc
                    font-size: 14px
                    height: 50px
                    line-height: 50px
                    margin-bottom: 4px
                    .data_desc_txt 
                        float: left 
                        white-space: nowrap 
                        overflow: hidden
                        text-overflow: ellipsis 
                        margin-right: 2px
                .data_statistic 
                    height: 23px
                    line-height: 23px
                    display: flex
                    padding-left: 0px
                .data_actions 
                    float: left 
li 
    list-style: none

a 
    text-decoration: none 
    color: #000
</style>
