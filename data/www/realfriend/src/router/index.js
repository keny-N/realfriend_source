import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/main'
import Game from '@/components/game'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/game',
      name: 'Game',
      component: Game
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    },
    {
      path: '/',
      name: 'Main',
      component: Main
    }
  ]
})
