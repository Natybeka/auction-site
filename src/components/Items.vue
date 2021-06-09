<template>
<!-- Render products -->
<div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4">
    <div  :key="item.id" v-for="item in items">
        <Item_Card  :item="item"/>
    </div>
</div>
  
</template>

<script>
import Item_Card from "./Item_Card.vue"
export default {
  name: "Items",
  components:{
      Item_Card
  },
  props : {
       items : Array
  }
};
</script>

<style scoped>
</style>
