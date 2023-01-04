// Vue
import { createApp } from "vue";
import { createPinia } from "pinia";
import VeeValidatePlugin from "@/includes/validation";
import App from "./App.vue";
import router from "./router";

// Css
import "./assets/main.css";

// Axios
import "./interceptors/axiosRequest";
import "./interceptors/axiosResponse";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(VeeValidatePlugin);

document.title = "Converseo";
app.mount("#app");
