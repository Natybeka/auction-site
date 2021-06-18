<template>
    <div id="app">
        <Navigation activeLink="Add"/>
        <router-view></router-view>
        <Simple-Stepper />
        <Footer />
    </div>
</template>

<script>
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue'
import SimpleStepper from '../demos/SimpleStepper.vue' 

export default {
   name : 'AddItem',
   components : {
       Navigation,
       Footer,
       SimpleStepper
   }
}
</script>
