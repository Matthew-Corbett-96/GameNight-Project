<script setup lang="ts">
import Navigation from '@/components/Navigation.vue';
import SettingNav from '@/components/SettingsNav.vue';

</script>

<template>
   <header>
      <div class="wrapper">
         <Navigation />
         <SettingNav/>
      </div>
   </header>
</template>

<style scoped>
.wrapper {
   max-width: 100vw;
   margin: 0 auto 1rem auto;
   padding: 0;
   display: grid;
   grid-template-columns: 10fr 1fr;
}

</style>