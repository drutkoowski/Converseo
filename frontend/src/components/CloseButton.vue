<template>
  <div
    class="ml-auto close-btn transition-all hover:scale-105"
    @click.prevent="this.$emit('openModal')"
  >
    &#10006;
  </div>
</template>

<script>
export default {
  name: "CloseButton",
};
</script>

<style>
.close-btn {
  cursor: pointer;
  width: 20px;
}
</style>
