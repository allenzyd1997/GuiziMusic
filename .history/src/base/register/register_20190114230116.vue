<template>
    <div class="register">
        <el-form :model="newUser" :rules="RegisterRules" ref="User" >

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
import {requseRegister} from '@/axios/api'
export default {
    data() {
        var validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请再次输入密码'))
            } else if (value !== this.newUser.password) {
                callback(new Error('两次输入密码不一致'))
            } else {
                callback()
            }
        }
        return {
            dialogFormVisible: false,

            newUser: {
                username: '',
                password: '',
                checkPass: ''
            },
            RegisterRules: {
                username: [
                    {required: true, message: '请输入账号', trigger: 'blur'},
                    {min: 5, max: 20, message: '长度在5到20个字符', trigger: 'blur'}
                ],
                password: [{required: true, message: '请输入密码', trigger: 'blur'}],
                checkPass: [{validator: validatePass, trigger: 'blur'}]
            },
            checked: true,
            registering: false
        }
    },
    methods: {
        reset() {
            this.$refs.newUser.resetFields()
        },
        handleRegister() {
            this.$refs.User.validate((valid) => {
                if (valid) {
                    this.registering = true;
                    let registerParams = {
                        username: this.newUser.username,
                        password: this.newUser.password
                    }
                    requseRegister(registerParams).then(res => {
                        this.registering = false
                        
                        if (res.data) {
                            this.$message({
                                type: 'success',
                                message: '注册成功'
                            })
                            location.reload()
                            this.$router.go(0)
                        } else {
                            this.$message({
                                type: 'error',
                                message: '登陆成功'
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