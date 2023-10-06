import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')

export interface APIResponse {
   status: number
   message: string
   data: any
}

export interface User {
   id: number
   username: string
   email: string
   password: string
   created_at: string
   updated_at: string
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
