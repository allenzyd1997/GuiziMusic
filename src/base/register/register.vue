<template>
    <div class="register">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="名称" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass">
            <el-input v-model="ruleForm.pass" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="checkPass">
            <el-input v-model="ruleForm.checkPass" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
    </el-form>
    </div>
</template>

<script type="text/ecmascript-6">

export default {
    data() {
        let validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                if (this.ruleForm.checkPass !== '') {
                    this.$refs.ruleForm.validateField('checkPass')
                }
                callback()
            }
        }
        let validatePass2 = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请再输入密码'))
            } else if (value !== this.ruleForm.pass) {
                callback(new Error('两次输入密码不一致！'))
            } else {
                callback()
            }
        }
        return {
            activeName: 'second',
            ruleForm: {
                name: '',
                pass: '',
                checkPass: '',
            },
            rule: {
                name: [
                    {
                        required: true, message: '请输入您的名称', trigger: 'blur'
                    },
                    {
                        min: 2, max: 5, message: '长度在2到5个字符', trigger: 'blur'
                    }
                ], 
                pass: [
                    {
                        required: true, validator: validatePass, trigger: 'blur'
                    },
                    {
                        required: true, validator: validatePass2, trigger: 'blur'
                    }
                ]
            }
        }
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.$message({
                        type: 'success',
                        message: '注册成功'
                    })
                } else {
                    console.log('error submit!!')
                    return false
                }
            })
        },
        resetForm(formName) {
            this.$ref[formName].resetFields()
        }
    }
}