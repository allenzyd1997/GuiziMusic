<template>
    <div class="singer">
        <div class="my_singer">
            <h2 class="singer_push_tit">
                <i class="icon_txt">万千歌手，尽在眼前</i>
            </h2>
            <div class="singer_push_desc">
                <i lang="icon_txt">登陆查看你关注的歌手</i>
            </div>
            <a href="javascript:;" class="singer_push_btn" @click="loginVisible=true">
                立即登陆
                <span class="singer_push_btn_border"></span>
            </a>
        </div>
        <div class="main">
            <div class="singer_tag">
                <div class="singer_tag_list">
                    <a href="javascript:;" class="singer_tag_item">热门</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('A')">A</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('B')">B</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('C')">C</a>   
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('D')">D</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('E')">E</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('F')">F</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('G')">G</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('H')">H</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('I')">I</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('J')">J</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('K')">K</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('L')">L</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('M')">M</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('N')">N</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('O')">O</a>             
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('P')">P</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('Q')">Q</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('R')">R</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('S')">S</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('T')">T</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('U')">U</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('V')">V</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('W')">W</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('X')">X</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('Y')">Y</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByFirstName('Z')">Z</a>
                    <a href="javascript:;" class="singer_tag_item">#</a>
                </div>
                <div class="singer_tag_list">
                    <a href="javascript:;" class="singer_tag_item">全部</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByArea('10')">华语</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByArea('20')">欧美</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByArea('30')">韩国</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findByArea('40')">其他</a>
                </div>
                <div class="singer_tag_list">
                    <a href="javascript:;" class="singer_tag_item">全部</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findBySex('01')">男</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findBySex('02')">女</a>
                    <a href="javascript:;" class="singer_tag_item" @click="findBySex('03')">组合</a>
                </div>   
                <!-- <div class="singer_tag_list">
                    <a href="javascript:;" class="singer_tag_item">全部</a>
                    <a href="javascript:;" class="singer_tag_item">流行</a>
                    <a href="javascript:;" class="singer_tag_item">嘻哈</a>
                    <a href="javascript:;" class="singer_tag_item">摇滚</a>
                    <a href="javascript:;" class="singer_tag_item">电子</a>
                    <a href="javascript:;" class="singer_tag_item">民谣</a>
                    <a href="javascript:;" class="singer_tag_item">R&B</a>
                    <a href="javascript:;" class="singer_tag_item">民歌</a>
                    <a href="javascript:;" class="singer_tag_item">轻音乐</a>
                    <a href="javascript:;" class="singer_tag_item">爵士</a>
                    <a href="javascript:;" class="singer_tag_item">古典</a>
                    <a href="javascript:;" class="singer_tag_item">乡村</a>
                    <a href="javascript:;" class="singer_tag_item">蓝调</a>
                </div>                   -->
            </div>
            <div class="singer_list">
                <div class="top_singer_pic">
                    <ul class="singer_list__list">
                        <li class="singer_list__item" v-for="item in rec_row1" v-if="recommand">
                            <div class="singer_list__item_box">
                                <a href="javascript:;" class="singer_list__cover" @click="singerDetail(item.singer_id)">
                                    <img v-bind:src="item.img_url" class="singer_list__pic">
                                </a>
                                <h3 class="singer_list__title">
                                    <a>{{item.singer_name}}</a>
                                </h3>
                            </div>
                        </li>
                    </ul>
                    <ul class="singer_list__list">
                        <li class="singer_list__item" v-for="item in rec_row2" v-if="recommand">
                            <div class="singer_list__item_box">
                                <a href="javascript:;" class="singer_list__cover" @click="singerDetail(item.singer_id)">
                                    <img v-bind:src="item.img_url" class="singer_list__pic">
                                </a>
                                <h3 class="singer_list__title">
                                    <a>{{item.singer_name}}</a>
                                </h3>
                            </div>
                        </li>
                    </ul>                    
                </div>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row1">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row2">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row3">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row4">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row5">
                        <a href="" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row6">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row7">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row8">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row9">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item" v-for="item in row10">
                        <a href="javascript:;" @click="singerDetail(item.singer_id)">{{item.singer_name}}</a>
                    </li>
                </ul>                                                                                                                                                            
            </div>
            <div id="album_foot" class="album_foot">
                <el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">
                </el-pagination>
            </div>
        </div>
    </div>
</template>

<script>
import {listSinger, listSingerByFirstName, findSongByArea, findSongBySex, getPopularSinger} from '@/axios/api'
import singerDetailVue from '../singer-detail/singer-detail.vue';

    export default {
        data() {
            return {
                loginVisible: false,
                page: 1,
                size: 50,
				total: 0,
				filters: {},                
                rec_row1: '',
                rec_row2: '',
                row1: '',
                row2: '',
                row3: '',
                row4: '',
                row5: '',
                row6: '',
                row7: '',
                row8: '',
                row9: '',
                row10: '',
                pageLoading: false,
                recommand: true,
            }
        },
        mounted: function() {
            this.getRows()
            this.recommand = true
        },
        methods: {
			getRows() {
				if (this.pageLoading)
					return 
				this.pageLoading = true
				let params = {
					currentPage: this.page,
					pageSize: this.size,
				}
				getPopularSinger().then(res => {
                    if (!res.data)
                        return 
                    this.rec_row1 = res.data.slice(0, 5)
                    this.rec_row2 = res.data.slice(5, 10)                   
                })
				listSinger(params).then(res => {
					this.pageLoading = false
					if (!res.data)
						return 
					this.total = res.data.total
					this.row1 = res.data.slice(0, 5)
					this.row2 = res.data.slice(5, 10)
					this.row3 = res.data.slice(10, 15)
					this.row4 = res.data.slice(15, 20)
                    this.row5 = res.data.slice(20, 25)
                    this.row6 = res.data.slice(25, 30)
                    this.row7 = res.data.slice(30, 35)
                    this.row8 = res.data.slice(35, 40)
                    this.row9 = res.data.slice(40, 45)
                    this.row10 = res.data.slice(45, 50)

				}).catch(err => {
                	console.log(err)
                })
			},
			handleCurrentChange(val) {
				this.page = val
				this.getRows()
            },
            singerDetail(id) {
                this.$router.push({ path: '/singer-detail', query: { singerid: id }})
            },
            findByFirstName(firstName) {
                let params = {
                    page: this.page,
                    size: this.size,
                    name: firstName
                }
                console.log(params)
                listSingerByFirstName(params).then(res => {
                    if (!res.data)
                        return
                    console.log(res)
 					this.row1 = res.data.slice(0, 5)
					this.row2 = res.data.slice(5, 10)
					this.row3 = res.data.slice(10, 15)
					this.row4 = res.data.slice(15, 20)
                    this.row5 = res.data.slice(20, 25)
                    this.row6 = res.data.slice(25, 30)
                    this.row7 = res.data.slice(30, 35)
                    this.row8 = res.data.slice(35, 40)
                    this.row9 = res.data.slice(40, 45)
                    this.row10 = res.data.slice(45, 50)                      
                    this.recommand = false
                })
            },
            findBySex(sex) {
                let params = {
                    page: this.page,
                    size: this.size,
                    sex: sex
                }           
                findSongBySex(params).then(res => {
                    if (!res.data)
                        return 
 					this.row1 = res.data.slice(0, 5)
					this.row2 = res.data.slice(5, 10)
					this.row3 = res.data.slice(10, 15)
					this.row4 = res.data.slice(15, 20)
                    this.row5 = res.data.slice(20, 25)
                    this.row6 = res.data.slice(25, 30)
                    this.row7 = res.data.slice(30, 35)
                    this.row8 = res.data.slice(35, 40)
                    this.row9 = res.data.slice(40, 45)
                    this.row10 = res.data.slice(45, 50)     
                    this.recommand = false                
                })     
            },
            findByArea(area) {
                let params = {
                    page: this.page,
                    size: this.size,
                    area: area
                }           
                findSongByArea(params).then(res => {
                    if (!res.data)
                        return 
 					this.row1 = res.data.slice(0, 5)
					this.row2 = res.data.slice(5, 10)
					this.row3 = res.data.slice(10, 15)
					this.row4 = res.data.slice(15, 20)
                    this.row5 = res.data.slice(20, 25)
                    this.row6 = res.data.slice(25, 30)
                    this.row7 = res.data.slice(30, 35)
                    this.row8 = res.data.slice(35, 40)
                    this.row9 = res.data.slice(40, 45)
                    this.row10 = res.data.slice(45, 50)
                    this.recommand = false
                })     
            }
        }
    }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">

    .my_singer
        position: relative
        width: 100%
        height: 376px
        background: url(bg_singer.jpg) 50% 0 repeat-x
        overflow: hidden
        .singer_push_tit
            width: 494px
            height: 60px
            margin: 0 auto 
            margin-top: 100px
            .icon_txt
                color: #fff
                font-size: 50px
        .singer_push_desc
            width: 260px
            height: 26px
            margin-top: 20px
            margin: 0 auto
            background-position: 0 -70px
            i
                color: #c0c4cc
                font-size: 20px
        .singer_push_btn
            position: relative
            display: block
            margin: 20px auto 0
            font-size: 18px
            text-align: center
            color: #fff
            line-height: 48px
            width: 174px
            background-color: transparent
            border: 0 none
        a
            text-decoration: none 
            .singer_push_btn_border
                position: absolute 
                top: 0
                left: 0
                right: 0
                bottom: 0
                border-radius: 2px
                border: 1px solid #ffffff
                opacity: .2
                transition-property: opacity 
                transition-duration: .3s

    .singer_tag
        background-color: #fbfbfd
        padding: 34px 0 17px 40px
        margin: 30px 0 20px
        .singer_tag_list
            padding-bottom: 3px
            height: auto 
            zoom: 1
            clear: both
            overflow: hidden
            .singer_tag_item
                float: left 
                padding: 0 8px
                margin: 0 12px 14px 0
            a 
                text-decoration: none
                color: #000

    .singer_list
        overflow: hidden
        text-align: center
        .singer_list__list
            margin-bottom: 4px
            margin-right: -20px
            overflow: hidden
            zoom: 1
            .singer_list__item
                float: left 
                width: 20%
                margin-bottom: 20px
                overflow: hidden
            li
                list-style: none
                .singer_list__item_box
                    position: relative
                    margin-right: 20px
                    background-color: #fbfbfd
                    min-height: 195px
                    padding: 25px 0 
                    overflow: hidden
                    .singer_list__cover
                        display: block
                        width: 140px
                        height: 140px
                        border-radius: 126px
                        margin-left: auto 
                        margin-right: auto
                    a
                        color: #000
                        text-decoration: none 
                        .singer_list__pic
                            display: block
                            width: 140px
                            height: 140px
                            border-radius: 126px

    .singer_list_txt
        margin-right: -20px
        overflow: hidden
        margin-bottom: 60px
        .singer_list_txt_item
            float: left
            width: 20%
        li 
            list-style: none
            .singer_list_txt_item
                float: left 
                max-width: 90%
                white-space: nowrap 
                overflow: hidden
                text-overflow: ellipsis 
                font-size: 14px
                line-height: 36px
            a 
                color: #000
                text-decoration: none

</style>