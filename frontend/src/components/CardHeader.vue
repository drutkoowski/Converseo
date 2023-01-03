<template>
  <h2
    class="text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600 cursor-pointer text-6xl text-center"
  >
    {{ msg }}
  </h2>
</template>

<script>
export default {
  name: "CardHeader",
  props: ["msg"],
};
</script>
