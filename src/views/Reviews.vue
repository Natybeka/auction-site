<template>
    <div id="app">
        <Navigation activeLink="Reviews"/>
        <router-view></router-view>
        <Footer />
    </div>
</template>

<script>
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue' 

export default {
   name : 'Review',
   components : {
       Navigation,
       Footer
   }
}
</script>
