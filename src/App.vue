<template>
  <div id="app">
    <div class="header-wrap">
      <MHeader v-if="header_show"></MHeader>
      <Tab></Tab>
    </div>
    <router-view></router-view>
    <MFooter  v-if="footer_show"></MFooter>
  </div>
</template>

<script type="text/ecmascript-6">
import MHeader from '@/components/m-header/m-header'
import MFooter from '@/components/m-footer/m-footer'
import Tab from '@/components/tab/tab'

export default {

  name: "app",
  data(){
      return{
      header_show:true,
      footer_show:true,
    }
  },
  components: {
    MHeader,
    MFooter,
    Tab
  },
}
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
