<template>
  <div class="shop">
    <div class="filters">
      <select v-model="sort" @change="updateSort">
        <option value="">Sortuj wg ceny</option>
        <option value="asc">Rosnąco</option>
        <option value="desc">Malejąco</option>
      </select>
      <select v-model="filter.brand" @change="updateFilters">
        <option value="">Wszystkie marki</option>
        <option value="Romet">Romet</option>
        <option value="Bianchi">Bianchi</option>
        <option value="Unibike">Unibike</option>
        <option value="Folta">Folta</option>
        <option value="Overfly">Overfly</option>
        <option value="Ridley">Ridley</option>
        <option value="Ortega">Ortega</option>
        <option value="Trek">Trek</option>
        <option value="Cube">Cube</option>
        <option value="Fury">Fury</option>
      </select>
      <select v-model="filter.color" @change="updateFilters">
        <option value="">Wszystkie kolory</option>
        <option value="Czarny">Czarny</option>
        <option value="Biały">Biały</option>
        <option value="Niebieski">Niebieski</option>
        <option value="Beżowy">Beżowy</option>
        <option value="Szary">Szary</option>
        <option value="Zielony">Zielony</option>
      </select>
      <select v-model="filter.purpose" @change="updateFilters">
        <option value="">Wszystkie przeznaczenia</option>
        <option value="Górski">Górski</option>
        <option value="Kolarski">Kolarski</option>
        <option value="Miejski">Miejski</option>
      </select>
    </div>
    <div class="product-grid">
      <div class="product-card" v-for="bike in filteredBikes" :key="bike.id">
        <img :src="require(`@/assets/images/BikesShop/${bike.image}`)" alt="bike image" />
        <h2>{{ bike.brand }}</h2>
        <p>{{ bike.color }}</p>
        <p>{{ bike.purpose }}</p>
        <p>{{ bike.price }} zł</p>
        <button v-if="isLoggedIn" @click="addToCart(bike)">Dodaj do koszyka</button>
        <p v-else>Aby dodać do koszyka, musisz się najpierw zalogować.</p>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  name: 'sklep',
  isLoggedIn: false,
  created() { 
    console.log('Shop component loaded');
  },
  data() {
    return {
      sort: '',
      filter: {
        brand: '',
        color: '',
        purpose: ''
      },
        bikes: [
        {
          id: 1,
          image: 'Bike1.jpg',
          brand: 'Romet',
          color: 'Czarny',
          purpose: 'Górski',
          price: 2899
        },
        {
          id: 2,
          image: 'Bike2.jpg',
          brand: 'Bianchi',
          color: 'Niebieski',
          purpose: 'Kolarski',
          price: 7999
        },
        {
          id: 3,
          image: 'Bike3.jpg',
          brand: 'Romet',
          color: 'Biały',
          purpose: 'Górski',
          price: 2399
        },
        {
          id: 4,
          image: 'Bike4.jpg',
          brand: 'Unibike',
          color: 'Czarny',
          purpose: 'Miejski',
          price: 1999
        },        {
          id: 5,
          image: 'Bike5.jpg',
          brand: 'Folta',
          color: 'Czarny',
          purpose: 'Górski',
          price: 4999
        },
        {
          id: 6,
          image: 'Bike6.jpg',
          brand: 'Overfly',
          color: 'Beżowy',
          purpose: 'Miejski',
          price: 3599
        },
        {
          id: 7,
          image: 'Bike7.jpg',
          brand: 'Ridley',
          color: 'Czarny',
          purpose: 'Górski',
          price: 5999
        },
        {
          id: 8,
          image: 'Bike8.jpg',
          brand: 'Trek',
          color: 'Niebieski',
          purpose: 'Górski',
          price: 6999
        },
        {
          id: 9,
          image: 'Bike9.jpg',
          brand: 'Ortega',
          color: 'Biały',
          purpose: 'Górski',
          price: 3999
        },
        {
          id: 10,
          image: 'Bike10.jpg',
          brand: 'Cube',
          color: 'Szary',
          purpose: 'Górski',
          price: 4999
        },
        {
          id: 11,
          image: 'Bike.jpg',
          brand: 'Fury',
          color: 'Zielony',
          purpose: 'Górski',
          price: 9999
        },
        ]
      };
    },
    computed: {
    filteredBikes() {
      let bikes = this.bikes;
      if (this.sort === 'asc') {
        bikes = bikes.sort((a, b) => a.price - b.price);
      } else if (this.sort === 'desc') {
        bikes = bikes.sort((a, b) => b.price - a.price);
      }
      if (this.filter.brand) {
        bikes = bikes.filter(bike => bike.brand === this.filter.brand);
      }
      if (this.filter.color) {
        bikes = bikes.filter(bike => bike.color === this.filter.color);
      }
      if (this.filter.purpose) {
        bikes = bikes.filter(bike => bike.purpose === this.filter.purpose);
      }
      return bikes;
    }
  },
  methods: {
    addToCart(bike) {
      this.cart.push(bike);
      console.log(this.cart);
    },
  }
};
</script>

<style scoped>
.filters {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.filters select {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  font-size: 16px;
}
.product-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 20px;
}

.product-card {
  flex: 0 0 calc(33.33% - 20px);
  background-color: #fff;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-card img {
  width: 100%;
  height: auto;
}

.product-card h2, .product-card p {
  margin: 0 0 10px;
}

.product-card button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007BFF;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.product-card button:hover {
  background-color: #0056b3;
}
</style>