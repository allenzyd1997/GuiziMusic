<template>
    <div class="carousal">
        <div class="header">
            <div class="title" >
                <strong>歌</strong><strong>单</strong><strong>推</strong><strong>荐</strong>
            </div>
        </div>
        <div class="category">
            <a class="category_type">为你推荐</a>
            <a class="category_type">网络歌曲</a>
            <a class="category_type">情歌</a>
            <a class="category_type">KTV热歌</a>
            <a class="category_type">官方歌单</a>
            <a class="category_type">情歌</a>
        </div>
        <div class="carousal-wrap" id="carousal">
            <div class="carousal-container" id="carousal-container">
                <ul class="carousal-list" id="carousal-list">
                    <li class="carousal-item" ><a href="" class="avatar">
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
            <a @click='clickPre'><img src="./zuo.png" alt="" class="zuo-btn" ></a>
            <a @click='clickNext'><img src="./you.png" alt="" class="you-btn"></a>
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
            GetObj('carousal').scrollLeft -= 1300
        },        
        clickNext() {
            if(GetObj('carousal').scrollLeft >= GetObj('carousal-list').scrollWidth) {
                GetObj('carousal').scrollLeft = GetObj('carousal').scrollLeft - GetObj('carousal-list').scrollWidth
            }
            GetObj('carousal').scrollLeft += 1300
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
        font-size: 34px
        strong 
            margin-left: 5px
.category
    display: flex
    width: 60%
    margin: 0 auto
    margin-top: 50px
    .category_type
        flex: 1
.carousal-wrap
    width: 80%
    height: 250px
    margin: 0 auto 
    margin-top: 50px
    overflow: hidden
    .carousal-container
        width: 500%
        padding: 5px
        .carousal-list 
            float: left
            margin-left: -20px
            .carousal-item
                float: left
                list-style: none
                margin-left: 20px
                margin-right: 20px
                img 
                    height: 240px
                    width: 240px
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