import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import GameBody from "@/components/GameBody"
import LogIn from "@/components/LogIn"
import UserProfile from "@/components/UserProfile"
import UserChangeSuccess from "@/components/UserChangeSuccess"
import Log from "@/components/LogDisplayBody"
import store from "@/store"

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/game/:friendId',
      name: 'GameBody',
      component: GameBody
    },
    {
      path: '/main/',
      name: 'Main',
      component: Main,
    },
    {
      path: '/profile/:userId',
      name: 'Profile',
      component: UserProfile
    },
    {
      path: '/changesuccess/:userId',
      name: 'ChangeSuccess',
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
  ],

})

//グローバルにパラメータのバリデーションを行う
//アクセスのガードを行う
router.beforeEach((to, from, next) => {

  if (store.getters["token/loginGet"] === true) {
    this.$store.dispatch('counter/increment', "autoLogin")
    next()
  } else if (store.getters["token/tokenGet"] !== '0' && store.getters["token/firstFlagGet"] === false) {
    this.$store.dispatch('counter/increment', "autoLogin")
    next()
  } else {
    store.dispatch("token/setLogin", true)
    next('/login')
  }
})

export default router

