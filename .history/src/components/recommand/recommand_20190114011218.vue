<template>
    <div class="recommand">
        <div class="playlist">
            <div class="section-inner">
                <!-- <Carousal></Carousal> -->
    			<div class="album_content">
					<ul class="all_albums">
						<li class="one_album_el" v-for="item in row1">
							<div class="one_album">
								<a href="javascript:;" @click="random(item.album_id)">
									<div class="outer_cover">
										<img v-bind:src="item.album_pic">
										<div class="inner_cover">
											<img src="../../common/image/play_op.png" class="inner_img">
										</div>
									</div>
								</a>
								<div class="album_intro">
									<a href="javascript:;" class="album_name_link"><p class="album_name">{{item.album_name}}</p></a>
									<a href="javascript:;" class="artist_name_link"><p class="artist_name">{{item.singer_id}}</p></a>
									<p class="publish_time">{{item.album_date}}</p>
								</div>
							</div>
						</li>
					</ul>								
                </div>
            </div>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">
import Carousal from '@/base/carousal/carousal'
export default {
    components: {
        Carousal
    },
    data() {
        return {
            page: 1,
            size: 5,
            row1: ''  
        }
    },
    mounted: {
        this.getRows()
    },
    function: {
        getRows() {
            if (this.pageLoading)
                return 
            this.pageLoading = true
            let params = {
                currentPage: this.page,
                pageSize: this.size,
            }
            
            listAlbum(params).then(res => {
                this.pageLoading = false
                if (!res.data)
                    return 
                this.total = res.data.total
                this.page++
                this.row1 = res.data.slice(0, 5)
                this.row2 = res.data.slice(5, 10)
                this.row3 = res.data.slice(10, 15)
                this.row4 = res.data.slice(15, 20)
                
            }).catch(err => {
                console.log(err)
            })            
        }
    }
}


</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .playlist
        .carousal
            margin-bottom: 100px

            background-color: #ff7070;
            background-image: repeating-linear-gradient(90deg, transparent, transparent 50px,
                  rgba(255, 127, 0, 0.25) 50px, rgba(255, 127, 0, 0.25) 56px, transparent 56px, transparent 63px,
                  rgba(255, 127, 0, 0.25) 63px, rgba(255, 127, 0, 0.25) 69px, transparent 69px, transparent 116px,
                  rgba(255, 206, 0, 0.25) 116px, rgba(255, 206, 0, 0.25) 166px),
            repeating-linear-gradient(0deg, transparent, transparent 50px, rgba(255, 127, 0, 0.25) 50px,
                  rgba(255, 127, 0, 0.25) 56px, transparent 56px, transparent 63px, rgba(255, 127, 0, 0.25) 63px,
                  rgba(255, 127, 0, 0.25) 69px, transparent 69px, transparent 116px, rgba(255, 206, 0, 0.25) 116px,
                  rgba(255, 206, 0, 0.25) 166px),
            repeating-linear-gradient(-45deg, transparent, transparent 5px, rgba(143, 77, 63, 0.25) 5px,
                  rgba(143, 77, 63, 0.25) 10px),
            repeating-linear-gradient(45deg, transparent, transparent 5px, rgba(143, 77, 63, 0.25) 5px,
                  rgba(143, 77, 63, 0.25) 10px);

        
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

</style>





