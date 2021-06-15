<template>
    <div id="app">
        <Navigation activeLink=""/>
        <router-view></router-view>
        <Footer />
    </div>
</template>

<script>
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue' 

export default {
   name : 'Details',
   components : {
       Navigation,
       Footer
   },
   data() {
       return {
           item : Object
       }
   },
   created() {
        console.log(typeof this.$route.params.id);
        var itemId = parseInt(this.$route.params.id);
        this.item = this.fetchItem(itemId)
   },
   methods : {
       async fetchItem(itemId) {
            const response = await fetch(`http://localhost:5000/items/${itemId}`)

            console.log(await response.json());
            
       }
   }
}
</script>