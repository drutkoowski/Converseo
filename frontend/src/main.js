import { createApp } from "vue";
import { createPinia } from "pinia";
import VeeValidatePlugin from "@/includes/validation";

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";
import "./interceptors/axios";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(VeeValidatePlugin);

document.title = "Converseo";
app.mount("#app");
