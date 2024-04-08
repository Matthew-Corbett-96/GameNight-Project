<script setup lang="ts">
import { useAuthStore } from './store/auth';
import { useColorThemeStore } from './store/theme';
import { RouterView } from 'vue-router';
import { Icon } from '@iconify/vue';
import { TooltipProvider, Tooltip, TooltipTrigger, TooltipContent } from './@/components/ui/tooltip';
import { Button } from "./@/components/ui/button";

const links = [
  'About Us',
  'Contact Us',
  'Legal',
  'Privacy Policy',
  'Terms of Use'
]

const authStore = useAuthStore();
const themeStore = useColorThemeStore();
</script>

<template>
  <div >
  <v-app>
    
    <v-app-bar scroll-behavior="elevate">
      
        
      
      <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4 bg-slate-800">
        <a href="/dashboard" class="flex items-center space-x-3 rtl:space-x-reverse">
          <!-- <img src="src\assets\logoo.jpg" class="h-8" alt="Flowbite Logo" /> -->
          <span class="self-center text-2xl tt whitespace-nowrap dark:text-white">GameNight</span>
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
        <li>
          <a class="mr-4 inline-block bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded"
            v-if="authStore.isLoggedIn" href="/profile">Profile</a>
        </li>
        <li>
          <a class="mr-4 inline-block bg-yellow-500 hover:bg-yellow-400 text-white font-bold py-2 px-4 border-b-4 border-yellow-700 hover:border-yellow-500 rounded"
            href="/about">About</a>
        </li>
        <li>
          <a class="mr-4 inline-block bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 border-b-4 border-green-700 hover:border-green-500 rounded"
            v-if="authStore.isLoggedIn" @click="authStore.Logout">Logout</a>
        </li>
        <li>
          <a class="mr-4 inline-block bg-pink-600 hover:bg-pink-500 text-white font-bold py-2 px-4 border-b-4 border-pink-800 hover:border-pink-600 rounded"
            v-if="!authStore.isLoggedIn" @click="authStore.Login">Login</a>
        </li>
        <li class="mr-4">
          <a class="inline-block bg-purple-700 hover:bg-purple-600 text-white font-bold py-2 px-4 border-b-4 border-purple-900 hover:border-purple-700 rounded"
            v-if="!authStore.isLoggedIn" @click="authStore.Register">Register</a>
        </li>
      </ul>

      <TooltipProvider>
        <Tooltip>
          <TooltipTrigger asChild>
            <Button size="icon" variant="icon" @click="themeStore.toggleTheme">
              <Icon icon="radix-icons:sun"
                class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 text-secondary-foreground transition-all dark:-rotate-90 dark:scale-0" />
              <Icon icon="radix-icons:moon"
                class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100 dark:text-primary" />
            </Button>
          </TooltipTrigger>
          <TooltipContent>
            <span>Toggle Theme</span>
          </TooltipContent>
        </Tooltip>
      </TooltipProvider>
      
    </v-app-bar>

    <v-main>
      <RouterView />
    </v-main>

    <v-footer class="bg-grey-lighten-1">
      <v-row justify="center" no-gutters>
        <Button v-for="link in links" :key="link" variant="link" class="mx-2">
          {{ link }}
        </Button>
        <v-col class="text-center mt-4" cols="12" md="8" sm="4">
          {{ new Date().getFullYear() }} — <strong>White Fence Gang LLC</strong>
        </v-col>
      </v-row>
    </v-footer>

  </v-app>
  </div>
  </template>

<style scoped>
.tt {
  /* color: #fff; */
  font-family: 'Lato', sans-serif;
  text-align: center;
  /* font-size: 0.8rem; */
  line-height: 150%;
  letter-spacing: 2px;
  text-transform: uppercase;
}
</style>
