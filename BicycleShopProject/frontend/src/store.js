import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: []
  },
  mutations: {
    addToCart(state, bike) {
      state.cart.push(bike);
    }
  }
});