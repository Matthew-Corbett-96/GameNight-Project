
<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label>
        Email:
        <input type="email" v-model="email" required>
      </label>
      <label>
        Password:
        <input type="password" v-model="password" required>
      </label>
      <button type="submit">Login</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import type { Ref } from 'vue';
import axios from 'axios';


    const email: Ref<string>  = ref('');
    const password: Ref<string> = ref('');
    const error: Ref<string> = ref('');

    async function login() {
      try {
        const response = await axios.post('/api/login', { email: email.value, password: password.value });
        const data = response.data;
        console.log(data);
      } catch (err: any) {
        error.value = "Login Failed";
      }
    };

</script>

