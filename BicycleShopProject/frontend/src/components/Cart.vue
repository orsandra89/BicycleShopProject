<template>
  <div class="cart">
    <h1>Twój koszyk</h1>
    <div class="cart-item" v-for="(item, index) in cart" :key="item.id">
      <b-img fluid :src="require('@/assets/images/BikesShop/bike-placeholder.png')" alt="default image" width="100"
        height="100" />
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
      <div v-if="itemAdded" class="notification">
        Dodano do koszyka!
      </div>
    </div>
    <h2>Całkowita kwota: {{ totalAmount }} zł</h2>
    <button @click="completeOrder">Zrealizuj zamówienie</button>
    <!---<button @click="clearOrderHistory">Clear Order History</button> -->
  </div>
</template>

<script>
export default {
  name: 'Cart',
  data() {
    return {
      cart: [],
      itemAdded: false
    };
  },
  created() {
    const storedCart = localStorage.getItem('cart');
    if (storedCart) {
      this.cart = JSON.parse(storedCart).map(item => ({
        ...item,
        price: Number(item.price),
        quantity: item.quantity ? Number(item.quantity) : 1
      }));
    }
  },
  computed: {
    totalAmount() {
      return this.cart.reduce((total, item) => total + item.price * item.quantity, 0);
    }
  },
  methods: {
    completeOrder() {
      const orders = JSON.parse(localStorage.getItem('orders')) || [];
      const date = new Date().toLocaleString();
      this.cart.forEach(item => {
        orders.push({
          ...item,
          date,
          image: require(`@/assets/images/BikesShop/bike-placeholder.png`)
        });
      });
      localStorage.setItem('orders', JSON.stringify(orders));
      this.cart = [];
      localStorage.setItem('cart', JSON.stringify(this.cart));


      this.orderCompleted = true;
      setTimeout(() => {
        this.orderCompleted = false;
      }, 4000);
    },
    removeFromCart(index) {
      this.cart.splice(index, 1);
      localStorage.setItem('cart', JSON.stringify(this.cart));
    },
    increaseQuantity(index) {
      this.cart[index].quantity++;
      localStorage.setItem('cart', JSON.stringify(this.cart));
    },
    decreaseQuantity(index) {
      if (this.cart[index].quantity > 1) {
        this.cart[index].quantity--;
        localStorage.setItem('cart', JSON.stringify(this.cart));
      }
    },
    checkout() {
      this.$emit('checkout', this.cart);
      this.cart = [];
      localStorage.removeItem('cart');
    },
    clearOrderHistory() {
      localStorage.removeItem('orders');
      this.cart = [];
      localStorage.setItem('cart', JSON.stringify(this.cart));
    },


  }
};
</script>
<style scoped>
.cart {
  width: 80%;
  margin: 0 auto;
  font-family: Arial, sans-serif;
  background-color: #f8f8f8;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding: 20px 0;
}

.quantity-control {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 50px;
}

.quantity-control button {
  background-color: #f0f0f0;
  border: none;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin: 5px 0;
}

.quantity-control button:hover {
  background-color: #ddd;
}

.cart-item-image {
  width: 10%;
  height: 10%;
  object-fit: cover;
}

.notification {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 20px;
  background-color: #4caf50;
  color: white;
  border-radius: 5px;
  z-index: 1000;
}
</style>