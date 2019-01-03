<template>
    <div class="tab-wrap">
        <div class="tab">
            <router-link class="tab-item" to='/recommand'>
                <span class="tab-link">推荐</span>
            </router-link>
            <router-link class="tab-item" to="/singer">
                <span class="tab-link">歌手</span>
            </router-link>
            <router-link class="tab-item" to="/album">
                <span class="tab-link">专辑</span>
            </router-link>
            <router-link class="tab-item" to="/rank">
                <span class="tab-link">排行</span>
            </router-link>
            <router-link class="tab-item" to="/playlist">
                <span class="tab-link">歌单</span>
            </router-link>
        </div>
    </div>
</template>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .tab-wrap

      border-top: 1px solid #f2f2f2
      line-height: 51px
      height: 51px
      .tab
        margin-left: 300px
        margin-right: 300px
        display: flex
        .tab-item
            flex:1
            text-align: center
            text-decoration: none
            .tab-link   
                font-size: 15px
                color: #000
            &.router-link-active
                .tab-link   
                    color: #FFA5A5
</style>