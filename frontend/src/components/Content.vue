<template>
  <div class="main-div">
    <!-- Header-->
    <header class="bg-dark py-5">
      <div class="container px-4 px-lg-5 my-5">
        <div class="text-center text-white">
          <h1 class="display-4 fw-bolder">Welcome To Auction Site</h1>
          <p class="lead fw-normal text-white-50 mb-0">
            Bid on Items with style
          </p>
        </div>
      </div>
    </header>
    <!-- Section-->
    <section class="py-5">
      <div class="filters">
        <SearchBar @submittedItem="filterItems"/>
      </div>
      <div class="container px-4 px-lg-5 mt-5">
        <!-- Items are to be rendered here (from search and filtering) -->
        <Auctions :auctions="auctions" />
      </div>
    </section>
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue";
import Auctions from "./Auctions.vue";
import { mapGetters, mapActions, mapState } from "vuex";
export default {
  name: "Content",
  data() {
    return {
      
    }
  },
  components: {
    SearchBar,
    Auctions,
  },
  computed: {
    ...mapGetters(["auctions"]),
  },
  async created() {
    // Call the getAllAuctions action in auctions store
    // To obtain all the available auctions
    await this.getAllAuctions();
  },

  methods: {
    ...mapActions(["getAllAuctions"]),

    filterItems(itemName) {
      console.log("Code here");
      this.itemSubset = this.allAuctions.filter(auction => auction.item.name === itemName)
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
