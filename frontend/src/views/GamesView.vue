<script setup lang="ts">
import { ref, watch, onMounted, type Ref } from 'vue';
import { type Game, type GameFormData } from '../main';
import { useGameStore } from '../store/games';
import {Button} from '../@/components/ui/button'

const dialog = ref(false);
const gameStore = useGameStore();
// Array of games
const games: Ref<Game[]> = ref(gameStore.getGames);

// add watcher to games 
watch(() => gameStore.getGames, (newVal, oldVal) => {
  games.value = newVal;
});

// Form data for the create and update game forms
const gameformdata: Ref<GameFormData> = ref({
  name: '',
  description: '',
  min_players: 0,
  max_players: 0,
});

// Fetch games from the backend when the component is mounted
onMounted(() => {
  gameStore.fetchGames();
});


// Function for opening the update game form
function openUpdateForm(game: Game) {
  gameformdata.value = {
    name: game.name,
    description: game.description,
    min_players: game.min_players,
    max_players: game.max_players
  };
}

// Function for deleting a game
function deleteGame(game: Game) {
  gameStore.deleteGame(game);
  gameStore.fetchGames();
}

// Functions for submitting the create and update game forms
function createGame() {
  dialog.value = false;
  gameStore.createGame(gameformdata.value);
  gameStore.fetchGames();
}

// Function for submitting the update game form
function updateGame(formData: GameFormData) {
  gameStore.updateGame(formData);
  gameStore.fetchGames();
}

</script>

<template>
  <h1 class="text-h2 text-center mb-36"> Games </h1>

  <v-row justify="center">
    <v-dialog v-model="dialog" persistent width="1024" transition="dialog-bottom-transition">

      <template v-slot:activator="{ props }">
        <Button v-bind="props">Create Game</Button>
      </template>

      <v-card>
        <v-card-title>
          <span class="text-h5">Create Game</span>
        </v-card-title>

        <v-card-text>
          <v-container>

            <!-- Row 1 -->
            <v-row>
              <!-- <form @submit.prevent="createGame"> -->
              <v-col cols="12" sm="6" md="4">
                <v-text-field 
                v-model="gameformdata.name" 
                label="Name"
                hint="example of helper text only on focus"
                />
              </v-col>

              <v-col cols="12" sm="6" md="4">
                <v-text-field 
                v-model="gameformdata.description" 
                label="Discription" 
                hint="Be creative" 
                persistent-hint
                required
                />
              </v-col>
            </v-row>

            <!-- Row 2 -->
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-select 
                v-model="gameformdata.min_players" 
                :items="[1, 2, 3, 4, 5]" 
                label="min_players"
                required
                />
              </v-col>

              <v-col cols="12" sm="6" md="4">
                <v-select 
                v-model="gameformdata.max_players" 
                :items="[1, 2, 3, 4, 5]" 
                label="max_players"
                required
                />
              </v-col>
            </v-row>
            <!-- </form> -->

          </v-container>

          <small>*indicates required field</small>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <Button color="blue-darken-1" variant="default" @click="dialog = false">
            Close
          </Button>
          <Button color="blue-darken-1" variant="default" @click="createGame">
            Submit
          </Button>
        </v-card-actions>

      </v-card>
    </v-dialog>
  </v-row>
</template>

<style scoped>
.display-games-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 1rem;
  margin: 1rem;
  background-color: rgb(180, 181, 181);
}

.v-row {
  justify-content: center;
}
</style>
