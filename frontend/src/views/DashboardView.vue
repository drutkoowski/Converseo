<template>
  <div class="bg-gradient-to-r from-gray-700 to-gray-900 min-h-screen">
    <Navbar />
    <SearchButton />
  </div>
</template>

<script>
import useUserStore from "@/stores/user";
import { mapState } from "pinia/dist/pinia";
import Navbar from "@/components/Navbar.vue";
import SearchButton from "@/components/SearchButton.vue";
import axios from "axios";

export default {
  name: "DashboardView",
  components: {
    Navbar,
    SearchButton,
  },
  data() {
    return {};
  },
  computed: {
    ...mapState(useUserStore, ["isAuthenticated", "access", "refresh"]),
  },
  async created() {
    const userStore = useUserStore();
    const response = await axios.get("user/current");
    userStore.username = response.data.username;
  },
};
</script>

<style scoped></style>
