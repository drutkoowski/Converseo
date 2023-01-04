import useUserStore from "@/stores/user";

export default {
  resetToken() {
    localStorage.setItem("isAuthenticated", JSON.stringify(false));
    localStorage.setItem("accessToken", "");
    localStorage.setItem("refreshToken", "");
    useUserStore.isAuthenticated = false;
    useUserStore.access = "";
    useUserStore.refresh = "";
  },
  setToken(access, refresh) {
    useUserStore.isAuthenticated = true;
    useUserStore.refresh = refresh;
    useUserStore.access = access;
    localStorage.setItem("isAuthenticated", JSON.stringify(true));
    localStorage.setItem("accessToken", access);
    localStorage.setItem("refreshToken", refresh);
  },
};
