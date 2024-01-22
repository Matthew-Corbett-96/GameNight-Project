<script lang="ts" setup>
import { useAuthStore } from '../store/auth';
import { useRouter } from 'vue-router';
import type { ComputedRef } from 'vue';
import { computed } from 'vue';
import { onMounted } from 'vue';
import { type AuthProfile } from '../main';
import {Button} from '../@/components/ui/button'

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
    <Button> 
      Hello
    </Button>
    <h1 class="bg-primary text-primary-foreground hover:bg-primary/30">{{current_user.username}}'s Profile Page</h1>
    <p class="bg-gray-50 text-center hover:bg-gray-950">Email: {{current_user.email}}</p>
    <p>Email Verified: {{ auth_profile.email_verified }}</p>
    <p>Username: {{current_user.username}}</p>
    <p>First Name: {{current_user.first_name}}</p>
    <p>Last Name: {{current_user.last_name}}</p>
    <p>Created At: {{current_user.created_on}}</p>
    <p>Updated At: {{current_user.updated_on}}</p>
  </div>
</template>

<style scoped>

</style>