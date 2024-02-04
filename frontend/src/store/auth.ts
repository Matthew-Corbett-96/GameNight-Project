import { defineStore } from "pinia";
import { computed, type Ref, ref } from "vue";
import { useAuth0 } from '@auth0/auth0-vue';
import { type User} from '@auth0/auth0-spa-js';
import type { AppUser } from "../main";

export const useAuthStore = defineStore(
   'auth',
   () => {

      const { loginWithRedirect, logout, isAuthenticated, user } = useAuth0();
      const current_user: Ref<AppUser> = ref({} as AppUser);

      const getHeaders = computed(() => {
         let headers = new Headers();
         // headers.append('Authorization', `Bearer ${token.value}`);
         headers.append('Content-Type', 'application/json');
         headers.append('Accept', 'application/json');
         headers.append('Origin', import.meta.url);
         headers.append('Access-Control-Allow-Origin', '*');
         return headers;
      });

      const getAuthProfile = computed(() => {
         if (typeof user.value !== 'undefined') {
            return user.value;
         } else {
            return {} as User;
         }
      });

      const getCurrentUser = computed(() => {
         if (typeof current_user.value !== 'undefined') {
            return current_user.value;
         } else {
            return {} as AppUser;
         }
      });

      const isLoggedIn = computed(() => {
         return isAuthenticated.value;
      });

      async function Login() {
         try {
            await loginWithRedirect({
               appState: {
                  target: '/profile'
               }
            });
         }
         catch (e) {
            console.error(e);
         }
      }

      async function Register() {
         try {
            await loginWithRedirect({
               appState: {
                  target: '/profile'
               },
               authorizationParams: {
                  screen_hint: 'signup'
               }
            });
         }
         catch (e) {
            console.error(e);
         }
      }

      async function Logout() {
         try {
            await logout({
               logoutParams: {
                  returnTo: window.location.origin
               }
            });
            clearUser();
         }
         catch (e) {
            console.error(e);
         }
      }

   async function updateCurrentUser(): Promise<void> {
      if ( typeof getCurrentUser.value.username === 'undefined' ) {
         try {
            const response = await fetch( import.meta.env.VITE_API_SERVER_URL  + '/auth0/users/' + getAuthProfile.value.sub, {
               method: 'GET',
               headers: getHeaders.value,
               mode: 'cors',
            });
            const data = await response.json();
            current_user.value = data.data.user as AppUser;
         } catch (e: any) {
            console.error('Somthing Went Wrong:', e);
         }
      }
   }

   function clearUser(): void {
      current_user.value = {} as AppUser;
   }

      return { isLoggedIn, getAuthProfile, getHeaders, updateCurrentUser, Login, Logout, Register, getCurrentUser }
   },
   {
      persist: true
   }

);