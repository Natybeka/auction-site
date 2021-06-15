import Vue from 'vue'
import App from './App.vue'
// import router from './router'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Login from './views/Login'
import Details from './views/Details'
Vue.config.productionTip = false


Vue.use(VueRouter);

// set up routes for pages
const router = new VueRouter({
  mode : 'history',
  routes : [
    {
      path : '/home',
      name : 'Home',
      component : Home
    },
    {
      path : '/',
      name :'Login',
      component: Login
    },
    {
      path : '/details/:id',
      name : 'Details',
      component : Details,
      props : true
    }
  ]
})
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

