<template>
    <div class="recommand">
        <div class="playlist">
            <div class="section-inner">
                <div class="title">
                    <h2>歌单推荐</h2>
                </div>
                <div class="category">
                    <a>为你推荐</a>
                    <a>网络歌曲</a>
                    <a>情歌</a>
                    <a>KTV热歌</a>
                    <a>官方歌单</a>
                    <a>情歌</a>
                </div>
                <div class="carousal-wrap">
                    <div class="carousal">
                        <ul class="carousal-list">
                            <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/1.jpg"></a></li>
                            <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/2.jpg"></a></li>
                            <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/3.jpg"></a></li>
                            <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/4.jpg"></a></li>
                            <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/5.jpg"></a></li>
                        </ul>
                    </div>
                    <div class="lr-tab">
                        <img src="./zuo.png" alt="" class="zuo-btn">
                        <img src="./you.png" alt="" class="you-btn">
                    </div>
                    <div class="spot">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">

</script>

<style scoped lang="stylus" rel="stylesheet/stylus">


.carousal-wrap
    width: 80%
    height: 250px
    margin: 0 auto 
    margin-top: 50px
    .carousal
        .carousal-list
            display: flex
            width: 100%
            padding-left: 0
            .carousal-item
                flex: 1
                float: left
                list-style: none
                img 
                    height: 224px
                    width: 224px
            .carousal-item:hover img 
                transform: scale(1.3)
                transition: all 1s ease 0s
                -webkit-transform: scale(1.1)
                -webkit-transform: all 1s ease 0s        
    .lr-tab
        img 
            position: absolute 
            top: 384px
            opacity: 0.5
            :hover
                opacity: 1
                cursor: pointer
        .zuo-btn
            left: 0 
            width: 79px
            height: 108px
            opacity: 0.1
        .you-btn
            right: 0
            width: 79px
            height: 108px
            opacity: 0.1
        
    .spot span   
        width: 8px;
        height: 8px;
        background: #ccc;
        display: inline-block;
        border-radius: 50%;        
/*    .carousal-wrap
        width: 800px
        height: 250px
        margin: 0 auto 
        background: palegolderod 
        margin-top: 50px
        overflow: hidden
        .carousal
            padding: 5px
            width: 500%
            .carousal-list
                display: flex
                .carousal-item
                    flex: 1
                    list-style: none
                a 
                    flex: 1
                    width: 300px
                    margin: 0 auto
                    overflow: hidden
                img
                    flex: 1
                    transform: scale(1.3);
                    transition: all 1s ease 0s;
                    -webkit-transform: scale(1.3);
                    -webkit-transform: all 1s ease 0s;
            */
</style>


