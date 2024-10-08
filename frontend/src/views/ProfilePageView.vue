<script lang="ts" setup>
import { useRouter } from 'vue-router';
import { computed, onMounted, ref, watch } from 'vue';
import type { ComputedRef, Ref } from 'vue';
import { Gender, type AuthProfile, type AppUser } from '../main';
import { useAuthStore } from '../store/auth';
import * as z from 'zod';
import { toTypedSchema } from '@vee-validate/zod';
// UI Components 
import { Button } from '../@/components/ui/button';
import { Input } from '../@/components/ui/input';
import { Label } from '../@/components/ui/label';
import { Checkbox } from '../@/components/ui/checkbox';
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger
} from '../@/components/ui/tabs';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '../@/components/ui/card';
import { useForm } from 'vee-validate';
import {
  FormField,
  FormControl,
  FormDescription,
  FormMessage,
  FormLabel,
  FormItem,
  Form
} from '../@/components/ui/form';

const authStore = useAuthStore();
const current_user: Ref<AppUser> = ref(authStore.getCurrentUser);

watch(() => authStore.getCurrentUser, (newVal, oldVal) => {
  current_user.value = newVal;
});

onMounted(() => {
  authStore.updateCurrentUser();
});
// const auth_profile: ComputedRef<AuthProfile> = computed(() => authStore.getAuthProfile);

const schema = toTypedSchema(z.object({
  email: z.string().email(),
  phone: z.string().min(10).max(15),
  username: z.string().min(2).max(50),
  first_name: z.string().min(2).max(50),
  last_name: z.string().min(2).max(50),
  created_on: z.date().optional(),
  updated_on: z.date().optional(),
  is_active: z.boolean(),
  role_name: z.string().min(2).max(50),
}));


const form = useForm({
  validationSchema: schema,
  initialValues: {
    email: current_user.value.email,
    phone: current_user.value.phone_number,
    username: current_user.value.username,
    first_name: current_user.value.first_name,
    last_name: current_user.value.last_name,
    is_active: current_user.value.is_active,
    role_name: current_user.value.role_name,
  }
})



const onSubmit = form.handleSubmit((values) => {
  console.log('Form submitted!', values);
})




</script>

<template>
  <div>
    <Card>
      <CardHeader>
        <CardTitle>Welcome {{ current_user.first_name }}!</CardTitle>
      </CardHeader>
      <CardContent class="shadow-2xl">
        <Tabs default-value="account">
          <TabsList class="grid w-auto grid-cols-2">
            <TabsTrigger value="account">
              Account
            </TabsTrigger>
            <TabsTrigger value="password">
              Password
            </TabsTrigger>
          </TabsList>
          <TabsContent value="account" class="">
            <Card>
              <CardHeader>
                <CardDescription>
                  Make changes to your account here. Click save when you're done.
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div class="">
                  <form @submit="onSubmit">
                    <FormField v-slot="{ componentField }" name="username">
                      <FormItem>
                        <FormLabel>Username</FormLabel>
                        <FormControl>
                          <Input type="text" v-model="current_user.username" :value="current_user.username"
                            v-bind="componentField" />
                        </FormControl>
                        <FormDescription>
                          This is your public display name.
                        </FormDescription>
                        <FormMessage />
                      </FormItem>
                    </FormField>
                    <div class="mb-5 flex items-center space-x-2">
                      <div class="w-50">
                        <FormField v-slot="{ componentField }" name="first_name">
                          <FormItem>
                            <FormLabel>First Name</FormLabel>
                            <FormControl>
                              <Input type="text" v-model="current_user.first_name" :value="current_user.first_name"
                                v-bind="componentField" />
                            </FormControl>
                            <FormDescription>
                            </FormDescription>
                            <FormMessage />
                          </FormItem>
                        </FormField>
                      </div>
                      <div class="w-50">
                        <FormField v-slot="{ componentField }" name="last_name">
                          <FormItem>
                            <FormLabel>Last Name</FormLabel>
                            <FormControl>
                              <Input type="text" v-model="current_user.last_name" :value="current_user.last_name"
                                v-bind="componentField" />
                            </FormControl>
                            <FormDescription>
                            </FormDescription>
                            <FormMessage />
                          </FormItem>
                        </FormField>
                      </div>
                    </div>
                    <div class="mb-5 flex items-center space-x-2">
                      <div class="w-50">
                        <FormField v-slot="{ componentField }" name="email">
                          <FormItem>
                            <FormLabel>Email</FormLabel>
                            <FormControl>
                              <Input type="text" v-model="current_user.email" :value="current_user.email"
                                v-bind="componentField" />
                            </FormControl>
                            <FormDescription>
                            </FormDescription>
                            <FormMessage />
                          </FormItem>
                        </FormField>
                      </div>
                      <div class="w-50">
                        <FormField v-slot="{ componentField }" name="phone">
                          <FormItem>
                            <FormLabel>Phone Number</FormLabel>
                            <FormControl>
                              <Input type="tel" v-model="current_user.phone_number" :value="current_user.phone_number"
                                v-bind="componentField" />
                            </FormControl>
                            <FormDescription>
                              Do not include +1 before the number.
                            </FormDescription>
                            <FormMessage />
                          </FormItem>
                        </FormField>
                      </div>
                    </div>
                    <div class="mb-5 flex items-center space-x-2">
                      <div class="w-50">
                        <FormField v-slot="{ componentField }" name="role_name">
                          <FormItem>
                            <FormLabel>Role</FormLabel>
                            <FormControl>
                              <Input type="text" v-model="current_user.role_name" :value="current_user.role_name"
                                v-bind="componentField" />
                            </FormControl>
                            <FormDescription>
                              This is your role name.
                            </FormDescription>
                            <FormMessage />
                          </FormItem>
                        </FormField>
                      </div>
                      <div class="w-50">
                        <FormField v-slot="{ value, handleChange }" type="checkbox" name="is_active">
                          <FormItem class="flex flex-row items-start gap-x-3 space-y-0 rounded-md border p-4">
                            <FormControl>
                              <Checkbox :checked="value" @update:checked="handleChange" />
                            </FormControl>
                            <div class="space-y-1 leading-none">
                              <FormLabel>Active User</FormLabel>
                              <FormDescription>
                              </FormDescription>
                              <FormMessage />
                            </div>
                          </FormItem>
                        </FormField>
                      </div>
                    </div>
                  </form>
                </div>
              </CardContent>
              <CardFooter>
                <Button @click="onSubmit">Save changes</Button>
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
                <div class="space-y-1 w-50">
                  <Label for="current">Current password</Label>
                  <Input id="current" type="password" />
                </div>
                <div class="space-y-1 w-50">
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

<style scoped></style>