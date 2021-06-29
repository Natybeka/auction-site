<template>
  <div>
    <div class="flash-container mt-2" style="margin-left:250px;">
      <FlashMessage :position="'top'"></FlashMessage>
    </div>
    <div class="container main-container row " style="margin-top:110px">
      <section class="item col-lg-6 d-flex flex-column align-items-center">
        <h2>Item Information</h2>
        <div class="row">
          <div class="form-group">
            <label for="fullName">Item Name</label>
            <input
              type="text"
              class="form-control"
              placeholder="Enter The Item Name"
              v-model="formData.itemName"
            />
          </div>

          <div class="form-group">
            <label for="fullName">Category</label>
            <select class="form-control" v-model="formData.category" required>
              <option value="" selected disabled
                >Please select a category</option
              >
              <option value="Accessories">Accessories</option>
              <option value="Car Spare Parts">Car Spare Parts</option>
              <option value="Electronics">Electronics</option>
              <option value="Clothes">Clothes</option>
              <option value="Building Materials">Building Materials</option>
              <option value="Others">Others</option>
            </select>
          </div>

          <div class="form-group d-flex flex-column">
            <label for="description">Description</label>
            <textarea
              name="description"
              class="form-control"
              id="des"
              cols="30"
              rows="8"
              v-model="formData.description"
            >
Add a description</textarea
            >
          </div>
        </div>
      </section>

      <section class="auction col-lg-6 d-flex flex-column align-items-center">
        <h2>Auction Information</h2>
        <div class="row">
          <div class="form-group">
            <label for="ExpiryDate">Expiry Date</label>
            <input
              type="date"
              class="form-control"
              placeholder="Enter the expiry date"
              v-model="formData.expiryDate"
            />
          </div>
          <div class="form-group">
            <label for="StartingPrice">Starting Price</label>
            <input
              type="Number"
              class="form-control"
              placeholder="Enter the starting price"
              v-model="formData.startingPrice"
            />
          </div>
        </div>
        <div class="button-container mt-5 w-100">
          <button class="btn btn-primary w-75" v-on:click="addItem">
            + Add Item
          </button>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddItemForm",
  data() {
    // Save the form data here
    return {
      formData: {
        itemName: "",
        category: "",
        description: "",
        expiryDate: null,
        startingPrice: null,
      },
    };
  },
  methods: {
    /**
     * Add item to auction
     */
    async addItem() {
      let isValid = this.validateInputs();
      if (isValid) {
        let path = "http://localhost:5000";
        /**
         * fields required for adding new item
         */
        let itemId = this.uuidv4();
        let userId = sessionStorage.getItem("userId");
        const postItemResponse = await fetch(`${path}/items/items`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ItemId: itemId,
            ItemName: this.formData.itemName,
            Description: this.formData.description,
            Category: this.formData.category,
            Image: "image",
            SellerId: userId,
          }),
        });
        console.log(postItemResponse);

        /**
         * fields required for adding auction
         */
        let auctionId = this.uuidv4();
        const postAuctionResponse = await fetch(`${path}/auction/auction`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            AuctionId: auctionId,
            ItemId: itemId,
            StartDate: new Date(Date.now()),
            EndDate: this.formData.expiryDate,
            InitialPrice: this.formData.startingPrice,
            CurrentPrice: this.formData.startingPrice,
            IsCompleted: false,
            HighestBidder: userId,
          }),
        });
        console.log(postAuctionResponse);
      } else {
        this.flashMessage.error({
          title: "Form error!",
          message: "Please enter all the fields",
        });
      }
    },
    validateInputs() {
      if (
        this.formData.itemName == "" ||
        this.formData.category == "" ||
        this.formData.description == "" ||
        this.formData.expiryDate == null ||
        this.formData.startingPrice == null
      ) {
        return false;
      }
      return true;
    },
    // Random id generator for items and auctions
    uuidv4() {
      return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(
        c
      ) {
        var r = (Math.random() * 16) | 0,
          v = c == "x" ? r : (r & 0x3) | 0x8;
        return v.toString(16);
      });
    },
  },
};
</script>

<style scoped>
div.main-container,
button {
  position: absolute;
  left: 50%;
  transform: translate(-50%);
}
div.button-container {
  position: relative;
}
select option:disabled {
  color: grey;
}
</style>
