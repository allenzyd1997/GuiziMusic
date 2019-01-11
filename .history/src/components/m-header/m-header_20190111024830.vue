<template>

    <div class="m-header">
        <div><hr class="line"></div>
        <h1 class="icon">
            <a href="" >
                <img src="../../common/image/logo.png" alt="桂子音乐" class="icon_img">
            </a>
        </h1>
        <div class="tab">
            <ul>
                <li class="nav_item"><router-link class="nav_item_link" to="/"><div class="current_block">音乐馆</div></router-link></li>
                <li class="nav_item"><router-link class="nav_item_link" to="/profile"><div class="other_block">我的音乐</div></router-link></li>  
            </ul>            
        </div>


        <div class="search">
            <el-autocomplete placeholder="搜索音乐、专辑、歌单、用户" v-model="search" :fetch-suggestions="querySearchAsync" @select="handleSelect">
                <i slot="prefix" class="el-input__icon el-icon-search"></i>
            </el-autocomplete>
        </div>
        <div class="login_btn">
            <el-button type="text" @click="loginVisible=true">登陆</el-button>
        </div>
        <el-dialog title="登陆" :visible.sync="loginVisible" center:append-to-body="true" :lock-scroll="false" width="25%">
           <Login @showRegisterForm="showRegisterForm"></Login>
        </el-dialog>
        <el-dialog title="注册" :visible.sync="registerVisible" center:append-to-body="true" :lock-scroll="false" width="25%">
           <Register></Register>
        </el-dialog>       
    </div>
</template>

<script type="text/ecmascript-6">
import Login from '@/base/login/login'
import Register from '@/base/register/register'

    const delay = (function() {
        let timer = 0;
        return function(callback, ms) {
            clearTimeout(timer)
            timer = setTimeout(callback, ms)
        }
    })()
    
    export default {
        data() {
            return {
                loginVisible: false,
                registerVisible: false,
                search: '',
                songs: [],
                timeout: null 
            }
        },
        methods: {
            showRegisterForm: function() {
                this.loginVisible = false,
                this.registerVisible = true
            },
            loadSong() {
                return 
            },
            querySearchAsync(queryString, cb) {
                var songs = this.songs
                var results = queryString ? songs.filter(this.createStateFilter(queryString)) : songs
                clearTimeout(this.timeout)
                this.timeout = setTimeout(() => {
                    cb(results)
                }, 3000 * Math.random()) 
            },
            createStateFilter(queryString) {
                return (state) => {
                    return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
                }
            },
            handleSelect(item) {
                console.log(item)
            }
        },
        components: {
            Register,
            Login
        },
    }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .m-header
        display: flex
        align-items: center
        background-color: #FFFFFF
        padding-left:50px
        margin-top: -46px
        margin-bottom:-40px
        .line
            margin-top: -60px
        .icon
            .icon_img
                width:120px
                height:115px
            a
                text-decoration: none
            .icon_txt 
                padding-top: 50px
        .tab
            display: flex

            .nav_item
                flex: 1
                
                width: 200px
                height: 90px
                float: left 
                text-align: center
                line-height: 90px
                list-style: none
                .nav_item_link
                    display: block
                    height: 90px
                    font-size: 18px
                    text-decoration: none
                    
                    .current_block
                        color: #FFFFFF
                        background: #FFA5A5
                        font-size: 30px
                    .other_block
                        color: #000000
                        font-size: 30px
                    .other_block:hover
                        color: #FFA5A5
        .search
            position: relative
            left: 200px
            width: 250px
            border-radius: 3px
            border: 1px solid #c9c9c9
        .login_btn
            position: relative
            left: 300px
</style>
