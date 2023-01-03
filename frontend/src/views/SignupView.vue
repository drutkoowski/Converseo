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
          <button
            class="w-full font-semibold block h-20 bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer uppercase text-stone-50 text-lg rounded-md transition-all hover:-translate-y-0.5 hover:scale-0.5"
          >
            Join
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import CardHeader from "@/components/CardHeader.vue";
export default {
  name: "SignupView",
  components: {
    CardHeader,
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
