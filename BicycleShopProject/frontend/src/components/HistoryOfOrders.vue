<template>
    <div>
      <h1>Historia zamówień</h1>
      <ul>
        <li v-for="(order, index) in orders" :key="index">
          Zamówienie #{{ order.id }}: {{ order.item }} - {{ order.quantity }} sztuk
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        orders: [
          { id: 1, item: 'Rower górski', quantity: 2 },
          { id: 2, item: 'Rower miejski', quantity: 1 },
          { id: 3, item: 'Rower BMX', quantity: 5 },
          { id: 4, item: 'Rower szosowy', quantity: 3 },
          { id: 5, item: 'Rower turystyczny', quantity: 2 },
          { id: 6, item: 'Rower crossowy', quantity: 1 },
          { id: 7, item: 'Rower gravelowy', quantity: 4 },
          { id: 8, item: 'Rower hybrydowy', quantity: 2 },
          { id: 9, item: 'Rower kolarski', quantity: 2 },
          { id: 10, item: 'Rower trekkingowy', quantity: 3 },
          { id: 11, item: 'Rower trialowy', quantity: 2 },
          { id: 12, item: 'Rower elektryczny', quantity: 1 },
          { id: 13, item: 'Rower downhillowy', quantity: 3 },
          { id: 14, item: 'Rower freestyle', quantity: 2 },
          { id: 15, item: 'Rower z biegami w piaście', quantity: 2 },
          { id: 16, item: 'Rower z napędem pasowym', quantity: 1 },
          { id: 17, item: 'Rower z amortyzacją pełną', quantity: 2 },
          { id: 18, item: 'Rower dirtowy', quantity: 1 },
          { id: 19, item: 'Rower tadem', quantity: 3 },
          { id: 20, item: 'Rower Fatbike', quantity: 2 },
          { id: 21, item: 'Rower składany', quantity: 2 },
          { id: 22, item: 'Rower cruiser', quantity: 1 },
          { id: 23, item: 'Rower cargo', quantity: 4 },
          { id: 24, item: 'Rower szosowo-turystyczny', quantity: 2 },
          { id: 25, item: 'Rower komfortowy', quantity: 2 },
          { id: 26, item: 'Rower uniwersalny', quantity: 1 },
          { id: 27, item: 'Rower enduro', quantity: 3 },
          { id: 28, item: 'Rower hardtail', quantity: 2 },
          { id: 29, item: 'Rower full suspension', quantity: 2 },
          { id: 30, item: 'Rower plus', quantity: 1 },
          { id: 31, item: 'Rower XXL', quantity: 3 },
          { id: 32, item: 'Rower mini', quantity: 2 },
          { id: 33, item: 'Rower z kołami 29"', quantity: 2 },
          { id: 34, item: 'Rower z kołami 27.5"', quantity: 1 },
          { id: 35, item: 'Rower z kołami 26"', quantity: 3 },
          { id: 36, item: 'Rower z kołami 24"', quantity: 2 },
          { id: 37, item: 'Rower z kołami 20"', quantity: 2 },
          { id: 38, item: 'Rower z kołami 16"', quantity: 1 },
          { id: 39, item: 'Rower z kołami 12"', quantity: 3 },
          { id: 40, item: 'Rower dla seniora', quantity: 2 },
          { id: 41, item: 'Rower dla młodzieży', quantity: 2 },
          { id: 42, item: 'Rower dla dziecka', quantity: 1 },
          { id: 43, item: 'Rower dla dorosłego', quantity: 2 },
          { id: 44, item: 'Rower dla amatora', quantity: 1 },
          { id: 45, item: 'Rower dla profesjonalisty', quantity: 3 },
          { id: 46, item: 'Rower dla entuzjasty', quantity: 2 },
          { id: 47, item: 'Rower dla ekstremalisty', quantity: 2 },
          { id: 48, item: 'Rower dla hobbysty', quantity: 1 },
          { id: 49, item: 'Rower dla sportowca', quantity: 2 },
          { id: 50, item: 'Rower dla rekreacji', quantity: 2 },
        ],
      };
    },
  };
  </script>