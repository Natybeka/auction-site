<template>
  <div class="col mb-5">
    <div class="card h-100">
      <!-- Product image-->
      <img
        class="card-img-top"
        src="../assets/images/cameras.jpg"
        alt="product-image"
      />
      <!-- Product details-->
      <div class="card-body p-4">
        <div class="text-center">
          <!-- Product name-->
          <h5 class="fw-bolder">{{auction.item.name}}</h5>
          <!-- Product price-->
          <p>{{auction.item.description}}</p>
        </div>
      </div>
      <!-- Product actions-->
      <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
        <div class="text-center">
          <a v-on:click="goToDetails(auction.id)" class="btn btn-outline-dark mt-auto">View Bids</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default ({
    name : "Auction_Card",
    props : {
        auction : Object
    },
    methods : {
      goToDetails(auctionId) {
        this.$router.push({name : 'Details', params:{id:auctionId}})
      }
    }
});
</script>
