<script setup lang="ts">
import { ref } from 'vue';
import { Avatar, AvatarImage, AvatarFallback } from '../@/components/ui/avatar'
import { AlertDialogRoot, AlertDialogTrigger, AlertDialogPortal, AlertDialogOverlay, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogCancel, AlertDialogAction } from 'radix-vue';
import { Button } from '../@/components/ui/button'
import { Checkbox } from '../@/components/ui/checkbox'
import { Separator } from '../@/components/ui/separator';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '../@/components/ui/card';
import { KeyboardButton } from '../@/components/ui/keyboardButton'

// keyboard button variants
const colors = ref(['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'gray'])
const sizes = ref(['sm', 'md', 'lg']);
// button variants
const btnVariants = ref(['default', 'secondary', 'outline', 'destructive', 'link', 'ghost'])
const btnSizes = ref(['icon', 'sm', 'md', 'lg',])
// avatar variants
const avatarSizes = ref(['sm', 'md', 'lg', 'xl'])
const avatarShapes = ref(['circle', 'square'])

</script>

<template>
   <h1 class="text-4xl font-bold text-red-500">
      Playground
   </h1>

   <div class="grid grid-rows-3 gap-4">

      <div class="row-span-1 p-4">
         <section class="flex items-center justify-center">
            <Avatar shape="square" size="lg">
               <AvatarImage src="../assets/logoo.jpg">
                  <AvatarFallback :delay-ms="123">
                     <span>JD</span>
                  </AvatarFallback>
               </AvatarImage>
            </Avatar>
         </section>
      </div>

      <Separator />

      <div class="row-span-1 p-4">
         <section class="flex items-center justify-center">
            <AlertDialogRoot>
               <AlertDialogTrigger>
                  <Button>Cancel Account</Button>
               </AlertDialogTrigger>
               <AlertDialogPortal>
                  <AlertDialogOverlay class="fixed inset-0 bg-black opacity-50" />
                  <AlertDialogContent
                     class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-lg p-4">
                     <AlertDialogTitle>
                        Cancel your account
                     </AlertDialogTitle>
                     <AlertDialogDescription class="text-center text-base">
                        Are you sure you want to cancel your account? This action cannot be undone.
                     </AlertDialogDescription>
                     <div class="flex justify-center mt-4">
                        <AlertDialogCancel>
                           <Button size="md">Cancel</Button>
                        </AlertDialogCancel>
                        <AlertDialogAction>
                           <Button :variant="'destructive'">Confirm</Button>
                        </AlertDialogAction>
                     </div>
                  </AlertDialogContent>
               </AlertDialogPortal>
            </AlertDialogRoot>
         </section>
      </div>

      <Separator />

      <section class="row-span-1 p-4 m-4 flex flex-col">
         <div class="flex flex-col items-center justify-center">
            <h2 class="text-center font-bold text-xl">Keyboard Buttons</h2>
         </div>

         <div class="grid grid-cols-3 gap-4">
            <div v-for="color in colors" :key="color" class="flex flex-col items-center justify-center p-4">
               <KeyboardButton v-for="size in sizes" :key="size"
                  :color="color as 'red' | 'green' | 'blue' | 'yellow' | 'purple' | 'pink' | 'grey' | null | undefined"
                  :size="size as 'sm' | 'md' | 'lg'">
                  Button
               </KeyboardButton>
            </div>
         </div>
      </section>

      <Separator />

      <section class="row-span-1 p-4 m-4 flex flex-col">
         <div class="flex flex-col items-center justify-center">
            <h2 class="text-center font-bold text-xl">Buttons</h2>
         </div>
         <div class="grid grid-cols-3 gap-4">
            <div v-for="variant in btnVariants" :key="variant" class="flex flex-col items-center justify-center p-4">
               <Button v-for="size in btnSizes" :size="size as 'sm' | 'md' | 'lg' | 'icon' | null | undefined"
                  :variant="variant as 'default' | 'destructive' | 'outline' | 'secondary' | 'ghost' | 'link' | null | undefined">
                  Button
               </Button>
            </div>
         </div>
      </section>

      <Separator />

      <section class="row-span-1 p-4">
         <div>
            <button class="bg-button-secondary hover:bg-button-secondary/70    text-white font-bold py-2 px-4 rounded">
               Button
            </button>
         </div>
      </section>

      <Separator />
   </div>

</template>
