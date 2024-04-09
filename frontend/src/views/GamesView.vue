<script setup lang="ts">
import { ref, watch, onMounted, type Ref } from 'vue';
import { type Game, type GameFormData } from '../main';
import { useGameStore } from '../store/games';
import zod from 'zod';
import { toTypedSchema } from '@vee-validate/zod';
import { Button } from '../@/components/ui/button';
import { Input } from '../@/components/ui/input';
import { Label } from '../@/components/ui/label';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger
} from '../@/components/ui/dialog';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '../@/components/ui/card';
import { useForm } from 'vee-validate';
import { DialogClose } from 'radix-vue';
import {
  FormField,
  FormControl,
  FormDescription,
  FormMessage,
  FormLabel,
  FormItem,
  Form
} from '../@/components/ui/form';
import { GameCard } from '../@/components/gamenight/gameCard';

const dialog = ref(false);
const gameStore = useGameStore();
// Array of games
const games: Ref<Game[]> = ref(gameStore.getGames);

// add watcher to games 
watch(() => gameStore.getGames, (newVal, oldVal) => {
  games.value = newVal;
});

// Fetch games from the backend when the component is mounted
onMounted(() => {
  gameStore.fetchGames();
});


// schema for game form 
const schema = toTypedSchema(zod.object({
  name: zod.string().min(2).max(50),
  description: zod.string().min(2).max(50),
  min_players: zod.number().min(1).max(5),
  max_players: zod.number().min(1).max(5),
}));

// form variable for game creation and update
const form = useForm({
  validationSchema: schema
});

// function to submit form
const onSubmit = form.handleSubmit((values) => {
  console.log('Form submitted!', values);
});

// Form data for the create and update game forms
const gameformdata: Ref<GameFormData> = ref({
  name: '',
  description: '',
  min_players: 0,
  max_players: 0,
} as GameFormData);


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
  clearForm();
}

// Function for submitting the update game form
function updateGame(formData: GameFormData) {
  dialog.value = false;
  gameStore.updateGame(formData);
  gameStore.fetchGames();
}

//clear form data
function clearForm() {
  form.resetForm();
}

</script>

<template>
  <div class="bg-slate-800 min-h-screen">
    <h1 class="text-h2 text-center mb-15"> Games </h1>

    <!-- create Game -->
    <Dialog class="items-center flex space-x-2">
      <div class="flex items-center justify-center">
        <DialogTrigger asChild>
          <Button variant="default" class="hover:bg-blue-500 hover:text-white">Create Game</Button>
        </DialogTrigger>
      </div>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Create Game</DialogTitle>
          <DialogDescription>
            Make changes to game here. Click save when you're done.
          </DialogDescription>
        </DialogHeader>
        <DialogBody>
          <form @submit="onSubmit">
            <FormField v-slot="{ componentField }" name="name">
              <FormItem>
                <FormLabel>Name</FormLabel>
                <FormControl>
                  <Input type="text" v-model="gameformdata.name" required :value="gameformdata.name"
                    v-bind="componentField" class="mb-5" />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <div class="mb-5">
              <FormField v-slot="{ componentField }" name="description">
                <FormItem>
                  <FormLabel>Description</FormLabel>
                  <FormControl>
                    <Input type="text" v-model="gameformdata.description" required :value="gameformdata.description"
                      v-bind="componentField" />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              </FormField>
            </div>
            <div class="mb-5 flex items-center space-x-2">
              <div class="w-50">
                <FormField v-slot="{ componentField }" name="min_players">
                  <FormItem>
                    <FormLabel>Minimum Players</FormLabel>
                    <FormControl>
                      <Input type="number" v-model="gameformdata.min_players" required :value="gameformdata.min_players"
                        v-bind="componentField" />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                </FormField>
              </div>
              <FormField v-slot="{ componentField }" name="max_players">
                <FormItem>
                  <FormLabel>Maximum Players</FormLabel>
                  <FormControl>
                    <Input type="number" v-model="gameformdata.max_players" required :value="gameformdata.max_players"
                      v-bind="componentField" />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              </FormField>
            </div>
          </form>
        </DialogBody>
        <DialogClose>
          <Button variant="outline" @click="clearForm" class="m-2">Cancel</Button>
          <Button @click="createGame">Create</Button>
        </DialogClose>
      </DialogContent>
    </Dialog>
    <!-- End create Game -->

    <!-- Show all games here -->
    <div class="grid grid-cols-4 gap-4">
      <div v-for="game in games" :key="game.id">
        <div class="flex flex-col items-center">
          <GameCard :game="game" @update="console.log('updated', $event)" @delete="console.log('deleted')">
          </GameCard>
        </div>
      </div>
    </div>
    <!-- End show all games here -->

  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Righteous&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap');

.v-row {
  justify-content: center;
}

h1 {
  font-family: 'Righteous', cursive;
  font-size: 3rem;
  color: #fff;
}

.fill {
  background: rgba(0, 212, 255, 0.9);
  color: rgba(255, 255, 255, 0.95);
  filter: drop-shadow(0);
  font-weight: bold;
  transition: all .3s ease;
}

.fill:hover {
  transform: scale(1.125);
  border-color: rgba(255, 255, 255, 0.9);
  filter: drop-shadow(0 10px 5px rgba(0, 0, 0, 0.125));
  transition: all .3s ease;
}
</style>
