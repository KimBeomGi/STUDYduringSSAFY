import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '../views/HelloView'
import AboutView from '../views/AboutView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/hello/userName',
    name: 'hello',
    component : HelloView
  },
  {
    path:'/about',
    name:'about',
    component : AboutView,
    beforEnter(to, from, next){
      next({name:'hello', params:{userName:'About'}})
    }
  }
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next)=>{
  // console.log("이거 실행됩니다.")
  // console.log
  // console.log(to)
  // console.log(from)
  // // next()//next는 세번째 인자로 받아오는게 next 함수이다.
  // // next({name:'about'})  // 그냥 이래만 해놓으면 무한루프 돌아버림
  // // 그래서 아래처럼 하면됨
  // if(to.name != 'about'){
  //   next({name:'about'})
  // }else{
  //   next()
  // }
  next()
})

export default router
