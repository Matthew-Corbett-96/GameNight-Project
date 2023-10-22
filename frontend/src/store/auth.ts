import { defineStore } from "pinia";
import { computed, type Ref} from "vue";
import { useAuth0 } from '@auth0/auth0-vue';
import type { User } from '@auth0/auth0-spa-js';

export const useAuthStore = defineStore(

   'auth',

   () => {

      const { loginWithRedirect, logout, isAuthenticated, user } = useAuth0();

      const getHeaders = computed(() => {
         let headers = new Headers();
         // headers.append('Authorization', `Bearer ${token.value}`);
         headers.append('Content-Type', 'application/json');
         headers.append('Accept', 'application/json');
         headers.append('Origin', 'http://localhost:3000');
         return headers;
      });

      const getUser = computed(() => {
        if (typeof user.value !== 'undefined') {
           return user.value;
        } else {
           return {} as User;
        }
      });

      const isLoggedIn = computed(() => {
         return isAuthenticated.value;
      });

      async function Login() {
         try {
            loginWithRedirect({
               appState: {
                  target: '/profile'
               }
            });
         }
         catch (e) {
            console.error(e);
         }

         try {
            const response = await fetch('http://localhost:3000/users/' + user.value?.sub , {
               method: 'GET',
               headers: getHeaders.value
            });
            const data = await response.json();
            console.log(data);
         } catch (error) {
            
         }
      }

      async function Register() {
         try {
            loginWithRedirect({
               appState: {
                  target: '/profile'
               },
               authorizationParams: {
                  screen_hint: 'signup'
               }
            });
            const response = await fetch('http://localhost:3000/users/', {
               method: 'POST',
               headers: getHeaders.value,
               body: JSON.stringify({
                  auth0_id: user.value?.sub,
                  username: user.value?.nickname,
                  email: user.value?.email
               })
            });
            const data = await response.json();
            console.log(data);
         }
         catch (e) {
            console.error(e);
         }
      }

      async function Logout() {
         try {
            logout({
               logoutParams: {
                  returnTo: window.location.origin
               }
            });
         }
         catch (e) {
            console.error(e);
         }
      }

      return { isLoggedIn, getUser, getHeaders, Login, Logout, Register }
   },
   {
      persist: true
   }

);