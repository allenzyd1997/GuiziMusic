<template>
    <div class="play">
        <p>this is title</p>
    </div>
</template>

<script>
export default {
    data () {
        return {

        }
    },
    created: function() {
        this.$emit('public_header', false)
        this.$emit('public_footer', false)
    }
}
</script>

<style>

</style>
