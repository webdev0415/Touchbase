import Vue from 'vue'
import './plugins/vuetify'
import store from '@/store/init'
import router from '@/router'
import ImgInputer from 'vue-img-inputer'
import 'vue-img-inputer/dist/index.css'

import { createProvider } from '@/apollo'

import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false
Vue.component('ImgInputer', ImgInputer)

// NOTE: could possibly make it a key and test decrypt just as a little bit more security
// Vue.prototype.$loggedIn = function() {
//   return localStorage.getItem('jwt-token') ? true : false
// }
Vue.prototype.$loggedIn = function() {
  return true
}

Vue.prototype.$username = function() {
  return localStorage.getItem('username')
}

new Vue({
  router,
  store,
  apolloProvider: createProvider(),
  render: h => h(App)
}).$mount('#app')
