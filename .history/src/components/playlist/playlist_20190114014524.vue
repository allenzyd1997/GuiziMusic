
<template>
    <div class="playlist">
    	<div class="tab">
				<ul class="tab_table">
					<!-- <li class="tab"><a href="javascript:;">主页</a></li> -->
					<!-- <li class="tab"><a href="javascript:;">新闻</a></li> -->
					<div class="dropdown">
						<a href="javascript:;" class="dropbtn">语种</a>
						<div class="dropdown-content">
							<a href="javascript:;">链接 1</a>
							<a href="javascript:;">链接 2</a>
							<a href="javascript:;">链接 3</a>
				    	</div>
				 	</div>
				 	<div class="dropdown">
				    	<a href="javascript:;" class="dropbtn">流派</a>
						<div class="dropdown-content">
							<a href="javascript:;">链接 5</a>
							<a href="javascript:;">链接 6</a>
							<a href="javascript:;">链接 7</a>
				    	</div>
				    </div>
				 	<div class="dropdown">
				    	<a href="javascript:;" class="dropbtn">心情</a>
						<div class="dropdown-content">
							<a href="javascript:;">链接 5</a>
							<a href="javascript:;">链接 6</a>
							<a href="javascript:;">链接 7</a>
				    	</div>
				    </div>
				 	<div class="dropdown">
				    	<a href="javascript:;" class="dropbtn">主题</a>
						<div class="dropdown-content">
							<a href="javascript:;">链接 5</a>
							<a href="javascript:;">链接 6</a>
							<a href="javascript:;">链接 7</a>
				    	</div>
				    </div>
				 	<div class="dropdown">
				    	<a href="javascript:;" class="dropbtn">场景</a>
						<div class="dropdown-content">
							<a href="javascript:;">链接 5</a>
							<a href="javascript:;">链接 6</a>
							<a href="javascript:;">链接 7</a>
				    	</div>
				    </div>
				</ul>
    	</div>
    	<div class="lists">
    		<div class="head"> 
    			<h3 class="h_title">全部歌单</h3>
    			<div class="recommand_or_new">
    				<a href="javascript:;" class="">推荐</a>
    				<a href="javascript:;" class="">最新</a>
    			</div>
    			<div class="albums">
	    			<div class="album_content">
						<ul class="all_albums">
							<li class="one_album_el" v-for = "item in row1">
								<div class="one_album">
									<a href="/#/play">
										<div class="outer_cover">
											<img :src="item.imgUrl">
											<div class="inner_cover">
												<img src="../../common/image/play_op.png" class="inner_img">
											</div>
										</div>
									</a>
									<div class="album_intro">
										<a href="javascript:;" class="album_name_link"><p class="album_name">歌单： {{item.songlist_name}}</p></a>
										<a href="javascript:;" class="artist_name_link"><p class="artist_name">创建者： {{item.user_id}}</p></a>
										<p class="publish_time">播放量：{{item.list_amount}}</p>
									</div>
								</div>
							</li> 
						</ul>
						<ul class="all_albums">
							<li class="one_album_el" v-for = "item in row2">
								<div class="one_album">
									<a href="/#/play">
										<div class="outer_cover">
											<img :src="item.imgUrl">
											<div class="inner_cover">
												<img src="../../common/image/play_op.png" class="inner_img">
											</div>
										</div>
									</a>
									<div class="album_intro">
										<a href="javascript:;" class="album_name_link"><p class="album_name">歌单： {{item.songlist_name}}</p></a>
										<a href="javascript:;" class="artist_name_link"><p class="artist_name">创建者： {{item.user_id}}</p></a>
										<p class="publish_time">播放量：{{item.list_amount}}</p>
									</div>
								</div>
							</li> 
						</ul>
						<ul class="all_albums">
							<li class="one_album_el" v-for = "item in row3">
								<div class="one_album">
									<a href="/#/play">
										<div class="outer_cover">
											<img :src="item.imgUrl">
											<div class="inner_cover">
												<img src="../../common/image/play_op.png" class="inner_img">
											</div>
										</div>
									</a>
									<div class="album_intro">
										<a href="javascript:;" class="album_name_link"><p class="album_name">歌单： {{item.songlist_name}}</p></a>
										<a href="javascript:;" class="artist_name_link"><p class="artist_name">创建者： {{item.user_id}}</p></a>
										<p class="publish_time">播放量：{{item.list_amount}}</p>
									</div>
								</div>
							</li> 
						</ul>
						<ul class="all_albums">
							<li class="one_album_el" v-for = "item in row4">
								<div class="one_album">
									<a href="/#/play">
										<div class="outer_cover">
											<img :src="item.imgUrl">
											<div class="inner_cover">
												<img src="../../common/image/play_op.png" class="inner_img">
											</div>
										</div>
									</a>
									<div class="album_intro">
										<a href="javascript:;" class="album_name_link"><p class="album_name">歌单： {{item.songlist_name}}</p></a>
										<a href="javascript:;" class="artist_name_link"><p class="artist_name">创建者： {{item.user_id}}</p></a>
										<p class="publish_time">播放量：{{item.list_amount}}</p>
									</div>
								</div>
							</li> 
						</ul>
					</div>
	    		</div>

    		</div>
		</div>
		<div id="album_foot" class="album_foot">
					<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">
					</el-pagination>
				</div>

    </div>
</template>


<script type="text/ecmascript-6">
	import {listSongList} from '@/axios/api'
import {listAlbum, findSongByAlbum} from '@/axios/api'
import {formatUnixtimestamp} from '@/common/js/util'
import {createSong} from '@/common/js/song'
import {mapGetters, mapActions} from 'vuex'

	export default{

	data(){
		return{
			page:1,
			size:20,
			total:0,
			filters:{},
			row1:[],
			row2:[],
			row3:[],
			row4:[],
			label:'',
			pageLoading:false,
		}
	},
	mounted: function() {
			this.getRows()
	},
	methods:{
		getRows() {
				if (this.pageLoading)
					return 
				this.pageLoading = true
				let params = {
					currentPage: this.page,
					pageSize: this.size,
					songlist_label: this.label
				}
				
				listSongList(params).then(res => {
					this.pageLoading = false
					console.log('222')
					console.log(res.data)
					if (!res.data)
						return 
					this.page++
					this.row1 = res.data.slice(0, 5)
					this.row2 = res.data.slice(5, 10)
					this.row3 = res.data.slice(10, 15)
					this.row4 = res.data.slice(15, 20)
					
				}).catch(err => {
                	console.log(err)
                })
			},
			handleCurrentChange(val) {
				this.page = val
				this.getRows()
			},
			//随机播放
			random(params) {
				findSongByAlbum(params).then(res => {
					if (!res.data)
						return 
					this.songs = this.normalizeSongs(res.data)
					this.page++				
					this.randomPlay({
						list: this.songs
					
					})
				}).catch(err => {
					console.log(err)
				})

				// 跳转到播放页面
				// let routeUrl = this.$router.resolve({
				// 	path: "/player"
				// })
				// window.open(routeUrl .href, '_blank')
				this.$router.push({path: '/player'})
			},
			normalizeSongs(list) {
				let ret = []
				list.forEach((item) => {
					let musicData = item
					console.log(musicData)
					console.log('musicData')
					
					if (musicData.song_id && musicData.album_id) {
						ret.push(createSong(musicData))
					}
				})
				return ret
			},
			...mapActions({	
				randomPlay: 'play/randomPlay'
			})
	},
			computed: {
			...mapGetters({
				sequenceList: 'play/sequenceList'
			})
		}
}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
a{text-decoration:none}
.playlist
	background-color: rgb(255,0,100);
	background-image: 
	
	repeating-linear-gradient(90deg, transparent, transparent 50px,
      rgba(0,160,50, 0.25) 50px, rgba(0,160,50, 0.25) 56px, transparent 56px, transparent 63px,
      rgba(0,160,50, 0.25) 63px, rgba(0,160,50, 0.25) 69px, transparent 69px, transparent 116px,
      rgba(255, 206, 0, 0.25) 116px, rgba(255, 206, 0, 0.25) 166px),

	repeating-linear-gradient(0deg, transparent, transparent 50px, rgba(0,160,50, 0.25) 50px,
	rgba(0,160,50, 0.25) 56px, transparent 56px, transparent 63px, rgba(0,160,50, 0.25) 63px,
	rgba(0,160,50, 0.25) 69px, transparent 69px, transparent 116px, rgba(255, 206, 0, 0.25) 116px,
	rgba(255, 206, 0, 0.25) 166px),

	repeating-linear-gradient(-45deg, transparent, transparent 5px, rgba(143, 77, 63, 0.25) 5px,
	rgba(143, 77, 63, 0.25) 10px),

	repeating-linear-gradient(45deg, transparent, transparent 5px, rgba(143, 77, 63, 0.25) 5px,
	rgba(143, 77, 63, 0.25) 10px);
.head{
	.h_title{
		width:150px
		color:#fff
	}
	.recommand_or_new{
		text-align:center
		margin-top:-40px
		margin-left:1300px
		width:100px

		a{	
			
			color:#fff	
			padding:10px
		}
		a:hover{
			color:#ffa0cf
			background:#000		
		}

	}
}

.tab_table{
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;

}
.tab_table{
	z-index: 10
	.tab{
	   float: left; 
	}
}
	.tab a, .dropbtn {
	    display: inline-block;
	    color: white;
	    text-align: center;
	    padding: 14px 16px;
	    text-decoration: none;
	}

	.tab a:hover, .dropdown:hover .dropbtn {
    background-color: #FFF;
    color: #000
	}

.dropdown {
	
	display: inline-block;
    width: 150px
    
}

	.dropdown-content {
	    display: none;
	    position: absolute;
	    background-color: #FFFFFF;
	    min-width: 160px;
	    z-index:20
	    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
	}

	.dropdown-content a {
	    color: #000000;
	    padding: 12px 16px;
	    text-decoration: none;
	    display: block;
	}

	.dropdown-content a:hover {
		background-color: #000;
		color:#ffa0cf;
	}

.dropdown:hover .dropdown-content {
    display: block;
}



.albums{
	img{
		z-index: -1
	}
}

.album_content

	.all_albums
		display: flex
		max-width: 800px
		width: 100%
		margin-left: 50px
		margin-right: 50px	
		padding-left: 70px
		.one_album_el
			list-style:none
			margin: 20px auto
			margin-right:60px
			word-wrap: break-word;
			word-break: normal; 
			.one_album
				.outer_cover
					flex:1
					float:left
					position:relative

					img
						width:240px
						height:240px
				.outer_cover:hover img 
					transform: scale(1.4)
					transition: all 0.3s ease 0s
					-webkit-transform: scale(1.1)
					-webkit-transform: all 0.5s ease 0s    


				.inner_cover
					position:absolute
					top:90px
					right:90px
					img
						width:60px
						height:60px
						opacity:0

				.outer_cover:hover .inner_cover
					img
						opacity:1
						transition: opacity 0.3s ease 0s;
						-moz-transition: opacity 0.3s ease 0s;
						-webkit-transition:opacity 0.3s ease 0s;
						-o-transition: opacity 0.3s ease 0s;
						-ms-transition: opacity 0.3s ease 0s;
				.album_intro
					color:#80ff95

					.album_name_link
						.album_name
							color:#80ff95
							text-align: left
						.album_name:hover
							color:#380177

					.artist_name_link
						.artist_name
							color:#80ff95
							position:relative
							text-align: left
							top:-20px
						
						.artist_name:hover
							color:#380177
						
					.publish_time
						
						position:relative
						text-align: left
						top:-40px







.album_foot
	position:relative
	right:500px

	.current_foot

		background: #FFA5A5
		color: #FFFFFF
		padding-left:20px
		padding-right:20px
		padding-top:15px
		padding-bottom:15px
	.other_foot

		color: #000000
		padding-top:15px
		padding-bottom:15px
		padding-left:20px
		padding-right:20px
	.other_foot:hover
		background: #FFA5A5
		color: #FFFFFF



</style>