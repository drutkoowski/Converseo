import { defineStore } from "pinia";
import router from "@/router";
import axios from "axios";
import tokenActions from "@/includes/tokenActions";

export default defineStore("user", {
  state: () => ({
    access: localStorage.getItem("accessToken") || "",
    refresh: localStorage.getItem("refreshToken") || "",
    username: "",
    avatarPath:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6sGddmMZFZCqb7aJFx5eV-8FGj2gJWz7abGntj8IuyYdAv7W2HEJyi5WY3xbpLLzf-Zg&usqp=CAU",
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
