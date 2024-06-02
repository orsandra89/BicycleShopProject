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
        <b-button v-if="isLoggedIn" @click="addToCart(bike)" variant="primary">Dodaj do koszyka</b-button>
        <p v-else>Aby dodać do koszyka, musisz się najpierw zalogować.</p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'shop',
  data() {
    return {
      cart: [],
      sort: '',
      filter: {
        brand: '',
        category: '',
        color: ''
      },
      bikes: [
        {
          id: 1,
          image: 'Bike1.jpg',
          brand: 'Romet',
          color: 'Czarny',
          category: 'Górski',
          price: 2899
        },
        {
          id: 2,
          image: 'Bike2.jpg',
          brand: 'Bianchi',
          color: 'Niebieski',
          category: 'Kolarski',
          price: 7999
        },
        {
          id: 3,
          image: 'Bike3.jpg',
          brand: 'Romet',
          color: 'Biały',
          category: 'Górski',
          price: 2399
        },
        {
          id: 4,
          image: 'Bike4.jpg',
          brand: 'Unibike',
          color: 'Czarny',
          category: 'Miejski',
          price: 1999
        },
        {
          id: 5,
          image: 'Bike5.jpg',
          brand: 'Folta',
          color: 'Czarny',
          category: 'Górski',
          price: 4999
        },
        {
          id: 6,
          image: 'Bike6.jpg',
          brand: 'Overfly',
          color: 'Beżowy',
          category: 'Miejski',
          price: 3599
        },
        {
          id: 7,
          image: 'Bike7.jpg',
          brand: 'Ridley',
          color: 'Czarny',
          category: 'Górski',
          price: 5999
        },
        {
          id: 8,
          image: 'Bike8.jpg',
          brand: 'Trek',
          color: 'Niebieski',
          category: 'Górski',
          price: 6999
        },
        {
          id: 9,
          image: 'Bike9.jpg',
          brand: 'Ortega',
          color: 'Biały',
          category: 'Górski',
          price: 3999
        },
        {
          id: 10,
          image: 'Bike10.jpg',
          brand: 'Cube',
          color: 'Szary',
          category: 'Górski',
          price: 4999
        },
        {
          id: 11,
          image: 'r2.jpg',
          brand: 'Fury',
          color: 'Zielony',
          category: 'Górski',
          price: 9999
        },
        {
          id: 12,
          image: 'Bike11.jpg',
          brand: 'Storm',
          color: 'Czerwony',
          category: 'Górski',
          price: 2799
        },
        {
          id: 13,
          image: 'Bike12.jpg',
          brand: 'Storm',
          color: 'Szary',
          category: 'Górski',
          price: 2999
        },
        {
          id: 14,
          image: 'Bike13.jpg',
          brand: 'Trek',
          color: 'Niebieski',
          category: 'Górski',
          price: 4799
        },
        {
          id: 15,
          image: 'Bike14.jpg',
          brand: 'Ridley',
          color: 'Miedziany',
          category: 'Kolarski',
          price: 8999
        },
        {
          id: 16,
          image: 'Bike15.jpg',
          brand: 'Orbea',
          color: 'Czarny',
          category: 'Górski',
          price: 7999
        },
        {
          id: 17,
          image: 'Bike16.jpg',
          brand: 'Trek',
          color: 'Czarny',
          category: 'Górski',
          price: 3599
        },
        {
          id: 18,
          image: 'Bike17.jpg',
          brand: 'Kross',
          color: 'Szary',
          category: 'Górski',
          price: 3599
        },
        {
          id: 19,
          image: 'Bike18.jpg',
          brand: 'Romet',
          color: 'Czarny',
          category: 'Górski',
          price: 4999
        },
        {
          id: 20,
          image: 'Bike19.jpg',
          brand: 'Folta',
          color: 'Czarny',
          category: 'Miejski',
          price: 3999
        },
        {
          id: 21,
          image: 'Bike20.jpg',
          brand: 'Kross',
          color: 'Czarny',
          category: 'Górski',
          price: 10999
        },
        {
          id: 22,
          image: 'Bike12.jpg',
          brand: 'Giant',
          color: 'Czarny',
          category: 'Terenowy',
          price: 5999
        },
        {
          id: 23,
          image: 'Bike9.jpg',
          brand: 'Bike',
          color: 'Szary',
          category: 'Szosowy',
          price: 9999

        },
        {
          id: 24,
          image: 'Bike20.jpg',
          brand: 'Merida',
          color: 'Czerwony',
          category: 'Górski',
          price: 6799
        },
        {
          id: 25,
          image: 'Bike18.jpg',
          brand: 'Specialized',
          color: 'Biały',
          category: 'Kolarski',
          price: 11999
        },
        {
          id: 26,
          image: 'Bike15.jpg',
          brand: 'Cannondale',
          color: 'Zielony',
          category: 'Górski',
          price: 5599
        },
        {
          id: 27,
          image: 'Bike17.jpg',
          brand: 'Scott',
          color: 'Niebieski',
          category: 'Kolarski',
          price: 8999
        },
        {
          id: 28,
          image: 'Bike13.jpg',
          brand: 'Cube',
          color: 'Czarny',
          category: 'Górski',
          price: 7999
        },
        {
          id: 29,
          image: 'Bike12.jpg',
          brand: 'Bianchi',
          color: 'Turkusowy',
          category: 'Kolarski',
          price: 13999
        },
        {
          id: 30,
          image: 'Bike16.jpg',
          brand: 'Focus',
          color: 'Szary',
          category: 'Górski',
          price: 6299
        },
        {
          id: 31,
          image: 'Bike19.jpg',
          brand: 'Cannondale',
          color: 'Pomarańczowy',
          category: 'Terenowy',
          price: 4999
        },
        {
          id: 32,
          image: 'Bike14.jpg',
          brand: 'Giant',
          color: 'Czerwony',
          category: 'Szosowy',
          price: 10999
        },
        {
          id: 33,
          image: 'Bike18.jpg',
          brand: 'Canyon',
          color: 'Czarny',
          category: 'Kolarski',
          price: 15999
        },
        {
          id: 34,
          image: 'Bike17.jpg',
          brand: 'Stevens',
          color: 'Biały',
          category: 'Miejski',
          price: 4199
        },
        {
          id: 35,
          image: 'Bike13.jpg',
          brand: 'KTM',
          color: 'Zielony',
          category: 'Górski',
          price: 8799
        },
        {
          id: 36,
          image: "Bike13.jpg",
          brand: "Giant",
          color: "Czarny",
          category: "Górski",
          price: 7899
        },
        {
          id: 37,
          image: "Bike14.jpg",
          brand: "Trek",
          color: "Niebieski",
          category: "Górski",
          price: 6199
        },
        {
          id: 38,
          image: "Bike17.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9299
        },
        {
          id: 39,
          image: "Bike15.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Terenowy",
          price: 7999
        },
        {
          id: 40,
          image: "Bike16.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Górski",
          price: 6499
        },
        {
          id: 41,
          image: "Bike20.jpg",
          brand: "Cube",
          color: "Szary",
          category: "Kolarski",
          price: 7499
        },
        {
          id: 42,
          image: "Bike19.jpg",
          brand: "Merida",
          color: "Czarny",
          category: "Górski",
          price: 8299
        },
        {
          id: 43,
          image: "Bike18.jpg",
          brand: "Giant",
          color: "Pomarańczowy",
          category: "Szosowy",
          price: 8899
        },
        {
          id: 44,
          image: "Bike20.jpg",
          brand: "Trek",
          color: "Czarny",
          category: "Terenowy",
          price: 6799
        },
        {
          id: 45,
          image: "Bike17.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9999
        },
        {
          id: 46,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Górski",
          price: 7499
        },
        {
          id: 47,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Miejski",
          price: 5299
        },
        {
          id: 48,
          image: "Bike16.jpg",
          brand: "Giant",
          color: "Czarny",
          category: "Górski",
          price: 7899
        },
        {
          id: 49,
          image: "Bike15.jpg",
          brand: "Trek",
          color: "Niebieski",
          category: "Górski",
          price: 6199
        },
        {
          id: 50,
          image: "Bike18.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9299
        },
        {
          id: 51,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Terenowy",
          price: 7999
        },
        {
          id: 52,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Górski",
          price: 6499
        },
        {
          id: 53,
          image: "Bike20.jpg",
          brand: "Cube",
          color: "Szary",
          category: "Kolarski",
          price: 7499
        },
        {
          id: 54,
          image: "Bike19.jpg",
          brand: "Merida",
          color: "Czarny",
          category: "Górski",
          price: 8299
        },
        {
          id: 55,
          image: "Bike18.jpg",
          brand: "Giant",
          color: "Pomarańczowy",
          category: "Szosowy",
          price: 8899
        },
        {
          id: 56,
          image: "Bike20.jpg",
          brand: "Trek",
          color: "Czarny",
          category: "Terenowy",
          price: 6799
        },
        {
          id: 57,
          image: "Bike17.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9999
        },
        {
          id: 58,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Górski",
          price: 7499
        },
        {
          id: 59,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Miejski",
          price: 5299
        },
        {
          id: 60,
          image: "Bike16.jpg",
          brand: "Giant",
          color: "Czarny",
          category: "Górski",
          price: 7899
        },
        {
          id: 61,
          image: "Bike15.jpg",
          brand: "Trek",
          color: "Niebieski",
          category: "Górski",
          price: 6199
        },
        {
          id: 62,
          image: "Bike18.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9299
        },
        {
          id: 63,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Terenowy",
          price: 7999
        },
        {
          id: 64,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Górski",
          price: 6499
        },
        {
          id: 65,
          image: "Bike20.jpg",
          brand: "Cube",
          color: "Szary",
          category: "Kolarski",
          price: 7499
        },
        {
          id: 66,
          image: "Bike19.jpg",
          brand: "Merida",
          color: "Czarny",
          category: "Górski",
          price: 8299
        },
        {
          id: 67,
          image: "Bike18.jpg",
          brand: "Giant",
          color: "Pomarańczowy",
          category: "Szosowy",
          price: 8899
        },
        {
          id: 68,
          image: "Bike20.jpg",
          brand: "Trek",
          color: "Czarny",
          category: "Terenowy",
          price: 6799
        },
        {
          id: 69,
          image: "Bike17.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9999
        },
        {
          id: 70,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Górski",
          price: 7499
        },
        {
          id: 71,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Miejski",
          price: 5299
        },
        {
          id: 72,
          image: "Bike16.jpg",
          brand: "Giant",
          color: "Czarny",
          category: "Górski",
          price: 7899
        },
        {
          id: 73,
          image: "Bike15.jpg",
          brand: "Trek",
          color: "Niebieski",
          category: "Górski",
          price: 6199
        },
        {
          id: 74,
          image: "Bike18.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9299
        },
        {
          id: 75,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Terenowy",
          price: 7999
        },
        {
          id: 76,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Górski",
          price: 6499
        },
        {
          id: 77,
          image: "Bike20.jpg",
          brand: "Cube",
          color: "Szary",
          category: "Kolarski",
          price: 7499
        },
        {
          id: 78,
          image: "Bike19.jpg",
          brand: "Merida",
          color: "Czarny",
          category: "Górski",
          price: 8299
        },
        {
          id: 79,
          image: "Bike18.jpg",
          brand: "Giant",
          color: "Pomarańczowy",
          category: "Szosowy",
          price: 8899
        },
        {
          id: 80,
          image: "Bike20.jpg",
          brand: "Trek",
          color: "Czarny",
          category: "Terenowy",
          price: 6799
        },
        {
          id: 81,
          image: "Bike17.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9999
        },
        {
          id: 82,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Górski",
          price: 7499
        },
        {
          id: 83,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Miejski",
          price: 5299
        },
        {
          id: 84,
          image: "Bike16.jpg",




          brand: "Giant",
          color: "Czarny",
          category: "Górski",
          price: 7899
        },




        {
          id: 85,
          image: "Bike15.jpg",
          brand: "Trek",
          color: "Niebieski",
          category: "Górski",
          price: 6199
        },
        {
          id: 86,
          image: "Bike18.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9299
        },
        {
          id: 87,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Terenowy",
          price: 7999
        },
        {
          id: 88,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Górski",
          price: 6499
        },
        {
          id: 89,
          image: "Bike20.jpg",
          brand: "Cube",
          color: "Szary",
          category: "Kolarski",
          price: 7499
        },
        {
          id: 90,
          image: "Bike19.jpg",
          brand: "Merida",
          color: "Czarny",
          category: "Górski",
          price: 8299
        },
        {
          id: 91,
          image: "Bike18.jpg",
          brand: "Giant",
          color: "Pomarańczowy",
          category: "Szosowy",
          price: 8899
        },






        {
          id: 92,
          image: "Bike20.jpg",
          brand: "Trek",
          color: "Czarny",
          category: "Terenowy",
          price: 6799
        },
        {
          id: 93,
          image: "Bike17.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9999
        },
        {
          id: 94,
          image: "Bike14.jpg",
          brand: "Cannondale",
          color: "Biały",
          category: "Górski",
          price: 7499
        },




        {
          id: 95,
          image: "Bike13.jpg",
          brand: "Specialized",
          color: "Zielony",
          category: "Miejski",
          price: 5299
        },


        {
          id: 96,
          image: "Bike16.jpg",
          brand: "Giant",
          color: "Czarny",
          category: "Górski",
          price: 7899
        },
        {
          id: 97,
          image: "Bike15.jpg",
          brand: "Trek",
          color: "Niebieski",
          category: "Górski",
          price: 6199
        },
 







        {
          id: 98,
          image: "Bike18.jpg",
          brand: "Scott",
          color: "Czerwony",
          category: "Kolarski",
          price: 9299
        },


        {
          id: 99,
          image: "Bike14.jpg",
          brand: "Cannondalee",
          color: "Biały",
          category: "Terenowy",
          price: 7999
        },



        

 

      ],
      brands: [],
      categories: [],
      isLoggedIn: false,
    };






  },
  async created() {
    try {
      // Fetch data from the server
      const response = await axios.get('http://localhost:8000/bicycles/');
      this.bikes = response.data.bicycles;
      
      // Populate brands and categories
      this.brands = [...new Set(this.bikes.map(bike => bike.brand))];
      this.categories = [...new Set(this.bikes.map(bike => bike.category))];
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

<style scoped>
.shop {
  padding: 20px;
}
</style>
