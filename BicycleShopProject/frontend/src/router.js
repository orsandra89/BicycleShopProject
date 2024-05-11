import { createRouter, createWebHistory } from "vue-router";
import Main from "./components/Main.vue";
import About from "./components/About.vue";
import Registration from "./components/Registration.vue";

const routes = [
  { path: "/", component: Main },
  { path: "/kontakt", component: About },
  { path: "/rejestracja", component: Registration },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
