<template>
  <transition name="fade" mode="out-in">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div
          class="modal-container bg-gradient-to-r from-gray-700 to-gray-900 text-stone-50"
        >
          <CloseButton @click.prevent="this.$emit('closeModal')" />

          <div
            class="dropbox-container"
            :class="{
              'bg-slate-500': is_dragover,
              'bg-slate-700': !is_dragover,
            }"
            @drag.prevent.stop=""
            @dragstart.prevent.stop=""
            @dragend.prevent.stop="is_dragover = false"
            @dragover.prevent.stop="is_dragover = true"
            @dragenter.prevent.stop="is_dragover = true"
            @dragleave.prevent.stop="is_dragover = false"
            @drop.prevent.stop="upload($event)"
          >
            <label
              class="flex justify-center w-full h-64 px-4 transition rounded-md border-2 border-dashed appearance-none cursor-pointer hover:border-gray-400 focus:outline-none"
            >
              <span class="flex items-center space-x-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6 text-red-500"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                  />
                </svg>
                <span class="font-medium text-red-500" v-if="isUploaded">
                  Drop files to Attach, or
                  <span class="text-red-300 underline">browse</span>
                </span>
                <span class="font-medium text-red-500" v-else>
                  Successfully Uploaded
                </span>
              </span>
              <input
                type="file"
                name="file_upload"
                class="hidden"
                @change="upload"
              />
            </label>
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
  name: "UploadPopup",
  props: ["btnMsg", "header"],
  components: { CloseButton },
  data() {
    return {
      is_dragover: false,
      isUploaded: false,
      uploadFile: "",
    };
  },
  methods: {
    async upload(ev) {
      console.log(ev);
      this.isUploaded = true;
    },
  },
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

.dropbox-container {
  margin: 2rem auto;
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
