const state = {
    auctions: [],
};

const getters = {
    allAuctions : state => state.auctions,
    activeAuction : (state) => (id) => {
        return state.auctions.find(auc => auc.id == id);
    }
};

const actions = {
    // Get all auctions
    async getAllAuctions({commit}) {
        console.log("Getting all auctions");
        const response = await fetch("http://localhost:5000/auction/auction");
        const data = await response.json();
        
        console.log(data);
        commit('setAuctions', data);
    },
    async getActiveAuction({commit}) {
        const response = await fetch("http://localhost:5000/")
    },
    async updateAuctions({commit}, auction) {
        // get the auction to be updated
        console.log("code here")
        const updateRes = await fetch(`http://localhost:5000/auction/auction/${auction.id}`, {
            method : 'PUT',
            headers : {
                'Content-Type' : "application/json"
            },
            body : JSON.stringify({
                'latestBid' : auction.currentHighest,
                'latestBidder' : auction.highestBidder,
            })
        });
        const postResponse = await fetch(`http://localhost:5000/bids/bids`, {
            method : 'POST',
            headers : {
                'Content-Type' : "application/json"
            },
            body : JSON.stringify({
                'AuctionId' : auction.id,
                'UserId' : auction.highestBidder,
                'Amount' : auction.currentHighest
            })
        });
        
        commit('updateAuctions', auction);

    },
    async getAuction({commit}, id) {
        const response = await fetch(`http://locahost:5000/auction/${id}`);
        const data = await response.json();
        commit('setAuction', data);
    }
};


//changes to state for item will logged here
const mutations = {
    // Set the auction to the request response
    setAuctions : (state, auctions) => (state.auctions = auctions),
    updateAuctions : function(state, auction) {
        state.auctions = state.auctions.map(auc => {
            if (auc.id == auction.id)
                return auction
        })
    },
    setAuction : (state, auction) => (state.auction = auction)
};

export default {
    state,
    getters,
    actions,
    mutations
};