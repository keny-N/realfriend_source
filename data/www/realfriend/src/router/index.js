import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import GameBody from "@/components/GameBody"
import LogIn from "@/components/LogIn"
import Log from "@/components/LogDisplayBody"
import Menu from "@/components/Menu"
import Opening from "@/components/Opening"


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/game/:friendId',
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
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/log',
      name: 'Log',
      component: Log
    },
    {
      path:'/menu',
      name:'Menu',
      component: Menu
    },
    {
      path:'/opening',
      name:'Opening',
      component: Opening
    },
  ]
})
