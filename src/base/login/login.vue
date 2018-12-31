<!--<template>
    <p class="login">
            <el-tabs v-model="activeName" @tab-click="handleClick">
                <el-tab-pane label="登陆" name="first">
                    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                        <el-form-item label="名称" prop="name">
                            <el-input v-model="ruleForm.name"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="pass">
                            <el-input type="password" v-model="ruleForm.pass" auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('ruleForm')">登陆</el-button>
                            <el-button @click="resetForm('ruleForm')">重置</el-button>
                        </el-form-item>
                    </el-form>
                </el-tab-pane>
                <el-tab-pane>
                    <el-tab-pane label="注册" name="second">
                        <register></register>
                    </el-tab-pane>
                </el-tab-pane>
            </el-tabs>
    </p>
</template>-->

<template>
    <div class="login">
        <el-form :model="User" :rules="Rules" ref="User" >

        <el-form-item label="账号" prop="name" >
        <el-input v-model="User.name" ></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="pass" >
        <el-input type="password" v-model="User.pass" auto-complete="new-password"></el-input>
        </el-form-item>


        <el-form-item label="记住密码" prop="delivery">
        <el-switch v-model="User.delivery"></el-switch>
        </el-form-item>

          <span class="pwd">
            <el-button >忘记密码？</el-button>
            <el-button @click='register'>还没账号,注册一个</el-button>
          </span>
        </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button >取 消</el-button>
      <el-button type="primary" @click="submitForm()">登 录</el-button>
    </div>
    </div>
</template>

<script type="text/ecmascript-6">

export default {
    data() {
        return {
            dialogFormVisible: false,

            User: {
                name: '',
                password: '',
                delivery: ''
            },
            Rules: {

            },
          
        }
    },
    methods: {
        handleClick(tab, event) {

        },
        resetForm(formName) {
            this.$refs[formName].resetFields()
        },
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.$message({
                        type: 'success',
                        message: '登陆成功'
                    })
                    this.$router.push('recommand')
                } else {
                    console.log('error submit')
                    return false
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