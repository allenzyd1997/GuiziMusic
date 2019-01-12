<template>
    <div class="profile" >
        <div class="mod_profile" v-if="hasUser">
            <div class="section_inner">
                <div class="profile_cover_link">
                    <img src="../../common/image/1.jpg" alt="" class="profile_cover">
                </div>
                <h1 class="profile_tit">
                    <span class="profile_name">冰菓</span>
                </h1>
                <ul class="mod_user_statistic">
                    <li class="user_statistic_item">
                        <a href="javascript:;" class="js_tab">
                            <strong class="user_statistic_num">1</strong>
                            <span class="user_statistic_tit">关注</span>
                        </a>
                    </li>
                    <li class="user_statistic_item">
                        <a href="javascript:;" class="js_tab">
                            <strong class="user_statistic_num">1</strong>
                            <span class="user_statistic_tit">粉丝</span>
                        </a>
                    </li>                    
                </ul>
            </div>
        </div>
        <div class="main_profile" v-if="hasUser">
            <div class="mod_tab profile_nav">
                <router-link to="/profile/like"><span class="mod_tab_item">我喜欢</span></router-link>
                
                <router-link><span class="mod_tab_item">我创建的歌单</span></router-link>
                <router-link><span class="mod_tab_item">关注</span></router-link>
                <router-link><a class="mod_tab_item">粉丝</a></router-link>
                <a class="mod_tab_item">我上传的歌曲</a>
            </div>
            <!-- <div class="js_box" id="like_box">
                <div class="mod_tab">
                    <a href="javascript:;" class="mod_tab_item" @click="active_sub1">歌曲</a>
                    <a href="javascript:;" class="mod_tab_item" @click="active_sub2">歌单</a>
                    <a href="javascript:;" class="mod_tab_item" @click="active_sub3">专辑</a>
                </div>
                <div class="profile_cont">
                    <div v-if="js_sub1" class="js_sub">
                        <div class="mod_songlist_toolbar">
                            <el-button class="songlist_btn">播放全部</el-button>
                            <el-button class="songlist_btn">添加到</el-button>
                            <el-button class="songlist_btn">下载</el-button>
                            <el-button class="songlist_btn">批量操作</el-button>
                        </div>
                        <div class="playlist">
                            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle"
                            @cell-mouse-enter="handleMouseEnter" @cell-mouse-leave="handleMouseOut">
                            
                                <el-table-column type="selection" width="55">
                                </el-table-column>
                                <el-table-column label="歌单" width="200" prop="song">
                                    <template scope="scope">
                                        <img src="../../common/image/2.jpg" width="60px" height="60px"><span>刘思源</span>
                                    </template>
                                </el-table-column> 
                                <el-table-column width="400px">
                                    <template scope="scope">
                                        <IconMenu></IconMenu>
                                    </template>                            
                                </el-table-column>
                                <el-table-column label="曲目数" width="200" prop="singer">

                                </el-table-column>
                                <el-table-column label="创建人" width="200" prop="duration">

                                </el-table-column>
                            </el-table>                             
                        </div>
                    </div>
                    <div v-if="js_sub2" class="js_sub">
                        <div class="playlist">
                            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle"
                            @cell-mouse-enter="handleMouseEnter" @cell-mouse-leave="handleMouseOut">
                            
                                <el-table-column type="selection" width="55">
                                </el-table-column>
                                <el-table-column label="歌单" width="200" prop="song">
                                    <template scope="scope">
                                        <img src="../../common/image/2.jpg" width="60px" height="60px"><span>刘思源</span>
                                    </template>
                                </el-table-column> 
                                <el-table-column width="400px">
                                    <template scope="scope">
                                        <IconMenu></IconMenu>
                                    </template>                            
                                </el-table-column>
                                <el-table-column label="曲目数" width="200" prop="singer">

                                </el-table-column>
                                <el-table-column label="创建人" width="200" prop="duration">

                                </el-table-column>
                            </el-table>                             
                        </div>
                    </div>
                    <div v-if="js_sub3" class="js_sub">
                        <div class="playlist">
                            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle"
                            @cell-mouse-enter="handleMouseEnter" @cell-mouse-leave="handleMouseOut">
                            
                                <el-table-column type="selection" width="55">
                                </el-table-column>
                                <el-table-column label="专辑" width="200" prop="song">
                                    <template scope="scope">
                                        <img src="../../common/image/2.jpg" width="60px" height="60px"><span>刘思源</span>
                                    </template>
                                </el-table-column> 
                                <el-table-column width="400px">
                                    <template scope="scope">
                                        <IconMenu></IconMenu>
                                    </template>                            
                                </el-table-column>
                                <el-table-column label="曲目数" width="200" prop="singer">

                                </el-table-column>
                                <el-table-column label="歌手" width="200" prop="duration">

                                </el-table-column>
                                <el-table-column label="发行时间" width="200" prop="duration">

                                </el-table-column>
                            </el-table>                             
                        </div>
                    </div>
                </div>
            </div>
            <div class="js_box" id="create_box">
                <div class="display_tool_box">
                    <el-button>新建歌单</el-button>
                    <el-button>导入歌单</el-button>
                    <el-button>恢复歌单</el-button>
                </div>
                <div class="mod_playlist_text">
                    <div class="playlist">
                        <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle"
                        @cell-mouse-enter="handleMouseEnter" @cell-mouse-leave="handleMouseOut">
                        
                            <el-table-column type="selection" width="55">
                            </el-table-column>
                            <el-table-column label="歌单" width="200" prop="song">
                                <template scope="scope">
                                    <img src="../../common/image/2.jpg" width="60px" height="60px"><span>刘思源</span>
                                </template>
                            </el-table-column> 
                            <el-table-column width="400px">
                                <template scope="scope">
                                    <IconMenu></IconMenu>
                                </template>                            
                            </el-table-column>
                            <el-table-column label="曲目数" width="200" prop="singer">

                            </el-table-column>
                            <el-table-column label="收听" width="200" prop="duration">

                            </el-table-column>
                        </el-table>                             
                    </div>                    
                </div>
            </div>
            <div class="js_box" id="focus_box">
                <div class="mod_tab">
                    <a class="mod_tab_item">
                        歌手
                    </a>
                    <a class="mod_tab_item">
                        用户
                    </a>
                </div>
                <div class="profile_cont">
                    <div class="js_sub">
                        
                    </div>
                    <div class="js_sub">

                    </div>
                </div>
            </div> -->
            <router-view></router-view>
        </div>
        <div class="unlogin_profile" v-if="!hasUser">
            <div class="mod_unlogin_play">
                <div class="section_inner">
                    <h2 class="profile_unlogin_tit">
                        私人音乐空间，听我喜欢听的歌
                    </h2>
                    <el-button @click="LoginVisible(true)">立即登陆</el-button>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'
export default {
    data() {
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
            ],
            js_sub1: true,
            js_sub2: false,
            js_sub3: false
        }
    },
    methods: {
        ...mapActions({
            'LoginVisible': 'login/LoginVisible'
        }),
        active_sub1() {
            this.js_sub1 = true,
            this.js_sub2 = false,
            this.js_sub3 = false
        },
        active_sub2() {
            this.js_sub1 = false,
            this.js_sub2 = true,
            this.js_sub3 = false
        },
        active_sub3() {
            this.js_sub1 = false,
            this.js_sub2 = false,
            this.js_sub3 = true
        },                
    },
    computed: {
        ...mapGetters({
            loginVisible: 'login/loginVisible',
            hasUser: 'login/hasUser'
        })
    },
}
</script>

<style scoped lang="stylus">
    .mod_profile
        padding-top: 65px
        background: url(bg_profile.jpg)
        background-size: cover
        text-align: center
        color: #fff
        .section_inner
            height: 315px
            .profile_cover_link
                width: 102px
                height 102px
                margin: 0 auto 
                .profile_cover
                    width: 100%
                    height: 100%
                    border: 4px solid #ffffff
                    background: #ffffff
                    border-radius: 99px
            .profile_tit
                .profile_name
                    font-size: 30px
                    font-weight: 400
                    line-height: 64px
            .mod_user_statistic
                height: 40px
                margin: 4px 15px 26px
                .user_statistic_item
                    display: inline-block
                    border-right: solid 1px #24313d
                    width: auto 
                    text-align: center
                    padding: 0 25px
                    .user_statistic_num
                        color: #ffffff
                        font-size: 22px
                        line-height: 24px
                        margin-top: -1px
                        font-weight: 400
                    .user_statistic_tit
                        color: #ffffff
                        font-size: 14px
    .main_profile
        position: relative
        .profile_nav
            position: absolute 
            top: -56px
            left: 60px
            margin-bottom: 0
            width: 80%
            .mod_tab_item
                float: left 
                font-size: 16px
                margin-right: 40px
                color: #fff
        .js_box
            .mod_tab 
                margin-bottom: 30px
                float: left
                border-bottom: 0 none 
                margin-left: 60px
                margin-top: 30px
                .mod_tab_item
                    position: relative
                    float: left 
                    font-size: 16px
                    margin-right: 55px
            .profile_cont
                .js_sub
                    .mod_songlist_toolbar
                        padding-top: 20px
                        margin-bottom: 20px
                        width: 100%
                        float: left
                        margin-left: 60px
                        .songlist_btn
                            float: left
                    .playlist
                        margin-left: 60px

    .unlogin_profile
        .mod_unlogin_play
            height: 622px
            background: url(bg_profile_unlogin.jpg)
            background-size: cover
            .section_inner
                margin: 0 50px
                .profile_unlogin_tit
                    color: #fff
</style>
