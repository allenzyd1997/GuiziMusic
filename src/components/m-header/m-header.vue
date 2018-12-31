<template>
    <div class="m-header">
        <h1 class="icon">
            <a href="" >
                <img src="" alt="桂子音乐">
            </a>
        </h1>
        <div class="tab">
            <ul>
                <li class="nav_item"><router-link class="nav_item_link" to="/">音乐馆</router-link></li>
                <li class="nav_item"><router-link class="nav_item_link" to="/profile">我的音乐</router-link></li>  
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
emit
<script type="text/ecmascript-6">
import Login from '@/base/login/login'
import Register from '@/base/register/register'
    export default {
        props: {
                User: {
                    name: '',
                    password: '',
                    delivery: ''
                },
                Rules: {

                }
        },
        data() {
            return {
                loginVisible: false,
                registerVisible: false     
            }
        },
        methods: {
            showRegisterForm() {
                loginVisible = false,
                registerVisible = true
            }
        },
        components: {
            Login,
            Register
        }
    }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .m-header
        display: flex
        align-items: center
        background-color: #fff
        .tab
            display: flex
            .nav_item
                flex: 1
                background: #31c27c
                width: 94px
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
