<template>
<!-- Home page has Navigation, content and footer components -->
  <div id="app">
    <Navigation activeLink="Home"/>
    <Content />
    <router-view></router-view>
    <Footer />
  </div>

</template>

<script>
import Content from "../components/Content";
import Navigation from "../components/Navigation.vue";
import Footer from '../components/Footer.vue'

export default {
  name: "Home",
  components: {
    Content,
  },
  components: {
    Navigation,
    Content,
    Footer
  }, 
  
};
</script>
