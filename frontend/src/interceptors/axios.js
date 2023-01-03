import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/api/";

let refresh = false;
axios.interceptors.response.use(
  (resp) => resp,
  async (error) => {
    console.log(error.response);
    if (error.response?.status === 401 && !refresh) {
      refresh = true;
      const { status, data } = await axios.post(
        "refresh",
        {},
        {
          withCredentials: true,
        }
      );
      if (status === 200) {
        axios.defaults.headers.common["Authorization"] = `Bearer ${data.token}`;
        return axios(error.config);
      }
    }
    refresh = false;
    return error;
  }
);
