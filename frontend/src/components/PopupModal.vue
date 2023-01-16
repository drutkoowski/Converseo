<template>
  <transition name="fade" mode="out-in">
    <div
      class="modal-mask"
      @click="this.$emit('closeModal')"
      :class="{ 'modal-mask-white': bgWhite }"
    >
      <div class="modal-wrapper">
        <div
          class="modal-container bg-gradient-to-r from-gray-700 to-gray-900 text-stone-50"
        >
          <CloseButton @click.prevent="this.$emit('closeModal')" />
          <div class="modal-header">
            <h3 class="text-red-500">{{ header }}</h3>
          </div>

          <div class="modal-body">
            <p>{{ body }}</p>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button
                class="modal-default-button mb-4 w-24 rounded-full transition-all bg-gradient-to-r hover:scale-105 from-orange-200 to-red-600 cursor-pointer"
                @click.prevent="this.$emit('closeConversation')"
              >
                {{ btnMsg }}
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import CloseButton from "./CloseButton.vue";
export default {
  name: "PopupModal",
  props: ["header", "body", "bgWhite", "btnMsg"],
  components: { CloseButton },
  created() {
    document.onkeydown = (evt) => {
      evt = evt || window.event;
      if (evt.keyCode == 27) {
        this.$emit("closeModal");
      }
    };
  },
};
</script>

<style scoped lang="scss">
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
