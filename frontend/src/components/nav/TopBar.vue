<script setup lang="ts">
import { useAuthStore } from '@/store/auth';

const authStore = useAuthStore();

function login() {
   authStore.Login();
}

function logout() {
   authStore.Logout();
}

function register() {
   authStore.Register();
}

</script>

<template>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>Game Night</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn variant="text" v-if="authStore.isLoggedIn" to="/games">Games</v-btn>
      <v-btn variant="text" v-if="authStore.isLoggedIn" to="/profile">Profile</v-btn>
      <v-btn variant="text" v-if="authStore.isLoggedIn" @click="logout">Logout</v-btn>
      <v-btn variant="text" v-if="!authStore.isLoggedIn" @click="login">Login</v-btn>
      <v-btn variant="text" v-if="!authStore.isLoggedIn" @click="register">Register</v-btn>
      <v-btn variant="text" v-if="authStore.isLoggedIn" to="/about">About</v-btn>
</template>