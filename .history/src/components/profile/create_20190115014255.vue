<template>
    <div class="song">
        <div class="profile_cont">
            <div class="mod_songlist_toolbar">
                <el-button>新建歌单</el-button>
            </div>
            <div class="mod_songlist">
            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%">
            
                <el-table-column label="歌单" width="200" prop="song">
                    <template scope="scope">
                        <img src="../../common/image/2.jpg" width="60px" height="60px"><span>刘思源</span>
                    </template>
                </el-table-column> 
                <el-table-column width="400px">
                    <template scope="scope">
                        <IconMenu></IconMenu>
                    </template>                            
                </el-table-column>
                <el-table-column label="曲目数" width="200" prop="singer">

                </el-table-column>
                <el-table-column label="收听" width="200" prop="duration">

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
export default {
    data() {
        return {
            tableData: {

            }
        }
    },
    methods: {
        getRows() {

        }
    },
    mounted() {
        getRows()
    }
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