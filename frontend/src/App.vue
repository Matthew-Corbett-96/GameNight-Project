<script setup lang="ts">
import TopBar from './components/nav/TopBar.vue';
import { RouterView } from 'vue-router';
import CustomFooter from './components/CustomFooter.vue';

</script>

<template>
  <div class="page-container">
    <TopBar />
    <main>
      <RouterView />
    </main>
    <CustomFooter />
  </div>
</template>

<style scoped>
.page-container {
  display: grid;
  grid-template-rows: 1fr 10fr 1fr;
}
</style>
