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
  import { ref } from 'vue';
  
  export default {
    name: 'HistoryOfOrders',
    setup() {
      const orders = ref([]);
  
      const addOrders = (newOrders) => {
        orders.value = orders.value.concat(newOrders);
      };
  
      this.$emitter.on('checkout', addOrders);
  
      return {
        orders,
      };
    },
  };
  </script>