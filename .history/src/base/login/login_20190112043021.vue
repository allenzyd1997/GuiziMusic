<template>
    <div class="login">
        <el-form :model="User" :rules="loginRules" ref="User" >

        <el-form-item label="账号" prop="username" >
        <el-input v-model="User.username" ></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="password" >
        <el-input type="password" v-model="User.password" auto-complete="new-password"></el-input>
        </el-form-item>


        <el-form-item label="记住密码" prop="delivery">
        <el-switch v-model="User.delivery"></el-switch>
        </el-form-item>

          <span class="pwd">
            <el-button >忘记密码？</el-button>
            <el-button @click.native.prevent='register'>还没账号,注册一个</el-button>
          </span>
        </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="primary" @click.native.prevent="reset">重 置</el-button>
      <el-button type="primary" @click.native.prevent="handleLogin" :loading=logining>登 录</el-button>
    </div>
    </div>
</template>

<script type="text/ecmascript-6">
import {requseLogin} from '@/axios/api'
import { mapGetters, mapActions, mapState } from 'vuex'
export default {
    data() {
        return {
            dialogFormVisible: false,

            User: {
                username: '',
                password: '',
                delivery: ''
            },
            loginRules: {
                username: [{required: true, message: '请输入账号', trigger: 'blur'}],
                password: [{required: true, message: '请输入密码', trigger: 'blur'}]
            },
            checked: true,
            logining: false
        }
    },
    methods: {
        ...mapActions({
            'userLogin': 'login/UserLogin'
        }),
        reset() {
            this.$refs.User.resetFields()
        },
        handleLogin() {
            this.$refs.User.validate((valid) => {
                if (valid) {
                    this.logining = true;
                    let loginParams = {
                        username: this.User.username,
                        password: this.User.password
                    }
                    requseLogin(loginParams).then(res => {

                        this.logining = false
                        let { code, msg, user} = res.data
                        if (code === 200) {
                            this.$message({
                                type: 'success',
                                message: msg
                            })
                            this.userLogin(JSON.stringify(user))                            
                            //sessionStorage.setItem('user', JSON.stringify(user))
                            
                            location.reload()
                            this.$router.go(0)
                        } else {
                            this.$message({
                                type: 'error',
                                message: msg
                            })
                        }
                    }).catch(err => {
                        console.log(err)
                    })
                }
            })
        },
        register() {
            this.$emit('showRegisterForm')
        }
    },
    computed: {
        ...mapGetters({
            loginVisible: 'login/loginVisible'
        })
    },
}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    a
        text-decoration: none
        color: #000
    .login
        margin-top: -50px
        .dialog-footer
            margin-top: 20px
</style>