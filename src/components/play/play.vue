<template>
    <div class="player">
        <h1 class="player_logo">
            <a href="">
                <img class="player_logo_pic" src="../../common/image/logo.png" width="50" height="50" alt="桂子音乐">
            </a>
        </h1>
        <div class="mod_player_login">
            <div id="player_login">
                <a class="player_login_link" href="javascript:;">
                    <img style="border-radius: 90px; margin-right: 5px; vertical-align: -10px" src="../../common/image/1.jpg" width="30px" height="30px" >
                    <span class="player_login_txt">冰果</span>
                </a>
                <a class="player_login_link" href="javascript:;">
                    <span class="player_login_out">退出</span>
                </a>
            </div>
        </div>
        <div class="mod_player">
            <div class="player_bd">
                <div class="player_style_normal js_box">
                    <div class="mod_songlist_toolbar">
                        <el-button class="songlist_btn">添加</el-button>
                        <el-button class="songlist_btn">收藏到</el-button>
                        <el-button class="songlist_btn">下载</el-button>
                        <el-button class="songlist_btn">删除</el-button>
                        <el-button class="songlist_btn">清空列表</el-button>
                    </div>
                    <div class="sb_scrollable sb_main">
                        <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle">
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
                    </div>
                    <div class="mod_song_info">
                        <div class="song_info">
                            <a class="song_info_cover" href="javascript:;">
                                <img src="../../common/image/3.jpg" class="song_info_pic">
                            </a>
                            <div class="song_info_name">
                                歌曲名:
                                <a href="">太阳</a>
                            </div>
                            <div class="song_info_singer">
                                歌手名:
                                <a href="">刘思源</a>
                            </div>
                            <div class="song_info_album">
                                专辑名:
                                <a href="">RISE</a>
                            </div>
                        </div>
                        <div class="song_info_lyric">
                            <div class="song_info_lyric_box">
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="player_ft">

            </div>
            <div class="bg_player_mask">

            </div>
            <div class="bg_player">

            </div>
        </div>
    </div>
</template>


<script type="text/ecmascript-6">
    import {mapGetters} from 'vuex'

    export default {
        data () {
            return {
                tableData: [{
                    song: '关键词',
                    singer: '刘思源',
                    duration: '03:32',
                },
                {
                    song: '关键词',
                    singer: '刘思源',
                    duration: '03:32',
                },
                {
                    song: '关键词',
                    singer: '刘思源',
                    duration: '03:32',
                },
                ]
            }
        },
        created: function(){
            this.$emit('public_header', false)
            this.$emit('public_footer', false)
            this.$emit('public_tab', false)
        },
        computed:{
            ...mapGetters([
            'fullScreen',
            'playlist'
            ])
        }
    }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
    @import "~common/stylus/variable"
    @import "~common/stylus/mixin"
    .player
        background-color: rgb(64, 64, 32)
        .player_logo
            position: absolute
            top: -5px
            left: 20px
            .player_logo_pic
                opacity: .3
        .mod_player_login
            position: absolute
            top: 20px
            right: 20px
            text-align: right
            padding-right: 28px
            .player_login
                .player_login_link
                    position: relative
                    float: left 
                    margin-right: 15px
                .player_login_out
                    color: #fff
                    opacity: .3
                    line-height: 30px
                    position: absolute
                    top: 0
                    right: -99px
        .mod_player
            .player_bd
                position: absolute
                top: 11%
                bottom: 18%
                width: 100%
                cursor: default
                .player_style_normal
                    display: block
                    .mod_songlist_toolbar
                        position: relative
                        margin-bottom: 20px
                    .sb_main
                        position: relative
                    .mod_song_info
                        position: relative
                        top: 0
                        right: 0
                        height: 100%
                        text-align: center
                        font-size: 14px
                        line-height: 24px
                        .song_info
                            .song_info_cover
                                position: relative
                                display: block
                                width: 186px
                                height: 186px
                                margin: auto
                                .song_info_pic
                                    vertical-align: middle
                                    width: 186px
                                    height: 186px

a 
    color: #333
    text-decoration: none
</style>

