<template>
    <div class="play">
        <!--遮罩-->
        <p>yoyoyo</p>
        <div class="mmPlayer-bg"
             :style="{backgroundImage: picUrl}"></div>
        <div class="mmPlayer-mask"></div>
    </div>
</template>


<script>
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
}
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
	
	/*遮罩*/
        .mmPlayer-mask, .mmPlayer-bg {
            position: absolute;
            top: 0;
            right: 0;
            left: 0;
            bottom: 0;
        }
        
        .mmPlayer-mask {
            z-index: -1;
            background-color: @mask_color;
        }
        
        .mmPlayer-bg {
            z-index: -2;
            background-repeat: no-repeat;
            background-size: cover;
            background-position: 50%;
            filter: blur(12px);
            opacity: .7;
            transform: translateZ(0);
            transition: all .8s;
        }
        

</style>

