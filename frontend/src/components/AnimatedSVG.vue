<template>
  <object
    class="modal-wrapper__icon-container__icon-animated mx-auto filter-red"
    :data="data"
    type="image/svg+xml"
  ></object>
</template>

<script>
export default {
  name: "AnimatedSVG",
  props: ["data", "type"],
};
</script>

<style scoped>
.filter-red {
  filter: invert(25%) sepia(53%) saturate(4579%) hue-rotate(347deg)
    brightness(112%) contrast(79%);
}

@keyframes spiral {
  0% {
    width: 30rem;
  }
  10% {
    transform: scale(0.95) rotate(0.25turn);
  }
  30% {
    transform: scale(0.85) rotate(0.5turn);
  }
  50% {
    transform: scale(0.65) rotate(0.75turn);
  }
  60% {
    transform: scale(0.55) rotate(1turn);
  }
  75% {
    transform: scale(0.45) rotate(1.25turn);
  }
  90% {
    transform: scale(0.35) rotate(1.5turn);
  }
  100% {
    transform: scale(0.25) rotate(1.75turn);
  }
}
object {
  fill: red !important;
  width: 20rem;
  animation: spiral 2s normal linear;
}
</style>
