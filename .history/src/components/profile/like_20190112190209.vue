<template>
    <div class="like">
        <div class="mod_tab profile_nav">
            <router-link to="/profile/like/song"><span class="mod_tab_item">歌曲</span></router-link>      
            <router-link to="/profile/create/songlist"><span class="mod_tab_item">歌单</span></router-link>
            <router-link to="/profile/focus/album"><span class="mod_tab_item">专辑</span></router-link>
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
    position: absolute 
    top: -56px
    left: 60px
    margin-bottom: 0
    width: 80%

a
    color: #fff
    text-decoration: none
</style>
