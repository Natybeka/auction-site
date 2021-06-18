import Vue from 'vue'
import App from './App.vue'
// import router from './router'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Login from './views/Login'
import Details from './views/Details'
import Track from './views/Track'
import AddItem from './views/AddItem'
import Reviews from './views/Reviews'
import EditReview from './views/EditReview'
import Profile from './views/Profile'
import Register from './views/SignUp'
import store from './store'

import FlashMessage from "@smartweb/vue-flash-message"
import firebase from 'firebase/app'
import 'firebase/auth'
import randomWords from 'random-words'

var firebaseConfig = {
  apiKey: "AIzaSyDzsSTmNB89pp75V5UW4Cqdz0sAJoEToxs",
  authDomain: "webappelectro-acd0d.firebaseapp.com",
  projectId: "webappelectro-acd0d",
  storageBucket: "webappelectro-acd0d.appspot.com",
  messagingSenderId: "47353199602",
  appId: "1:47353199602:web:bd4745ecd2973e6c2b496b",
  measurementId: "G-TXK37G52MJ"
};

firebase.initializeApp(firebaseConfig);

Vue.use(FlashMessage);
Vue.use(randomWords)

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
      path : '/login',
      name :'Login',
      component: Login
    },
    {
      path : '/details/:id',
      name : 'Details',
      component : Details,
      props : true
    },
    {
      path : '/Track',
      name : 'Track',
      component : Track,
      props : true
    },
    {
      path : '/Add',
      name : 'AddItem',
      component : AddItem,
      props : true
    },
    {
      path : '/Reviews',
      name : 'Reviews',
      component : Reviews,
      props : true
    },
    {
      path : '/Review/:id',
      name : 'EditReview',
      component : EditReview,
      props : true
    },
    {
      path : '/Profile',
      name : 'Profile',
      component : Profile,
      props : true
    },
    {
      path : '/',
      name : 'Signup',
      component : Register,
      props : true
    }

  ]
})

// Entry point to application
new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')

