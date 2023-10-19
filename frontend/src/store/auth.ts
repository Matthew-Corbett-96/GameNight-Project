import { defineStore } from "pinia";
import { type User } from "../main"
import { computed, ref, type Ref } from "vue";

export const useAuthStore = defineStore(

   'auth',

   () => {
      const user = ref<User>({} as User);
      // const token: Ref<string> = ref('sdhjfgvasdufhgwfuywfgwefbwf');

      const getHeaders = computed(() => {
         let headers = new Headers();
         // headers.append('Authorization', `Bearer ${token.value}`);
         headers.append('Content-Type', 'application/json');
         headers.append('Accept', 'application/json');
         headers.append('Origin', 'http://localhost:3000');
         return headers;
      });

      const isAuthenticated = computed(() => {
         return !!user.value;
         // return !!user.value && !!token.value;
      });

      async function Login(email: string, password: string): Promise<number> {

         try {
            const response = await fetch('http://localhost:5000/login/', {
               method: 'POST',
               mode: 'cors',
               headers: getHeaders.value,
               body: JSON.stringify({
                  email,
                  password
               })
            });
            const data = await response.json();
            if (data.status !== 200) {
               console.error('Error: ', data);
               return data.status;
            }
            user.value = data.data;
            // token.value = data.token;
            return 200;
         } catch (error: any) {
            console.error('Error: ', error);
            return 500;
         }
      }

      function Logout(): void {
         user.value = {} as User;
         // token.value = '';
      }

      return { user, isAuthenticated, getHeaders, Login, Logout }
   },
   {
      persist: true
   }

);