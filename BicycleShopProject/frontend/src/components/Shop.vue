<template>
  <b-container class="shop">
    <div class="d-flex justify-content-between mb-3">
      <b-form-select v-model="sort" class="p-2 rounded border shadow-sm">
        <option value="">Sortuj wg ceny</option>
        <option value="asc">Rosnąco</option>
        <option value="desc">Malejąco</option>
      </b-form-select>
      <b-form-select v-model="filter.brand" class="p-2 rounded border shadow-sm">
        <option value="">Wszystkie marki</option>
        <option v-for="brand in brands" :key="brand" :value="brand">{{ brand }}</option>
      </b-form-select>
      <b-form-select v-model="filter.category" class="p-2 rounded border shadow-sm">
        <option value="">Wszystkie przeznaczenia</option>
        <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
      </b-form-select>
    </div>
    <b-row class="mt-3">
      <b-col lg="3" md="6" sm="12" class="mb-3 bg-white rounded shadow-sm" v-for="bike in filteredBikes" :key="bike.id">
        <b-img fluid :src="require('@/assets/images/BikesShop/bike-placeholder.png')" alt="default image" />
        <h2>{{ bike.brand }}</h2>
        <p>{{ bike.color }}</p>
        <p>{{ bike.category }}</p>
        <p>{{ bike.price }} zł</p>
        <b-button v-if="!isLoggedIn" @click="addToCart(bike)" variant="primary">Dodaj do koszyka</b-button>
        <p v-else>Aby dodać do koszyka, musisz się najpierw zalogować.</p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'sklep',
  data() {
    return {
      cart: [],
      sort: '',
      filter: {
        brand: '',
        color: '',
        category: ''
      },
      bikes: [],
      brands: [],
      categories: [],
      isLoggedIn: false,
    };
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:8000/bicycles/');
      this.bikes = response.data.bicycles;
      console.log(this.bikes);

      this.brands = this.bikes
        .map(bike => bike.brand)
        .filter((brand, index, self) => self.indexOf(brand) === index);

      this.categories = this.bikes
        .map(bike => bike.category)
        .filter((category, index, self) => self.indexOf(category) === index);
    } catch (error) {
      console.error(error);
    }
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
      if (this.filter.category) {
        bikes = bikes.filter(bike => bike.category === this.filter.category);
      }
      return bikes;
    }
  },
  methods: {
    addToCart(bike) {
      this.cart.push(bike);
      localStorage.setItem('cart', JSON.stringify(this.cart));
    },
    logIn() {
      this.isLoggedIn = true;
    },
    logOut() {
      this.isLoggedIn = false;
    },
  },
};
</script>

<style scoped></style>