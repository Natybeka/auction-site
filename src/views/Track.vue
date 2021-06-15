<template>
    <div id="app">
        <Navigation />
        
        <router-view></router-view>
        <Footer />
  </div>
</template>

<script>
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue' 

export default {
   name : 'Track',
   components : {
       Navigation,
       Footer
   }
}
</script>
