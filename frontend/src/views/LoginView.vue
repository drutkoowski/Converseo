<template>
  <div
    class="bg-hero-pattern bg-repeat animate-ltr-linear-infinite flex h-screen"
  >
    <div class="m-auto w-30 h-50 w-4/12 h-6/6 rounded-2xl">
      <CardHeader :msg="'Login'" />
      <vee-form @submit="login" :validation-schema="loginSchema">
        <div class="relative my-12 mx-5">
          <vee-field
            name="username"
            type="text"
            id="username"
            class="block h-20 text-2xl rounded-lg px-2.5 pb-1.5 pt-5 w-full text-sm text-black bg-gray-50 dark:bg-gradient-to-r from-orange-100 to-orange-200 border-2 border-orange-500 appearance-none dark:text-black dark:border-orange-500 dark:focus:border-orange-700 focus:outline-none focus:ring-0 focus:border-orange-600 peer"
            placeholder=" "
          />
          <label
            class="absolute text-2xl text-stone-50 dark:text-orange-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-orange-600 peer-focus:dark:text-orange-700 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4"
            >Username</label
          >
        </div>
        <div class="relative mt-12 mx-5">
          <vee-field
            name="password"
            type="password"
            id="password"
            class="block h-20 text-2xl rounded-lg px-2.5 pb-1.5 pt-5 w-full text-sm text-black bg-gray-50 dark:bg-gradient-to-r from-orange-100 to-orange-200 border-2 border-orange-500 appearance-none dark:text-black dark:border-orange-500 dark:focus:border-orange-700 focus:outline-none focus:ring-0 focus:border-orange-600 peer"
            placeholder=" "
          />
          <label
            class="absolute text-2xl text-stone-50 dark:text-orange-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-orange-600 peer-focus:dark:text-orange-700 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4"
            >Password</label
          >
        </div>
        <div class="relative mx-5 mt-4 text-white">
          <div class="flex h-4">
            <ErrorMessage class="text-red-600" name="username" />
            <ErrorMessage class="text-red-600 ml-1" name="password" />
          </div>
          <div class="flex h-4" v-if="isError">
            <p class="text-red-600">{{ errorMsg }}</p>
          </div>
          <p
            class="cursor-pointer mt-3 text-stone-300 hover:-translate-y-0.5 hover:scale-0.5 transition-all"
          >
            <router-link :to="{ name: 'signup' }"
              >Don't have an account?</router-link
            >
          </p>
        </div>
        <div class="relative my-3 mx-5">
          <CardButton :text="'Login'" />
        </div>
      </vee-form>
    </div>
  </div>
</template>

<script>
import CardHeader from "@/components/CardHeader.vue";
import CardButton from "@/components/CardButton.vue";
import useUserStore from "@/stores/user";
import { mapState } from "pinia";

import axios from "axios";
import tokenActions from "../includes/tokenActions";

export default {
  name: "LoginView",
  components: {
    CardHeader,
    CardButton,
  },
  data() {
    return {
      loginSchema: {
        username: "required|min:3|max:100",
        password: "required|min:3|max:100",
      },
      isError: false,
      errorMsg: "",
    };
  },
  computed: {
    ...mapState(useUserStore, ["isAuthenticated", "access", "refresh"]),
  },
  methods: {
    async login(values) {
      const username = values.username;
      const password = values.password;
      this.isError = false;
      this.errorMsg = "";
      console.log(username, password);
      try {
        const data = await axios.post(
          "token/",
          {
            username: username,
            password: password,
          },
          { withCredentials: true }
        );
        console.log(data);
        if (data.status !== 200) {
          this.isError = true;
          this.errorMsg = "User does not exist or credentials are invalid.";
          return;
        }
        this.isError = false;
        this.errorMsg = "";
        tokenActions.setToken(data.data.access, data.data.refresh);
        this.$router.push("/");
      } catch (error) {
        console.log(error);
        this.isError = true;
        this.errorMsg = "Something went wrong.";
      }
    },
  },
};
</script>

<style scoped>
body {
  overflow: hidden;
}
.bg-hero-pattern {
  background-size: contain;
}
</style>
