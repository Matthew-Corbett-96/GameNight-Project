// Pinia store for color theme
import { defineStore } from 'pinia'
import { useColorMode } from '@vueuse/core';

export const useColorThemeStore = defineStore(
   'theme', () => {

      const mode = useColorMode();

      function toggleTheme(): void {
         mode.value = mode.value === 'dark' ? 'light' : 'dark';
      }

      return { toggleTheme };
   },
   {
      persist: true
   }
);