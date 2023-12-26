import Vue from 'vue'
import Router from 'vue-router'
import Profile from '@/components/profile/profile'
import Recommand from '@/components/recommand/recommand'
import Rank from '@/components/rank/rank'
import Singer from '@/components/singer/singer'
import Album from '@/components/album/album'
import Playlist from '@/components/playlist/playlist'
import Login from '@/base/login/login'
import Register from '@/base/register/register'
import store from '../store'

import SingerDetail from '@/components/singer-detail/singer-detail'
import IconMenu from '@/base/icon-menu/icon-menu'
import AlbumDetail from '@/components/album-detail/album-detail'
import Play from '@/components/play/play'
import Comment from '@/base/comment/comment'
import Search from '@/components/search/search'
import Player from '@/components/player/player'
Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/recommand'
    },
    {
      path: '/profile',
      component: Profile,
      children: [
        {
          path: '/',
          redirect: '/profile/like'
        },
        {
          path: '/profile/like',
          component: () => import('@/components/profile/like.vue'),
          children: [
            {
              path: '/',
              redirect: '/profile/create'
            },
            {
              path: '/profile/like/song',
              component: () => import('@/components/profile/like/song')
            },
            {
              path: '/profile/like/songlist',
              component: () => import('@/components/profile/like/songlist')
            },
            {
              path: '/profile/like/album',
              component: () => import('@/components/profile/like/album')
            }
          ]
        },
        {
          path: '/profile/create',
          component: () => import('@/components/profile/create.vue')
        },
        {
          path: '/profile/upload',
          component: () => import('@/components/profile/upload.vue')
        },
        
      ]
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
      path: '/play',
      component: Play
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
      path: '/singer-detail',
      component: SingerDetail
    },
    {
      path: '/comment',
      component: Comment
    },
    {
      path: '/album-detail',
      component: AlbumDetail
    },
    {
      path: '/search',
      component: Search
    },
    {
      path: '/player',
      component: Player
    }
  ]
})

/**
 * 路由守卫
 */


export default router