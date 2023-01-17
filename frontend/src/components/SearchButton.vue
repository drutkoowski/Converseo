<template>
  <div
    class="flex flex-col justify-center mt-48 transition-all items-center"
    :class="[!isSearching ? 'bounce-light' : '']"
  >
    <div
      v-if="isTalkerFound"
      class="h-40 w-40 bg-red-600 rounded-full flex justify-center items-center cursor-pointer transition-all hover:scale-105 bounce-light"
    >
      <img
        :src="talkerAvatarPath"
        alt="Avatar"
        class="rounded-full outline outline-offset-2 align-text-bottom transition-all hover:-translate-y-0.5 hover:scale-105 user-avatar"
      />
    </div>
    <div
      v-else
      class="h-40 w-40 bg-red-600 rounded-full flex justify-center items-center cursor-pointer transition-all hover:scale-105"
      :class="[isSearching ? 'animation-pulse' : '']"
      @click.prevent="toggleSearch"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="5em"
        height="5em"
        fill="currentColor"
        class="bi bi-chat-dots"
        viewBox="0 0 16 16"
        v-if="!isSearching"
      >
        <path
          d="M5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
        />
        <path
          d="m2.165 15.803.02-.004c1.83-.363 2.948-.842 3.468-1.105A9.06 9.06 0 0 0 8 15c4.418 0 8-3.134 8-7s-3.582-7-8-7-8 3.134-8 7c0 1.76.743 3.37 1.97 4.6a10.437 10.437 0 0 1-.524 2.318l-.003.011a10.722 10.722 0 0 1-.244.637c-.079.186.074.394.273.362a21.673 21.673 0 0 0 .693-.125zm.8-3.108a1 1 0 0 0-.287-.801C1.618 10.83 1 9.468 1 8c0-3.192 3.004-6 7-6s7 2.808 7 6c0 3.193-3.004 6-7 6a8.06 8.06 0 0 1-2.088-.272 1 1 0 0 0-.711.074c-.387.196-1.24.57-2.634.893a10.97 10.97 0 0 0 .398-2z"
        />
      </svg>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="5em"
        height="5em"
        fill="currentColor"
        class="bi bi-search"
        viewBox="0 0 16 16"
        v-if="isSearching"
      >
        <path
          d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
        />
      </svg>
    </div>
    <p class="mt-2 text-stone-50 text-xl" v-if="isTalkerFound">
      {{ talkerUsername }}
    </p>
    <h3
      class="text-center mt-10 text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer text-3xl transition-all hover:-translate-y-0.5 hover:scale-105 ml-1"
    >
      {{ lowerSearchMsg }}
    </h3>
    <div class="flex mt-4" v-if="isTalkerFound">
      <DeciderButton :is-accept="false" @userChoice="sendChoice" />
      <DeciderButton :is-accept="true" @userChoice="sendChoice" />
    </div>
  </div>
  <PopupSVG
    v-if="isDeclined"
    @animationEnd="isDeclined = false"
    svgSrc="https://converseo.s3.eu-central-1.amazonaws.com/chat-declined.svg"
    msg="'Declined'"
  />
  <PopupSVG
    v-if="isMatched"
    @animationEnd="isMatched = false"
    svgSrc="https://converseo.s3.eu-central-1.amazonaws.com/puzzle.svg"
    msg="'Matched'"
  />
</template>

<script>
import DeciderButton from "./DeciderButton.vue";
import PopupSVG from "./PopupSVG.vue";
import useUserStore from "@/stores/user";

export default {
  name: "SearchButton",
  components: {
    DeciderButton,
    PopupSVG,
  },
  data() {
    return {
      isSearching: false,
      isTalkerFound: false,
      talkerUsername: "",
      talkerAvatarPath: "",
      matchId: "",
      talkerId: "",
      lowerSearchMsg: "Search Converseo",
      ws: "",
      isDeclined: false,
      isMatched: false,
    };
  },
  methods: {
    clearSearch() {
      this.isSearching = !this.isSearching;
      this.isTalkerFound = false;
      this.talkerUsername = "";
      this.talkerAvatarPath = "";
      this.matchId = "";
      this.queueId = "";
      this.lowerSearchMsg = this.isSearching
        ? "Searching..."
        : "Search Converseo";
    },
    fillSearchInfo(username, avatarPath, matchId, talkerId) {
      this.isSearching = !this.isSearching;
      this.isTalkerFound = true;
      this.talkerUsername = username;
      this.talkerAvatarPath = avatarPath;
      this.matchId = matchId;
      this.talkerId = talkerId;
      this.lowerSearchMsg = "You found someone!";
    },
    async toggleSearch() {
      this.clearSearch();
      this.lowerSearchMsg = this.isSearching
        ? "Searching..."
        : "Search Converseo";
      const userStore = useUserStore();
      const ws = new WebSocket(
        `ws://127.0.0.1:8000/ws/queue/?token=${userStore.access}`
      );
      this.ws = ws;
      if (this.isSearching) {
        const ref = this;
        ws.onmessage = function (e) {
          const data = JSON.parse(e.data);
          const matchId = data.random_talker.matchId;
          const talkerId = data.random_talker.talkerId;
          const randomTalker = data.random_talker.random_talker;
          const subject = data.random_talker.subject;
          if (subject === "found") {
            ref.fillSearchInfo(
              randomTalker.username,
              randomTalker.avatar,
              matchId,
              talkerId
            );
          } else if (subject === "declined") {
            ref.isSearching = true;
            ref.clearSearch();
            ref.isDeclined = true;
          }
        };
      } else {
        ws.close(1000);
      }
    },
    async sendChoice(evt, choice) {
      const userStore = useUserStore();
      const router = this.$router;
      const ref = this;
      await ref.ws.send(
        JSON.stringify({
          choice: choice,
          matchId: this.matchId,
          talkerId: this.talkerId,
          token: userStore.access,
        })
      );
      if (choice === false) {
        this.isSearching = true;
        this.clearSearch();
      }
      ref.ws.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const subject = data.random_talker.subject;
        const roomId = data.random_talker.room_id;
        if (subject === "matched") {
          ref.isMatched = true;
          ref.ws.close(1000);
          setTimeout(() => {
            router.push({
              name: "conversation",
              params: { conversation_id: roomId },
            });
          }, 2000);
        } else if (subject === "declined") {
          ref.isSearching = true;
          ref.clearSearch();
          ref.isDeclined = true;
        }
      };
    },
  },
};
</script>

<style scoped>
.bounce-light {
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateY(-5%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}

.animation-pulse {
  /*box-shadow: 0 0 0 20px rgba(229, 62, 62, 0.5);*/
  /*transform: scale(0.8);*/
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(0.8);
    box-shadow: 0 0 0 0 rgba(229, 62, 62, 1);
  }

  70% {
    transform: scale(1);
    box-shadow: 0 0 0 60px rgba(229, 62, 62, 0);
  }

  100% {
    transform: scale(0.8);
  }
}
.user-avatar {
  height: 100%;
  width: 100%;
}
</style>
