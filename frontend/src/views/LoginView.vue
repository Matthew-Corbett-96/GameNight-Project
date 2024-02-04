<script lang="ts" setup>
import Button from '../components/core/Button.vue';
import { useAuthStore } from '../store/auth';
const authStore = useAuthStore();
</script>

<template>
  <div class="login-container">
      <h1 class="login-title">
        WELCOME TO GAME NIGHT
      </h1>
      <Button v-if="!authStore.isLoggedIn" text="Login" @clicked="authStore.Login" />
      <p class="reg-message">Not a User Yet?</p>
      <Button v-if="!authStore.isLoggedIn" text="Register" @clicked="authStore.Register" />
      <Button v-if="authStore.isLoggedIn" text="LogOut" @clicked="authStore.Logout" />
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f2f2f2;
}

.login-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
  text-align: center;
}
</style>