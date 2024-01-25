<script lang="ts" setup>
import { useAuthStore } from '../store/auth';
import { useRouter } from 'vue-router';
import type { ComputedRef } from 'vue';
import { computed } from 'vue';
import { onMounted } from 'vue';
import { type AuthProfile } from '../main';
import {Button} from '../@/components/ui/button'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../@/components/ui/tabs'
import { Input } from '../@/components/ui/input'
import { Label } from '../@/components/ui/label'

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '../@/components/ui/card'

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
    <Card>
    <CardHeader>
      <CardTitle>Welcome Matthew{{current_user.username}}!</CardTitle>
    </CardHeader>
    <CardContent>

      <Tabs default-value="account">
    <TabsList class="grid w-full grid-cols-2">
      <TabsTrigger value="account">
        Account
      </TabsTrigger>
      <TabsTrigger value="password">
        Password
      </TabsTrigger>
    </TabsList>
    <TabsContent value="account">
      <Card>
        <CardHeader>
          <CardDescription>
            Make changes to your account here. Click save when you're done.
          </CardDescription>
        </CardHeader>
        <CardContent class="space-y-2">
          <div class="space-y-1">
            <Label for="name">Email</Label>
            <Input id="name" default-value="" />
          </div>
          <div class="space-y-1">
            <Label for="name">First Name</Label>
            <Input id="name" default-value="" />
          </div>
          <div class="space-y-1">
            <Label for="username">Last Name</Label>
            <Input id="username" default-value="" />
          </div>
          <div class="space-y-1">
            <Label for="name">Email Verified</Label>
            <Input id="name" default-value="" />
          </div>
          <div class="space-y-1">
            <Label for="name">Created At</Label>
            <Input id="name" default-value="" />
          </div>
          <div class="space-y-1">
            <Label for="name">Updated At</Label>
            <Input id="name" default-value={{current_user.updated_on}} />
          </div>
        </CardContent>
        <CardFooter>
          <Button>Save changes</Button>
        </CardFooter>
      </Card>
    </TabsContent>
    <TabsContent value="password">
      <Card>
        <CardHeader>
          <CardDescription>
            Change your password here. After saving, you'll be logged out.
          </CardDescription>
        </CardHeader>
        <CardContent class="space-y-2">
          <div class="space-y-1">
            <Label for="current">Current password</Label>
            <Input id="current" type="password" />
          </div>
          <div class="space-y-1">
            <Label for="new">New password</Label>
            <Input id="new" type="password" />
          </div>
        </CardContent>
        <CardFooter>
          <Button>Save password</Button>
        </CardFooter>
      </Card>
    </TabsContent>
  </Tabs>
      
    </CardContent>
  </Card>
  </div>
</template>

<style scoped>

</style>