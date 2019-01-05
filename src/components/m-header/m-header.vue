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
            <form>
                <input class="input" type="text" placeholder="请输入您要搜索的内容...">
                <button class="search-btn" type="submit"></button>
            </form>
        </div>
        <div class="login">
            <el-button type="text" @click="registerVisible=true">注册</el-button>/
            <el-button type="text" @click="loginVisible=true">登陆</el-button>
        </div>
        <el-dialog title="登陆" :visible.sync="loginVisible" center:append-to-body="true" :lock-scroll="false" width="25%">
           <Login></Login>
        </el-dialog>
        <el-dialog title="注册" :visible.sync="registerVisible" center:append-to-body="true" :lock-scroll="false" width="25%">
           <Register></Register>
        </el-dialog>       
    </div>
</template>

<script type="text/ecmascript-6">
import Login from '@/base/login/login'
import Register from '@/base/register/register'
    export default {
        data() {
            return {
                loginVisible: false,
                registerVisible: false     
            }
        },
        methods: {
            showRegisterForm() {
                loginVisible = false,
                registerVisible = false
            }
        },
        components: {
            Register,
            Login
        }
    }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .m-header
        display: flex
        align-items: center
        background-color: #FFFFFF
        padding-left:50px
        margin-bottom:-40px
        .line
            margin-top: -60px
        .icon
            .icon_img
                width:120px
                height:115px
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
                    .other_block
                        color: #000000
                    .other_block:hover
                        color: #FFA5A5
        .search
            position: relative
            left: 100px
            width: 250px
            border-radius: 3px
            border: 1px solid #c9c9c9
            .input
                height: 36px
                width: 174px
                font-size: 14px
                border: 0 
            .search-btn
                position: absolute
                right: 0px; 
                width: 38px
                height: 36px
                border: 0 none
                padding: 0 0 0 0 
                
        .login
            flex: 1
</style>
