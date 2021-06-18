<template>
    <div id="app">
        <Navigation activeLink="Reviews"/>
        <router-view></router-view>
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
        <Footer />
    </div>
</template>

<script>
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue' 

export default {

    props: {
        id: {
            type: [Number, String],
            required: true,
        }
    },

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
   name : 'EditReview',
   components : {
       Navigation,
       Footer
   },
   methods : {
       editReview(){
           if(!this.description || !this.rating){
                    this.warning = "Please fill all the fields"
           }else{
                fetch(`http://localhost:5000/reviews/review/${this.id}`,{
                    method : "PUT",
                    headers : {
                        "Content-Type" : "application/json"
                    },
                    body: JSON.stringify({
                        Description:this.description,
                        Rating:this.rating,
                    })
                }).then(resp => resp.json())
                .then(() => {
                    this.$router.push({
                        name:'Reviews'
                    })
                })
                .catch(error => {  
                    console.log(error)
                })
           }
       }
   },
   beforeRouteEnter(to, from, next){
       if(to.params.id != undefined){
           fetch(`http://localhost:5000/reviews/review/${to.params.id}`,{
               method : "GET",
               headers : {
                   "Content-Type" : "application/json"
               }
           }).then(resp => resp.json())
           .then(data => {
               return next(vm => (vm.description=data.Description, vm.rating=data.Rating))
           })
           .catch(error => {
               console.log(error)
           })
       }else{
           return next()
       }

   }
}
</script>
