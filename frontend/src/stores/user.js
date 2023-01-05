import { defineStore } from "pinia";
import router from "@/router";
import axios from "axios";
import tokenActions from "@/includes/tokenActions";

export default defineStore("user", {
  state: () => ({
    access: localStorage.getItem("accessToken") || "",
    refresh: localStorage.getItem("refreshToken") || "",
    username: "",
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
        try {
          const response = await axios.post("token/refresh/", {
            refresh: refresh,
          });
          tokenActions.setToken(response.data.access, response.data.refresh);
        } catch (error) {
          tokenActions.resetToken();
          router.push("login/");
        }
      }
    },
    signOut() {
      tokenActions.resetToken();
      router.push("login/");
    },
  },
});
