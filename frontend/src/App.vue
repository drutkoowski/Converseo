<template>
  <router-view v-slot="{ Component, route }">
    <transition name="fade" mode="out-in">
      <div :key="route.name">
        <component :key="route.name" :is="Component"></component>
      </div>
    </transition>
  </router-view>
</template>

<script></script>

<style scoped>
body {
  overflow: hidden;
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
</style>
