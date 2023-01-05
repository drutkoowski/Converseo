<template>
  <nav class="w-100 flex py-10 px-10">
    <img
      class="h-20 w-20 rounded-2xl outline-pink-500 outline outline-offset-2 align-text-bottom transition-all hover:-translate-y-0.5 hover:scale-105"
      :src="avatarPath"
      alt="User Image"
    />
    <p
      v-if="username"
      class="ml-5 mt-4 text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer text-3xl underline underline-offset-8 underline decoration-orange-500/[.33] decoration-1 transition-all hover:-translate-y-0.5 hover:scale-105"
    >
      {{ username }}
    </p>
    <p
      @click.prevent="signOut"
      class="ml-auto mt-4 text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer text-3xl underline underline-offset-8 underline decoration-orange-500/[.33] decoration-1 transition-all hover:-translate-y-0.5 hover:scale-105"
    >
      Logout
    </p>
  </nav>
</template>

<script>
import useUserStore from "@/stores/user";
import { mapActions, mapState } from "pinia";

export default {
  name: "Navbar",
  computed: {
    ...mapState(useUserStore, ["username", "avatarPath"]),
    ...mapActions(useUserStore, ["signOut"]),
  },
};
</script>
