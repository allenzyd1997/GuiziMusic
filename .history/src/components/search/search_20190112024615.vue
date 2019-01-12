<template>
    <div class="search">
        <div class="mod_search">
            <el-autocomplete placeholder="搜索音乐、专辑、歌单、用户" v-model="search" :fetch-suggestions="querySearchAsync" @select="handleSelect" value-key="address">
                <i slot="prefix" class="el-input__icon el-icon-search"></i>
                <template slot-scope="{ item }">

                    <div class="name" v-if="item.address=='song'">歌曲:{{ item.value }}</div>

                    <span class="addr" v-if="item.address=='singer'">歌手:{{ item.value }}</span>
                </template>
            </el-autocomplete>
        </div>
        <div class="main">
            <div class="main_inner">
                <div class="result">
                    <div class="mod_tab">
                        <a href="javascript:;" class="mod_tab_item" @click="active_sub1">歌曲</a>
                        <a href="javascript:;" class="mod_tab_item" @click="active_sub2">歌单</a>
                        <a href="javascript:;" class="mod_tab_item" @click="active_sub3">专辑</a>
                    </div>
                    <div class="profile_cont">
                        <div v-if="js_sub1" class="js_sub">
                            <div class="mod_songlist_toolbar">
                                <el-button class="songlist_btn">播放全部</el-button>
                                <el-button class="songlist_btn">添加到</el-button>
                                <el-button class="songlist_btn">下载</el-button>
                                <el-button class="songlist_btn">批量操作</el-button>
                            </div>
                            <div class="playlist">
                                <el-table ref="multipleTable" :data="tableData" tooltip-effect="dark" style="width: 100%" selection-change="handleSelectionChange" :row-style="setRowStyle"
                                @cell-mouse-enter="handleMouseEnter" @cell-mouse-leave="handleMouseOut">
                                
                                    <el-table-column type="selection" width="55">
                                    </el-table-column>
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
                                    <el-table-column label="创建人" width="200" prop="duration">

                                    </el-table-column>
                                </el-table>                             
                            </div>
                        </div>              
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
  export default {
    data() {
      return {
        restaurants: [],
        state4: '',
        timeout:  null
      };
    },
    methods: {
            loadSong() {
                return [
        {"value": "123", "address": "song"},
        {"value": "456", "address": "song"},
        {"value": "1243", "address": "song"},
        {"value": "89", "address": "song"},
        {"value": "675", "address": "song"},
        {"value": "ads", "address": "singer"},
        {"value": "ds", "address": "singer"},
        {"value": "1fdsf", "address": "singer"},
        {"value": "dsf", "address": "singer"},
        {"value": "sdf", "address": "singer"},
                ];

            },
      querySearchAsync(queryString, cb) {
        var restaurants = this.restaurants;
        var results = queryString ? restaurants.filter(this.createStateFilter(queryString)) : restaurants;

        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(results);
        }, 3000 * Math.random());
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      handleSelect(item) {
        console.log(item);
      }
    },
    mounted() {
      this.restaurants = this.loadAll();
    }
  };
</script>

<style>

</style>
