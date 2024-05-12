<template>
  <div>
    <h1>Historia zamówień</h1>
    <ul>
      <li v-for="(order, index) in orders" :key="index">
        <p>Marka: {{ order.brand }}</p>
        <p>Cena: {{ order.price }} zł</p>
        <p>Data zakupu: {{ order.date }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HistoryOfOrders',
  data() {
    return {
      orders: []
    };
  },
  created() {
    const storedOrders = localStorage.getItem('orders');
    if (storedOrders) {
      this.orders = JSON.parse(storedOrders);
    }
  },
};
</script>

<style scoped>
  ul {
    list-style: none;
    padding: 0;
  }

  li {
    margin-bottom: 20px;
    padding: 20px;
    border: 1px solid #ccc;
  }
</style>