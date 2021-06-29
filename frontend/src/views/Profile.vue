<template>
    <div id="app">
        <Navigation activeLink="Profile"/>
        <router-view></router-view>
        <div class="container">
            <div class="main-body">
                <div class="row gutters-sm">
                    <div class="col-md-4 mb-3">
                        <div class="card">
                            <div class="card-body">
                                <div class="d-flex flex-column align-items-center text-center">

                                    <img src="https://www.seekpng.com/png/detail/847-8474751_download-empty-profile.png" alt="Profile picture" class="rounded-circle" style="width:200px;height:200px;">
                                    <div class="mt-3">
                                        <h4>{{profile.FirstName}}  {{profile.LastName}}</h4>

                                        <p class="text-muted font-size-sm">{{profile.Email}}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-8">
                        <div class="card mb-3">
                            <div class="card-body">
                                <div class="row">
                                    <div class="col-sm-3">
                                        <h6 class="mb-0">First Name</h6>
                                    </div>
                                    <div class="col-sm-9 text-secondary">
                                        {{profile.FirstName}}
                                    </div>
                                </div>
                                <hr>
                                <div class="row">
                                    <div class="col-sm-3">
                                        <h6 class="mb-0">Last Name</h6>
                                    </div>
                                    <div class="col-sm-9 text-secondary">
                                        {{profile.LastName}}
                                    </div>
                                </div>
                                <hr>
                                <div class="row">
                                    <div class="col-sm-3">
                                        <h6 class="mb-0">Email</h6>
                                    </div>
                                    <div class="col-sm-9 text-secondary">
                                        {{profile.Email}}
                                    </div>
                                </div>
                                <hr>
                                <div class="row">
                                    <div class="col-sm-3">
                                        <h6 class="mb-0">Phone</h6>
                                    </div>
                                    <div class="col-sm-9 text-secondary">
                                        {{profile.PhoneNumber}}
                                    </div>
                                </div>
                                <hr>
                                <div class="row">
                                    <div class="col-sm-3">
                                        <h6 class="mb-0">Address</h6>
                                    </div>
                                    <div class="col-sm-9 text-secondary">
                                        {{profile.Address}}
                                    </div>
                                </div>
                                <hr>
                                <div class="row">
                                    <div class="col-sm-3">
                                        <h6 class="mb-0">Seller Rating</h6>
                                    </div>
                                    <!-- @* Display the Seller Rating *@
                                    @if (profile.Rating != 0)
                                    { -->
                                        <div v-if="profile.Rating != 0" class="col-sm-9 text-secondary">
                                            <div class="rating">
                                                {{profile.Rating}} / 5
                                                <div class="stars-outer">
                                                    <div class="stars-inner"></div>
                                                </div>
                                            </div>
                                        
                                        </div>
                                    <!-- }
                                    else
                                    { -->
                                        <div v-else class="col-sm-9 text-secondary">
                                            <div class="rating">
                                                {{profile.Rating}} / 5
                                                <div class="stars-outer">
                                                    <div class="stars-inner"></div>
                                                </div>
                                            </div>
                                            <h6 class="text-info">(Start Selling Items To Grow Your Rating)</h6>
                                        </div>
                                    <!-- } -->

                                </div>
                                <hr>
                                <div class="row">
                                    <div class="col-sm-12">
                                        <a class="btn btn-info text-white" id="profile-popup">Edit Details <i class="far fa-edit"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="row gutters-sm">
                            <div class="col-sm-12 mb-3">
                                <div class="card h-100">
                                    <div class="card-body">
                                        <h6 class="d-flex align-items-center mb-3"><i class="material-icons text-info mr-2">Reviews for</i>{{profile.Username}}</h6>
                                        <!-- @if (profile.UserReviews.Count() == 0)
                                        { -->
                                            <div v-if="profile.user_reviews == []" class="card mt-1"> You don't have any reviews yet</div>
                                        <!-- }
                                        else
                                        {
                                            foreach(var review in profile.UserReviews) { -->
                                                <div v-else class="card mt-1">
                                                    <div v-for="review in profile.user_reviews" :key="review.id">
                                                        <div class="card-header">
                                                            <h6 style="color: rgba(63, 155, 209, 0.6);">user {{review.ReviewerId}} <em>reviewed you on {{review.Date}}</em></h6>
                                                            <h6 display='inline'>
                                                                Rating : <span class="rating">
                                                                    {{review.Rating}} / 5
                                                                    <div class="stars-outer">
                                                                        <div class="stars-inner"></div>
                                                                    </div>
                                                                </span>

                                                            </h6>
                                                        </div>
                                                        <div class="card-body">
                                                            <p>
                                                                {{review.Description}}
                                                            </p>
                                                        </div>
                                                    </div>
                                                </div>
                                            <!-- }
                                        } -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="container">
                        <div class="profile-popup">
                            <div class="profile-popup-content">
                                <div class="close"><h3 style="position: absolute;top:-2%; left: 50%;transform: translate(-50%);">X</h3></div>
                                <div class="row">
                                    <div class="col-sm-12">
                                        {{warning}}
                                        <form @submit.prevent="editProfile" enctype="multipart/form-data">
                                            <div class="form-group">
                                                <input class="form-control" v-model="id" hidden />
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control" v-model="username" hidden/>
                                                <span class="text-danger"></span>
                                            </div>
                                            
                                            <div class="form-group">
                                                <label>Firstname</label>
                                                <input class="form-control" v-model="firstname"/>
                                                <span class="text-danger"></span>
                                            </div>
                                        
                                            <div class="form-group">
                                                <label>Lastname</label>
                                                <input class="form-control" v-model="lastname"/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <label>PhoneNumber</label>
                                                <input class="form-control" v-model="phonenumber"/>
                                                <span class="text-danger"></span>
                                            </div>
                                        
                                            <div class="form-group">
                                                <input class="form-control" v-model="email" hidden/>
                                                <span class="text-danger"></span>
                                            </div>
                                            
                                            <div class="form-group">
                                                <label>Address</label>
                                                <input class="form-control" v-model="address"/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control" v-model="rating" hidden/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control" v-model="userreviews" hidden/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <input type="submit" class="btn btn-info" value="Update" />
                                            </div>
                                        </form>
                                    </div>

                                </div>

                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
        <Footer />
    </div>
</template>

<script>

import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue' 

export default {
    
    data(){
        return{
            profile : {},
            id:null,
            username: null,
            firstname: null,
            lastname:null,
            phonenumber:null,
            email:null,
            address:null,
            warning:null,
            rating:null,
            userreviews:null
        }
    },
   name : 'Profile',
   components : {
       Navigation,
       Footer
   },
   methods : {
       getProfile(){
           let userId = sessionStorage.getItem('userId');
           console.log(userId);
           fetch(`http://localhost:5000/auth/users/${userId}`,{
               method : "GET",
               headers : {
                   "Content-Type" : "application/json"
               }
           }).then(resp => resp.json())
           .then(data => {
               this.username = data.Username
               this.firstname = data.FirstName
               this.lastname = data.LastName
               this.email = data.Email
               this.address = data.Address
               this.phonenumber = data.PhoneNumber
               this.profile = data
               this.id = data.UserId
               this.rating = data.Rating
           })
           .catch(error => {
               console.log(error)
           })
       },
       editProfile(){
           console.log("Edit Entered")
           if(!this.firstname || !this.lastname || 
                !this.phonenumber || !this.address){
                    this.warning = "Please fill all the fields"
           }else{
            let userId = sessionStorage.getItem("userId");
            fetch(`http://localhost:5000/auth/users/${userId}`,{
               method : "PUT",
               headers : {
                   "Content-Type" : "application/json"
               },
               body: JSON.stringify({
                   Username:this.username,
                   FirstName:this.firstname,
                   LastName:this.lastname,
                   PhoneNumber:this.phonenumber,
                   Email:this.email,
                   Address:this.address,
                   Rating:this.rating
               })
            }).then(resp => resp.json())
            .then(() => {
                document.querySelector(".profile-popup").style.display = "none";
                location.reload()
            })
            .catch(error => {  
                console.log(error)
            })
           }
       },
       popUp(){
           console.log("Entered Popup");
            document.getElementById("profile-popup").addEventListener('click',
                function () {
                    document.querySelector(".profile-popup").style.display = "flex";
                });

            document.querySelector('.profile-popup').addEventListener('click',
                function (e) {
                    if (e.target.parentElement.classList.contains('close'))
                        document.querySelector(".profile-popup").style.display = "none";
                });
            console.log("Everything is fine");
            // Calcuate the width of the stars and display in the UI
            const allRatings = document.querySelectorAll('.rating');
            var rating;
            var starPercentage;
            var starPercentageRounded;
            
            for (let i = 0; i < allRatings.length; i++) {
                rating = parseInt(allRatings[i].innerText);
                console.log(rating);
                starPercentage = (rating / 5) * 100;
                starPercentageRounded = `${Math.round(starPercentage / 10) * 10}%`;
                console.log(allRatings[i].firstElementChild)

                if (allRatings[i].firstElementChild.hasChildNodes()) {
                    allRatings[i].firstElementChild.firstElementChild.style.width = starPercentageRounded;
                }

            }
       }
   },
   mounted(){
           this.popUp()
    },
   created(){
       this.getProfile()
   }
}
</script>

<style>

</style>