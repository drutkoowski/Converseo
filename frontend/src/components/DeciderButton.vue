<template>
  <button
    class="h-12 w-12 place-content-center grid rounded-md"
    :class="[isAccept ? 'ml-4' : 'mr-4']"
  >
    <svg
      v-if="isAccept"
      xmlns="http://www.w3.org/2000/svg"
      width="3em"
      height="3em"
      fill="white"
      class="bi bi-heart-fill"
      viewBox="0 0 16 16"
    >
      <path
        fill-rule="evenodd"
        d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
      />
    </svg>
    <svg
      v-else
      xmlns="http://www.w3.org/2000/svg"
      width="3em"
      height="3em"
      fill="white"
      class="bi bi-heartbreak-fill"
      viewBox="0 0 16 16"
    >
      <path
        d="M8.931.586 7 3l1.5 4-2 3L8 15C22.534 5.396 13.757-2.21 8.931.586ZM7.358.77 5.5 3 7 7l-1.5 3 1.815 4.537C-6.533 4.96 2.685-2.467 7.358.77Z"
      />
    </svg>
  </button>
</template>

<script>
export default {
  name: "DeciderButton",
  props: ["isAccept"],
};
</script>
