<template>
  <div class="container">
    <header>
      <h1>Witaj w Sklepie Rowerowym</h1>
      <p>Znajdź idealnych pedałów dla siebie</p>
    </header>
    <b-carousel id="carousel-1" :interval="4000" controls indicators background="#ababab" class="custom-carousel">
      <b-carousel-slide :img-src="bikeImages[0]">
        <div class="carousel-caption">
        </div>
      </b-carousel-slide>
      <b-carousel-slide :img-src="bikeImages[1]">
        <div class="carousel-caption">
        </div>
      </b-carousel-slide>
      <b-carousel-slide :img-src="bikeImages[2]">
        <div class="carousel-caption">
        </div>
      </b-carousel-slide>
    </b-carousel>
    <div class="row">
      <div class="col-md-4" v-for="bike in bikes" :key="bike.id">
        <div class="card">
          <img :src="bike.image" class="card-img-top" alt="Rower">
          <div class="card-body">
            <h5 class="card-title">{{ bike.name }}</h5>
            <p class="card-text">{{ bike.description }}</p>
            <b-button variant="primary">Dodaj do koszyka</b-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { BCarousel, BCarouselSlide, BButton } from 'bootstrap-vue-next';
import bike1 from '@/assets/images/bike1.jpg';
import bike2 from '@/assets/images/bike2.jpg';
import bike3 from '@/assets/images/bike3.jpg';

export default {
  name: 'AppMain',
  components: {
    BCarousel,
    BCarouselSlide,
    BButton,
  },
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
      ],
      bikeImages: [bike1, bike2, bike3]
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

.custom-carousel {
  width: 100%;
  height: 0;
  padding-bottom: 50%;
  overflow: hidden;
  margin-bottom: 20px;
}

.custom-carousel img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
}
</style>