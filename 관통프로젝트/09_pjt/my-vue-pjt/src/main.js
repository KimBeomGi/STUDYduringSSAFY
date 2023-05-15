import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import jquery from 'jquery'
window.$ = window.jQuery = jquery
import 'popper.js/dist/umd/popper.js'



Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
