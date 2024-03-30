<script setup lang="ts">
import { ref, watch, onMounted, type Ref } from 'vue';
import { type Game, type GameFormData } from '../main';
import { useGameStore } from '../store/games';
import {Button} from '../@/components/ui/button'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '../@/components/ui/dialog'

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

  <Dialog>
    <DialogTrigger as-child>
      <Button variant="outline">
        Add a Game
      </Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Edit profile</DialogTitle>
        <DialogDescription>
          Make changes to your profile here. Click save when you're done.
        </DialogDescription>
      </DialogHeader>
      <div class="grid gap-4 py-4">
        <div class="grid grid-cols-4 items-center gap-4">
          <Label for="name" class="text-right">
            Name
          </Label>
          <Input id="name" value="Pedro Duarte" class="col-span-3" />
        </div>
        <div class="grid grid-cols-4 items-center gap-4">
          <Label for="username" class="text-right">
            Username
          </Label>
          <Input id="username" value="@peduarte" class="col-span-3" />
        </div>
      </div>
      <DialogFooter>
        <Button type="submit">
          Save changes
        </Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>

 
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
