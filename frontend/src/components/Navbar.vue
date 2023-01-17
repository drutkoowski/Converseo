<template>
  <nav class="w-100 flex py-10 px-10">
    <router-link :to="{ name: 'dashboard' }" class="flex">
      <img
        class="h-20 w-20 rounded-2xl outline-pink-500 outline outline-offset-2 align-text-bottom transition-all hover:-translate-y-0.5 hover:scale-105"
        :src="avatarPath"
        alt="User Image"
        @click.prevent="isUploading = !isUploading"
      />
      <p
        v-if="username"
        class="ml-5 mt-4 text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer text-3xl underline underline-offset-8 underline decoration-orange-500/[.33] decoration-1 transition-all hover:-translate-y-0.5 hover:scale-105"
      >
        {{ username }}
      </p>
    </router-link>
    <p
      @click.prevent="signOut"
      class="ml-auto mt-4 text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer text-3xl underline underline-offset-8 underline decoration-orange-500/[.33] decoration-1 transition-all hover:-translate-y-0.5 hover:scale-105"
    >
      Logout
    </p>
  </nav>
  <UploadPopup
    v-if="isUploading"
    header="Upload Avatar"
    btn-msg="Upload"
    @closeModal="isUploading = false"
  />
</template>

<script>
import useUserStore from "@/stores/user";
import { mapActions, mapState } from "pinia";
import axios from "axios";
import UploadPopup from "./UploadPopup.vue";

export default {
  name: "Navbar",
  data() {
    return {
      isUploading: false,
    };
  },
  components: {
    UploadPopup,
  },
  computed: {
    ...mapState(useUserStore, ["username", "avatarPath"]),
    ...mapActions(useUserStore, ["signOut"]),
  },
  async created() {
    const userStore = useUserStore();
    const response = await axios.get("user/current");
    userStore.username = response.data.username;
    userStore.avatarPath = response.data.avatar;
  },
};
</script>
