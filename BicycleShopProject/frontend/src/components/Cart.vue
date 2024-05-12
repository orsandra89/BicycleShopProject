<template>
    <div class="cart">
      <h1>Twój koszyk</h1>
      <div class="cart-item" v-for="(item, index) in cart" :key="item.id">
        <img :src="`assets/BikesShop/${item.image}`" alt="bike image" />
        <h2>{{ item.brand }}</h2>
        <p>{{ item.color }}</p>
        <p>{{ item.purpose }}</p>
        <p>{{ item.price }} zł</p>
        <button @click="removeFromCart(index)">Usuń</button>
      </div>
      <button @click="checkout">Zrealizuj zamówienie</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Cart',
    data() {
      return {
        cart: [] // Tutaj powinny być dane z koszyka
      };
    },
    methods: {
      removeFromCart(index) {
        this.cart.splice(index, 1);
      },
      checkout() {
        this.$emit('checkout', this.cart);
      this.cart = []; // Czyść koszyk po zrealizowaniu zamówienia
      }
    }
  };
  </script>
  
  <style scoped>
  /* Twoje style */
  </style>