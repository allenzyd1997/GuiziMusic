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
                            <a href=""><span>单曲</span><strong>264</strong></a>
                        </li>
                        <li class="data_statistic_item">
                            <a href=""><span>专辑</span><strong>43</strong></a>
                        </li>                        
                    </ul>
                    <div class="data_actions">
                        <el-button @click="random" class="btn">播放歌手热门歌曲</el-button>
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
                        
                            <el-table-column type="selection" width="55">
                            </el-table-column>
                            <el-table-column label="歌曲" width="200" prop="song">
                                <template scope="scope">
                                    <img src="../../common/image/2.jpg" width="60px" height="60px"><span>刘思源</span>
                                </template>
                            </el-table-column> 
                            <el-table-column width="400px">
                                <template scope="scope">
                                    <IconMenu></IconMenu>
                                </template>                            
                            </el-table-column>
                            <el-table-column label="歌手" width="200" prop="singer">

                            </el-table-column>
                            <el-table-column label="时长" width="200" prop="duration">

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
import {findSingerById, findSongBySingerId} from '@/axios/api'
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
        }
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
