// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import 'element-ui/lib/theme-chalk/index.css'
import store from './store'
import '@/common/stylus/index.styl'
import Mock from './mock/index.js'


 
import '@/assets/theme/element-#ffa5a5/index.css'
import ElementUI from 'element-ui'

Mock.init()
Vue.config.productionTip = false

Vue.use(ElementUI)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
})
