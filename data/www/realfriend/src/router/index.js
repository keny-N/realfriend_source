import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import GameBody from "@/components/GameBody"
import LogIn from "@/components/LogIn"
import UserProfile from "@/components/UserProfile"
import User from "@/components/User"
import UserChangeSuccess from "@/components/UserChangeSuccess"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/game/:friendid',
      name: 'GameBody',
      component: GameBody
    },
    {
      path: '/main/:userId',
      name: 'Main',
      component: Main,
    },
    {
      path: '/user/:userId',
      name: 'User',
      component: User,
      children: [
        {
          path: 'profile',
          component: UserProfile

        },
        {
          path: 'success',
          component: UserChangeSuccess,
        }
      ]
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
  ]
})
