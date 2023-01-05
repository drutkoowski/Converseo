<template>
  <div class="bg-gradient-to-r from-gray-700 to-gray-900 min-h-screen">
    <Navbar />
    <SearchButton />
  </div>
</template>

<script>
import useUserStore from "@/stores/user";
import Navbar from "@/components/Navbar.vue";
import SearchButton from "@/components/SearchButton.vue";
import axios from "axios";

export default {
  name: "DashboardView",
  components: {
    Navbar,
    SearchButton,
  },
  async created() {
    const userStore = useUserStore();
    const response = await axios.get("user/current");
    userStore.username = response.data.username;
    userStore.avatarPath = response.data.avatar;
  },
};
</script>

<style scoped></style>
