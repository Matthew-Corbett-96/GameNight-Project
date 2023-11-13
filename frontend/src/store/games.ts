// Pinia store for games
import { defineStore } from 'pinia'
import { useToast } from 'vue-toastification'
import { computed, type Ref, ref } from "vue";
import { useAuthStore } from '@/store/auth';
import type { APIResponse, AppUser, ErrorAPIResponse, Game, GameFormData } from "@/main";
import { totalmem } from 'os';

export const useGameStore = defineStore(
   'games',
   () => {

   const toast = useToast();
   const authStore = useAuthStore();
   const headers = authStore.getHeaders;
   const games: Ref<Game[]> = ref([]);

   const getGames = computed(() => games.value);

   // Functions for fetching games from the backend
   async function fetchGames(): Promise<void> {
      try {
         let response = await fetch('http://localhost:5000/games/');
         let data: APIResponse = await response.json();
         
         if (data.status === 200)
            games.value = data.data.games;
         else
            toast.error(data.message);
         
      } catch (e: any) {
         toast.error(e.message);
      }
   }

   // Function for deleting a game
   async function deleteGame(game: Game) {

      try {
         let response = await fetch('http://localhost:5000/games/' + game.id, {
         method: 'DELETE',
         mode: 'cors',
         headers: headers
         });
         let data = await response.json();
   
         if (data.status === 200)
            toast.info('Game deleted successfully');
         else
            toast.error(data.message);

         fetchGames();

      } catch (e: any) { 
         toast.error(e.message);
      }

   }

   //Create game
   async function createGame(formData: GameFormData) {
    
      try {
         let response = await fetch('http://localhost:5000/games/', {
           method: 'POST',
           mode: 'cors',
           headers: headers,
           body: JSON.stringify({
             name: formData['name'],
             description: formData['description'],
             min_players: formData['min_players'],
             max_players: formData['max_players']
           })
         });
   
         let data = await response.json();
   
         if (data.status === 200)
            toast.success('Game created successfully');
         else
            toast.error(data.message);
   
         fetchGames();
      } catch (e: any) {
         toast.error(e.message);
      }

   }

   async function updateGame(formData: GameFormData) {
    
      let game = games.value.find(game => game.name === formData.name);
    
      if (game === undefined) {
         toast.error('Game not found');
         return;
      }
    
      try {
         let response = await fetch('http://localhost:5000/games/' + game.id, {
           method: 'PUT',
           mode: 'cors',
           headers: headers,
           body: JSON.stringify({
             name: formData['name'],
             description: formData['description'],
             min_players: formData['min_players'],
             max_players: formData['max_players']
           })
         });
   
         let data = await response.json();
         if (data.status === 200)
            toast.success('Game updated successfully');
         else 
            toast.error(data.message);
         
         fetchGames();
         
      } catch (e: any) {
         toast.error(e.message);
      }

    }

   function reset(): void {
      games.value = [];
   }
      return { reset, getGames, fetchGames, deleteGame, createGame, updateGame  }
   },
   {
      persist: true
   }

);

