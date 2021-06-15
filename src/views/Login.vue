<template>
  <div>
    <!-- Login view accessed at / route -->
    <div class="welcome-section bg-light container">
      <h1>Welcome to this Auction Site(Test section)</h1>

      <div
        class="g-signin2"
        data-onsuccess="onSignIn"
        data-longtitle="true"
        data-theme="dark"
      ></div>
      <router-link to="/home" class="btn" >Log In</router-link>
    </div>
  </div>
</template>

<style scoped>
.welcome-section {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
}
</style>