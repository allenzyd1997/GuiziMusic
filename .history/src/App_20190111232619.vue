<template>
  <div id="app">

    <div class="header-wrap">
      <MHeader v-if="header_show"></MHeader>
      <Tab v-if="tab_show"></Tab>
    </div>

    <router-view v-if="isRouterAlive" v-on:public_tab="public_tab" v-on:public_header="public_header" v-on:public_footer="public_footer"></router-view> 

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
        tab_show:true,
        isRouterAlive: true
    }
  },
  components: {
    MHeader,
    MFooter,
    Tab,
  },
  methods: {
    public_header: function (bool) {
      this.header_show = bool
    },
    public_footer: function (bool) {
      this.footer_show = bool
    },

    public_tab:function(bool){
      this.tab_show = bool
    },
  }, 
}
</script>

<style scoped>

.header-wrap {
  margin: 0 100px;
}


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
