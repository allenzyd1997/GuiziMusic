<template>
    <div class="rank">
        <div class="main">
            <div class="toplist_nav">
                <dl class="toplist_nav__list">
                    <dt class="toplist_nav__tit">
                        QQ音乐巅峰榜
                    </dt>
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">巅峰榜流行指数</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">巅峰榜流行指数</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">巅峰榜流行指数</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">巅峰榜流行指数</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">巅峰榜流行指数</a>
                    </dd>
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">巅峰榜流行指数</a>
                    </dd>                                                                                                   
                </dl>
                <dl class="toplist_nav__list">
                    <dt class="toplist_nav__tit">全球榜</dt>
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">美国iTunes榜</a>
                    </dd>                   
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">美国iTunes榜</a>
                    </dd>   
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">美国iTunes榜</a>
                    </dd>   
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">美国iTunes榜</a>
                    </dd>   
                    <dd class="toplist_nav__item">
                        <a href="" class="toplist_nav__link">美国iTunes榜</a>
                    </dd>                                                                                  
                </dl>
            </div>  
            <div class="toplist">
                <div class="toplist_hd">
                    <h1 class="toplist_tit">巅峰榜流行指数</h1>
                </div>
                <div class="songlist_toolbar">
                    <a href="" class="btn_play_green">
                        <i class="btn_play_green"></i>播放全部
                    </a>
                    <a href="">
                        <i class="btn_play"></i>添加
                    </a>
                    <a href="">
                        <i class="btn_play"></i>下载
                    </a>
                    <a href="">
                        <i class="btn_play"></i>批量操作
                    </a>
                    <a href="">
                        <i class="btn_play"></i>评论
                    </a>                                                                               
                </div>
                <div class="songlist">
                    <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange">
                        <el-table-column type="selection" width="55">
                            
                        </el-table-column>
                        <el-table-column label="歌曲" width="120" prop="song">

                        </el-table-column> 
                        <el-table-column label="歌手" width="120" prop="singer">

                        </el-table-column>
                        <el-table-column label="时长" width="120" prop="duration">

                        </el-table-column>
                    </el-table> 
                </div>
                <div class="comment">
                    <div class="part_hd">
                        <h2 class="part_tit">
                            评论
                            <span class="">
                                共251723条评论
                            </span>
                        </h2>
                    </div>
                    <div class="comment_input">
                        <div class="comment_textarea">
                            <div class="comment_textarea_inner">
                                <div class="comment_textarea_blur">
                                    期待你的神评论...
                                </div>
                            </div>
                        </div>
                        <div class="comment_tool">
                            <a href="javascript:;" class="comment_tool_btn">发表评论</a>
                        </div>
                    </div>
                    <div class="all_comment">
                        <p class="comment_rule">
                            <a class="rule_btn" href="javascript:;"></a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .main
        padding-top: 60px
        .toplist_nav
            float: left 
            border-width: 1px
            border-style: solid 
            border-color: rgba(153, 153, 153, 2)
            .toplist_nav__list
                margin-botton: 20px
                .toplist_nav__tit
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
                margin-bottom: 20px
                .btn_play_green
                    border: 1px solid #31c27c
                    background-color: #31c27c
                    color: #fff
                    border-radius: 2px
                    font-size: 14px
                    margin-right: 6px
                    padding: 0 23px
                    height: 38px
                    line-height: 38px
                    display: inline-block
                    white-space: nowrap 
                    box-sizing: border-box
                    overflow: hidden
</style>

<script type="text/ecmascript-6">
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
                ]
            }
        },
        methods: {
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
            }
        }
    }
</script>