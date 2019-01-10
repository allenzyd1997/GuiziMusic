<template>
    <div class="recommand">
        <div class="playlist">
            <div class="section-inner">
                <Carousal></Carousal>
            </div>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">
import Carousal from '@/base/carousal/carousal'
export default {
    components: {
        Carousal
    }
}


</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .playlist
        
        .carousal
            margin-bottom: 100px
            background: linear-gradient(to bottom, #FFF0F0, #FFFFFF)
</style>





