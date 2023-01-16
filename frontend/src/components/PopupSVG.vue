<template>
  <transition name="fade" mode="out-in">
    <div class="modal-mask">
      <div class="modal-wrapper text-center">
        <div class="modal-wrapper__icon-container">
          <object
            class="modal-wrapper__icon-container__icon-animated mx-auto filter-red"
            data="https://converseo.s3.eu-central-1.amazonaws.com/chat-declined.svg"
            type="image/svg+xml"
          ></object>
        </div>

        <h3
          class="text-6xl mt-5 text-stone-50 text-transparent bg-clip-text bg-gradient-to-br from-orange-200 to-red-600"
        >
          Declined :(
        </h3>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "PopupModal",
};
</script>

<style scoped lang="scss">
.filter-red {
  filter: invert(25%) sepia(53%) saturate(4579%) hue-rotate(347deg)
    brightness(112%) contrast(79%);
}

@keyframes spiral {
  0% {
    width: 30rem;
  }
  20% {
    transform: scale(0.95) rotate(0.25turn);
  }
  40% {
    transform: scale(0.85) rotate(0.5turn);
  }
  60% {
    transform: scale(0.75) rotate(0.75turn);
  }
  80% {
    transform: scale(0.65) rotate(1turn);
  }
  100% {
    transform: scale(0.55) rotate(1.25turn);
  }
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
  &-white {
    background-color: rgba(235, 235, 235, 1) !important;
  }
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
  &__icon-container {
    height: 25rem;
    &__icon-animated {
      fill: red !important;
      width: 20rem;
      animation: spiral 2s normal linear;
    }
  }
}

.modal-container {
  width: 40%;
  height: auto;
  margin: 0px auto;
  padding: 20px 10px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  font-size: 1.5rem;
}

.modal-body {
  margin: 2rem 0;
  font-size: 1rem;
}

.modal-default-button {
  float: right;
  margin-bottom: 0.5rem;
}

.fade-enter-from {
  opacity: 0;
}

.fade-enter-active {
  transition: all 0.5s linear;
}

.fade-leave-to {
  transition: all 0.5s linear;
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.modal-footer {
  margin-bottom: 3.5rem;
}
</style>
