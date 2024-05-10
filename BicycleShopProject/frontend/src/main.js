import { createApp } from "vue";
import {
  BNavbar,
  BNavbarBrand,
  BNavbarNav,
  BNavItem,
  BNavbarToggle,
  BCollapse,
  BNavForm,
  BFormInput,
  BButton,
  BNavItemDropdown,
  BDropdownItem,
} from "bootstrap-vue-next";
import App from "./App.vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";

const app = createApp(App);

app.component("BNavbar", BNavbar);
app.component("BNavbarBrand", BNavbarBrand);
app.component("BNavbarNav", BNavbarNav);
app.component("BNavItem", BNavItem);
app.component("BNavbarToggle", BNavbarToggle);
app.component("BCollapse", BCollapse);
app.component("BNavForm", BNavForm);
app.component("BFormInput", BFormInput);
app.component("BButton", BButton);
app.component("BNavItemDropdown", BNavItemDropdown);
app.component("BDropdownItem", BDropdownItem);

app.mount("#app");
