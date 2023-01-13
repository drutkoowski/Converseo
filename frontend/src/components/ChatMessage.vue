<template>
  <div class="card__message-container__message--receiver mt-2" v-if="isHost">
    <p class="bg-gradient-to-r from-gray-700 to-gray-900 text-stone-50">
      {{ content }}
    </p>
  </div>
  <div class="card__message-container__message--talker mt-2" v-else>
    <img
      class="ml-4 rounded-full outline outline-pink-500 outline-offset-0.5 transition-all hover:-translate-y-0.5 hover:scale-105 w-10 h-10"
      :src="avatar"
      alt="Talker Avatar"
    />
    <p class="ml-4 bg-gradient-to-r from-stone-50 to-stone-200 text-black-50">
      {{ content }}
    </p>
  </div>
</template>

<script>
export default {
  name: "ChatMessage",
  props: ["isHost", "content", "avatar"],
};
</script>

<style scoped lang="scss">
.card__message-container__message--receiver {
  display: flex;
  align-items: center;
  p {
    font-size: 2rem;
    padding: 0.25rem 2rem;
    border-radius: 10px;
  }
}
.card__message-container__message--talker {
  display: flex;
  align-items: center;
  p {
    font-size: 2rem;
    padding: 0.25rem 2rem;
    border-radius: 10px;
  }
  img {
    margin-left: auto;
  }
}
</style>
