import axios from "axios";
import tokenActions from "../includes/tokenActions";

axios.defaults.baseURL = "http://52.28.70.2" + "/api/";

// request interceptor
const axiosConfigRequest = axios.interceptors.request.use(
  function (config) {
    // Do something before request is sent
    let authKey = localStorage.getItem("accessToken");
    config.headers["Authorization"] = "Bearer " + authKey;
    tokenActions.setToken(authKey, localStorage.getItem("refreshToken"));
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default axiosConfigRequest;
