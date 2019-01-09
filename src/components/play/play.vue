<template>
    <div class="player">
        <div class="normal-player" v-show='fullScreen'>
            播放器
        </div>
        <div class="mini-player" v-show='!fullScreen'>
            mini播放器
        </div>
    </div>
</template>


<script type="text/ecmascript-6">
    import {mapGetters} from 'vuex'

    export default {
        data () {
            return {

            }
        },
        created: function(){
            this.$emit('public_header', false)
            this.$emit('public_footer', false)
            this.$emit('public_tab', false)
        },
        computed:{
            ...mapGetters([
            'fullScreen',
            'playlist'
            ])
        }
    }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
    @import "~common/stylus/variable"
    @import "~common/stylus/mixin"
    .player
        .normal-player
            position:fixed
            left: 0
            right:0
            top:0
            bottom: 0
            z-index:150
            background: $color-background
        .background
            position:absolute
            left:0
            top:0
            width:100%
            height:100%
            z-index:-100
            opacity:0.6
            filter: blur(20px)
</style>

