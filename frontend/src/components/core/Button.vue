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

<template >
   <div class="button-container">
      <v-btn color="primary" @click="emit('clicked')"> {{ text }} </v-btn>
   </div>
</template>

<style scoped>

.button-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>