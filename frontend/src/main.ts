import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { createPersistedState } from 'pinia-plugin-persistedstate'
import { type } from 'os'

const pinia = createPinia();
pinia.use(createPersistedState());
const app = createApp(App)
app.use(router).use(pinia);
app.mount('#app')

export interface APIResponse {
   status: number
   message: string
   data: any
}

export interface User {
   id: string
   username: string
   first_name: string
   last_name: string
   gender: Gender
   email: string
   phone_number: string
   role_id: string
   role_name: string
   password: string
   is_active: boolean
   created_on: string
   updated_on: string
   RSVPs: RSVP[]
}

export interface RSVP {
   id: string
   user_id: string
   user_name: string
   game_night_id: string
   game_night: string
   response_date: string
   response_status: string
   created_on: string
   updated_on: string
};

export enum Gender {
   MALE = 'male',
   FEMALE = 'female',
   OTHER = 'other'
}

export interface Game {
   id: string
   name: string
   description: string
   min_players: number
   max_players: number
   created_on: string
   updated_on: string
}

export interface FormField {
   label: string;
   type: string;
}

export interface FormData {
   [key: string]: any;
}

export interface GameFormData extends FormData {
   name: string;
   description: string;
   min_players: number;
   max_players: number;
}
