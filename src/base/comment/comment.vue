<template>
    <div class="comment">
        <div class="part_hd">
            <h2 class="part_tit">
                评论
                <span class="part_tit_desc">共264324条评论</span>
            </h2>
        </div>
        <div class="mod_comment">
            <el-input type="textarea" :rows="3" placeholder="期待你的神评论" v-model="textarea"></el-input>
            <el-button>发表评论</el-button>
        </div>
        <div class="mod_all_comment">
            <div class="mod_type_title">
                <h2>最新评论</h2>
            </div>
            <ul class="comment_list">
                <li class="comment_list_item">
                    <a href="javascript:;" class="comment_avatar">
                        <img src="" alt="">
                    </a>
                    <h4 class="user_name">
                        3424
                    </h4>
                    <p class="comment_text">
                        ewqeweqwewqewe
                    </p>
                    <div class="comment_opt">
                        <span class="comment_date">2017.1.8 10:25</span>
                        <a class="comment_report">举报</a>
                        <a class="comment_zan">赞</a>
                    </div>
                </li>
            </ul>
            <div class="mod_page_nav">
                <el-pagination background layout="prev, pager, next" :total="1000"></el-pagination>
            </div>
        </div>
    </div>
</template>

<style scoped lang="stylus">
    .part_hd
        overflow: hidden
        height: 60px
        .part_tit
            float: left
            font-size: 24px
            font-weight: 400
            line-height: 58px
            .part_tit_desc
                margin-left: 12px
                font-size: 14px
    .mod_all_comment
        margin-bottom: 46px
        .mod_type_title
            position: relative
            height: 34px
            line-height: 34px
            padding-bottom: 26px
            border-bottom-width: 1px
            border-bottom-style: solid 
            border-color: #ededed
            h2 
            font-weight: 400
            font-size: 16px
            overflow: hidden
            text-overflow: ellipsis 
            white-space: nowrap
        .comment_list
            padding-bottom: 14px
            .comment_list_item
                position: r-elative
                padding: 15px 0 15px 56px
                border-bottom-width: 1px
                border-bottom-style: solid 
                border-color: #ededed
                .comment_avatar
                    position: relative
                    left: 0
                    top: 20px
                    width: 38px
                    height: 38px
                    img 
                        width: 100%
                        height: 100%
                        border-radius: 999px
                .user_name
                    font-weight: 400
                    margin-bottom: 6px
                    overflow: hidden
                    height 20px
                    white-space nowrap
                    text-overflow ellipsis
                    a 
                        float left
                .comment_text
                    overflow hidden
                    line-height 24px
                    text-align justify
                .comment_opt
                    line-height 24px
                    text-align right
                    overflow hidden
                    .comment_date
                        float left 
                        line-height 28px
                    .comment_report
                        margin-right 22px
                    .comment_zan
                        margin-right 22px
a 
    color: #000
    text-decoration: none
li
    list-style: none
</style>