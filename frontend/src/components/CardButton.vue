<template>
  <button
    type="submit"
    class="w-full font-semibold block h-20 bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer uppercase text-stone-50 text-lg rounded-md transition-all hover:-translate-y-0.5 hover:scale-0.5"
  >
    {{ text }}
  </button>
</template>

<script>
export default {
  name: "CardButton",
  props: ["text"],
};
</script>
