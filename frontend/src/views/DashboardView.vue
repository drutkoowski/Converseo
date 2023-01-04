<template>
  <h1>WITAM W DASHBOARDZIE</h1>
  <router-link :to="{ name: 'test' }">go to test</router-link>
  <button @click="logOut">logout</button>
</template>

<script>
import useUserStore from "@/stores/user";
import { mapState } from "pinia/dist/pinia";

export default {
  name: "DashboardView",
  computed: {
    ...mapState(useUserStore, ["isAuthenticated", "access", "refresh"]),
  },
  methods: {
    logOut() {
      localStorage.setItem("isAuthenticated", JSON.stringify(false));
      localStorage.setItem("accessToken", "");
      localStorage.setItem("refreshToken", "");
      console.log(useUserStore.isAuthenticated);
      useUserStore.isAuthenticated = false;
      console.log(useUserStore.isAuthenticated);
      useUserStore.access = "";
      useUserStore.refresh = "";
      this.$router.push("login/");
    },
  },
};
</script>
