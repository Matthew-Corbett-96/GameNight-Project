<script lang="ts" setup>
import { useAuthStore } from '@/store/auth';
import { useRouter } from 'vue-router';
import Button from '@/components/core/Button.vue';
import type { ComputedRef } from 'vue';
import { computed } from 'vue';
import { onMounted } from 'vue';
import { type AuthProfile } from '@/main';

const authStore = useAuthStore();
const router = useRouter();

const current_user = computed(() => authStore.getCurrentUser);
const auth_profile: ComputedRef<AuthProfile> = computed(() => authStore.getAuthProfile);

onMounted(() => {
  authStore.updateCurrentUser();
});

// leave for debugging
const logUser = () => console.log(current_user.value);

</script>

<template>
  <div>
    <h1>{{current_user.username}}'s Profile Page</h1>
    <p>Email: {{current_user.email}}</p>
    <p>Email Verified: {{ auth_profile.email_verified }}</p>
    <p>Username: {{current_user.username}}</p>
    <p>First Name: {{current_user.first_name}}</p>
    <p>Last Name: {{current_user.last_name}}</p>
    <p>Created At: {{current_user.created_on}}</p>
    <p>Updated At: {{current_user.updated_on}}</p>
  </div>

  <Button text="Log User" @clicked="logUser"> </Button>
</template>

<style scoped>

</style>