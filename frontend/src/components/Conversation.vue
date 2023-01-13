<template>
  <div class="grid-container">
    <div class="card bg-gradient-to-br from-orange-200 to-red-300">
      <div class="card__user-header mt-10 ml-4">
        <img
          class="rounded-full outline outline-pink-500 outline-offset-0.5 transition-all hover:-translate-y-0.5 hover:scale-105 w-20 h-20"
          src="https://converseo.s3.amazonaws.com/media/avatars/nf.png"
          alt=""
        />
        <h1
          class="bg-clip-text from-orange-200 to-red-600 cursor-pointer text-4xl transition-all hover:-translate-y-0.5 hover:scale-105 ml-4 uppercase"
        >
          Username
        </h1>
      </div>
      <hr class="mt-4" />
      <div class="card__message-container">
        <div class="card__message-container__message--receiver">
          <p class="bg-gradient-to-r from-gray-700 to-gray-900 text-stone-50">
            Hello World!
          </p>
        </div>

        <div class="card__message-container__message--talker mt-4">
          <img
            class="ml-4 rounded-full outline outline-pink-500 outline-offset-0.5 transition-all hover:-translate-y-0.5 hover:scale-105 w-10 h-10"
            src="https://converseo.s3.amazonaws.com/media/avatars/nf.png"
            alt=""
          />
          <p
            class="ml-4 bg-gradient-to-r from-stone-50 to-stone-200 text-black-50"
          >
            Hello World!
          </p>
        </div>
      </div>
      <div class="card__message-creator">
        <input
          type="text"
          id="message"
          v-model="message"
          placeholder="Type a message..."
          class="w-9/12 h-12 rounded-full text-xl"
        />
        <button
          @click.prevent="sendMessage"
          class="bg-gradient-to-r from-gray-700 to-gray-900 text-stone-50 h-12 w-44 ml-4 rounded-full text-center text-uppercase text-2xl"
        >
          Send
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import useUserStore from "@/stores/user";

export default {
  name: "Conversation",
  props: ["id"],
  data() {
    return {
      message: "",
      ws: "",
    };
  },
  created() {
    const userStore = useUserStore();
    this.ws = new WebSocket(
      `ws://127.0.0.1:8000/ws/conversations/${this.id}/?token=${userStore.access}`
    );
    this.ws.onmessage = function (e) {
      console.log(e);
    };
  },
  methods: {
    async sendMessage() {
      const userStore = useUserStore();
      this.ws.send(
        JSON.stringify({
          message: this.message,
          conversation_id: this.id,
          token: userStore.access,
        })
      );
    },
  },
};
</script>

<style scoped lang="scss">
.isTalker {
  margin-left: auto;
}

.grid-container {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 0.25fr 1fr 0.25fr;
  justify-content: center;
  align-content: center;
  margin-top: 6rem;
  height: 75vh;
}
.card {
  height: 85%;
  border-radius: 20px;
  grid-column: 2/3;
  grid-row: 1/2;
  hr {
    border-top-width: 3px;
  }
  &__user-header {
    display: flex;
    align-items: center;
  }
  &__message-container {
    padding: 2rem 2rem;
    height: 65%;
    overflow-y: hidden;
    &__message--receiver {
      display: flex;
      align-items: center;
      p {
        font-size: 2rem;
        padding: 0.25rem 2rem;
        border-radius: 10px;
      }
    }
    &__message--talker {
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
  }
  &__message-creator {
    padding: 0 2rem;
    input {
      padding: 0 2rem;
      transition: all 0.3s ease-in;
      &:focus {
        outline: none;
        transform: scale(1.01);
      }
    }
    button {
      transition: all 0.3s ease-in;
      &:hover {
        transform: scale(1.02);
      }
    }
  }
}
</style>
