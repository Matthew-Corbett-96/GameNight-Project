<script setup lang="ts">
import TopBar from './components/nav/TopBar.vue';
import { RouterView } from 'vue-router';
import CustomFooter from './components/CustomFooter.vue';

</script>

<template>

  <v-app>

    <v-app-bar scroll-behavior="elevate">
      <TopBar />
    </v-app-bar>

    <v-main>
        <RouterView />
    </v-main>

    <v-footer>
      <CustomFooter />
    </v-footer>

  </v-app>

</template>

<style scoped>

</style>
