<template>
  <div class="main-div">
    <!-- Header-->
    <header class="bg-dark py-5">
      <div class="welcome-section bg-light container">
        <h1>Welcome to this Auction Site(Test section)</h1>

        <div
          class="g-signin2"
          v-show="checkIfLoggedIn()"
          data-onsuccess="onSignIn"
          data-longtitle="true"
          data-theme="dark"
        ></div>
        <button class="btn" onclick="logOut()">Log out</button>
        <!-- Search Bar Component -->
        <SearchBar />
      </div>

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
      <div class="filters"></div>
      <div class="container px-4 px-lg-5 mt-5">
          <!-- Items are to be rendered here (from search and filtering) -->
          <Items :items="items"/>
      </div>
    </section>
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue"
import Items from "./Items.vue"
export default {
    name : 'Content',
    components : {
        SearchBar,
        Items
    },
    data : () => {
        return {
            items : [],
        }
    },
    async created() {
        this.items = await this.fetchItems();
        console.log(this.items);  
    },
    methods : {
        checkIfLoggedIn() {
            // Check if user has logged in with sessionStorage == null comparison
            if (sessionStorage.getItem('myUserEntity') == null) {
                console.log("logged in");
                return true;
            }
            console.log("logged out");
            return false;
        },

        //function that fetches all items
        async fetchItems() {
            console.log("Code is here");
            const res = await fetch("api/items");
           
            const data = await res.json();
            return data;
        }
    }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.welcome-section {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
}
</style>
