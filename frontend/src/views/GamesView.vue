<script setup lang="ts">
import { defineProps } from 'vue';
import { ref } from 'vue';
import type { Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import router from '@/router';
import PopupForm from '@/components/core/PopupForm.vue';
import { onMounted } from 'vue';
import { type FormData, type FormField, type Game, type GameFormData } from '@/main';
import { watch } from 'vue';


onMounted(() => {
  fetchGames();
});

function fetchGames(): void {
  fetch('http://localhost:5000/games/')
    .then(response => response.json())
    .then(data => {
      if (data.status === 200) {
        console.log('Games fetched successfully.');
        console.log(data);
        games.value = data.data;
      } else {
        console.log(data);
      }
    })
    .catch(error => {
      console.log('Error:', error);
    });
}

const games: Ref<Game[]> = ref([]);
// Toggles for showing/hiding the create and update game forms
const showCreateGameForm: Ref<boolean> = ref(false);
const showUpdateGameForm: Ref<boolean> = ref(false);

// Form fields and data for the create and update game forms
let gameformfields: FormField[] = [
  { label: 'Name', type: 'text' },
  { label: 'Description', type: 'text' },
  { label: 'Min Players', type: 'number' },
  { label: 'Max Players', type: 'number' }
];

// Form data for the create and update game forms
let gameformdata: GameFormData = {
  name: '',
  description: '',
  min_players: 0,
  max_players: 0
};

watch( () => gameformdata, (newVal, oldVal) => {
  gameformdata.name = newVal.name;
  gameformdata.description = newVal.description;
  gameformdata.min_players = newVal.min_players;
  gameformdata.max_players = newVal.max_players;
});

// Functions for toggling the create and update game forms
function toggleCreateGameForm() {
  showCreateGameForm.value = !showCreateGameForm.value;
}
function toggleUpdateGameForm() {
  showUpdateGameForm.value = !showUpdateGameForm.value;
}

function deleteGame(id: string) {
  let headers = new Headers();
  headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');
  headers.append('Origin', 'http://localhost:3000');

  fetch('http://localhost:5000/games/' + id, {
    method: 'DELETE',
    mode: 'cors',
    headers: headers
  })
    .then(response => response.json())
    .then(data => {
      if (data.status === 200) {
        console.log('Game deleted successfully.');
        console.log(data);
      } else {
        console.log(data);
      }
    })
    .catch(error => {
      console.log('Error:', error);
    });
}

function openUpdateForm(game: Game) {
  gameformdata = {
    name: game.name,
    description: game.description,
    min_players: game.min_players,
    max_players: game.max_players
  };
  toggleUpdateGameForm();
}

// Functions for submitting the create and update game forms
function submitCreateGameForm(formData: any) {

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
      toggleCreateGameForm();
    });
}

function submitUpdateGameForm(formData: any) {
  
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('Origin', 'http://localhost:3000');
  
    fetch('http://localhost:5000/games/', {
      method: 'PUT',
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
          console.log('Game updated successfully.');
          console.log(data);
        } else {
          console.log(data);
        }
      })
      .catch(error => {
        console.log('Error:', error);
      })
      .finally(() => {
        toggleUpdateGameForm();
      });
}

</script>

<template>
  <h1>
   Games 
  </h1>

  <section>
    <Button
    @clicked="toggleCreateGameForm"
    :text="'Create Game'"
    />
  </section>

  <section class="display-games-container">
    <div v-for="game in games" :key="game.id" class="game-box">
      <div class="game-info">
        <h3 class="game-item name "> {{ game.name }} </h3>
        <p class="game-item description"> {{ game.description }} </p>
        <p class="game-item min-player"> {{ 'Min Players:' + game.min_players }} </p>
        <p class="game-item max-player"> {{'Max Players:' + game.max_players }} </p>
      </div>
      <div class="bottom-bar">
        <Button @clicked="deleteGame(game.id)" :text="'Delete'" class="btn" />
        <Button @clicked="openUpdateForm(game)" :text="'Update'" class="btn" /> 
      </div>
    </div>
  </section>

  <div class="popup-container">
    <PopupForm
    @submit="submitCreateGameForm" 
    @cancel="toggleCreateGameForm" 
    :show="showCreateGameForm"
    :title="'Create Game'"
    :form-fields="gameformfields">
    </PopupForm>

    <PopupForm
    @submit="submitUpdateGameForm" 
    @cancel="toggleUpdateGameForm" 
    :show="showUpdateGameForm"
    :title="'Update Game'"
    :form-fields="gameformfields"
    :form-data="gameformdata">
    </PopupForm>
  </div>

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

.game-box {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: rgb(255, 255, 255);
  border-radius: 0.5rem;
}

.game-item {
  margin: 0.5rem;
}

.game-item.name {
  font-size: 1.5rem;
}

.game-item.description {
  font-size: 1rem;
}

.game-item.min-player {
  font-size: 0.8rem;
}

.game-item.max-player {
  font-size: 0.8rem;
}

.bottom-bar {
  display: flex;
  justify-content: space-around;
  width: 100%;
}



</style>
