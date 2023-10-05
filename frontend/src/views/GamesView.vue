<script setup lang="ts">
import { defineProps } from 'vue';
import { ref } from 'vue';
import type { Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import router from '@/router';
import PopupForm from '@/components/core/PopupForm.vue';

const show: Ref<boolean> = ref(true);

let gameformlables: string[] = [
  'Game Name', 
  'Game Type', 
  'Game Description',
  'Maximum Players',
  'Minimum Players',
]

function toggleCreateGamePopup() {
  show.value = !show.value;
}

</script>

<template>
  <h1>
   Games 
  </h1>
  <div>
    <PopupForm
    @submit="submitform" 
    @close="toggleCreateGamePopup" 
    :show="show"
    :title="'Create Game'"
    :lables="gameformlables">
    </PopupForm>
  </div>
</template>

<style scoped></style>
