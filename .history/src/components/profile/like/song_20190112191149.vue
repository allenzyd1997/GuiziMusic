<template>
    <div class="song">
        <div class="songlist">
            <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle"
            @cell-mouse-enter="handleMouseEnter" @cell-mouse-leave="handleMouseOut">
            
                <el-table-column type="selection" width="55">
                </el-table-column>
                <el-table-column label="歌曲" width="200" prop="song">
                    <template scope="scope">
                        <img src="../../common/image/2.jpg" width="60px" height="60px"><span>刘思源</span>
                    </template>
                </el-table-column> 
                <el-table-column width="400px">
                    <template scope="scope">
                        <IconMenu></IconMenu>
                    </template>                            
                </el-table-column>
                <el-table-column label="歌手" width="200" prop="singer">

                </el-table-column>
                <el-table-column label="时长" width="200" prop="duration">

                </el-table-column>
            </el-table> 
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
