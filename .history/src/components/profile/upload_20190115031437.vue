<template>
    <div class="upload">
        <div class="notic">
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
        padding-left: 100px
</style>
