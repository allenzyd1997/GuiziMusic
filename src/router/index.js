import Vue from 'vue'
import Router from 'vue-router'
import Profile from '@/components/profile/profile'
import Recommand from '@/components/recommand/recommand'
import Rank from '@/components/rank/rank'
import Singer from '@/components/singer/singer'
import Album from '@/components/album/album'
import Playlist from '@/components/playlist/playlist'
import Login from '@/base/login/login'
import store from '../store'
import SingerDetail from '@/components/singer-detail/singer-detail'
import IconMenu from '@/base/icon-menu/icon-menu'
Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/recommand'
    },
    {
      path: '/profile',
      component: Profile
    },
    {
      path: '/recommand',
      component: Recommand
    },
    {
      path: '/rank',
      component: Rank
    },
    {
      path: '/singer',
      component: Singer
    },
    {
      path: '/album',
      component: Album
    },
    {
      path: '/playlist',
      component: Playlist
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/singer-detail',
      component: SingerDetail
    },
  ]
})

/**
 * 路由守卫
 */

router.beforeEach((to, from, next) => {

  let token = store.state.token
  // 判断路由是否需要权限
  if (to.meta.requiresAuth) {
    if (token) {
      next()
    } else {
      next({
        path: '/login',
        query: {
          redirect: to.fullPath // 将刚刚要去的路由path作为参数，方便登录成功后直接跳转到该路由
        }
      })
    }
  } else {
    next()
  }
})

export default router