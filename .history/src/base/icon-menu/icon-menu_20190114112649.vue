<template>
    <div class="icon-menu">
        <a href="javascript:;" title="播放" @click="play">
            <i class="icon_button icon_play_opacity"></i>
        </a>
        <a href="javascript:;" title="添加到歌单" @click="add">
            <i class="icon_button icon_add_opacity"></i>
        </a>
        <a href="javascript:;" title="下载" @click="download">
            <i class="icon_button icon_upload_opacity"></i>
        </a>                   
    </div>
</template>

<script type="text/ecmascript-6">

    export default {
        methods: {
            play() {
                this.$emit("play")
            },
            add() {
                this.$emit("add")
            },
            download() {
                this.$emit("download")
            }
        },
        props: [SongIndex],
    }

</script>  

<style scoped lang="stylus" rel="stylesheet/stylus">
    .icon-menu
        transform: scale(0.7)
</style>