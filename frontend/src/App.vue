<script setup lang="ts">
import { useAuthStore } from './store/auth';
import { RouterView } from 'vue-router';
import { Avatar, AvatarFallback, AvatarImage } from '../src/@/components/ui/avatar'

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
      
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
          <a href="/dashboard" class="flex items-center space-x-3 rtl:space-x-reverse">
            <img src="src\assets\logoo.jpg" class="h-8" alt="Flowbite Logo" />
            <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">GameNight</span>
          </a>
        </div>
        <v-spacer></v-spacer>
        <ul class="flex-grow lg:flex lg:items-center lg:w-auto ">
        <li class="mr-4">
          <a class="inline-block bg-red-500 hover:bg-red-400 text-white font-bold py-2 px-4 border-b-4 border-red-700 hover:border-red-500 rounded"
            href="/dashboard">Dashboard</a>
        </li>
        <li class="mr-4">
          <a class="inline-block bg-gray-500 hover:bg-gray-400 text-white font-bold py-2 px-4 border-b-4 border-gray-700 hover:border-gray-500 rounded"
            href="/games">Games</a>
        </li>
        <li class="mr-4">
          <a class="inline-block bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded"
            v-if="authStore.isLoggedIn" 
            href="/profile">Profile</a>
        </li>
        <li class="mr-4">
          <a class="inline-block bg-yellow-500 hover:bg-yellow-400 text-white font-bold py-2 px-4 border-b-4 border-yellow-700 hover:border-yellow-500 rounded"
            href="/about">About</a>
        </li>
        <li class="mr-4">
          <a class="inline-block bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 border-b-4 border-green-700 hover:border-green-500 rounded"
            v-if="authStore.isLoggedIn" @click="authStore.Logout">Logout</a>
        </li>
        <li class="mr-4">
          <a class="inline-block bg-pink-600 hover:bg-pink-500 text-white font-bold py-2 px-4 border-b-4 border-pink-800 hover:border-pink-600 rounded"
            v-if="!authStore.isLoggedIn" @click="authStore.Login">Login</a>
        </li>
        <li class="mr-4">
          <a class="inline-block bg-purple-700 hover:bg-purple-600 text-white font-bold py-2 px-4 border-b-4 border-purple-900 hover:border-purple-700 rounded"
            v-if="!authStore.isLoggedIn" @click="authStore.Register">Register</a>
        </li>
      </ul>
     
      
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

  </v-app></template>

<style scoped></style>
