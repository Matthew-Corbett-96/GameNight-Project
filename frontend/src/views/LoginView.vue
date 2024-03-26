<script lang="ts" setup>
import { Button } from '../@/components/ui/button';
import { useAuthStore } from '../store/auth';
const authStore = useAuthStore();
</script>

<template>
  <div class="bg-background flex flex-col items-center justify-center login-container">
    <h1 class="login-title">
      WELCOME TO GAME NIGHT
    </h1>
    <Button v-if="!authStore.isLoggedIn" @click="authStore.Login" >
      Login
    </Button>
    <p class="reg-message">Not a User Yet?</p>
    <Button v-if="!authStore.isLoggedIn"  @click="authStore.Register" > 
      Register
    </Button>
    <Button v-if="authStore.isLoggedIn"  @click="authStore.Logout" >
      Logout
    </Button>
  </div>
</template>

<style scoped>
.login-container {
  height: 100vh;
}

.login-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
  text-align: center;
}
</style>