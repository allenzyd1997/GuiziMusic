<template>
    <div class="upload">
        <div class="notic">
        <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%">

        <el-table-column label="通知标题" width="200px" prop="song">
        <template scope="scope">
            <span>{{scope.row.notification_head}}</span>
        </template>
        </el-table-column> 
        <el-table-column width="600px" label="通知内容">
        <template scope="scope">
            <span>{{scope.row.notification_content}}</span>
        </template>                            
        </el-table-column>
        <el-table-column label="通知时间" width="200" prop="songlist_label">

        </el-table-column>
        </el-table> 
            		<div id="album_foot" class="album_foot">
					<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :total="total" style="float:right;">
					</el-pagination>
				</div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            tableData: []
        }
    }
}
</script>

<style scoped lang="stylus">
    .notic
        padding-top: 50px
        padding-left: 130px
</style>
