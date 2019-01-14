<template>
    <div class="rank">
        <div class="main">
            <div class="toplist_nav">
                <dl class="toplist_nav__list">
                    <dt class="toplist_nav__tit">
                        桂子音乐特色榜
                    </dt>
                    <dd class="toplist_nav__item">
                        <a href="javascript:;" class="toplist_nav__link" @click="getRankSong(19723756)">云音乐飙升榜</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="javascript:;" class="toplist_nav__link" @click="getRankSong(3779629)">云音乐新歌榜</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="javascript:;" class="toplist_nav__link" @click="getRankSong(2884035)">云音乐原创榜</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="javascript:;" class="toplist_nav__link" @click="getRankSong(3778678)">云音乐热歌榜</a>
                    </dd>                                                                                                                                  
                </dl>
                <dl class="toplist_nav__list">
                    <dt class="toplist_nav__tit">全球榜</dt>
                    <dd class="toplist_nav__item">
                        <a href="javascript:;" class="toplist_nav__link" @click="getRankSong(180106)">UK排行榜周榜</a>
                    </dd>                   
                    <dd class="toplist_nav__item">
                        <a href="javascript:;" class="toplist_nav__link" @clikc="getRankSong(60198)">Billboard周榜</a>
                    </dd>      
                    <dd class="toplist_nav__item">
                        <a href="javascript:;" class="toplist_nav__link" @click="getRankSong(11641012)">iTunes榜</a>
                    </dd>                                                                                              
                </dl>
            </div>  
            <div class="toplist">
                <div class="toplist_hd">
                    <h1 class="toplist_tit">巅峰榜流行指数</h1>
                </div>
                <div class="songlist">
                    <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle">
                       
                        <el-table-column label="歌曲" width="560">
                            <template scope="scope">
                                <img :src="scope.row.album.picUrl" width="60px" height="60px"><span>{{scope.row.album.name}}</span>
                            </template>
                        </el-table-column> 
                        <el-table-column label="歌手" width="300" prop="album.artists[0].name">

                        </el-table-column>
                        <el-table-column label="时长" width="300">
                            <template scope="scope">
                                <span>{{format(scope.row.duration/1000)}}</span>
                            </template>
                        </el-table-column>
                    </el-table> 
                </div>
                <div class="comment">
                    <Comment></Comment>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .main
        padding-top: 60px
        margin: 0 160px
        .toplist_nav
            float: left 
            border-width: 1px
            border-style: solid 
            border-color: rgba(255, 106, 113, 2)
            .toplist_nav__list
                margin-botton: 20px
                .toplist_nav__tit
                    color: rgba(255, 106, 113, 2)
                    line-height: 60px
                    font-weight: 400
                    border-bottom: 1px solid #ebebeb
                    margin: 0 17px 10px
                .toplist_nav__item
                    margin-left: 0px
                    a 
                        text-decoration: none
                        color: #000
                    .toplist_nav__link
                        display: block
                        line-height: 22px
                        padding: 8px 17px
                        font-size: 18px
        .toplist
            margin-left: 190px
            position: relative
            .toplist_hd
                line-height: 64px
                height: 64px
                margin-bottom: 10px
                .toplist_tit
                    float: left
                    font-weight: 400
                    font-size: 28px
                    margin-right: 15px
            .songlist_toolbar
                position: relative
                float: left
                margin-bottom: 20px
                .green_btn
                    margin-left: -308px
                    margin-top: 22px
</style>

<script type="text/ecmascript-6">
import Comment from '@/base/comment/comment'
import IconMenu from '@/base/icon-menu/icon-menu'
import {getRank} from '@/axios/api'

    export default {
        data() {
            return {
                tableData: [],
                songlist: []
            }
        },
        mounted() {
            getRank(19723756).then(res => {
                if (!res)
                    return 
                console.log(res.data.result.tracks)
                this.tableData = res.data.result.tracks
            })
        },
        methods: {
            format(s){
                var t;
                if(s > -1){
                    var min = Math.floor(s/60) % 60;
                    var sec = s % 60;
                    if(min < 10){t += "0";}
                    t = min + ":";
                    if(sec < 10){t += "0";}
                    t += sec.toFixed(0);
                }
                return t;
            },
            setRowStyle({row, rowIndex}) {
                if (rowIndex % 2 === 1) {
                    return 'background-color: rgba(0,0,0,0.1); height:100px'
                } else {
                    return 'height:100px'
                }
            },
            toggleSelection(rows) {
                if (rows) {
                    rows.forEach(row => {
                        this.$refs.multipleSelection.toggleRowSelection(row)
                    });
                } else {
                    this.$refs.multipleTable.clearSelection();
                }
            },
            handleSelectionChange(val) {
                this.multipleSelection = val
            },
            getRows() {

            },
            getRankSong(id) {
                getRank(id).then(res => {
                    if (!res)
                        return 
                    console.log(res.data.result.tracks)
                    this.tableData = res.data.result.tracks
                })
            },

        },
        components: {
            IconMenu,
            Comment
        }
    }
</script>