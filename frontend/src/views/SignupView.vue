<template>
  <div
    class="bg-hero-pattern bg-repeat animate-ltr-linear-infinite flex h-screen"
  >
    <div class="m-auto w-30 h-70 w-4/12 h-6/6 rounded-2xl">
      <CardHeader :msg="'Sign up'" />
      <vee-form @submit="signUp" :validation-schema="signupSchema">
        <div class="relative my-12 mx-5">
          <vee-field
            name="username"
            type="text"
            class="block h-20 text-2xl rounded-lg px-2.5 pb-1.5 pt-5 w-full text-sm text-black bg-gray-50 dark:bg-gradient-to-r from-orange-100 to-orange-200 border-2 border-orange-500 appearance-none dark:text-black dark:border-orange-500 dark:focus:border-orange-700 focus:outline-none focus:ring-0 focus:border-orange-600 peer"
            placeholder=" "
          />
          <label
            class="absolute text-2xl text-stone-50 dark:text-orange-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-orange-600 peer-focus:dark:text-orange-700 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4"
            >Username</label
          >
        </div>
        <div class="relative my-12 mx-5">
          <vee-field
            type="email"
            name="email"
            class="block h-20 text-2xl rounded-lg px-2.5 pb-1.5 pt-5 w-full text-sm text-black bg-gray-50 dark:bg-gradient-to-r from-orange-100 to-orange-200 border-2 border-orange-500 appearance-none dark:text-black dark:border-orange-500 dark:focus:border-orange-700 focus:outline-none focus:ring-0 focus:border-orange-600 peer"
            placeholder=" "
          />
          <label
            class="absolute text-2xl text-stone-50 dark:text-orange-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-orange-600 peer-focus:dark:text-orange-700 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4"
            >Email</label
          >
        </div>
        <div class="relative mt-4 mx-5">
          <vee-field
            type="password"
            name="password"
            class="block h-20 text-2xl rounded-lg px-2.5 pb-1.5 pt-5 w-full text-sm text-black bg-gray-50 dark:bg-gradient-to-r from-orange-100 to-orange-200 border-2 border-orange-500 appearance-none dark:text-black dark:border-orange-500 dark:focus:border-orange-700 focus:outline-none focus:ring-0 focus:border-orange-600 peer"
            placeholder=" "
          />
          <label
            class="absolute text-2xl text-stone-50 dark:text-orange-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-orange-600 peer-focus:dark:text-orange-700 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4"
            >Password</label
          >
        </div>
        <div class="relative mx-5 mt-1 text-white flex">
          <div class="flex h-4">
            <ErrorMessage class="text-red-600 block" name="username" />
            <ErrorMessage class="text-red-600 ml-1" name="email" />
            <ErrorMessage class="text-red-600 ml-1" name="password" />
          </div>
        </div>
        <div class="relative mx-5 mt-9 text-white flex">
          <p
            class="cursor-pointer text-stone-300 hover:-translate-y-0.5 hover:scale-0.5 transition-all"
          >
            <router-link :to="{ name: 'login' }"
              >Already have an account?</router-link
            >
          </p>
        </div>
        <div class="relative my-3 mx-5">
          <CardButton :text="'Join'" />
        </div>
      </vee-form>
    </div>
  </div>
</template>

<script>
import CardHeader from "@/components/CardHeader.vue";
import CardButton from "@/components/CardButton.vue";
import axios from "axios";

export default {
  name: "SignupView",
  components: {
    CardButton,
    CardHeader,
  },
  data() {
    return {
      signupSchema: {
        username: "required|min:3|max:100",
        email: "required|min:3|max:100|email",
        password: "required|min:3|max:100",
      },
      isError: false,
      errorMsg: "",
    };
  },
  methods: {
    async signUp(values) {
      this.isError = false;
      this.errorMsg = "";
      const username = values.username;
      const email = values.email;
      const password = values.password;
      const data = await axios.post("user/create", {
        username: username,
        password: password,
        email: email,
      });
      if (data.status !== 200 && data.status !== 201) {
        this.isError = true;
        this.errorMsg = "Something went wrong.";
        return;
      }
      this.$router.push({ name: "login" });
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
