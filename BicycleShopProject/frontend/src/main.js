import { createApp } from "vue";
import { createVuetify } from "vuetify";
import { VApp } from "vuetify/lib/components";
import { useHead } from "@vueuse/head";
import App from "./App.vue";

const app = createApp(App);

app.use(useHead);
app.use(createVuetify, {
  components: {
    VApp,
  },
});

app.mount("#app");
