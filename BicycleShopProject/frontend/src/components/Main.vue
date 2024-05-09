<template>
    <div class="container">
      <header>
        <h1>Witaj w Sklepie Rowerowym</h1>
        <p>Znajdź idealnych pedałów dla siebie</p>
      </header>
      <div class="row">
        <div class="col-md-4" v-for="bike in bikes" :key="bike.id">
          <div class="card">
            <img :src="bike.image" class="card-img-top" alt="Rower">
            <div class="card-body">
              <h5 class="card-title">{{ bike.name }}</h5>
              <p class="card-text">{{ bike.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AppMain',
    data() {
      return {
        bikes: [
          {
            id: 1,
            name: 'Rower górski',
            description: 'Idealny rower do jazdy w trudnym terenie.',
            price: 1500,
            image: 'https://via.placeholder.com/300'
          },
          {
            id: 2,
            name: 'Rower szosowy',
            description: 'Przeznaczony do szybkiej jazdy po asfalcie.',
            price: 2000,
            image: 'https://via.placeholder.com/300'
          },
          {
            id: 3,
            name: 'Rower miejski',
            description: 'Wygodny i praktyczny rower na co dzień.',
            price: 1200,
            image: 'https://via.placeholder.com/300'
          }
        ]
      };
    }
  }
  </script>
  
  <style scoped>
  .header {
    text-align: center;
    margin-bottom: 50px;
  }
  
  .card {
    margin-bottom: 20px;
  }
  </style>
  