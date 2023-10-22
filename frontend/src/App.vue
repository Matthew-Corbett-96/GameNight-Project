<script setup lang="ts">
import TopBar from './components/nav/TopBar.vue';
import { RouterView } from 'vue-router';
import CustomFooter from './components/CustomFooter.vue';
import { useAuthStore } from './store/auth';

const authStore = useAuthStore();

</script>

<template>
  <div class="page-container">
    <TopBar v-if="authStore.isLoggedIn" />
    <main>
      <RouterView />
    </main>
    <CustomFooter v-if="authStore.isLoggedIn" />
  </div>
</template>

<style scoped>
.page-container {
  display: grid;
  grid-template-rows: 1fr 10fr 1fr;
}
</style>
