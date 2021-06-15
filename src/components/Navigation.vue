<template>
  <!-- Navigation-->
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container px-4 px-lg-5">
      <a class="navbar-brand" href="#">Auction-Site</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
          <li class="nav-item">
            <router-link class="nav-link" :class="activeLink ==='Home'? ' active':''" aria-current="page" to="/Home">Home</router-link>
          </li>
          <li class="nav-item"><router-link class="nav-link" :class="activeLink === 'track'? ' active':''" to="/Track">Track Bids</router-link></li>
          <li class="nav-item">
            <!-- <a
              class="nav-link dropdown-toggle"
              id="navbarDropdown"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              >Shop</a
            >
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="#!">All Products</a></li>
              <li><hr class="dropdown-divider" /></li>
              <li><a class="dropdown-item" href="#!">Popular Items</a></li>
              <li><a class="dropdown-item" href="#!">New Arrivals</a></li>
            </ul> -->
            <router-link class="nav-link" :class="activeLink ==='Add'? ' active':''" to='/Add'>Add Item</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="activeLink ==='Reviews'? ' active':''" to="/Reviews">My Reviews</router-link>
          </li>
        </ul>
        <form class="d-flex">
          <button class="btn btn-outline-dark" type="submit">
            <i class="bi-cart-fill me-1"></i>
            Cart
            <span class="badge bg-dark text-white ms-1 rounded-pill">0</span>
          </button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navigation",
  props : {
    activeLink : String
  } 
};
</script>

<style >
.nav-item .nav-link:hover, .nav-item .nav-link.active{
  text-decoration: underline black;
  text-underline-offset: 10px;
  text-decoration-thickness: 3px;
  font-weight: 600;
}
.nav-item {
  padding: 0;
  margin: 0;
}
</style>