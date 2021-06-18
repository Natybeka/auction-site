<template>
  <FormWizard
    ref="formwizard"
    @onComplete="onComplete"
    @onNextStep="nextStep"
    @onPreviousStep="previousStep"
    @onReset="reset"
    class="mt-3"
  >
    <tab-content title="Product Information" :selected="true">
      <div class="form-group">
        <label for="fullName">Full Name</label>
        <input
          type="text"
          class="form-control"
          :class="hasError('fullName') ? 'is-invalid' : ''"
          placeholder="Enter your name"
          v-model="formData.fullName"
        />
        <div v-if="hasError('fullName')" class="invalid-feedback">
          <div class="error" v-if="!$v.formData.fullName.required">
            Please provide a valid name.
          </div>
        </div>
      </div>
      <br />

    

      <br />

      <div class="form-group">
        <label for="referral">Category </label>
        <select
          :class="hasError('referral') ? 'is-invalid' : ''"
          class="form-control"
          v-model="formData.referral"
        >
          <option>Accessories</option>
          <option>Car Spare Parts</option>
          <option>Electronics</option>
          <option>Clothes</option>
          <option>Building Materials</option>
          <option>Others</option>
        </select>
        <div v-if="hasError('referral')" class="invalid-feedback">
          <div class="error" v-if="!$v.formData.referral.required">
            Please select on of the fields.
          </div>
        </div>
      </div>
    </tab-content>
    <tab-content title="Auction Information">
      <div class="form-group">
        <label for="ExpiryDate">Expiry Date</label>
        <input
          type="date"
          class="form-control"
          :class="hasError('companyName') ? 'is-invalid' : ''"
          placeholder="Enter the expiry date"
          v-model="formData.companyName"
        />

        <div v-if="hasError('companyName')" class="invalid-feedback">
          <div class="error" v-if="!$v.formData.companyName.required">
            Please provide a valid company name.
          </div>
        </div>
      </div>
      <br />
      <div class="form-group">
        <label for="StartingPrice">Starting Price</label>
        <input
          type="Number"
          class="form-control"
          :class="hasError('StartingPrice') ? 'is-invalid' : ''"
          placeholder="Enter the starting price"
          v-model="formData.StartingPrice"
        />
        <div v-if="hasError('StartingPrice')" class="invalid-feedback">
          <div class="error" v-if="!$v.formData.numberOfEmployees.required">
            Please provide number of employees in your company.
          </div>
          <div class="error" v-if="!$v.formData.numberOfEmployees.numeric">
            Should be a valid value.
          </div>
        </div>
      </div>
    </tab-content>
  </FormWizard>
</template>

<script>
import FormWizard from "../components/FormWizard.vue";
import TabContent from "../components/TabContent.vue";
import ValidationHelper from "../components/ValidationHelper.vue";
import { required } from "vuelidate/lib/validators";

import { numeric } from "vuelidate/lib/validators";
const checked = (value) => value === true;

import axios from "axios";
export default {
  name: "SimpleStepper",
  components: {
    FormWizard,
    TabContent,
  },
  mixins: [ValidationHelper],
  data() {
    return {
      formData: {
        fullName: "",
        selectedFile: null,
        fielUpload: "",
        date: "",
        ExpiryDate: null,
        StartingPrice: null,
        referral: null,
        terms: false,
      },
      validationRules: [
        { fullName: { required } },
        { ExpiryDate: { required }, StartingPrice: { required, numeric } },
        { referral: { required }, terms: { checked } },
      ],
    };
  },
  methods: {
    onComplete() {
      alert("Submitting Form ! Rock On");
      console.log("Submitting form");

      this.$refs.formwizard.changeStatus();
    },

    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },

    onUpload() {
      const fd = new FormData();
      fd.append("image", this.selectedFile, this.selectedFile.name);
      axios.post("", fd);
    },

    reset() {
      for (let field in this.formData) {
        this.formData[field] = null;
      }
    },

    nextStep() {
      //alert("On Next Step");
    },

    previousStep() {
      //alert("On Previous Step");
    },
  },
};
</script>




