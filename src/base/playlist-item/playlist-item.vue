<template>
    <div class="playlist-item">
        <a href="">
            <img src="" onmouseover="waitPlay">
        </a>
    </div>
</template>

<script type="text/ecmascript-6">
export default {
    props: {
        height,
        width
    },
    methods: {
        waitPlay() {
            
        }
    } 
}
</script>

<style lang="stylus" scoped>
    .playlist-itemd
        img
            transform: scale(1.3);
            transition: all 1s ease 0s;
            -webkit-transform: scale(1.3);
            -webkit-transform: all 1s ease 0s;
</style>

