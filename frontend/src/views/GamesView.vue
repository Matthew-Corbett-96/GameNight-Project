<script setup lang="ts">
import { ref, watch, onMounted, type Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import PopupForm from '@/components/core/PopupForm.vue';
import GameCard from '@/components/core/GameCard.vue';
import { type FormField, type Game, type GameFormData } from '@/main';
import { useGameStore } from '@/store/games';

const gameStore = useGameStore();
// Array of games
const games: Ref<Game[]> = ref(gameStore.getGames);

// add watcher to games 
watch(() => gameStore.getGames, (newVal, oldVal) => {
  games.value = newVal;
});

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

// Fetch games from the backend when the component is mounted
onMounted(() => {
  gameStore.fetchGames();
});

// Functions for toggling the create and update game forms
function toggleCreateGameForm() {
  showCreateGameForm.value = !showCreateGameForm.value;
}
function toggleUpdateGameForm() {
  showUpdateGameForm.value = !showUpdateGameForm.value;
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

// Function for deleting a game
function deleteGame(game: Game) {
  gameStore.deleteGame(game);
  gameStore.fetchGames();
}

// Functions for submitting the create and update game forms
function createGame(formData: GameFormData) {
  toggleCreateGameForm();
  gameStore.createGame(formData);
  gameStore.fetchGames();
}

// Function for submitting the update game form
function updateGame(formData: GameFormData) {
  toggleUpdateGameForm();
  gameStore.updateGame(formData);
  gameStore.fetchGames();
}

</script>

<template>
  <h1 class="text-h2 text-center">
    Games
  </h1>

  <section>
    <v-btn @click="toggleCreateGameForm" text="Create Game" block />
  </section>

  <section class="display-games-container">
    <div v-for="game in games" :key="game.id">
      <GameCard :game="game" @delete="deleteGame" @update="openUpdateForm" />
    </div>
  </section>

  <section class="popup-container">
    <PopupForm @submit="createGame" @cancel="toggleCreateGameForm" :show="showCreateGameForm" :title="'Create Game'"
      :form-fields="gameformfields">
    </PopupForm>

    <PopupForm @submit="updateGame" @cancel="toggleUpdateGameForm" :show="showUpdateGameForm" :title="'Update Game'"
      :form-fields="gameformfields" :form-data="gameformdata">
    </PopupForm>
  </section>
</template>

<style scoped>

.display-games-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 1rem;
  margin: 1rem;
  background-color: rgb(180, 181, 181);
}
</style>
