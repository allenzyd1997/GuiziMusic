<template>
	<div class="play">
		
	</div>
</template>

<script type="text/ecmascript-6">

	export default{

		name: 'play',
		components:{

		},
		data(){
			return{
				
			}
		},
		function(){
			this.$emit('public_header', false);
			this.$emit('public_footer', false);
		}
	}
</script>