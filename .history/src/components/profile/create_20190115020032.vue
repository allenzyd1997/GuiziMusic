<template>
    <div class="song">
        <div class="profile_cont">
            <div class="mod_songlist_toolbar">
                <el-button>新建歌单</el-button>
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
                        <IconMenu></IconMenu>
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
    </div>
</template>

<script>
import {getSongListByUser} from '@/axios/api'
import { mapGetters} from 'vuex'
export default {
    data() {
        return {
            page: 1,
            size: 100,
            tableData: [],
            total: 0,
        }
    },
    methods: {
        getRows() {
            getSongListByUser(this.hasUser).then(res => {
                if(!res.data)
                    return 
                this.tableData = res.data
            })
        },
        handleCurrentChange(val) {
            this.page = val
            this.getRows()
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
}
</script>

<style scoped lang="stylus">
    .mod_songlist_toolbar
        padding-top: 50px
        padding-right: 928px
    .mod_songlist
        margin-top: 50px
        margin-left: 50px
</style>