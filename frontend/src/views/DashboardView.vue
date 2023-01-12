<template>
  <div class="bg-gradient-to-r from-gray-700 to-gray-900 min-h-screen">
    <Navbar />
    <SearchButton />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SearchButton from "@/components/SearchButton.vue";

export default {
  name: "DashboardView",
  components: {
    Navbar,
    SearchButton,
  },
};
</script>

<style scoped></style>
