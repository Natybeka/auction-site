<template>
  <div class="main-div">
    <!-- Header-->
    <header class="bg-dark py-5">
      <div class="container px-4 px-lg-5 my-5">
        <div class="text-center text-white">
          <h1 class="display-4 fw-bolder">Shop in style</h1>
          <p class="lead fw-normal text-white-50 mb-0">
            With this shop hompeage template
          </p>
        </div>
      </div>
    </header>
    <!-- Section-->
    <section class="py-5">
      <div class="filters">
        <SearchBar />
      </div>
      <div class="container px-4 px-lg-5 mt-5">
        <!-- Items are to be rendered here (from search and filtering) -->
        <Auctions :auctions="allAuctions" />
      </div>
    </section>
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue";
import Auctions from "./Auctions.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Content",
  components: {
    SearchBar,
    Auctions,
  },
  computed: {
    ...mapGetters(["allAuctions"]),
  },
  async created() {
    this.allAuctions = await this.getAllAuctions(); 
  },

  methods: {
    ...mapActions(["getAllAuctions"]),
    checkIfLoggedIn() {
      // Check if user has logged in with sessionStorage == null comparison
      if (sessionStorage.getItem("myUserEntity") == null) {
        console.log("logged in");
        return true;
      }
      console.log("logged out");
      return false;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.filters {
  display: flex;
  justify-content: center;
}
</style>
