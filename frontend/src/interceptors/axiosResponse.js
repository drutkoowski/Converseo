import axios from "axios";
import tokenActions from "@/includes/tokenActions";
// response interceptor
const axiosConfigResponse = axios.interceptors.response.use(
  function (response) {
    if (response.status !== 200) {
      tokenActions.resetToken();
      this.$router.push("login/");
    }
    return response;
  },
  (error) => {
    tokenActions.resetToken();
    this.$router.push("login/");
    return Promise.reject(error.message);
  }
);
export default axiosConfigResponse;
