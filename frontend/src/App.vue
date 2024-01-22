<script setup lang="ts">
import { useAuthStore } from '@/store/auth';
import { RouterView } from 'vue-router';

const links = [
  'About Us',
  'Contact Us',
  'Legal',
  'Privacy Policy',
  'Terms of Use'
]

const authStore = useAuthStore();

</script>

<template>
  <v-app>

    <v-app-bar scroll-behavior="elevate">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>Game Night</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn variant="text" v-if="authStore.isLoggedIn" to="/games">Games</v-btn>
      <v-btn variant="text" v-if="authStore.isLoggedIn" to="/profile">Profile</v-btn>
      <v-btn variant="text" v-if="authStore.isLoggedIn" to="/about">About</v-btn>
      <v-btn variant="text" v-if="authStore.isLoggedIn" @click="authStore.Logout">Logout</v-btn>
      <v-btn variant="text" v-if="!authStore.isLoggedIn" @click="authStore.Login">Login</v-btn>
      <v-btn variant="text" v-if="!authStore.isLoggedIn" @click="authStore.Register">Register</v-btn>

    </v-app-bar>

    <v-main>
      <RouterView />
    </v-main>

    <v-footer class="bg-grey-lighten-1">
      <v-row justify="center" no-gutters>
        <v-btn v-for="link in links" :key="link" color="primary" variant="text" class="mx-2" rounded="xl">
          {{ link }}
        </v-btn>
        <v-col class="text-center mt-4" cols="12" md="8" sm="4">
          {{ new Date().getFullYear() }} — <strong>White Fence Gang LLC</strong>
        </v-col>
      </v-row>
    </v-footer>

  </v-app>
</template>

<style scoped></style>
