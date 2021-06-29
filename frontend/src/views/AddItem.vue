<template>
  <div id="app">
    <Navigation activeLink="Add" />
    <router-view></router-view>
    <!-- <Simple-Stepper /> -->
    <AddItemForm />
    <Footer />
    
  </div>
</template>

<script>
import Navigation from "../components/Navigation.vue";
import Footer from "../components/Footer.vue";
// import SimpleStepper from '../demos/SimpleStepper.vue'
import AddItemForm  from "../components/AddItemForm.vue";
import {mapState} from "vuex"

export default {
  name: "AddItem",
  components: {
    Navigation,
    Footer,
    //    SimpleStepper
    AddItemForm,
  },
  computed : {
    ...mapState(['store'])
  },
  methods : {
    getMethod() {
      this.store.getters()
    }
  } 
};
</script>
