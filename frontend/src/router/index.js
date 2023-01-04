import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import SignupView from "@/views/SignupView.vue";
import DashboardView from "@/views/DashboardView.vue";
import TestView from "@/views/TestView.vue";

import useUserStore from "@/stores/user";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/",
      name: "dashboard",
      component: DashboardView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/test",
      name: "test",
      component: TestView,
      meta: {
        requiresAuth: true,
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (!to.meta.requiresAuth) {
    next();
    return;
  }
  if (
    useUserStore.isAuthenticated ||
    JSON.parse(localStorage.getItem("isAuthenticated"))
  ) {
    const store = useUserStore();
    store.refreshToken();
    next();
  } else {
    next({ name: "login" });
  }
});

export default router;
