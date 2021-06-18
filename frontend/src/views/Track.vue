<template>
    <div id="app">
        <Navigation activeLink="track"/>
        <router-view></router-view>

        <!-- Track user bids here -->
        <div class="container" style="margin:40px auto">
            <table class="table text-center">
                <thead>
                    <th>Item Name</th>
                    <th>Item Description</th>
                    <th>My Bid</th>
                    <th>Highest Bid</th>
                    <th>Expiration Date</th>
                    <th></th>
                </thead>
                <tbody>
                    <tr v-for="detail in bidDetails" :key="detail.id">
                        <td>{{detail.item_name}}</td>
                        <td>{{detail.item_description}}</td>
                        <td>{{detail.amount}}</td>
                        <td>{{detail.current_price}}</td>
                        <td>{{detail.expiration_date}}</td>
                        <td><router-link :to="{name: 'Details', params:{id:detail.auction_id}}">Go To Details</router-link></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <Footer />
    </div>
</template>

<script>
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue' 

export default {
   name : 'Track',
   components : {
       Navigation,
       Footer
   },
   data(){
       return {
        bidDetails : Array
       }
   } ,
    created() {
        let userId = sessionStorage.getItem('userId');
        fetch(`http://localhost:5000/bids/bid/${userId}`)
        .then(res => res.json())
        .then(data => this.bidDetails = data);
        // var data = await userBids.json();
        // console.log(data);
        // this.bidDetails = data;
        // console.log(this.bidDetails);

    }
}
</script>
