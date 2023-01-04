import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/api/";

// request interceptor
const axiosConfigRequest = axios.interceptors.request.use(
  function (config) {
    // Do something before request is sent
    let authKey = localStorage.getItem("accessToken");
    config.headers["Authorization"] = "Bearer " + authKey;
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default axiosConfigRequest;
