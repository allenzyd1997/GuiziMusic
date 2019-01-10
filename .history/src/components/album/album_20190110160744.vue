<template>
    <div class="album">
        <div class="tag">
            <div class="tag_list">
            </div>
            <div class="tag_list">
                <h3 class="tag_tit"></h3>
                <a href="" class="tag_item"></a>
                <a href="" class="tag_item"></a>
                
            </div>
            <div class="tag_list"></div>
            <div class="tag_list"></div>
        </div>
    	<div class="album_block">
    		<div class="tag_list">
    			<div id="tags" class="tags">
    				<h3 class="tag_tit"></h3>
	    			<a href="javascript:;" class="current_tag" @click="test_func()">推荐</a>
	    			<a href="javascript:;" class="other_tag"  @click="test_func()">内地</a>
	    			<a href="javascript:;" class="other_tag"  @click="test_func()">港台</a>
	    			<a href="javascript:;" class="other_tag"  @click="test_func()">欧美</a>
	    			<a href="javascript:;" class="other_tag"  @click="test_func()">韩国</a>
	    			<a href="javascript:;" class="other_tag"  @click="test_func()">日本</a>
	    			<a href="javascript:;" class="other_tag"  @click="test_func()">其他</a>
    			</div>

    			<div>
    				<div id="genre" class="genre">
		    			<a href="javascript:;" class="current_tag" @click="test_func()">全部</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">流行</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">古典</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">乡村</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">R&B</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">金属</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">拉丁</a>    					
    				</div>
	    				<div id="classes" class="classes">
		    			<a href="javascript:;" class="current_tag" @click="test_func()">全部</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">专辑</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">EP</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">Single</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">演唱会</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">动漫</a>
		    			<a href="javascript:;" class="other_tag"  @click="test_func()">游戏</a>    					
    				</div>
    			</div>
    		</div>
    		

    		<div class="albums">
    			<div class="album_head">
    				<h2 id="current_head" class="album_head_tit">推荐</h2>
    			</div>

    			<div class="album_content">
					<ul class="all_albums">
						<li class="one_album_el">
							<div class="one_album">
								<a href="javascript:;">
									<div class="outer_cover">
										<img src="../../common/image/1.jpg">
										<div class="inner_cover">
											<img src="../../common/image/play_op.png" class="inner_img">
										</div>
									</div>
								</a>
								<div class="album_intro">
									<a href="javascript:;" class="album_name_link"><p class="album_name">album name</p></a>
									<a href="javascript:;" class="artist_name_link"><p class="artist_name">artist name</p></a>
									<p class="publish_time">publish time</p>
								</div>
							</div>
						</li>

						<li class="one_album_el">
							<div class="one_album">
								<a href="javascript:;">
									<div class="outer_cover">
										<img src="../../common/image/2.jpg">
										<div class="inner_cover">
											<img src="../../common/image/play_op.png" class="inner_img">
										</div>
									</div>
								</a>
								<div class="album_intro">
									<a href="javascript:;" class="album_name_link"><p class="album_name">album name</p></a>
									<a href="javascript:;" class="artist_name_link"><p class="artist_name">artist name</p></a>
									<p class="publish_time">publish time</p>
								</div>
							</div>
						</li>

						<li class="one_album_el">
							<div class="one_album">
								<a href="javascript:;">
									<div class="outer_cover">
										<img src="../../common/image/3.jpg">
										<div class="inner_cover">
											<img src="../../common/image/play_op.png" class="inner_img">
										</div>
									</div>
								</a>
								<div class="album_intro">
									<a href="javascript:;" class="album_name_link"><p class="album_name">album name</p></a>
									<a href="javascript:;" class="artist_name_link"><p class="artist_name">artist name</p></a>
									<p class="publish_time">publish time</p>
								</div>
							</div>
						</li>

						<li class="one_album_el">
							<div class="one_album">
								<a href="javascript:;">
									<div class="outer_cover">
										<img src="../../common/image/4.jpg">
										<div class="inner_cover">
											<img src="../../common/image/play_op.png" class="inner_img">
										</div>
									</div>
								</a>
								<div class="album_intro">
									<a href="javascript:;" class="album_name_link"><p class="album_name">album name</p></a>
									<a href="javascript:;" class="artist_name_link"><p class="artist_name">artist name</p></a>
									<p class="publish_time">publish time</p>
								</div>
							</div>
						</li>

						<li class="one_album_el">
							<div class="one_album">
								<a href="javascript:;">
									<div class="outer_cover">
										<img src="../../common/image/5.jpg">
										<div class="inner_cover">
											<img src="../../common/image/play_op.png" class="inner_img">
										</div>
									</div>
								</a>
								<div class="album_intro">
									<a href="javascript:;" class="album_name_link"><p class="album_name">album name</p></a>
									<a href="javascript:;" class="artist_name_link"><p class="artist_name">artist name</p></a>
									<p class="publish_time">publish time</p>
								</div>
							</div>
						</li>
					</ul>
                </div>
    			
    			<div id="album_foot" class="album_foot">
    				<a href="javascript:;" class="current_foot">1</a>
    				<a href="javascript:;" class="other_foot">2</a>
    				<a href="javascript:;" class="other_foot">3</a>
    				<a href="javascript:;" class="other_foot">4</a>
    				<a href="javascript:;" class="other_foot">5</a>
    				<a href="javascript:;" class="other_foot">6</a>
    				<a href="" class="other_foot">
    				<span>></span>
    				</a>
    			</div>
    		</div>
    	</div>
    </div>
</template>



<script type="text/ecmascript-6">
	export default {
		data() {
			return {
				page: 1,
				size: 20,
				total: 0,
				filters: {},
				rows: [],
				pageLoading: false,
			}
		},
		created: function() {
			listAlbum().then(res => {

			})
		}
	}
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
a{text-decoration:none}

.album
	padding-left:0px
	margin-top:-100px
.album_block
	background: linear-gradient(to bottom, #FFF0F0, #FFFFFF);
.tag_list
	padding-top:20px
	right:0px
	width:800px
	font-style: normal
	font-size: 1em
	text-align: left
	margin-left: 100px
	line-height: 50px
	font-size: 20px
	.current_tag
		text-decoration:none
		background: #FFA5A5
		color: #FFFFFF
		padding-left:10px
		padding-right:10px
		margin-left:20px

	.other_tag
		text-decoration:none
		color: #9E0047
		margin-left:20px
		margin-right:20px
	.other_tag:hover
		color: #FFA5A5



.album_head_tit
	color: #9E0047
	font-style: normal
	font-size: 2em
	font-weight: bold


.album_content
	.all_albums
		display: flex
		width: 100%
		max-width: 800px
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
					top:70px
					right:70px
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
					color:#d1005d

					.album_name_link
						.album_name
							color:#d1005d
							text-align: left
						.album_name:hover
							color:#380177

					.artist_name_link
						.artist_name
							color:#d1005d
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
	margin-top:20px
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


