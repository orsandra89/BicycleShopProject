<template>
    <div class="shop">
      <div class="product-grid">
        <div class="product-card" v-for="bike in bikes" :key="bike.id">
          <img :src="`assets/BikesShop/${bike.image}`" alt="bike image" />
          <h2>{{ bike.brand }}</h2>
          <p>{{ bike.color }}</p>
          <p>{{ bike.purpose }}</p>
          <p>{{ bike.price }} zł</p>
          <button @click="addToCart(bike)">Dodaj do koszyka</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'sklep',
    data() {
      return {
        bikes: [
        {
          id: 1,
          image: 'BicycleShopProject\frontend\src\assets\images\BikesShop\Bike1.jpg',
          brand: 'Brand1',
          color: 'Red',
          purpose: 'Mountain',
          price: 1000
        },
        {
          id: 2,
          image: 'BicycleShopProject\frontend\src\assets\images\BikesShop\Bike2.jpg',
          brand: 'Brand2',
          color: 'Blue',
          purpose: 'Road',
          price: 2000
        },
        {
          id: 3,
          image: 'BicycleShopProject\frontend\src\assets\images\BikesShop\Bike3.jpg',
          brand: 'Brand1',
          color: 'Red',
          purpose: 'Mountain',
          price: 1000
        },
        {
          id: 4,
          image: 'BicycleShopProject\frontend\src\assets\images\BikesShop\Bike4.jpg',
          brand: 'Brand2',
          color: 'Blue',
          purpose: 'Road',
          price: 2000
        },        {
          id: 5,
          image: 'BicycleShopProject\frontend\src\assets\images\BikesShop\Bike5.jpg',
          brand: 'Brand1',
          color: 'Red',
          purpose: 'Mountain',
          price: 1000
        },
        {
          id: 6,
          image: 'BicycleShopProject\frontend\src\assets\images\BikesShop\Bike6.jpg',
          brand: 'Brand2',
          color: 'Blue',
          purpose: 'Road',
          price: 2000
        },

        ]
      };
    },
    methods: {
      addToCart(bike) {
        
      }
    }
  };
  </script>
  
  <style scoped>
  /* Tutaj dodaj style */
  </style>