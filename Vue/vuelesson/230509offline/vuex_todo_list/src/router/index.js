import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPage from '@/views/AllTodoPage'
import ImportantTodoPage from '@/views/ImportantTodoPage'
import TodayTodoPage from '@/views/TodayTodoPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'AllTodoPage',
    component: AllTodoPage
  },
  {
    path: '/important',
    name: 'ImportantTodoPage',
    component: ImportantTodoPage
  },
  {
    path: '/today',
    name: 'TodayTodoPage',
    component: TodayTodoPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
