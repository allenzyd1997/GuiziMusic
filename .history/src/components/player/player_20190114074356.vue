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
                        <el-button class="songlist_btn">收藏</el-button>
                        <el-button class="songlist_btn">添加到</el-button>
                        <el-button class="songlist_btn" @click="">下载</el-button>
                        <el-button class="songlist_btn" @click="">删除</el-button>
                        <el-button class="songlist_btn" @click="">清空列表</el-button>
                    </div>
                    <div class="mid_page"> 
                        <div class="table_list">
                        <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle">
                        
                            <el-table-column type="selection" width="55">
                            </el-table-column>
                            <el-table-column label="歌曲" width="200" prop="name">

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
                                <scroll class="middle-r" ref="lyricList" :data="currentLyric && currentLyric.lines">
                                    <div class="lyric-wrapper">
                                    <div v-if="currentLyric">
                                        <p ref="lyricLine"
                                        class="text"
                                        :class="{'current': currentLineNum ===index}"
                                        v-for="(line,index) in currentLyric.lines">{{line.txt}}</p>
                                    </div>
                                    </div>
                                </scroll>
                            </div>
                        </div>
                    </div>
            </div>
            <!-- <div class="player_ft">
                <div class = "control_bar">
                    <audio ref="audio" 
                    @pause="onPause" 
                    @play="ready" 
                    @timeupdate="updateTime"
                    @loadedmetadata="onLoadedmetadata"
                    @ended="end"

                    :src="currentSong.song" 
                    >
                    </audio>
                    
                    <div class="control_buttoms">

                            <a href="javascript:;" @click="prev"><img src="../../common/image/QUICK_BAK.png" class="qb_buttom"></a>


                            <a href="javascript:;" @click="togglePlaying"><img src="../../common/image/PLAY.png" class="outer_img"></a>

                            <a href="javascript:;" @click="next"><img src="../../common/image/QUICK_FOR.png" class="qf_buttom"></a>

                    </div>
                    <div class="play_slider">

          
          <div class="progress-wrapper">
            <span class="time time-l">{{currentTime}}</span>
            <div class="progress-bar-wrapper">
              <progress-bar :percent="percent" @percentChange="onProgressBarChange"></progress-bar>
            </div>
            <span class="time time-r">{{currentSong.duration}}</span>
          </div>                    

                    <div class="volume_buttom">
                        <a href="javascript:;"  @click="showVolume"><img src="../../common/image/VOLUME.png" class="volume_img"></a>
                    </div>

                    <el-slider v-model="volume" v-show="show_volume" :format-tooltip="formatVolumeToolTip"  @change="changeVolume" class="vol_slider"></el-slider>
                    </div>
                </div>

            </div> -->
        <div class="bottom">
          <div class="progress-wrapper">
            <span class="time time-l">{{format(currentTime)}}</span>
            <div class="progress-bar-wrapper">
              <progress-bar :percent="percent" @percentChange="onProgressBarChange"></progress-bar>
            </div>
            <span class="time time-r">{{(currentSong.duration)}}</span>
          </div>
          <div class="operators">
            <!-- <div class="icon i-left" @click="changeMode">
              <i :class="iconMode"></i>
            </div> -->
            <div class="icon i-left" :class="disableCls">
              <i @click="prev" class="icon-prev"></i>
            </div>
            <div class="icon i-center" :class="disableCls">
              <i @click="togglePlaying" :class="playIcon"></i>
            </div>
            <div class="icon i-right" :class="disableCls">
              <i @click="next" class="icon-next"></i>
            </div>
          </div>
        </div>

        </div>
    <audio ref="audio" id="main-audio" :src="currentSong.song" @play="ready" @error="error" @timeupdate="updateTime"
           @ended="end"></audio>
            <div class="bg_player_mask">

            </div>
            <div class="bg_player" >

            </div>
    </div>
</template>


<script type="text/ecmascript-6">
import ProgressBar from '@/base/progress-bar/progress-bar'
  import Scroll from '@/base/scroll/scroll'
import {playMode} from 'common/js/config'
    import {mapGetters, mapActions, mapMutations} from 'vuex'

    import {playSongList} from '@/axios/api'

    import Lyric from 'lyric-parser'
 import {prefixStyle} from 'common/js/dom'
import IconMenu from '@/base/icon-menu/icon-menu'
import {playerMixin} from 'common/js/mixin'


    export default {
        data () {
            return {
                someReady: false,
                songReady: false,
                currentTime: 0,
                radius: 32,
                currentLyric: null,
                currentLineNum: 0,
                currentShow: 'cd',
                playingLyric: '',        
                sliderTime: 0,       
                show_volume: true,
                volume: 100,

                // currentSongIndex: 0,

                // volume: 100,
                // show_play: true,
                // show_volume: true,
                // activetest:true,

                tableData: [
 
                ],


                selectedTable:[],
            }
        },
        created: function(){
            this.$emit('public_header', false)
            this.$emit('public_footer', false)
            this.$emit('public_tab', false)
            this.getSongs()
        },
        computed:{
            ...mapGetters({
            playlist: 'play/playlist',
            currentSong: 'play/currentSong',
            currentIndex: 'play/currentIndex',
            playing: 'play/playing',
            sequenceList: 'play/sequenceList'
            }),
            cdCls() {
                return this.playing ? 'play' : 'play pause'
            },
            playIcon() {
                return this.playing ? 'icon-pause' : 'icon-play'
            },
            miniIcon() {
                return this.playing ? 'icon-pause-mini' : 'icon-play-mini'
            },
            disableCls() {
                return this.songReady ? '' : 'disable'
            },            
            percent() {
                return this.currentTime / this.currentSong.duration
            },
        },
        mounted: function(){
            console.log('9999999999'),
            console.log(this.playing)
        },
        methods:{
            play(){
                this.$refs.audio.play()
            },
            pause(){
                this.$refs.audio.pause()
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

            changeVolume(index = 0){
                this.$refs.audio.volume = index / 100
                this.volume = index
            },
            formatVolumeToolTip(index = 0){
                index = parseInt(index)
                return '音量: '+ index
            },
            //控制audio
            end() {
                if (this.mode == playMode.loop) {
                    this.loop()
                } else {
                    this.next()
                }
            },

            loop() {
                this.$refs.audio.currentTime = 0
                this.$refs.audio.play()
                this.setPlayingState(true)
                if (this.currentLyric) {
                this.currentLyric.seek(0)
                }                
            },

            next() {
                if (!this.songReady) {
                return
                }
                if (this.playlist.length === 1) {
                this.loop()
                return
                } else {
                let index = this.currentIndex + 1
                if (index === this.playlist.length) {
                    index = 0
                }
                this.setCurrentIndex(index)
                if (!this.playing) {
                    this.togglePlaying()
                }
                }
                this.songReady = false                
            },
            togglePlaying() {
                if (!this.songReady) {
                return
                }
                this.setPlayingState(!this.playing)
        if (this.currentLyric) {
          this.currentLyric.togglePlay()
        }
            },            
            prev() {
                if (!this.songReady) {
                return
                }
                if (this.playlist.length === 1) {
                this.loop()
                return
                } else {
                let index = this.currentIndex - 1
                if (index === -1) {
                    index = this.playlist.length - 1
                }
                this.setCurrentIndex(index)
                if (!this.playing) {
                    this.togglePlaying()
                }
                }
                this.songReady = false
            },

            ready() {
                this.songReady = true

            },
            error() {
                this.songReady = true
            },
            updateTime(e) {
                this.currentTime = e.target.currentTime
            },

            onProgressBarChange(percent) {
                const currentTime = this.time_to_sec(this.currentSong.duration) * percent
                this.$refs.audio.currentTime = currentTime
                if (!this.playing) {
                this.togglePlaying()
                }
                if (this.currentLyric) {
                this.currentLyric.seek(currentTime * 1000)
                }
            },
            getLyric() {
                console.log(this.currentSong.lrc_url)
                this.currentLyric = new Lyric(this.currentSong.lrc_url, this.handleLyric)
                if (this.playing) {
                    this.currentLyric.play()
                }
            },
            handleLyric({lineNum, txt}) {
                this.currentLineNum = lineNum
                if (lineNum > 5) {
                let lineEl = this.$refs.lyricLine[lineNum - 5]
                this.$refs.lyricList.scrollToElement(lineEl, 1000)
                } else {
                this.$refs.lyricList.scrollTo(0, 0, 1000)
                }
                this.playingLyric = txt
            },

            //秒转时分秒
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


            // 加入歌单到当前list
            getSongs(){
                if (this.pageLoading)
                    return 
                this.pageLoading = true
                let params = {
                    size: this.size,
                }
                
                this.tableData = this.sequenceList;



            },   
            time_to_sec(time) {
                var s = '';


                var min = time.split(':')[0];
                var sec = time.split(':')[1];

                s = Number(min*60) + Number(sec);

                return s;
            },


            setRowStyle() {

            },
            ...mapMutations({
                setCurrentIndex: 'play/SET_CURRENT_INDEX',
                setPlayingState: 'play/SET_PLAYING_STATE'
            }),
            ...mapActions({

            }),


            downloadSong() {

            },
            show_play() {

            }
        },

        watch: {
            currentSong(newSong, oldSong) {
                if (!newSong.id) {
                return
                }
                if (newSong.id === oldSong.id) {
                return
                }
                if (this.currentLyric) {
                this.currentLyric.stop()
                this.currentTime = 0
                this.playingLyric = ''
                this.currentLineNum = 0
                }
                clearTimeout(this.timer)
                this.timer = setTimeout(() => {
                this.$refs.audio.play()
                this.getLyric()
                }, 1000)
            },
            playing(newPlaying) {
                const audio = this.$refs.audio
                this.$nextTick(() => {
                newPlaying ? audio.play() : audio.pause()
                })
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

        components: {
            IconMenu,
            Scroll,
            ProgressBar
        }
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
                position: absolute
                top: 11%
                bottom: 18%
                width: 90%
                cursor: default
                .player_style_normal
                    .mod_songlist_toolbar
                        position: relative
                        
                        left:-480px
                        top:10px
                        margin-bottom: 20px
                        .el-button
                            padding: 5px 10px;
                        .el-button:hover
                            color:#fff
                    .sb_main
                        position: relative
                    .mod_song_info
                        position: absolute
                        top: 0
                        right: 0
                        height: 90%
                        text-align: center
                        font-size: 14px
                        line-height: 24px
                        .song_info
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

      .bottom
        position: absolute
        bottom: 50px
        width: 100%
        .progress-wrapper
          display: flex
          align-items: center
          width: 80%
          margin: 0px auto
          padding: 10px 0
          .time
            color: #000
            font-size: $font-size-small
            flex: 0 0 30px
            line-height: 30px
            width: 30px
            &.time-l
              text-align: left
            &.time-r
              text-align: right
          .progress-bar-wrapper
            flex: 1
        .operators
          display: flex
          align-items: center
          .icon
            flex: 1
            color: $color-theme
            &.disable
              color: $color-theme-d
            i
              font-size: 30px
          .i-left
            text-align: right
          .i-center
            padding: 0 20px
            text-align: center
            i
              font-size: 40px
          .i-right
            text-align: left
          .icon-favorite
            color: $color-sub-theme                 

.bg_player_mask
    background-color: rgba(0, 0, 0, .35)
    z-index: 2
    position: absoulte
    top: 0
    left: 0
    width: 100%
    height: 100%

.bg_player
    background-image: url("https://y.gtimg.cn/music/photo_new/T002R300x300M0000015rUVB2OUdGA.jpg?max_age=2592000")
    opacity: .6
    background-size: cover
    background-position: 50%
    position: absoulte
    top: 0
    left: 0
    width: 100%
    height: 100%    
    
.mid_page
    width:1100px;
    height:520px;
    .table_list
        overflow: auto
        height:460px;
        
        // overflow-y:scroll;  /*纵向滚动条始终显示 */


// .control_bar
//     .control_buttoms

//         position:absolute
//         top:695px
//         left:100px
//         z-index:10
//         .qb_buttom
//             position:absolute
//             left:-20px
//             width:50px
//             height:50px
//         .outer_img
//             position:absolute
//             left:40px
//             width:50px
//             height:50px
//         .inner_img
//             position: absolute
//             left:35px
//             width:50px
//             height:50px
//         .qf_buttom
//             position:absolute
//             left:90px
//             width:50px
//             height:50px          

  
        
//     .vol_slider
//             position:absolute
//             padding-bottom:100px
//             left: 750px
//             width: 100px
//     .play_slider
//         position:absolute
//         z-index:10
//         top:670px
//         left:350px
//         .slider
//                 position: absolute
//                 width: 500px  
//         .time_played
//                 top:-5px          
//         .time_max
//                 position:absolute
//                 top:-5px
//                 left:440px
//     .volume_buttom
//             position:absolute
//             left:700px
//             .volume_img
//                 width:40px
//                 height:40px




a 
    color: #000
    text-decoration: none


.progress-wrapper
    display: flex
    align-items: center
    width: 80%
    margin: 0px auto
    padding: 10px 0
    .time
        color: #000
        font-size: $font-size-small
        flex: 0 0 30px
        line-height: 30px
        width: 30px
        &.time-l
            text-align: left
        &.time-r
            text-align: right
    .progress-bar-wrapper
        flex: 1

</style>
<style scoped>
.table_list::-webkit-scrollbar {/*滚动条整体样式*/
        width: 10px;     /*高宽分别对应横竖滚动条的尺寸*/
        height: 1px;
    }
.table_list::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
        border-radius: 10px;
         -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
        background: #535353;
    }
.table_list::-webkit-scrollbar-track {/*滚动条里面轨道*/
        -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
        border-radius: 10px;
        background: #EDEDED;
    }
</style>
