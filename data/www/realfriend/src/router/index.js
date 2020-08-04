import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import GameBody from "@/components/GameBody"
import LogIn from "@/components/LogIn"
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

//グローバルにパラメータのバリデーションを行う
//アクセスのガードを行う
router.beforeEach((to, from, next) => {
  console.log(store.getters.loginGet)

  //この書き方でstoreのトークンを取得しています。
  //importしたstoreでstoreフォルダのindex.jsを参照し。stateの中身を見に行っています
  //modluesに設定したtokenをさらに参照し、Token.jsのstateにあるtokenを呼び出しています
  console.log(store.state.token.token)
  if (store.token.getters.loginGet === true) {
    console.log('aaaa')
    next()
  } else if (store.token.getters.token !== 0 && store.token.getters.firstFlag === false) {
    console.log('bbbbb')
    next()
  } else {
    store.dispatch("token/setLogin", true)
    console.log(store.token.getters.loginGet)
    next('/login')
  }


})

export default router

