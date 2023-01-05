<template>
  <div
    class="flex flex-col justify-center mt-48 transition-all bounce-light items-center"
  >
    <div
      class="h-40 w-40 bg-red-600 rounded-full flex justify-center items-center cursor-pointer transition-all hover:scale-105"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="5em"
        height="5em"
        fill="currentColor"
        class="bi bi-chat-dots"
        viewBox="0 0 16 16"
      >
        <path
          d="M5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"
        />
        <path
          d="m2.165 15.803.02-.004c1.83-.363 2.948-.842 3.468-1.105A9.06 9.06 0 0 0 8 15c4.418 0 8-3.134 8-7s-3.582-7-8-7-8 3.134-8 7c0 1.76.743 3.37 1.97 4.6a10.437 10.437 0 0 1-.524 2.318l-.003.011a10.722 10.722 0 0 1-.244.637c-.079.186.074.394.273.362a21.673 21.673 0 0 0 .693-.125zm.8-3.108a1 1 0 0 0-.287-.801C1.618 10.83 1 9.468 1 8c0-3.192 3.004-6 7-6s7 2.808 7 6c0 3.193-3.004 6-7 6a8.06 8.06 0 0 1-2.088-.272 1 1 0 0 0-.711.074c-.387.196-1.24.57-2.634.893a10.97 10.97 0 0 0 .398-2z"
        />
      </svg>
    </div>
    <h3
      class="text-center mt-10 text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer text-3xl transition-all hover:-translate-y-0.5 hover:scale-105"
    >
      Search Converseo
    </h3>
  </div>
</template>

<script>
export default {
  name: "SearchButton",
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
  /*box-shadow: 0 0 0 20px rgba(229,62,62, 0.5);
    transform: scale(0.8);*/
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
</style>
