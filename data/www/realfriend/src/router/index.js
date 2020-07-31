import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import GameBody from "@/components/GameBody"
import LogIn from "@/components/LogIn"
import UserProfile from "@/components/UserProfile"
import UserChangeSuccess from "@/components/UserChangeSuccess"
import Log from "@/components/LogDisplayBody"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/game/:friendId',
      name: 'GameBody',
      component: GameBody
    },
    {
      path: '/main/:userId',
      name: 'Main',
      component: Main,
    },
    {
      path:'/profile/:userId',
      name:'Profile',
      component: UserProfile
    },
    {
      path:'changesuccess/:userId',
      name:'ChangeSuccess',
      component: UserChangeSuccess
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
  ]
})
