import axios from "axios";
import useUserStore from "@/stores/user";

axios.defaults.baseURL = "http://127.0.0.1:8000/api/";
if (useUserStore.isAuthenticated) {
  axios.defaults.headers.common["Authorization"] =
    "Bearer " + useUserStore.access;
} else {
  axios.defaults.headers.common["Authorization"] = "";
}
