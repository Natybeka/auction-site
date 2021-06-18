<template>
<!-- Render products -->
<div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4">
    <div  :key="auction.id" v-for="auction in auctions">
        <Auction_Card  :auction="auction"/>
    </div>
</div>
  
</template>

<script>
import Auction_Card from "./Auction_Card.vue"
export default {
  name: "Auctions",
  components:{
      Auction_Card
  },
  props : {
       auctions : Array
  },
  
};
</script>

<style scoped>
</style>
