<template>
  <div class="container">
    <header>
      <h1>Witaj w Sklepie Rowerowym</h1>
      <p>Znajdź idealny rower dla siebie</p>
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
    <div class="about-us">
      <h2>O naszym sklepie</h2>
      <p>
        Nasz sklep rowerowy jest znany z szerokiej gamy wysokiej jakości rowerów. 
        Niezależnie od tego, czy jesteś profesjonalnym kolarzem, czy też szukasz roweru do codziennego użytku, 
        mamy coś dla Ciebie. Jesteśmy dumni z naszego poziomu obsługi klienta i jesteśmy zawsze gotowi pomóc Ci 
        znaleźć idealny rower.
      </p>
    </div>
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
.about-us {
  text-align: center;
  margin: 20px 0;
}
</style>