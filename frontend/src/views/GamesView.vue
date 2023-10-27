<script setup lang="ts">
import { ref } from 'vue';
import type { Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import PopupForm from '@/components/core/PopupForm.vue';
import { onMounted } from 'vue';
import { type FormData, type FormField, type Game, type GameFormData } from '@/main';
import GameCard from '@/components/core/GameCard.vue';

// Array of games
const games: Ref<Game[]> = ref([]);

// Toggles for showing/hiding the create and update game forms
const showCreateGameForm: Ref<boolean> = ref(false);
const showUpdateGameForm: Ref<boolean> = ref(false);

// Form fields and data for the create and update game forms
const gameformfields: FormField[] = [
  { label: 'name', type: 'text' },
  { label: 'description', type: 'text' },
  { label: 'min_players', type: 'number' },
  { label: 'max_players', type: 'number' }
];

// Form data for the create and update game forms
const gameformdata: Ref<GameFormData> = ref({
  name: '',
  description: '',
  min_players: 0,
  max_players: 0
});

const error: Ref<boolean> = ref(false);
const error_message: Ref<string> = ref('');

// Fetch games from the backend when the component is mounted
onMounted(() => {
  fetchGames();
});

// Functions for fetching games from the backend
function fetchGames(): void {
  fetch('http://localhost:5000/games/')
    .then(response => response.json())
    .then(data => {
      if (data.status === 200) {
        console.log('Games fetched successfully.');
        console.log(data);
        games.value = data.data.games;
      } else {
        console.log(data);
      }
    })
    .catch(error => {
      console.log('Error:', error);
    });
}
// Functions for toggling the create and update game forms
function toggleCreateGameForm() {
  showCreateGameForm.value = !showCreateGameForm.value;
}
function toggleUpdateGameForm() {
  showUpdateGameForm.value = !showUpdateGameForm.value;
}

// Function for deleting a game
function deleteGame(game: Game) {
  let headers = new Headers();
  headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');
  headers.append('Origin', 'http://localhost:3000');

  fetch('http://localhost:5000/games/' + game.id, {
    method: 'DELETE',
    mode: 'cors',
    headers: headers
  })
    .then(response => response.json())
    .then(data => {
      if (data.status === 200) {
        console.log(data);
      } else {
        error_message.value = data.message;
        error.value = true;
      }
    })
    .catch(error => {
      error_message.value = error.message;
      error.value = true;
    })
    .finally(() => {
      fetchGames();
    });
}

// Function for opening the update game form
function openUpdateForm(game: Game) {
  gameformdata.value = {
    name: game.name,
    description: game.description,
    min_players: game.min_players,
    max_players: game.max_players
  };
  toggleUpdateGameForm();
}

// Functions for submitting the create and update game forms
function createGame(formData: GameFormData) {

  let headers = new Headers();
  headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');
  headers.append('Origin', 'http://localhost:3000');

  fetch('http://localhost:5000/games/', {
    method: 'POST',
    mode: 'cors',
    headers: headers,
    body: JSON.stringify({
      name: formData['name'],
      description: formData['description'],
      min_players: formData['min_players'],
      max_players: formData['max_players']
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
      toggleCreateGameForm();
      fetchGames();
    });
}

// Function for submitting the update game form
function updateGame(formData: GameFormData) {

  let headers = new Headers();
  headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');
  headers.append('Origin', 'http://localhost:3000');

  let id = games.value.find(game => game.name === gameformdata.value.name)?.id;

  if (id === undefined) {
    console.log('Error: Game not found.');
    error_message.value = 'Error: Game not found.';
    error.value = true;
    return;
  }

  fetch('http://localhost:5000/games/' + id, {
    method: 'PUT',
    mode: 'cors',
    headers: headers,
    body: JSON.stringify({
      name: formData['name'],
      description: formData['description'],
      min_players: formData['min_players'],
      max_players: formData['max_players']
    })
  })
    .then(response => response.json())
    .then(data => {
      if (data.status === 200) {
        console.log(data);
      } else {
        console.log(data);
        error_message.value = data.message;
        error.value = true;
      }
    })
    .catch(error => {
      error_message.value = error.message;
      error.value = true;
    })
    .finally(() => {
      toggleUpdateGameForm();
      fetchGames();
    });
}

</script>

<template>

  <h1>
    Games
  </h1>

  <section>
    <Button @clicked="toggleCreateGameForm" :text="'Create Game'" />
  </section>

  <section class="display-games-container">
    <div v-for="game in games" :key="game.id">
      <GameCard :game="game" @delete="deleteGame" @update="openUpdateForm" />
    </div>
  </section>

  <section class="popup-container">
    <PopupForm @submit="createGame" @cancel="toggleCreateGameForm" :show="showCreateGameForm"
      :title="'Create Game'" :form-fields="gameformfields">
    </PopupForm>

    <PopupForm @submit="updateGame" @cancel="toggleUpdateGameForm" :show="showUpdateGameForm"
      :title="'Update Game'" :form-fields="gameformfields" :form-data="gameformdata">
    </PopupForm>
  </section>

</template>

<style scoped>
h1 {
  text-align: center;
}

.display-games-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 1rem;
  margin: 1rem;
  background-color: rgb(180, 181, 181);
}

</style>
