<template>
  <div
    class="bg-hero-pattern bg-repeat animate-ltr-linear-infinite flex h-screen"
  >
    <div class="m-auto w-30 h-50 w-4/12 h-6/6 rounded-2xl">
      <CardHeader :msg="'Sign up'" />
      <form action="">
        <div class="relative my-12 mx-5">
          <input
            type="text"
            id="username"
            class="block h-20 text-2xl rounded-lg px-2.5 pb-1.5 pt-5 w-full text-sm text-black bg-gray-50 dark:bg-gradient-to-r from-orange-100 to-orange-200 border-2 border-orange-500 appearance-none dark:text-black dark:border-orange-500 dark:focus:border-orange-700 focus:outline-none focus:ring-0 focus:border-orange-600 peer"
            placeholder=" "
          />
          <label
            for="username"
            class="absolute text-2xl text-stone-50 dark:text-orange-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-orange-600 peer-focus:dark:text-orange-700 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4"
            >Username</label
          >
        </div>
        <div class="relative my-12 mx-5">
          <input
            type="password"
            id="password"
            class="block h-20 text-2xl rounded-lg px-2.5 pb-1.5 pt-5 w-full text-sm text-black bg-gray-50 dark:bg-gradient-to-r from-orange-100 to-orange-200 border-2 border-orange-500 appearance-none dark:text-black dark:border-orange-500 dark:focus:border-orange-700 focus:outline-none focus:ring-0 focus:border-orange-600 peer"
            placeholder=" "
          />
          <label
            for="password"
            class="absolute text-2xl text-stone-50 dark:text-orange-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-orange-600 peer-focus:dark:text-orange-700 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4"
            >Password</label
          >
        </div>
        <div class="relative my-12 mx-5 flex">
          <div class="w-3/6">
            <select
              name=""
              id=""
              class="h-9 w-5/6 rounded-md text-center mt-0.5"
            >
              <option value="male">Male</option>
              <option value="female">Female</option>
            </select>
          </div>
          <div class="w-3/6">
            <Datepicker
              class="h-10"
              :max-date="new Date()"
              :year-picker="true"
              :placeholder="'Birth Year'"
            />
          </div>
        </div>
        <div class="relative mx-5 text-white flex">
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
      </form>
    </div>
  </div>
</template>

<script>
import CardHeader from "@/components/CardHeader.vue";
import CardButton from "@/components/CardButton.vue";
import Datepicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

export default {
  name: "SignupView",
  components: {
    CardButton,
    CardHeader,
    Datepicker,
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
