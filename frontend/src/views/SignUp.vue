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
              <h3 class="mb-4 text-center">New to our site?</h3>
              <div class="signin-form">
                <!-- Email input field -->
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control username"
                    placeholder="Username"
                    v-model="username"
                    required
                  />
                </div>
                <div class="form-group">
                  <input
                    type="email"
                    class="form-control email"
                    placeholder="some@email.com"
                    v-model="email"
                    required
                  />
                </div>
                
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control fname"
                    placeholder="First Name"
                    v-model="firstname"
                    required
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control lname"
                    placeholder="Last Name"
                    v-model="lastname"
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
                  <input
                    type="text"
                    class="form-control address"
                    placeholder="stree, atCity"
                    v-model="address"
                    required
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control phone"
                    placeholder="+0123456789"
                    v-model="phone"
                    required
                  />
                </div>
                <div class="form-group">
                  <!-- <router-link
                    to="/home"
                    class="form-control btn btn-primary submit px-3"
                    >Log In</router-link
                  > -->
                  <button class="btn btn-defualt btn-block signInBtn" @click="normal_signUp">
                    Sign Up
                  </button>
                </div>
                <div class="form-group d-md-flex">
                  <div class="w-100 text-md-right">
                    <router-link to="/login" style="color: #fff"
                      >Already have an account</router-link
                    >
                  </div>
                  <!-- <div class="w-100 text-md-right">
                    <a href="#" style="color: #fff">Forgot Password</a>
                  </div> -->
                </div>
              </div>
              <p class="w-100 text-center">&mdash; Or Sign In With &mdash;</p>
              <div class="social d-flex text-center">
                <button class="btn btn-default btn-block mr-4" @click="handleGoogle">
                 <i class="fab fa-google fa-3x"></i>
                </button>
                <button class="btn btn-defualt btn-block mr-4" @click="handleFacebook">
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
// Firebase Library
import firebase from "firebase/app";
import "firebase/auth";
import axios from "axios";
import randomWords from "random-words"

let path = "http://localhost:5000/auth";

export default {
  name: "Register",
  data() {
    return {
      email: "",
      password: "",
      lastname: "",
      firstname: "",
      username: "",
      providerName: "",
      user_id: "",
      Username: "",
      phone: "",
      address: "",
      full_name: "",
    };
  },
  methods: {
    // Function to update db with firebase id
    update_api: async function (user_info) {
      console.log("here");
      axios
        .post(`${path}/signuser`, { user_info })
        .then(() => {})
        .catch((err) => {
          this.flashMessage.error({
            title: "Oops!",
            message: err.message,
          });
        });
    },

    // Function to get id from firebase_id

    get_user_id: function () {
      axios
        .get(`${path}/users/${this.firebase_id}`)
        .then(async (response) => {
          this.user_id = await response.data.id;

          // Add User ID to vue store
        })
        .catch((err) => {
          console.log(err.message);
          this.flashMessage.error({
            title: "Oops!",
            message: err.message,
          });
        });
    },

    // Function for firebase register with email and password
    normal_signUp() {
      // If Data is valid
      if (
        true
        // && this.validate_password()
      ) {
        // Call Firebase API
        firebase
          .auth()
          .createUserWithEmailAndPassword(this.email, this.password)
          .then(
            async () => {
              // Get Current User
              let user = firebase.auth().currentUser;
              this.firebase_id = user.uid;
              // Function to call api route for adding to db
              this.update_api({
                // userId: this.firebase_id,
                // Username: this.Username,
                // Phone: this.Phone,
                // Address: this.Address,
                UserId: this.firebase_id,
                Username: this.username,
                Password: this.password,
                FirstName: this.firstname,
                LastName: this.lastname,
                Email: this.email,
                Address: "Address",
                PhoneNumber: "PhoneNumber",
                Rating: 0,
              });
              // Redirect to login route
              this.$router.push({ name: "Login" });

              // GET USER ID
              this.get_user_id(this.firebase_id);
              // Flash Success Message at Login
              this.flashMessage.success({
                title: "Successfully Registered",
                message:
                  "Your Account has been created successfully. Please Sign in to continue",
              });
            },
            // If User email is already in use in firebase
            (err) => {
              this.flashMessage.error({
                title: "Oops!",
                message: `${err.message}`,
              });
            }
          );
      } else {
        this.flashMessage.error({
          title: "Invalid Credentials",
          message: "Please check you inputs",
          blockClass: "test",
          wrapperClass: "test",
          contentClass: "test",
        });
      }
    },

    // Function to handle SSO for all methods
    handle_sso: function () {
      // Find out the selected provider
      let provider;
      if (this.providerName == "Google") {
        provider = new firebase.auth.GoogleAuthProvider();
      } else if (this.providerName == "Github") {
        provider = new firebase.auth.GithubAuthProvider();
      } else if (this.providerName == "Facebook") {
        provider = new firebase.auth.FacebookAuthProvider();
      }

      // Call to firebase api
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(
          async () => {
            // Get Current User
            let user = firebase.auth().currentUser;
            // Get Firebase_id
            this.firebase_id = user.uid;
            // If API displays Full Name
            if (user.displayName) {
              this.full_name = user.displayName;
            } else {
              this.full_name = "Full Name";
            }
            // Request for id with firebase_id

            console.log("Here")
            
            axios
              .get(`${path}/getuser/${user.uid}`)
              .then((response) => {
                // If firebase_id in database
                console.log("Here2")
                if (response.data.code == "Error") {
                  // Redirect to home Component
                  
                  this.$router.push({ name: "Home" });
                  sessionStorage.setItem("userId", this.firebase_id);
                  // Call Function to HANDLE ID SHARING
                  this.get_user_id(this.firebase_id);
                }

                
                // If new firebase_id
                else if (response.data.code == "Success") {
                  // Add firebase_id to DB
                  console.log("Here3")
                  this.update_api({
                    UserId: this.firebase_id,
                    Username: randomWords(),
                    FirstName: "FirstName",
                    LastName: "LastName",
                    Email: user.email,
                    Address: "Address",
                    PhoneNumber: "PhoneNumber",
                    Rating: 0,
                  });

                  // Redirect to Pick Team Component
                  this.$router.push({ name: "Home" });
                  sessionStorage.setItem("userId", this.firebase_id);
                  // GET ID of user
                  this.get_user_id(this.firebase_id);
                }
              })
              .catch((err) => {
                console.log("Some error");
              });
          },
          () => {
            // Call Error Handler Function
            this.flashMessage.error({
              title: "Email already Associated with an account",
              message: "Registered with a different Provider",
            });
          }
        );
    },

    handleGoogle: function () {
      this.providerName = "Google";
      this.handle_sso();
    },

    github_login: function () {
      this.providerName = "Github";

      this.handle_sso();
    },

    handleFacebook: function () {
      this.providerName = "Facebook";

      this.handle_sso();
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
  background-repeat: no-repeat;
  background-size: cover;
  height: 120vh;
}
.flash-container {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  left: 35%;
  top: 3rem;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  background: transparent;
  color: white;
  font-weight: bold;
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
  color: #aaa;
  font-weight: normal;
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
.signInBtn{
  background-image: linear-gradient(to bottom right, rgb(99, 8, 87), rgb(241, 156, 28));
}
</style>