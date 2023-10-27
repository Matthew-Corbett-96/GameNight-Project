import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { createPersistedState } from 'pinia-plugin-persistedstate'
import { createAuth0 } from '@auth0/auth0-vue'
import { User } from '@auth0/auth0-spa-js'

const pinia = createPinia().use(createPersistedState())

const auth0 = createAuth0({
  domain: import.meta.env.VITE_AUTH0_DOMAIN,
  clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
  authorizationParams: {
    redirect_uri: import.meta.env.VITE_AUTH0_CALLBACK_URL
  }
});

const app = createApp(App).use(router).use(pinia).use(auth0);

app.mount('#app')

export interface APIResponse {
  status: number
  message: string
  data: any
}

export interface AuthProfile extends User {
}

export interface AppUser {
  id: string
  username: string
  first_name: string
  last_name: string
  gender: Gender
  email: string
  phone_number: string
  role_id: string
  role_name: string
  is_active: boolean
  created_on: string
  updated_on: string
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

export interface GameFormData extends FormData {
  name: string
  description: string
  min_players: number
  max_players: number
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
