<script setup lang="ts">
import { defineProps } from 'vue';
import { ref } from 'vue';
import type { Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import router from '@/router';
import PopupForm from '@/components/core/PopupForm.vue';

const show: Ref<boolean> = ref(true);

let gameformfields = [
  { label: 'Name', type: 'text' },
  { label: 'Description', type: 'text' },
  { label: 'Min Players', type: 'number' },
  { label: 'Max Players', type: 'number' }
];

function toggleCreateGamePopup() {
  show.value = !show.value;
}

function submitform(formData: any) {

  let headers = new Headers();
  headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');
  headers.append('Origin', 'http://localhost:3000');

  fetch('http://localhost:5000/games/', {
    method: 'POST',
    mode: 'cors',
    headers: headers,
    body: JSON.stringify({
      name: formData['Name'],
      description: formData['Description'],
      min_players: formData['Min Players'],
      max_players: formData['Max Players']
    })
  })
    .then(response => response.json())
    .then(data => {
      if (data.status === 200) {
        console.log('Game created successfully.');
        console.log(data);
      } else {
        console.log(data);
      }
    })
    .catch(error => {
      console.log('Error:', error);
    })
    .finally(() => {
      toggleCreateGamePopup();
    });
}

</script>

<template>
  <h1>
   Games 
  </h1>
  <div>
    <PopupForm
    @submit="submitform" 
    @cancel="toggleCreateGamePopup" 
    :show="show"
    :title="'Create Game'"
    :form-fields="gameformfields">
    </PopupForm>
  </div>
</template>

<style scoped></style>
