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
                        <el-button class="songlist_btn" @click=downloadSong>下载</el-button>
                        <el-button class="songlist_btn" @click="deleteSongs">删除</el-button>
                        <el-button class="songlist_btn" @click="clearList">清空列表</el-button>
                    </div>
                    <div class="mid_page"> 
                        <div class="table_list">
                        <table>
                            <thead>
                                <tr class = "title">
                                    <th class="first_title">
                                        <div></div>
                                    </th>
                                    <th>
                                        <div>歌曲</div>
                                    </th>
                                    <th>
                                        <div>歌手</div>
                                    </th>
                                    <th>
                                        <div>时长</div>
                                    </th>
                                </tr>
                            </thead>
                            <tr v-for = "(song, index) in tableData" class = "el">
                                <th>
                                    <a href="javascript:;" v-show="song.selected" @click="selectSong(index)"><img src="../../common/image/select.png" class="outer_img"></a>

                                    <div class="inner_div">
                                            <a href="javascript:;" v-show="!song.selected" @click="selectSong(index)"><img src="../../common/image/not_select.png" class="inner_img"></a>
                                     </div>
                                </th>
                                <th>
                                    {{song.song_name}}
                                </th>
                                <th>
                                    {{song.singer}}
                                </th>
                                <th>
                                    {{song.duration}}
                                </th>
                            </tr>
                        </table>
                                            
                    </div> 
                    </div>
                    
                    <div class="mod_song_info">
                            <div class="song_info">
                                <a class="song_info_cover" href="javascript:;">
                                    <div class="show_cover">
                                        <img src="../../common/image/10.jpg" class="song_info_pic">
                                    </div>
                                </a>
                                <div class="song_info_name">
                                    歌曲名:
                                    <a href="">719最帅的人是这首歌的歌手</a>
                                </div>
                                <div class="song_info_singer">
                                    歌手名:
                                    <a href="">刘思源</a>
                                </div>
                                <div class="song_info_album">
                                    专辑名:
                                    <a href="">719</a>
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
                <div class = "control_bar">
                    <audio ref="audio" 
                    @pause="onPause" 
                    @play="onPlay" 
                    @timeupdate="onTimeupdate"
                    @loadedmetadata="onLoadedmetadata"

                    :src="audio.song_url" 
                    >
                    </audio>
                    
                    <div class="control_buttoms">

                            <a href="javascript:;" @click="lastSong"><img src="../../common/image/QUICK_BAK.png" class="qb_buttom"></a>


                            <a href="javascript:;" v-show="show_play" @click="startPlayOrPause"><img src="../../common/image/PLAY.png" class="outer_img"></a>
                            <div class="inner_div">
                                <a href="javascript:;" v-show="!show_play" @click="startPlayOrPause"><img src="../../common/image/STOP.png" class="inner_img"></a>
                            </div>

                            <a href="javascript:;" @click="nextSong"><img src="../../common/image/QUICK_FOR.png" class="qf_buttom"></a>

                    </div>
                    <div class="play_slider">
                    <el-tag type="info" class="time_played">{{audio.currentTime | formatSecond}}</el-tag>    

                    <el-tag type="info" class="time_max">{{audio.maxTime | formatSecond}}</el-tag>    

                    <el-slider v-model="sliderTime" :format-tooltip="formatProcessToolTip" @change="changeCurrentTime" class="slider"></el-slider>
                    

                    <div class="volume_buttom">
                        <a href="javascript:;"  @click="showVolume"><img src="../../common/image/VOLUME.png" class="volume_img"></a>
                    </div>

                    <el-slider v-model="volume" v-show="show_volume" :format-tooltip="formatVolumeToolTip"  @change="changeVolume" class="vol_slider"></el-slider>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>


<script type="text/ecmascript-6">
    import {mapGetters} from 'vuex'

    import {playSongList} from '@/axios/api'

    import Lyric from 'lyric-parser'



    function realFormatSecond(second){
        var secondType = typeof second 

        if (secondType === 'number' || secondType === 'string') {
            second = parseInt(second)

            var hours = Math.floor(second / 3600)
            second = second - hours * 3600
            var mimute = Math.floor(second / 60)
            second = second - mimute * 60

            return hours + ':' + ('0' + mimute).slice(-2) + ':' + ('0' + second).slice(-2)
            } else {
            return '0:00:00'
            }
        }

    function sliderGetWidth(){
        return document.documentElement.clientWidth*0.333
    }

    export default {
        data () {
            return {


                audio:{
                    playing:false,
                    currentTime: 0,
                    maxTime: 0,
                    sliderTime: 0,
                    song_url: "", 
                    },


                currentSongIndex: 0,

                volume: 100,
                show_play: true,
                show_volume: true,
                activetest:true,

                size: 20,
                total: 0,
                filters:{},
                
                tableData: [{
                    song_name: "Light",
                    singer:"火箭少女刘思源",
                    duration:"03:30",
                    selected:false,
                    url:"http://m10.music.126.net/20190112144717/6dbf3077fed21704de0015132b370ad9/ymusic/9581/b80c/ec1e/35db1b25288729ed8cd41202ba4b98bd.mp3"
                    },{
                    song_name: "时间是金",
                    singer:"rap歌手刘思源",
                    duration:"03:20",
                    selected:false,
                    url:"http://m10.music.126.net/20190112144717/6dbf3077fed21704de0015132b370ad9/ymusic/9581/b80c/ec1e/35db1b25288729ed8cd41202ba4b98bd.mp3"
                    },{
                    song_name: "月亮警察",
                    singer:"火箭少女刘思源",
                    duration:"03:10",
                    selected:false,
                    url:"../../../static/music/火箭少女101-月亮警察.mp3"
                    },{
                    song_name: "Light",
                    singer:"火箭少女刘思源",
                    duration:"03:30",
                    selected:false,
                    url:"../../../static/music/火箭少女101-Light.mp3"
                    },{
                    song_name: "时间是金",
                    singer:"rap歌手刘思源",
                    duration:"03:20",
                    selected:false,
                    url:"../../../static/music/王以太-时间是金 (Live).mp3"
                    },{
                    song_name: "月亮警察",
                    singer:"火箭少女刘思源",
                    duration:"03:10",
                    selected:false,
                    url:"../../../static/music/火箭少女101-月亮警察.mp3"
                    },{
                    song_name: "Light",
                    singer:"火箭少女刘思源",
                    duration:"03:30",
                    selected:false,
                    url:"../../../static/music/火箭少女101-Light.mp3"
                    },{
                    song_name: "时间是金",
                    singer:"rap歌手刘思源",
                    duration:"03:20",
                    selected:false,
                    url:"../../../static/music/王以太-时间是金 (Live).mp3"
                    },{
                    song_name: "月亮警察",
                    singer:"火箭少女刘思源",
                    duration:"03:10",
                    selected:false,
                    url:"../../../static/music/火箭少女101-月亮警察.mp3"
                    },
                ],


                selectedTable:[],
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
        },
        mounted: function(){
            this.getSongs()
        },
        methods:{
            startPlayOrPause(){
                return this.audio.playing? this.pause() : this.play()
            },
            play(){
                this.$refs.audio.play()
            },
            pause(){
                this.$refs.audio.pause()
            },
            onPlay(){
                this.audio.playing=true
                this.show_play = false
            },
            onPause(){
                this.audio.playing=false
                this.show_play = true
            },
            showVolume(){
                this.show_volume = !this.show_volume
            },
            volumeShow(){
                this.show_volume = true
            },
            volumeHide(){
                this.show_volume = false
            },
            onLoadedmetadata(res){
                console.log('loadedmetadata')
                console.log(res)
                this.audio.maxTime = parseInt(res.target.duration)
            },
            // 拖动进度条，改变当前时间，index是进度条改变时的回调函数的参数0-100之间，需要换算成实际时间
            changeCurrentTime(index){
              this.$refs.audio.currentTime = parseInt(index)
            },
            // 当音频当前时间改变后，进度条也要改变
            onTimeupdate(res) {
              //console.log('timeupdate')
              //console.log(res)
              this.audio.currentTime = res.target.currentTime
              this.sliderTime = parseInt(this.audio.currentTime / this.audio.maxTime * 100)
            },

            // 进度条格式化toolTip
            formatProcessToolTip(index = 0) {
              index = parseInt(this.audio.maxTime / 100 * index)
              return '进度条: ' + realFormatSecond(index)
            },

            changeVolume(index = 0){
                this.$refs.audio.volume = index / 100
                this.volume = index
            },
            formatVolumeToolTip(index = 0){
                index = parseInt(index)
                return '音量: '+ index
            },


            // 加入歌单到当前list
            getSongs(){
                if (this.pageLoading)
                    return 
                this.pageLoading = true
                let params = {
                    size: this.size,
                    query: this.filters.query
                }
                
                playSongList(params).then(res=>{
                
                this.pageLoading = false

                if (!res.data || !res.data.rows)
                        return
                this.total = res.data.total
                res.data.rows.forEach(element=>{
                let key = "selected";
                let value = false;

                element[key] = value;

                })

                this.tableData = res.data.rows;



                }).catch(err => {
                    console.log(err);
                })
            },   

            //这里开始业务控制功能Jan.11

            // 选择歌曲， 选择的歌曲将加入selectedTable中
            selectSong(index){
                //将Vue tableData中的键值进行改变，主要是改前面的选中动画
                let origin_el = this.tableData[index];
                
                console.log(origin_el);

                this.tableData[index].selected = !this.tableData[index].selected;

                this.$set(this.tableData,index,this.tableData[index]);

                //将选中的歌加入selectedTable，取消选中的移出此数组

                if (origin_el.selected == true){
                    console.log("this is add song")
                    this.selectedTable.push(this.tableData[index]);
                }
                else{
                    console.log("remove song")
                    let found_index = this.selectedTable.indexOf(origin_el);
                    this.selectedTable.splice(found_index, 1);
                }
            },
            // 删除所选歌曲
            deleteSongs(){
                this.tableData.forEach(e => {
                    if(e.selected == true){
                        this.tableData.splice(this.tableData.indexOf(e), 1);
                    }
                });
            },

            // 清空列表
            clearList(){
                this.tableData = [];
            },

            lastSong(){
                if(this.currentSongIndex != 0){
                    this.currentSongIndex = this.currentSongIndex - 1  
                }
                this.loadSong()
            },
            nextSong(){
                if(this.currentSongIndex != this.tableData.length){
                    this.currentSongIndex = this.currentSongIndex + 1

                }
                else{
                    this.currentSongIndex = 0
                }
                this.loadSong()
            },
            loadSong(){
                this.audio.song_url = this.tableData[this.currentSongIndex].url
                this.audio.playing = false 
                this.currentTime = 0 
                this.sliderTime = 0
                this.show_play = true
            },
        },

        filters:{
            transPlayPause(value){
                return value ? ')(' : '>'
            },
            formatSecond(second = 0){
            return realFormatSecond(second)
            }
        },
    }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    @import "~common/stylus/variable"
    @import "~common/stylus/mixin"
    .player
        .player_logo_pic
            width:80px
            height:80px

        .player_logo
            position: absolute
            top: -15px
            left: 40px
        .mod_player_login
            position: absolute
            top: 40px
            right: 20px
            text-align: right
            padding-right: 28px
            .player_login
                .player_login_link
                    position: relative
                    float: left 
                    margin-right: 15px
                .player_login_out
                    color: #ffa5a5
                    opacity: .3
                    line-height: 30px
                    position: absolute
                    top: 0
                    right: -99px
        .mod_player
            .player_bd
                background: #fff
                position: absolute
                top: 11%
                bottom: 18%
                width: 100%
                cursor: default
                .player_style_normal
                    
                    display: block
                    background: rgba(255,240,110,1)
                    .mod_songlist_toolbar
                        position: relative
                        
                        left:-480px
                        top:10px
                        margin-bottom: 20px
                        .el-button
                            padding: 5px 10px;
                            color: #ffa5a5
                            background: rgba(255,240,110,1)
                        .el-button:hover
                            color:#fff
                            
                    .sb_main
                        position: relative
                    .mod_song_info
                        position: absolute
                        top: 30px
                        right: 100px
                        height: 100%
                        text-align: center
                        font-size: 14px
                        line-height: 24px
                        .song_info
                            color:#fff
                            .song_info_cover
                                position: relative
                                display: block
                                width: 250px
                                height: 250px
                                margin: 40px

                                .show_cover
                                    border-radius:125px;
                                    overflow: hidden;
                                    
                                    .song_info_pic
                                        vertical-align: middle;
                                        width: 250px;
                                        height: 250px;
                                        @keyframes rotate{
                                        from{-webkit-transform:rotate(0deg)}
                                        to{-webkit-transform:rotate(360deg)}
                                        }
                                        animation: 9.5s linear 0s normal none infinite rotate;

                                        

                            .song_info_name
                                top:30px
    
.mid_page
    
    width:800px;
    height:520px;
    background: rgba(255,240,110,1)
    .table_list
        width:800px;
        height:460px;
        
        overflow-y:scroll;  /*纵向滚动条始终显示 */
        overflow-x:none;
        table
            border-collapse:collapse

            border: 0px
            width:784px;   /*表格宽度＝div宽度(500px)－滚动条宽度(16px) */
            top:50px
            thead
                tr

                    POSITION: relative;  /*绝对定位 */
                    height:30px

                    th
                        background: rgba(255,240,110,1)
                        div
                            color: #000

            .el
                height:60px
                th
                    color: rgba(255,127,133,1)
                    font-size:13px
                    background: rgba(0,0,0,0.1)
                    a
                        .outer_img
                            
                            position:relative
                            width: 50px
                            height: 50px
                        .inner_img
                            position:relative

                            width: 50px
                            height: 50px
            .el:hover
                th
                    background: rgba(255,127,133,1)
                    color: #fff


.bg_player
    padding:300px
    width:840px
    height:230px
    background:#000
.control_bar
    .control_buttoms

        position:absolute
        top:695px
        left:100px
        z-index:10
        .qb_buttom
            position:absolute
            left:-20px
            width:50px
            height:50px
        .outer_img
            position:absolute
            left:40px
            width:50px
            height:50px
        .inner_img
            position: absolute
            left:35px
            width:50px
            height:50px
        .qf_buttom
            position:absolute
            left:90px
            width:50px
            height:50px          

  
        
    .vol_slider
            position:absolute
            padding-bottom:100px
            left: 750px
            width: 100px
    .play_slider
        position:absolute
        z-index:10
        top:670px
        left:350px
        .slider
                position: absolute
                width: 500px  
        .time_played
                top:-5px          
        .time_max
                position:absolute
                top:-5px
                left:440px
    .volume_buttom
            position:absolute
            left:700px
            .volume_img
                width:40px
                height:40px




a 
    color: #FFA5A5
    text-decoration: none

</style>

