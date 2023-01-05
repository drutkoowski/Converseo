<template>
  <div class="bg-gradient-to-r from-gray-700 to-gray-900 min-h-screen">
    <Navbar />
    <!--    <h1>WITAM W DASHBOARDZIE</h1>-->
    <!--    <router-link :to="{ name: 'test' }">go to test</router-link>-->
    <!--    <p v-for="post in posts" :key="post.author">Author: {{ post.author }}</p>-->
    <!--    <input type="text" placeholder="add post" v-model="author" />-->
    <!--    <button @click.prevent="addPost">add post</button>-->
    <!--    <button @click="logOut">logout</button>-->
    <SearchButton />
  </div>
</template>

<script>
import useUserStore from "@/stores/user";
import { mapState } from "pinia/dist/pinia";
import axios from "axios";
import Navbar from "@/components/Navbar.vue";
import SearchButton from "@/components/SearchButton.vue";

export default {
  name: "DashboardView",
  components: {
    Navbar,
    SearchButton,
  },
  data() {
    return {
      posts: [],
      author: "",
    };
  },
  async created() {
    const response = await axios.get("posts");
    this.posts = response.data;
  },
  computed: {
    ...mapState(useUserStore, ["isAuthenticated", "access", "refresh"]),
  },
  methods: {
    async addPost() {
      const response = await axios.post("posts", {
        author: this.author,
      });
      console.log(response);
    },
  },
};
</script>

<style scoped></style>
