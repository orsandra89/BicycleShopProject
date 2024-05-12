<template>
  <div class="cart">
    <h1>Twój koszyk</h1>
    <div class="cart-item" v-for="(item, index) in cart" :key="item.id">
      <img :src="`assets/BikesShop/${item.image}`" alt="bike image" />
      <h2>{{ item.brand }}</h2>
      <p>{{ item.color }}</p>
      <p>{{ item.purpose }}</p>
      <p>{{ item.price }} zł</p>
      <div class="quantity-control">
        <button @click="decreaseQuantity(index)">-</button>
        <p>{{ item.quantity }}</p>
        <button @click="increaseQuantity(index)">+</button>
      </div>
      <button @click="removeFromCart(index)">Usuń</button>
    </div>
    <h2>Całkowita kwota: {{ totalAmount }} zł</h2>
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
  computed: {
    totalAmount() {
      return this.cart.reduce((total, item) => total + item.price * item.quantity, 0);
    }
  },
  methods: {
    removeFromCart(index) {
      this.cart.splice(index, 1);
    },
    increaseQuantity(index) {
      this.cart[index].quantity++;
    },
    decreaseQuantity(index) {
      if (this.cart[index].quantity > 1) {
        this.cart[index].quantity--;
      }
    },
    checkout() {
      this.$emit('checkout', this.cart);
      this.cart = []; 
    }
  }
};
</script>

<style scoped>
.cart {
  width: 80%;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.quantity-control {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 50px;
}

.quantity-control button {
  background-color: #f0f0f0;
  border: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.quantity-control button:hover {
  background-color: #ddd;
}
</style>