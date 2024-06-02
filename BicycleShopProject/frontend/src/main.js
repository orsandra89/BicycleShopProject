import { createApp } from "vue";
import axios from "axios";

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
  BContainer,
  BRow,
  BCol,
  BAlert,
  BSpinner,
  BCarousel,
  BCarouselSlide,
  BImg,
  BFormSelect,
} from "bootstrap-vue-next";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faBasketShopping,
  faCircleUser,
  faBicycle,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import App from "./App.vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";

axios.defaults.baseURL = "http://localhost:8000";

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
app.component("BContainer", BContainer);
app.component("BRow", BRow);
app.component("BCol", BCol);
app.component("BAlert", BAlert);
app.component("BSpinner", BSpinner);
app.component("BCarousel", BCarousel);
app.component("BCarouselSlide", BCarouselSlide);
app.component("BImg", BImg);
app.component("BFormSelect", BFormSelect);

library.add(faBasketShopping);
library.add(faCircleUser);
library.add(faBicycle);

app.component("font-awesome-icon", FontAwesomeIcon);

app.mount("#app");
