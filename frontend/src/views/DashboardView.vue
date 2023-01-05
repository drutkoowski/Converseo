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
};
</script>

<style scoped></style>
