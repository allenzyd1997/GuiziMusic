<template>
    <div class="search">
        <div class="mod_search">
            <div class="mod_search_input">
                <input class="search_input" placeholder="请输入搜索内容">
            </div>
        </div>
        <div class="main">
            <div class="main_inner">
                <div class="result">
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
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
export default {

}
</script>

<style>

</style>
