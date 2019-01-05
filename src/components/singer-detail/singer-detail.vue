<template>
    <div class="singer-detail">
        <div class="main">
            <div class="singer_data">
                <span class="data_cover">
                    <img src="" class="data_photo">
                </span>
                <div class="data_cont">
                    <div class="data_name">
                        <h1 class="data_name_txt" title="G.E.M.邓紫棋">G.E.M.邓紫棋</h1> 
                    </div>
                    <div class="data_desc">
                        <div class="data_desc_txt">
                            中文名：邓紫棋
                        </div>
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
                        <el-button>播放歌手热门歌曲</el-button>
                        <el-button>关注799.3万</el-button>
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
                        <ul class="songlist_header">
                            <li class="songlist_header_name">歌曲</li>
                            <li class="songlist_header_album">专辑</li>
                            <li class="songlist_header_time">时长</li>
                        </ul>
                        <ul class="songlist_list">
                            <li>
                                <div class="songlist_item">
                                    <div class="songlist_number">1</div>
                                    <div class="songlist_songname">光年之外</div>
                                    <div class="songlist_album">光年之外</div>
                                    <div class="songlist_time">03:35</div>
                                </div>
                            </li>
                            <li>
                                <div class="songlist_item">
                                    <div class="songlist_number">1</div>
                                    <div class="songlist_songname">光年之外</div>
                                    <div class="songlist_album">光年之外</div>
                                    <div class="songlist_time">03:35</div>
                                </div>
                            </li>
                            <li>
                                <div class="songlist_item">
                                    <div class="songlist_number">1</div>
                                    <div class="songlist_songname">光年之外</div>
                                    <div class="songlist_album">光年之外</div>
                                    <div class="songlist_time">03:35</div>
                                </div>
                            </li>
                            <li>
                                <div class="songlist_item">
                                    <div class="songlist_number">1</div>
                                    <div class="songlist_songname">光年之外</div>
                                    <div class="songlist_album">光年之外</div>
                                    <div class="songlist_time">03:35</div>
                                </div>
                            </li>                                                                                    
                        </ul>
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

<style scoped lang="stylus" rel="stylesheet/stylus">
    .main
        margin: 0 50px
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
                    overflow: hidden
                    line-height: 50px
                    height: 50px
                    .data_name_txt
                        float: left 
                        font-size: 38px
                        font-weight: 400
                        white-space: nowrap 
                        overflow: hidden
                        text-overflow: ellipsis 
                        margin-right: 10px
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
                    overflow: hidden
</style>
