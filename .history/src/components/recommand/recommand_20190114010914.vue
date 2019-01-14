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
    },
    data() {
        return {
            page: 1,
            size: 20
            row1: ''  
        }
    } 
}


</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .playlist
        .carousal
            margin-bottom: 100px

            background-color: #ff7070;
            background-image: repeating-linear-gradient(90deg, transparent, transparent 50px,
                  rgba(255, 127, 0, 0.25) 50px, rgba(255, 127, 0, 0.25) 56px, transparent 56px, transparent 63px,
                  rgba(255, 127, 0, 0.25) 63px, rgba(255, 127, 0, 0.25) 69px, transparent 69px, transparent 116px,
                  rgba(255, 206, 0, 0.25) 116px, rgba(255, 206, 0, 0.25) 166px),
            repeating-linear-gradient(0deg, transparent, transparent 50px, rgba(255, 127, 0, 0.25) 50px,
                  rgba(255, 127, 0, 0.25) 56px, transparent 56px, transparent 63px, rgba(255, 127, 0, 0.25) 63px,
                  rgba(255, 127, 0, 0.25) 69px, transparent 69px, transparent 116px, rgba(255, 206, 0, 0.25) 116px,
                  rgba(255, 206, 0, 0.25) 166px),
            repeating-linear-gradient(-45deg, transparent, transparent 5px, rgba(143, 77, 63, 0.25) 5px,
                  rgba(143, 77, 63, 0.25) 10px),
            repeating-linear-gradient(45deg, transparent, transparent 5px, rgba(143, 77, 63, 0.25) 5px,
                  rgba(143, 77, 63, 0.25) 10px);
</style>





