<template>
    <div class="like">
        <div class="mod_tab profile_nav">
            <router-link to="/profile/like/song"><span class="mod_tab_item">歌曲</span></router-link>      
            <router-link to="/profile/like/songlist"><span class="mod_tab_item">歌单</span></router-link>
            <router-link to="/profile/like/album"><span class="mod_tab_item">专辑</span></router-link>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped lang="stylus">
.profile_nav
    float: left
    margin-left: 20px
    .mod_tab_item
        margin-left: 40px
        font-size: 16px
a
    color: #000
    text-decoration: none
</style>
