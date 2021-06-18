<template>
  <div>
    <div class="flash-container">
      <FlashMessage :position="'top'"></FlashMessage>
    </div>
    <!-- Login view accessed at / route -->
    <section class="login-section">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-6 text-center mb-5">
            <h2 class="heading-section">Auction Site</h2>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-md-6 col-lg-4">
            <div class="login-wrap p-0">
              <h3 class="mb-4 text-center">Have an account?</h3>
              <div action="" class="signin-form">
                 <!-- Email input field -->
                <div class="form-group">
                  <input
                    type="email"
                    class="form-control email"
                    placeholder="some@email.com"
                    v-model="email"
                    required
                  />
                </div>
                <!-- Password input field -->
                <div class="form-group">
                  <input
                    id="password-field"
                    type="password"
                    class="form-control password"
                    placeholder="Password"
                    v-model="password"
                    required
                  />
                  <!-- <span
                    toggle="#password-field"
                    class="fa fa-fw fa-eye field-icon toggle-password"
                  ></span> -->
                </div>
                <div class="form-group">
                  <!-- <router-link
                    to="/home"
                    class="form-control btn btn-primary submit px-3"
                    >Log In</router-link
                  > -->
                  <button
                    class="btn btn-block p-2 logInBtn"
                    @click="normal_login"
                  >
                    Login
                  </button>
                </div>
                <div class="form-group d-md-flex">
                  <div class="w-100 text-md-right">
                    <router-link to="/" style="color: #fff">Don't have an account</router-link>
                  </div>
                  <div class="w-100 text-md-right">
                    <a href="#" style="color: #fff">Forgot Password</a>
                  </div>
                </div>
              </div>
              <p class="w-100 text-center">&mdash; Or Sign In With &mdash;</p>
              <div class="social d-flex text-center">
                <button class="btn btn-default btn-block mr-4" @click="handleGoogle">
                 <i class="fab fa-google fa-3x"></i>
                </button>
                <button class="btn btn-defualt btn-block mr-4" @click="handleGoogle">
                 <i class="fab fa-facebook-f fa-3x"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- <div class="welcome-section bg-light container">
      <h1>Welcome to this Auction Site(Test section)</h1>

      <div
        class="g-signin2"
        data-onsuccess="onSignIn"
        data-longtitle="true"
        data-theme="dark"
      ></div>
      
      <router-link to="/home" class="btn btn-primary" >Log In</router-link>
    </div> -->
  </div>
</template>


<script>
import firebase from "firebase";
import "firebase/auth";
import axios from "axios"


let path = "http://localhost:5000/auth";

export default {
  name: "Login",

  data(){
    return {
      email:"",
      password:""
    };
  },
  methods: {
    update_api: function (user_info) {
      axios
        .post(`${path}/signuser, { user_info }`)
        .then(() => {})
        .catch((err) => {
          this.flashMessage.error({
            message: err.message,
          });
        });
    },
    // Function to get id from firebase_id
    get_user_id: function () {
      axios
        .post(`${path}/getUserID/${this.firebase_id}`)
        .then(async (response) => {
          this.user_id = await response.data.id;
          this.team_name = await response.data.team_name;


          // Add User ID to local storage or cookies
          // Update store state
          if (this.user_id) {
            refs/remotes/origin/master
            this.$store.commit("setCurrentUserID", this.user_id);
            this.$store.commit("setMyTeamName", this.team_name);
            localStorage.setItem("token", response.data.token);
            // this.$store.dispatch("getActiveGameweek");
          }

          
        })
        .catch((err) => {
          this.flashMessage.error({
            message: err.message,
          });
        });
    },
    normal_login() {
      if (
        true
        // this.validate_email()
        // && this.validate_password()
      ) {
        // Call Firebase API
        firebase
          .auth()
          .signInWithEmailAndPassword(this.email, this.password)
          .then(
            async () => {
              // Get Current User
              let user = firebase.auth().currentUser;
              this.firebase_id = user.uid;
              // Function to call api route for adding to db (Incase the call during registration was inturrepted)
              this.update_api({
                firebase_id: this.firebase_id,
                fname: "Full",
                lname: "Name",
                team_name: "randomWords()",
              });

              // GET USER ID
              // Redirect to MyTeam Component in get_user_id
              this.get_user_id(this.firebase_id);

              // Redirect to login route
              this.$router.push({ name: "Home" });

              sessionStorage.setItem("userId", this.firebase_id)

              // GET USER ID
              this.get_user_id(this.firebase_id);
              // Flash Success Message at Login
              this.flashMessage.success({
                title: "Successfully Logged In",
                message:
                  "Login was successful",
              });

             
            },
            // If User email is already in use in firebase
            (err) => {
              this.flashMessage.error({
                message: `${err.message}`,
              });
            }
          );
      } else {
        this.flashMessage.error({
          title: "Invalid Input",
          message: "Please check your input.",
        });
      }

    },

    // for google
    handleGoogle() {
      var googleProvider = new firebase.auth.GoogleAuthProvider();
      let user = firebase.auth().currentUser;
      this.firebase_id = user.uid;

      firebase
        .auth()
        .signInWithPopup(googleProvider)
        .then(async () => {
          let user = firebase.auth().currentUser;

          this.firebase_id = user.uid;

          if (user.displayName){
            this.full_name = user.displayName;
          }

          this.$router.push({ name: "Home"})

          sessionStorage.setItem("userId", this.firebase_id)
         
        }),
        
        () => {
            // Call Error Handler Function
            console.log("Some error")
          }
    },
    
  },
};
</script>


<style scoped>
/* .welcome-section {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
} */
.login-section {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10rem 10px;
  color: white;
  background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
    url("~@/assets/bg.jpg");
  height: 100vh;
}

.flash-container {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  left: 35%;
  top: 3rem;
}
input[type="email"],
input[type="password"] {
  background: transparent;
  color: white;
}
input:focus {
  border: none !important;
  outline: none !important;
  background: white;
  color: #333;
}
input {
  transition: all 0.8s;
  outline: none !important;
}
input::placeholder {
  color: white;
}
input:focus::placeholder {
  color: #333;
}
.fa-google {
  color:  #0F9D58;
 }
.fa-facebook-f{
  color: #4267B2;
} 
.logInBtn{
  background-image: linear-gradient(to bottom right, rgb(8, 63, 99), rgb(28, 138, 241));
}
</style>
    