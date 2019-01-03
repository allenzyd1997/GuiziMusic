<template>
    <div class="carousal">
        <div class="header">
            <h2 class="title">歌单推荐</h2>
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
            <div class="carousal-container" id="carousal-container">
                <ul class="carousal-list" id="carousal-list">
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/1.jpg" class="image"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/2.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/3.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/4.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/5.jpg"></a></li>          
                             
                </ul>
                
                <ul id="carousal-list-copy" class="carousal-list" style="display:none"></ul>
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
</template>

<script type="text/ecmascript-6">
window.onload = function(){
    var d1 = document.getElementById("carousal-container")
    var u1 = document.getElementById("carousal-list")
    var u2 = document.getElementById("carousal-list-copy")
    u2.innerHTML = u1.innerHTML
    console.log('init')
    console.log(u2.offsetWidth)
    console.log(d1.scrollLeft)
    function go(){
        console.log()
        if(u2.offsetWidth-d1.scrollLeft<=0){    /*offsetWidth:u2可见区域的宽；scrollLeft：d1左边被卷去的长度*/
            d1.scrollLeft-=u2.offsetWidth;
        } else {
            d1.scrollLeft++;
        }
    }

    var run = setInterval(go,1);
    d1.onmouseover = function(){    /*鼠标进过清除定时器*/
        window.clearInterval(run);
    }
    d1.onmouseout = function(){    /*鼠标移开继续轮播*/
        run = setInterval(go,1);
    }
}
export default {

}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">

.header
    padding-top: 40px
    .title
        margin: 0 auto 
        width: 196px
        height: 40px
.carousal-wrap
    width: 80%
    height: 250px
    margin: 0 auto 
    margin-top: 50px
    .carousal-container
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
            position: relative 
            top: -180px
            opacity: 0.5
            :hover
                opacity: 1
                cursor: pointer
        .zuo-btn
            left: -678px 
            width: 79px
            height: 108px
            opacity: 0.1
        .you-btn
            right: -678px
            width: 79px
            height: 108px
            opacity: 0.1
        
    .spot 
        margin-top: -100px
        span   
            width: 8px;
            height: 8px;
            background: #ccc;
            display: inline-block;
            border-radius: 50%;        
</style>