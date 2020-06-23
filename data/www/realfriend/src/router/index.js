import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import GameBody from "@/components/GameBody";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/game',
      name: 'GameBody',
      component: GameBody
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
    },
  ]
})
