import { createApp } from "vue";
import router from "./router";
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
  BForm,
  BFormGroup,
} from "bootstrap-vue-next";
import App from "./App.vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";

const app = createApp(App).use(router);

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
app.component("BForm", BForm);
app.component("BFormGroup", BFormGroup);

app.mount("#app");
