<script setup lang="ts">
import SettingIcon from '@/components/icons/SettingsIcon.vue';
import { ref } from 'vue';
import type { Ref } from 'vue';
import { RouterLink } from 'vue-router';

const openPanel: Ref<boolean> = ref(false);

function togglePanel(): void {
   openPanel.value = !openPanel.value;
}

</script>

<template>

   <div class="setting-container">
      <SettingIcon @click="togglePanel()" />
      <div v-if="openPanel" class="overlay" >
         <nav class="panel">
            <div class="place-holder"></div>
            <ul class="setting-nav">
               <li @click="togglePanel()" class="setting-item">
                  <RouterLink to="/settings" > Settings </RouterLink>
               </li>
               <li @click="togglePanel()" class="setting-item">
                  <RouterLink to="/profile" > Profile </RouterLink>
               </li>
               <li @click="togglePanel()" class="setting-item">
                  <RouterLink to="/login" > Logout </RouterLink>
               </li>
               <li class=" setting-item btn">
                  <div @click="togglePanel()" class="close-btn">X</div>
               </li>
            </ul>
         </nav>
      </div>
   </div>

</template>

<style scoped>
.overlay {
   position: absolute;
   height: 100%;
   width: 100%;
   background-color: rgba(0, 0, 0, 0.5);
   top: 0;
   left: 0;
   margin: 0;
   z-index: 10;
}
.panel {
   margin: 0 0 10px 10px;
   z-index: 11;
   display: grid;
   grid-template-columns: 90% 10%;
}

.setting-nav {
   display: flex;
   flex-direction: column;
   justify-items: stretch;
   list-style: none;
   margin: 0;
   padding: 0;
   color: black;
   width: auto;
   height: auto;
}

.setting-item {
   color: black;
   text-decoration: none;
   font-weight: bold;
   padding: 1rem 2rem;
   background-color: aqua;
}

.setting-item:hover {
   color: #ccccccf9;
   background-color: aquamarine;
}

nav .setting-item:active {
   color: #d11515;
}

.setting-item.btn {
   border-radius: 0 0 0 15px;
}

.close-btn {
   font-size: 1.5rem;
   font-weight: bold;
   color: #333;
   cursor: pointer;
   text-align: center;
}
</style>