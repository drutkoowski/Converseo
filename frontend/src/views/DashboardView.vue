<template>
  <h1>WITAM W DASHBOARDZIE</h1>
  <router-link :to="{ name: 'test' }">go to test</router-link>
  <p v-for="post in posts" :key="post.author">Author: {{ post.author }}</p>
  <input type="text" placeholder="add post" v-model="author" />
  <button @click.prevent="addPost">add post</button>
  <button @click="logOut">logout</button>
</template>

<script>
import useUserStore from "@/stores/user";
import { mapState } from "pinia/dist/pinia";
import axios from "axios";

export default {
  name: "DashboardView",
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
    logOut() {
      localStorage.setItem("isAuthenticated", JSON.stringify(false));
      localStorage.setItem("accessToken", "");
      localStorage.setItem("refreshToken", "");
      useUserStore.isAuthenticated = false;
      useUserStore.access = "";
      useUserStore.refresh = "";
      this.$router.push("login/");
    },
    async addPost() {
      const response = await axios.post("posts", {
        author: this.author,
      });
      console.log(response);
    },
  },
};
</script>
