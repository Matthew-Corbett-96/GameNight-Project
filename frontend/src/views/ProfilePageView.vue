<script lang="ts" setup>
import { useAuthStore } from '@/store/auth';
import { useRouter } from 'vue-router';
import Button from '@/components/core/Button.vue';

const authStore = useAuthStore();
const router = useRouter();
const current_user = authStore.getUser;

const logUser = () => console.log(current_user);

</script>

<template>
  <div>
    <h1>{{current_user.nickname}}'s Profile Page</h1>
    <p>Email: {{current_user.email}}</p>
    <picture>
      <img :src="current_user.picture" alt="Profile Picture" />
    </picture>
  </div>

  <Button text="Log User" @clicked="logUser"> </Button>
</template>

<style scoped>

</style>