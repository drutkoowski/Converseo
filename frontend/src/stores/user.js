import { defineStore } from "pinia";
import axios from "axios";

export default defineStore("user", {
  state: () => ({
    access: localStorage.getItem("accessToken") || "",
    refresh: localStorage.getItem("refreshToken") || "",
    isAuthenticated:
      JSON.parse(localStorage.getItem("isAuthenticated")) || false,
  }),
  actions: {
    async refreshToken() {
      const isAuthenticated = JSON.parse(
        localStorage.getItem("isAuthenticated") || false
      );
      const refresh = localStorage.getItem("refreshToken") || "";
      if (isAuthenticated) {
        const response = await axios.post("token/refresh/", {
          refresh: refresh,
        });
        localStorage.setItem("refreshToken", response.data.refresh);
        localStorage.setItem("accessToken", response.data.access);
        this.access = response.data.access;
        this.response = response.data.refresh;
      }
    },
  },
});
