import { createRouter, createWebHistory } from "vue-router";
import Main from "./components/Main.vue";
import About from "./components/About.vue";
import Registration from "./components/Registration.vue";
import Login from "./components/Login.vue";
import UserPanel from "./components/UserPanel.vue";
import Shop from "./components/Shop.vue";
import HistoryOfOrders from "./components/HistoryOfOrders.vue";
import Cart from "./components/Cart.vue";

const routes = [
  { path: "/", component: Main, name: "Main" },
  { path: "/kontakt", component: About },
  { path: "/rejestracja", component: Registration },
  { path: "/logowanie", component: Login },
  { path: "/user-panel", component: UserPanel },
  { path: "/sklep", component: Shop },
  { path: "/order-history", component: HistoryOfOrders },
  { path: "/koszyk", component: Cart },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
