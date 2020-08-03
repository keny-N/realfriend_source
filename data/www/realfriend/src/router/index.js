import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import GameBody from "@/components/GameBody"
import LogIn from "@/components/LogIn"
import Log from "@/components/LogDisplayBody"
import Store from "../store"

Vue.use(Router)

const router = new Router({
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
    }
  ],


})

router.beforeEach((to, from, next) => {
    console.log(Store.getters.loginGet)
    console.log(Store.token.state.token)
  if (Store.getters.loginGet === true){

    console.log('aaaa')
    next()
  } else if (Store.getters.token !== 0 && Store.getters.firstFlag === false){
    console.log('bbbbb')
    next()
  }else{
    Store.dispatch("setLogin", true)
    console.log(Store.getters.loginGet)
    next('/login')
  }


})

export default router

