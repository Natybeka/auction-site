<template>
    <div id="app">
        <Navigation activeLink="Reviews"/>
        <router-view></router-view>
        <div class="container">
            <div class="main-body">
                <!-- /Breadcrumb -->

                <div class="row gutters-sm">
                    <div class="col-sm-12 mb-3">
                        <div class="card h-100">
                            <div class="card-body">
                                <h6 class="d-flex align-items-center mb-3"><i class="material-icons text-info mr-2">Reviews given by you</i></h6>
                                <!-- @if (Model.UserReviews.Count() == 0)
                                { -->
                                    <div v-if = "reviewsByCurrentUser() === []" class="card mt-1"> You didn't give any reviews</div>
                                <!-- }
                                else
                                {
                                    foreach (var review in Model.UserReviews)
                                    { -->
                                        <div v-else v-for="review in reviewsByCurrentUser()" :key="review.ReviewId" class="card mt-1">
                                            <div class="card-header">
                                                <h6 style="color: rgba(63, 155, 209, 0.6);">user {{review.ReviewerId}} <em>reviewed {{review.SellerId}} on {{review.Date}}</em></h6>
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
                                            <form>
                                                <div class="row">
                                                    <div class="col-sm-12">
                                                        <router-link class="btn btn-info text-white ml-2 mb-2" name="button" id="review-button" aria-current="page" :to="{name: 'EditReview', params:{id:review.ReviewId}}">Edit Review <i class="far fa-edit"></i></router-link>
                                                        <!-- <button class="btn btn-info text-white" id="review-popup" name="button" v-bind="value={review}" @click="getSingleReview(this)">Edit Review <i class="far fa-edit"></i></button> -->
                                                    </div>
                                                </div>
                                            </form>
                                        </div>
                                    <!-- }
                                } -->
                            </div>
                        </div>
                    </div>
                    <div class="container">
                        <div class="review-popup">
                            <div class="review-popup-content">
                                <div class="close"><h3 style="position: absolute;top:-2%; left: 50%;transform: translate(-50%);">X</h3></div>
                                <div class="row">
                                    <div class="col-sm-12">
                                        {{warning}}
                                        <form @submit.prevent="editReview" enctype="multipart/form-data">
                                            <div class="form-group">
                                                <input class="form-control" v-model="id" hidden />
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control" v-model="sellerid" hidden/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control" v-model="reviewerid" hidden/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <label>Description</label>
                                                <input class="form-control" v-model="description"/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <label>Rating</label>
                                                <input class="form-control" v-model="rating"/>
                                                <span class="text-danger"></span>
                                            </div>
                                            <div class="form-group">
                                                <input class="form-control" v-model="reviewdate" hidden/>
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
            reviews : [],
            id:null,
            sellerid:null,
            reviewerid:null,
            description:null,
            rating:null,
            reviewdate:null,
            warning:null
        }
    },
   name : 'Review',
   components : {
       Navigation,
       Footer
   },
   methods : {
       getReviews(){
           fetch('http://localhost:5000/reviews/reviews',{
               method : "GET",
               headers : {
                   "Content-Type" : "application/json"
               }
           }).then(resp => resp.json())
           .then(data => {
               this.reviews.push(...data)
           })
           .catch(error => {
               console.log(error)
           })
       },
       getSingleReview(objbutton){
           var ReviewerId = objbutton.value.id
           Session["current_review"] = ReviewerId
           fetch(`http://localhost:5000/reviews/${ReviewerId}`,{
               method : "GET",
               headers : {
                   "Content-Type" : "application/json"
               }
           }).then(resp => resp.json())
           .then(data => {
               this.ReviewId = data.id
               this.sellerid = data.SellerId
               this.reviewerid = data.ReviewerId
               this.Description = data.description
               this.Rating = data.rating
               this.Date = data.review_date
           })
           .catch(error => {
               console.log(error)
           })
       },
       editReview(){
           console.log("Review Edit Entered")
           if(!this.description || !this.rating){
                    this.warning = "Please fill all the fields"
           }else{
            fetch(`http://localhost:5000/reviews/${Session["current_review"]}/`,{
               method : "PUT",
               headers : {
                   "Content-Type" : "application/json"
               },
               body: JSON.stringify({
                   SellerId:this.sellerid,
                   ReviewerId:this.reviewerid,
                   description:this.Description,
                   rating:this.rating,
                   review_date:this.reviewdate
               })
            }).then(resp => resp.json())
            .then(() => {
                document.querySelector(".review-popup").style.display = "none";
                location.reload()
            })
            .catch(error => {  
                console.log(error)
            })
           }
       },
       reviewsByCurrentUser() {
           let userId = sessionStorage.getItem('userId');
            return this.reviews.filter(review => review.ReviewerId == userId);
      }
   },
   mounted(){
        
    },
   created(){
       this.getReviews()
   }
}
</script>
