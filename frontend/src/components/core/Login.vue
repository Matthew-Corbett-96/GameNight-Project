<script lang="ts" setup>
import router from '@/router';
import { ref } from 'vue';
import type { Ref } from 'vue';
import Button from '@/components/core/Button.vue';

const email: Ref<string> = ref('');
const password: Ref<string> = ref('');
const showError: Ref<Boolean> = ref(false);
const error_message: Ref<string> = ref('');


function login() {

  let headers = new Headers();
  headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');
  headers.append('Origin', 'http://localhost:3000');

  fetch('http://localhost:5000/login/', {
    method: 'POST',
    mode: 'cors',
    headers: headers,
    body: JSON.stringify({
      email: email.value,
      password: password.value
    })
  })
    .then(response => response.json())
    .then(data => {
      if (data.status === 200) {
        router.push('/');
      } else {
        showError.value = true;
        error_message.value = data.message;
      }
    })
    .catch(error => {
      console.log('Error:', error);
      showError.value = true;
      error_message.value = 'An error occurred.';
    })
    .finally(() => {
      clearForm();
    });
  
}

function clearForm(): void {
  email.value = '';
  password.value = '';
}
</script>

<template>
  <div class="login-container">

    <div class='login-form-wrapper'>

      <h1 class="login-title">Login</h1>
      <p class="login-error" v-if="showError">{{ error_message }}</p>

      <form class="login-form" @submit.prevent="login">
        <label class="login-label">
          Email:
          <input class="login-input" type="email" v-model="email" required>
        </label>
        <label class="login-label">
          Password:
          <input class="login-input" type="password" v-model="password" required>
        </label>
        <Button text="Login" @clicked="submit" />
      </form>

    </div>
  
  </div>
</template>

<style scoped>
i.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f2f2f2;
}

.login-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
  text-align: center;
}

.login-form-wrapper {
  margin: 5vw 25vw;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #ffffff8a;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
}

.login-label {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: #333;
}

.login-input {
  padding: 0.5rem;
  border: none;
  border-radius: 0.25rem;
  box-shadow: 0 0.25rem 0.5rem rgba(0, 0, 0, 0.1);
}

.login-error {
  margin-top: 1rem;
  color: #cc0000;
  font-size: 1.2rem;
  text-align: center;
}
</style>