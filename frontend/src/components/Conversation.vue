<template>
  <div class="grid-container">
    <transition name="fade">
      <div class="card bg-gradient-to-br from-orange-200 to-red-300">
        <div class="card__user-header mt-5">
          <img
            class="rounded-full outline outline-pink-500 outline-offset-0.5 transition-all hover:-translate-y-0.5 hover:scale-105 w-20 h-20 ml-4"
            :src="talkerAvatar"
            alt=""
          />
          <h1
            class="bg-clip-text from-orange-200 to-red-600 cursor-pointer text-4xl transition-all hover:-translate-y-0.5 hover:scale-105 ml-4 uppercase"
          >
            {{ talkerUsername }}
          </h1>
          <CloseButton class="mr-5" @openModal="isModal = true" />
        </div>
        <div class="card__message-container mb-2" ref="scrollToMe">
          <div
            v-if="messages.length === 0"
            class="grid place-content-center justify-items-center mt-5"
          >
            <img
              src="https://converseo.s3.eu-central-1.amazonaws.com/no-message.svg"
              class="w-10 h-10"
              alt="No message icon"
            />
            <p class="text-2xl mt-4">No messages yet.</p>
          </div>
          <TransitionGroup name="fade">
            <ChatMessage
              v-for="message in messages"
              :key="message.id"
              :isHost="message.username !== talkerUsername"
              :content="message.content"
              :avatar="talkerAvatar"
            />
          </TransitionGroup>
        </div>

        <div class="card__message-creator">
          <input
            type="text"
            id="message"
            v-model="message"
            placeholder="Type a message..."
            class="h-12 rounded-full text-xl"
          />
          <button
            @click.prevent="sendMessage"
            class="bg-gradient-to-r from-gray-700 to-gray-900 text-stone-50 h-12 ml-4 rounded-full text-center text-uppercase text-2xl"
          >
            Send
          </button>
        </div>
      </div>
    </transition>
  </div>
  <PopupModal
    v-if="isModal"
    @closeModal="isModal = false"
    @closeConversation="closeConversation"
    @keyup.esc="isModal = false"
    :btnMsg="'OK'"
    :header="'Additional confirmation required'"
    :body="'Are you sure you want to delete this conversation?'"
    tabindex="0"
  />
  <PopupModal
    v-if="isModalClosed"
    @closeModal="this.$router.push({ name: 'dashboard' })"
    @keyup.esc="this.$router.push({ name: 'dashboard' })"
    :btnMsg="'OK'"
    :header="'Unable to display conversation'"
    :body="'The conversation was closed by one of the participants'"
    tabindex="0"
  />
  <PopupModal
    v-if="conversationNotFound"
    @closeModal="
      conversationNotFound = this.$router.push({ name: 'dashboard' })
    "
    @keyup.esc="conversationNotFound = this.$router.push({ name: 'dashboard' })"
    :btnMsg="'Back'"
    :bgWhite="true"
    :header="'Unable to display conversation'"
    :body="'The conversation you want to display, does not exist'"
    tabindex="0"
  />
</template>

<script>
import useUserStore from "@/stores/user";
import ChatMessage from "@/components/ChatMessage.vue";
import CloseButton from "@/components/CloseButton.vue";
import PopupModal from "@/components/PopupModal.vue";
import { mapState } from "pinia";

export default {
  name: "Conversation",
  components: {
    ChatMessage,
    CloseButton,
    PopupModal,
  },
  props: ["id"],
  data() {
    return {
      message: "",
      ws: "",
      messages: [],
      talkerUsername: "",
      talkerAvatar: "",
      isModal: false,
      isModalClosed: false,
      conversationNotFound: false,
    };
  },
  computed: {
    ...mapState(useUserStore, ["username"]),
  },
  updated() {
    this.scrollToBottom();
  },
  created() {
    const userStore = useUserStore();
    const ref = this;
    const originName = window.location.origin;
    this.ws = new WebSocket(
      `ws://${originName}/ws/conversations/${this.id}/?token=${userStore.access}`
    );
    this.ws.onmessage = function (e) {
      const data = JSON.parse(e.data);
      if (data.status === "initial") {
        ref.messages = Array.from(JSON.parse(data.messages));
        ref.talkerUsername = JSON.parse(data.talker)["username"];
        ref.talkerAvatar = JSON.parse(data.talker)["avatar"];
      }
      if (data.status === "update") {
        ref.messages.push(data.message);
      }
      if (data.status === "close") {
        ref.isModalClosed = true;
      }
      if (data.status === "not found") {
        ref.conversationNotFound = true;
      }
    };
  },
  methods: {
    async closeConversation() {
      const userStore = useUserStore();
      await this.ws.send(
        JSON.stringify({
          close: true,
          message: "",
          conversation_id: this.id,
          token: userStore.access,
        })
      );
      this.$router.push({ name: "dashboard" });
    },
    async sendMessage() {
      const userStore = useUserStore();
      await this.ws.send(
        JSON.stringify({
          close: false,
          message: this.message,
          conversation_id: this.id,
          token: userStore.access,
        })
      );
      this.message = "";
    },
    scrollToBottom() {
      const objDiv = this.$refs.scrollToMe;
      objDiv.scrollTop = objDiv.scrollHeight;
    },
  },
};
</script>

<style scoped lang="scss">
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.isTalker {
  margin-left: auto;
}

.grid-container {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 0.25fr 1fr 0.25fr;
  justify-content: center;
  align-content: center;
  margin-top: 3rem;
  height: 75vh;
}
.card {
  border-radius: 20px;
  grid-column: 2/3;
  grid-row: 1/2;
  display: grid;
  grid-template-rows: 0.5fr 2fr 0.35fr;
  grid-template-columns: 1fr;
  &__user-header {
    display: flex;
    align-items: center;
    grid-row: 1/2;
    grid-column: 1/2;
    border-bottom: 3px solid #ffffff;
  }

  &__message-container::-webkit-scrollbar {
    width: 12px; /* width of the entire scrollbar */
  }

  &__message-container::-webkit-scrollbar-track {
    background: inherit; /* color of the tracking area */
  }

  &__message-container::-webkit-scrollbar-thumb {
    background-color: #252424; /* color of the scroll thumb */
    border-radius: 30px; /* roundness of the scroll thumb */
    border: 3px solid #262626; /* creates padding around scroll thumb */
  }
  &__message-container {
    padding: 2rem 2rem;
    height: 95%;
    max-height: 25rem;
    overflow-y: auto;
    grid-row: 2/3;
    grid-column: 1/2;
  }
  &__message-creator {
    padding: 0 2rem;
    display: flex;
    input {
      padding: 0 2rem;
      transition: all 0.3s ease-in;
      width: 100%;
      &:focus {
        outline: none;
        transform: scale(1.01);
      }
    }
    button {
      transition: all 0.3s ease-in;
      width: 10rem;
      &:hover {
        transform: scale(1.02);
      }
    }
  }
}
</style>
