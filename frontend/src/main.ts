import './assets/main.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
// Pinia
import { createPinia } from 'pinia';
import { createPersistedState } from 'pinia-plugin-persistedstate';
// Auth0
import { createAuth0 } from '@auth0/auth0-vue';
import { User } from '@auth0/auth0-spa-js';
// Toastification
import { type PluginOptions } from 'vue-toastification';
import "vue-toastification/dist/index.css";
import toast from 'vue-toastification';
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const pinia = createPinia().use(createPersistedState());

const auth0 = createAuth0({
  domain: import.meta.env.VITE_AUTH0_DOMAIN,
  clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
  authorizationParams: { // Change this to localhost when working locally
    //redirect_uri: import.meta.env.VITE_AUTH0_CALLBACK_URL
    redirect_uri: 'http://localhost:5173/callback'
  }
});

const toastOptions: PluginOptions = {
  timeout: 5000
};

const vuetify = createVuetify({
  components,
  directives
});

const app = createApp(App)
  .use(router)
  .use(pinia)
  .use(auth0)
  .use(toast, toastOptions)
  .use(vuetify)
  .mount('#app');

export type SuccessAPIResponse = {
  status: 200 | 201
  message: string
  data: any
}

export type  ErrorAPIResponse = {
  status: 400 | 401 | 403 | 404 | 500
  message: string
}

export type APIResponse = SuccessAPIResponse | ErrorAPIResponse;

export interface AuthProfile extends User {}

export interface AppUser {
  id: string
  created_on: string
  updated_on: string
  auth0_id: string
  username: string
  first_name?: string
  last_name?: string
  gender?: Gender
  email: string
  phone_number?: string
  role_id?: string
  role_name?: string
  is_active: boolean
  RSVPs: RSVP[]
}

export interface Role {
  id: string
  name: string
  created_on: string
  updated_on: string
}

export interface GameNight {
  id: string
  name: string
  description: string
  date: string
  time: string
  location: string
  created_on: string
  updated_on: string
  games: Game[]
  RSVPs: RSVP[]
}

export interface Round {
  id: string
  game_night_id: string
  game_night: string
  game_id: string
  game: string
  created_on: string
  updated_on: string
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
}

export enum Gender {
  MALE = 'male',
  FEMALE = 'female',
  OTHER = 'other'
}

export interface Game {
  id: string
  name: string
  description: string
  rules: string
  house_rules: string
  min_players: number
  max_players: number
  created_on: string
  updated_on: string
}

export interface FormField {
  label: string
  type: string
}

export interface FormData {
  [key: string]: any
}

export interface GameFormData extends Game {
  id?: string
  name: string
  description: string
  min_players: number
  max_players: number
  created_on?: string
  updated_on?: string
}

export interface RoundFormData extends FormData {
  game_night_id: string
  game_id: string
}

export interface GameNightFormData extends FormData {
  name: string
  description: string
  date: string
  time: string
  location: string
  games: string[]
}

export interface UserFormData extends FormData {
  id: string
  username: string
  first_name: string
  last_name: string
  gender: Gender
  email: string
  phone_number: string
  role_name: string
  is_active: boolean
}
