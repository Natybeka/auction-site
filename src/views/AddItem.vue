<template>
    <div id="app">
        <Navigation activeLink="Add"/>
        <router-view></router-view>
        <Footer />
    </div>
</template>

<script>
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue' 

export default {
   name : 'AddItem',
   components : {
       Navigation,
       Footer
   }
}
</script>
