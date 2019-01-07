<template>
    <div class="carousal">
        <div class="header">
            <h2 class="title" >歌单推荐</h2>
        </div>
        <div class="category">
            <a>为你推荐</a>
            <a>网络歌曲</a>
            <a>情歌</a>
            <a>KTV热歌</a>
            <a>官方歌单</a>
            <a>情歌</a>
        </div>
        <div class="carousal-wrap" id="carousal">
            <div class="carousal-container" id="carousal-container">
                <ul class="carousal-list" id="carousal-list">
                    <li class="carousal-item"><a href="" class="avatar">
                        <img src="../../common/image/1.jpg"></a>
                    </li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/2.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/3.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/4.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/5.jpg"></a></li>  
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/6.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/7.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/8.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/9.jpg"></a></li>
                    <li class="carousal-item"><a href="" class="avatar"><img src="../../common/image/10.jpg"></a></li>                                      
                </ul>
                
                <ul id="carousal-list-copy" class="carousal-list"></ul>
            </div>
        </div>
        <div class="lr-tab">
            <button @click='clickPre'><img src="./zuo.png" alt="" class="zuo-btn" ></button>
            <button @click='clickNext'><img src="./you.png" alt="" class="you-btn"></button>
        </div>
        <div class="spot">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">


import {GetObj} from '@/common/js/common'
export default {

    methods: {
        init() {
            GetObj('carousal-list-copy').innerHTML = GetObj('carousal-list').innerHTML       
        },
        clickPre() {
            this.init()
            console.log("123")
            if(GetObj('carousal').scrollLeft <= 0){GetObj('carousal').scrollLeft = GetObj('carousal').scrollLeft + GetObj('carousal-list').offsetWidth}
            GetObj('carousal').scrollLeft -= 1100 
        },        
        clickNext() {
            if(GetObj('carousal').scrollLeft >= GetObj('carousal-list').scrollWidth) {
                GetObj('carousal').scrollLeft = GetObj('carousal').scrollLeft - GetObj('carousal-list').scrollWidth
            }
            GetObj('carousal').scrollLeft += 1000
        }
    }
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
    width: 1120px
    height: 250px
    margin: 0 auto 
    margin-top: 50px
    overflow: hidden
    .carousal-container
        width: 500%
        padding: 5px
        .carousal-list 
            float: left
            .carousal-item
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
        left: -514px 
        width: 79px
        height: 108px
        opacity: 0.1
    .you-btn
        right: -514px
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