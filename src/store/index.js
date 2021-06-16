import Vuex from 'vuex'
import Vue from 'vue'
import auctions from './modules/auctions'

Vue.use(Vuex)

export default new Vuex.Store({
    modules : {
        auctions
    }
})