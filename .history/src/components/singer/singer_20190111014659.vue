<template>
    <div class="singer">
        <div class="my_singer">
            <h2 class="singer_push_tit">
                <i class="icon_txt">万千歌手，尽在眼前</i>
            </h2>
            <div class="singer_push_desc">
                <i lang="icon_txt">登陆查看你关注的歌手</i>
            </div>
            <a href="" class="singer_push_btn">
                立即登陆
                <span class="singer_push_btn_border"></span>
            </a>
        </div>
        <div class="main">
            <div class="singer_tag">
                <div class="singer_tag_list">
                    <a href="javascript:;" class="singer_tag_item">热门</a>
                    <a href="javascript:;" class="singer_tag_item">A</a>
                    <a href="javascript:;" class="singer_tag_item">B</a>
                    <a href="javascript:;" class="singer_tag_item">C</a>   
                    <a href="javascript:;" class="singer_tag_item">D</a>
                    <a href="javascript:;" class="singer_tag_item">E</a>
                    <a href="javascript:;" class="singer_tag_item">F</a>
                    <a href="javascript:;" class="singer_tag_item">G</a>
                    <a href="javascript:;" class="singer_tag_item">H</a>
                    <a href="javascript:;" class="singer_tag_item">I</a>
                    <a href="javascript:;" class="singer_tag_item">J</a>
                    <a href="javascript:;" class="singer_tag_item">K</a>
                    <a href="javascript:;" class="singer_tag_item">L</a>
                    <a href="javascript:;" class="singer_tag_item">M</a>
                    <a href="javascript:;" class="singer_tag_item">N</a>
                    <a href="javascript:;" class="singer_tag_item">O</a>             
                    <a href="javascript:;" class="singer_tag_item">P</a>
                    <a href="javascript:;" class="singer_tag_item">Q</a>
                    <a href="javascript:;" class="singer_tag_item">R</a>
                    <a href="javascript:;" class="singer_tag_item">S</a>
                    <a href="javascript:;" class="singer_tag_item">T</a>
                    <a href="javascript:;" class="singer_tag_item">U</a>
                    <a href="javascript:;" class="singer_tag_item">V</a>
                    <a href="javascript:;" class="singer_tag_item">W</a>
                    <a href="javascript:;" class="singer_tag_item">X</a>
                    <a href="javascript:;" class="singer_tag_item">Y</a>
                    <a href="javascript:;" class="singer_tag_item">Z</a>
                    <a href="javascript:;" class="singer_tag_item">#</a>
                </div>
                <div class="singer_tag_list">
                    <a href="javascript:;" class="singer_tag_item">全部</a>
                    <a href="javascript:;" class="singer_tag_item">内地</a>
                    <a href="javascript:;" class="singer_tag_item">港台</a>
                    <a href="javascript:;" class="singer_tag_item">欧美</a>
                    <a href="javascript:;" class="singer_tag_item">韩国</a>
                    <a href="javascript:;" class="singer_tag_item">其他</a>
                </div>
                <div class="singer_tag_list">
                    <a href="javascript:;" class="singer_tag_item">全部</a>
                    <a href="javascript:;" class="singer_tag_item">男</a>
                    <a href="javascript:;" class="singer_tag_item">女</a>
                    <a href="javascript:;" class="singer_tag_item">组合</a>
                </div>   
                <div class="singer_tag_list">
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
                </div>                  
            </div>
            <div class="singer_list">
                <div class="top_singer_pic">
                    <ul class="singer_list__list">
                        <li class="singer_list__item" v-for="item in rec_row1">
                            <div class="singer_list__item_box">
                                <a href="" class="singer_list__cover">
                                    <img v-bind:src="item.image" class="singer_list__pic">
                                </a>
                                <h3 class="singer_list__title">
                                    <a>{{item.artist_name}}</a>
                                </h3>
                            </div>
                        </li>
                    </ul>
                    <ul class="singer_list__list">
                        <li class="singer_list__item" v-for="item in rec_row2">
                            <div class="singer_list__item_box">
                                <a href="" class="singer_list__cover">
                                    <img v-bind:src="item.image" class="singer_list__pic">
                                </a>
                                <h3 class="singer_list__title">
                                    <a>{{item.artist_name}}</a>
                                </h3>
                            </div>
                        </li>
                    </ul>                    
                </div>
                <ul class="singer_list_txt">
                    <li class="singer_list_txt_item">
                        <a href="">庄心妍</a>
                    </li>
                    <li class="singer_list_txt_item">
                        <a href="">庄心妍</a>
                    </li>
                    <li class="singer_list_txt_item">
                        <a href="">庄心妍</a>
                    </li>
                    <li class="singer_list_txt_item">
                        <a href="">庄心妍</a>
                    </li>
                    <li class="singer_list_txt_item">
                        <a href="">庄心妍</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import {listSinger} from '@/axios/api'
    export default {
        data() {
            return {
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
            }
        },
        mounted: function() {
            this.getRows()
        },
        methods: {
			getRows() {
				if (this.pageLoading)
					return 
				this.pageLoading = true
				let params = {
					page: this.page,
					size: this.size,
					query: this.filters.query
				}
				
				listSinger(params).then(res => {
					this.pageLoading = false
					if (!res.data || !res.data.rows)
						return 
					this.total = res.data.total
					this.page++
					this.row1 = res.data.rows.slice(0, 5)
					this.row2 = res.data.rows.slice(5, 10)
					this.row3 = res.data.rows.slice(10, 15)
					this.row4 = res.data.rows.slice(15, 20)
                    this.row5 = res.data.rows.slice(20, 25)
                    this.row6 = res.data.rows.slice(25, 30)
                    this.row7 = res.data.rows.slice(30, 35)
                    this.row8 = res.data.rows.slice(35, 40)
                    this.row9 = res.data.rows.slice(40, 45)
                    this.row10 = res.data.rows.slice(45, 50)
                    this.rec_row1 = res.data.rec_row1.slice(0, 5)
                    this.rec_row2 = res.data.rec_row2.slice(5, 10)
				}).catch(err => {
                	console.log(err)
                })
			},
			handleCurrentChange(val) {
				this.page = val
				this.getRows()
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