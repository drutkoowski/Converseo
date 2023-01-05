import axios from "axios";
import tokenActions from "@/includes/tokenActions";
import router from "../router";

// response interceptor
const axiosConfigResponse = axios.interceptors.response.use(
  function (response) {
    if (response.status !== 200 && response.status !== 201) {
      tokenActions.resetToken();
      router.push("login/");
    }
    return response;
  },
  (error) => {
    tokenActions.resetToken();
    router.push("login/");
    return Promise.reject(error.message);
  }
);
export default axiosConfigResponse;
