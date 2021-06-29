/**
 * A module to store the changes in auctions this store
 * should keep track of all the auctions in a list, update
 * the latest bid information as well as handle delete operations
 * on the auctions.
*/
const state = {
  auctions : [],
  auction : {}
};


const getters = {
  auctions  : (state) => state.auctions,
  auction : (state) => state.auction
};


const actions = {

  /**
   * @param {Object} commit
   * action that feches all the auctions 
   */
  async getAllAuctions({ commit }) {
    console.log("..........Getting all auctions.................");
    const response = await fetch("http://localhost:5000/auction/auction");
    const data = await response.json();
    console.log("...........data fetched successfully...............");
    commit("setAuctions", data);
  },


  /**
   * Documentation
   * @param {Object} commit Default Param
   * @param {String} auctionId 
   * Fetches the the active auction based on id
   */
  async getActiveAuction({ commit }, auctionId) {
    console.log("----------------Getting auction----------------------");
    const response = await fetch(`http://localhost:5000/auction/auction/${auctionId}`);
    const data = await response.json();
    console.log("-----------------data fetched succesfully------------------");
    commit("setAuction", data);
  },


  /**
   * @param {Object} auction
   * updates the auctions list to the current state
   * 1. PUT request to the auction table
   * 2. POST request to the bid table for adding the new bid
   * 3. use the passed commit object to reflect the changes
   */
  async updateAuctions({ commit }, auction) {
    console.log("---------------updateAuctions action called--------------------");
    const updateRes = await fetch(
      `http://localhost:5000/auction/auction/${auction.id}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          latestBid: auction.currentHighest,
          latestBidder: auction.highestBidder,
        }),
      }
    );
    const postResponse = await fetch(`http://localhost:5000/bids/bids`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        AuctionId: auction.id,
        UserId: auction.highestBidder,
        Amount: auction.currentHighest,
      }),
    });

    commit("updateAuctions", auction);
  },
};


/**
 * @description Logs changes of state
 */
const mutations = {


  /**
   * @param {Object} state State
   * @param {Array} auctions List of auctions
   * @description Sets the auctions state
   */
  setAuctions: (state, auctions) => (state.auctions = auctions),


  /**
   * Function that updates the state of the auctions
   * @param {Object} state State
   * @param {Array} auction Updated auction
   * 
   */
  updateAuctions: function(state, auction) {
    state.auctions = state.auctions.map((auc) => {
      if (auc.id == auction.id) return auction;
    });
  },
  setAuction: (state, auction) => (state.auction = auction),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
