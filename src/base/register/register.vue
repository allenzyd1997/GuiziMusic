<template>
    <div class="register">
        <el-form :model="newUser" :rules="loginRules" ref="User" >

        <el-form-item label="账号" prop="username" >
        <el-input v-model="newUser.username" ></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="password" >
        <el-input type="password" v-model="newUser.password" auto-complete="new-password"></el-input>
        </el-form-item>

        <el-form-item label="确认密码" prop="checkPass" >
        <el-input type="password" v-model="newUser.checkPass" auto-complete="new-password"></el-input>
        </el-form-item>

        </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="primary" @click.native.prevent="reset">重 置</el-button>
      <el-button type="primary" @click.native.prevent="handleRegister" :loading=registering>注 册</el-button>
    </div>
    </div>
</template>

<script type="text/ecmascript-6">
import {requseLogin} from '@/axios/api'
export default {
    data() {
        return {
            dialogFormVisible: false,

            newUser: {
                username: '',
                password: '',
                checkPass: ''
            },
            loginRules: {
                username: [{required: true, message: '请输入账号', trigger: 'blur'}],
                password: [{required: true, message: '请输入密码', trigger: 'blur'}]
            },
            checked: true,
            registering: false
        }
    },
    methods: {
        reset() {
            this.$refs.User.resetFields()
        },
        handleRegister() {
            this.$refs.User.validate((valid) => {
                if (valid) {
                    this.registering = true;
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
                            sessionStorage.setItem('user', JSON.stringify(user))
                            this.$router.push({path: '/'})
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
            this.$emit('showRegisterForm');
        }
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