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
      path: '/main/:userId',
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
  // console.log(store.token.getters.loginGet)

  //この書き方でstoreのトークンを取得しています。
  //importしたstoreでstoreフォルダのindex.jsを参照し。stateの中身を見に行っています
  //modluesに設定したtokenをさらに参照し、Token.jsのstateにあるtokenを呼び出しています
  // console.log(store.state.token.token)
  if (store.getters["token/loginGet"] === true) {
    // console.log('aaaa')
    next()
  } else if (store.getters["token/tokenGet"] !== '0' && store.getters["token/firstFlagGet"] === false) {
    // console.log('bbbbb')
    next()
  } else {
    store.dispatch("token/setLogin", true)
    // console.log(store.token.getters.loginGet)
    next('/login')
  }
})

export default router

