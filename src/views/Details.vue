<template>
  <div id="app">
    <Navigation />
    <router-view></router-view>
    <!-- Auction Detail View Component -->
    <div class="container h-100">
      <div class="row d-flex justify-content-between h-100">
        <!-- Images and description -->
        <div class="col-md-7 col-sm-12">
          <div
            class="
              card
              d-flex
              flex-column
              justify-content-between
              align-items-center
            "
            style="height: 50vh"
          >
            <img
              :src="auction.item.image"
              alt="Product Image"
              class="card-img-top"
            />
            <h3>Name : {{ auction.item.name }}</h3>
            <h4>Description : {{ auction.item.description }}</h4>
            <div class="text-center">
              <h3>Countdown Till Expiration Date</h3>
              <h5 id="timer" class="text-info"></h5>
            </div>
          </div>
        </div>
        <!-- Latest information -->
        <div class="col-md-5 col-sm-12 d-flex flex-column align-items-center">
          <div class="mt-2">
            <h3>Highest bid : {{ auction.currentHighest }}</h3>
            <h3>Initial Price : {{ auction.startingPrice }}</h3>
          </div>

          <div class="mt-2">
            <h3>Highest bidder details</h3>
          </div>
        </div>
        
        <!-- Form for entering bid -->
        <form class="mt-3 d-flex justify-content-center"  @submit="updateBid">
          <input
            type="number"
            v-model="bidAmount"
            class="form-control w-25"
            placeholder="Enter your bid here"
          />
          <button class="btn btn-warning searchButton" type="submit">
            Submit
          </button>
        </form>
        <div class="container mt-3">
          <table class="table text-center">
            <thead class="bg-light">
              <th>Bid No</th>
              <th>Bidder Name</th>
              <th>Bid Time</th>
              <th>Bid Amount</th>
            </thead>
            <tbody class="text-center">
              <!-- <tr v-if="itemDetails.bids.length === 0">
					<td colspan="4">No Bids for Item</td>
				</tr> -->

              <tr :key="bid.id" v-for="bid in auction.bids">
                <td>{{ bid.id }}</td>
                <td>{{ bid.bidder_id }}</td>
                <td>{{ bid.bid_date }}</td>
                <td>{{ bid.amount }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navigation from "../components/Navigation.vue";
import Footer from "../components/Footer.vue";
import { mapActions, mapGetters } from "vuex";
import auctions from '../store' 

export default {
  name: "Details",
  components: {
    Navigation,
    Footer,
  },
  data() {
    return {
      bidAmount: "",
      auction: Object,
    };
  },
  
  methods: {
    async fetchAuction(id) {
      
      const response = await fetch(`http://localhost:5000/auction/auction/${id}`);
      const data = await response.json();
      console.log(data);
      return data;
    },
    ...mapActions(['getAuction','updateAuctions']),
    countdown() {
      var date = this.auction.endDate;
      
      var countDownDate = new Date(date);
      console.log(date);
      // Update the count down every 1 second
      setInterval(function () {
        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor(
          (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
        );
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"
        document.getElementById("timer").innerHTML =
          days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

        // If the count down is finished, write some text
        if (distance < 0) {
          clearInterval(x);
          document.getElementById("timer").innerHTML = "EXPIRED";
        }
        
      }, 1000);
    },

    //update bids
    updateBid(e) {
      console.log("update bid called");
      e.preventDefault();
      
      this.auction.bids.unshift({
        id: Math.random(),
        bidder_id: "some_id2",
        amount: this.bidAmount,
        bid_date: Date.now(),
      });
      this.auction.currentHighest = this.bidAmount;
      this.updateAuctions(this.auction);
    },
  },
  
  // Get details and start countdown upon loading
  async created() {
    // this.auction = this.$store.getters.activeAuction(this.$route.params.id);
    this.auction = await this.fetchAuction(this.$route.params.id);
    console.log(this.auction);
    this.countdown();
  },
};
</script>

<style scoped>
input {
  border-radius: 0;
}
.searchButton {
  border: 1px solid #508086;
  background: #508086;
  text-align: center;
  color: #fff;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
}
</style>