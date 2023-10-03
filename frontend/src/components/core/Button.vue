<script setup lang="ts" emits="clicked">
import { defineProps } from 'vue';

// get value from parent component
const props = defineProps({
  text: {
    type: String,
    default: '',
    required: false
  }
});

const emit = defineEmits(['clicked']);

</script>

<template>
   <div class="button-container">
      <button class="button" @click="emit('clicked')"> {{ text }} </button>
   </div>
</template>

<style scoped>

.button-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  background-color: #0077cc;
  color: #fff;
  font-size: 1.2rem;
  cursor: pointer;
}

.button:hover {
  background-color: #005fa3;
}

</style>