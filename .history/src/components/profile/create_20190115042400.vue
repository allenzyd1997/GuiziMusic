<template>
    <div class="song">
        <div class="profile_cont">
            <div class="mod_songlist_toolbar">
                <el-button @click="createDialogVisible = true">新建歌单</el-button>
            </div>
            <div class="mod_songlist">
            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%">
            
                <el-table-column label="歌单" width="400px" prop="song">
                    <template scope="scope">
                        <img :src="scope.row.imgUrl" width="60px" height="60px"><span>{{scope.row.songlist_name}}</span>
                    </template>
                </el-table-column> 
                <el-table-column width="400px">
                    <template scope="scope">
                        <div class="icon-menu" style="transform: scale(0.7)">
                            <a href="javascript:;" title="播放">
                                <i class="icon_button icon_play_opacity"></i>
                            </a>
                            <a href="javascript:;" title="删除" @click="_deleteSonglist(scope.row.songlist_id)">
                                <i class="icon_button icon_add_opacity"></i>
                            </a>                
                        </div>
                    </template>                            
                </el-table-column>
                <el-table-column label="歌单标签" width="200" prop="songlist_label">

                </el-table-column>
            </el-table> 
            </div>
            		<div id="album_foot" class="album_foot">
					<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">
					</el-pagination>
				</div>

        </div>
        <el-dialog title="新建歌单" :visible.sync="createDialogVisible" width="30%" center>
            <el-form>
                <el-form-item label="歌单名称" v:model="form">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="createDialogVisible = false">取消</el-button>
                <el-button @click="_createSonglist">确定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import {getSongListByUser, createSonglist, deleteSonglist} from '@/axios/api'
import { mapGetters} from 'vuex'
import IconMenu from '@/base/icon-menu/icon-menu'
export default {
    data() {
        return {
            page: 1,
            size: 5,
            tableData: [],
            total: 0,
            form: {
                name: '',
            },
            createDialogVisible: false
        }
    },
    methods: {
        getRows() {
            getSongListByUser(this.hasUser).then(res => {
                if(!res.data)
                    return 
                this.tableData = res.data
                this.total = res.data.total
            })
        },
        handleCurrentChange(val) {
            this.page = val
            this.getRows()
        },
        _createSonglist() {
            let params = {
                songlist_id: Math.floor((Math.random()*90000)+1),
                user_id: this.hasUser,
                songlist_name: this.form.name,
                songlist_time: Date.parse(new Date())
            }
            createSonglist(params).then(res => {
                if (!res) {
                    this.$message({
                        type: error,
                        message: '创建失败'
                    })
                } else {
                    this.$message({
                        type: success,
                        message: '创建成功'
                    })
                }
            }).catch(err => {
                    console.log(err)
            })
        },
        _deleteSonglist(id) {
            deleteSonglist().then(res => {
                if (!res.data) {
                    this.$message({
                        type: error,
                        message: '删除失败'
                    })
                } else {
                    this.$message({
                        type:success,
                        message: '删除成功'
                    })
                }
            })
        }
    },
    mounted() {
        //console.log(this.hasUser)
        this.getRows()
    },
    computed: {
        ...mapGetters({
            hasUser: 'login/hasUser'
        })
    },
    components: {
        IconMenu
    }
}
</script>

<style scoped lang="stylus">
    .mod_songlist_toolbar
        padding-top: 50px
        padding-right: 1300px
    .mod_songlist
        margin-top: 50px
        margin-left: 120px
</style>