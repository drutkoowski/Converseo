<template>
  <div class="bg-gradient-to-r from-gray-700 to-gray-900 min-h-screen">
    <Navbar />
    <Conversation />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Conversation from "@/components/Conversation.vue";

export default {
  name: "ConversationView",
  components: {
    Navbar,
    Conversation,
  },
};
</script>

<style scoped></style>
