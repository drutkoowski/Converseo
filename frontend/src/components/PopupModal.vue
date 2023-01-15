<template>
  <transition name="modal">
    <div class="modal-mask" @keyup.esc="this.$emit('closeModal')">
      <div class="modal-wrapper">
        <div
          class="modal-container bg-gradient-to-r from-gray-700 to-gray-900 text-stone-50"
        >
          <CloseButton @click.prevent="this.$emit('closeModal')" />
          <div class="modal-header">
            <slot name="header"> {{ header }} </slot>
          </div>

          <div class="modal-body">
            <slot name="body"> {{ body }}</slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button
                class="modal-default-button mb-4 w-24 rounded-full transition-all bg-gradient-to-r hover:scale-105 from-orange-200 to-red-600 cursor-pointer"
              >
                OK
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
  props: ["header", "body"],
  components: { CloseButton },
};
</script>

<style scoped>
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
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 40%;
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
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.modal-footer {
  margin-bottom: 2.5rem;
}
</style>
