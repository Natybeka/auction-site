<template>
  <div class="col mb-5">
    <div class="card h-100">
      <!-- Product image-->
      <img
        class="card-img-top"
        v-bind:src="'./static/assets/'+item.image"
        alt="product-image"
      />
      <!-- Product details-->
      <div class="card-body p-4">
        <div class="text-center">
          <!-- Product name-->
          <h5 class="fw-bolder">{{item.name}}</h5>
          <!-- Product price-->
          <p>{{item.description}}</p>
        </div>
      </div>
      <!-- Product actions-->
      <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
        <div class="text-center">
          <a v-on:click="goToDetails(item.id)" class="btn btn-outline-dark mt-auto">View Bids</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default ({
    name : "Item_Card",
    props : {
        item : Object
    },
    methods : {
      goToDetails(itemId) {
        this.$router.push({name : 'Details', params:{id:itemId}})
      }
    }
});
</script>
