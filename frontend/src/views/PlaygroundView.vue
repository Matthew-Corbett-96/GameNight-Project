<script setup lang="ts">
import { ref } from 'vue';
import { Avatar, AvatarImage, AvatarFallback } from '../@/components/ui/avatar'
import { AlertDialogRoot, AlertDialogTrigger, AlertDialogPortal, AlertDialogOverlay, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogCancel, AlertDialogAction } from 'radix-vue';
import { Button, type ButtonVariantProps} from '../@/components/ui/button'
import { Checkbox } from '../@/components/ui/checkbox'
import { Separator } from '../@/components/ui/separator';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '../@/components/ui/card';
import { KeyboardButton, type KeyboardButtonVariantProps } from '../@/components/ui/keyboardButton'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger  } from '../@/components/ui/tooltip';
import { Icon } from '@iconify/vue';
import { useColorThemeStore } from '../store/theme';

// keyboard button variants
const colors = ref(['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'gray'])
const sizes = ref(['sm', 'md', 'lg']);
// button variants
const btnVariants = ref(['default', 'secondary', 'outline', 'destructive', 'link', 'ghost'])
const btnSizes = ref(['icon', 'sm', 'md', 'lg',])
// avatar variants
const avatarSizes = ref(['sm', 'md', 'lg', 'xl'])
const avatarShapes = ref(['circle', 'square'])
const themeStore = useColorThemeStore();
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
                           <Button>Cancel</Button>
                        </AlertDialogCancel>
                        <AlertDialogAction>
                           <Button variant="destructive">Confirm</Button>
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
                  :color="color as KeyboardButtonVariantProps['color']"
                  :size="size as KeyboardButtonVariantProps['size']">
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
               <Button v-for="size in btnSizes" 
                  :size="size as ButtonVariantProps['size']"
                  :variant="variant as ButtonVariantProps['variant']">
                  Button
               </Button>
            </div>
         </div>
      </section>

      <Separator />

      <section class="row-span-1 p-4">
         <div class="flex flex-col items-center justify-center">
            <Card>
               <CardHeader>
                  <CardTitle>
                     Card Title
                  </CardTitle>
               </CardHeader>
               <CardContent>
                  <CardDescription>
                     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed
                     cursus ante dapibus diam. Sed nisi.
                  </CardDescription>
               </CardContent>
               <CardFooter>
                  <Button>Read More</Button>
               </CardFooter>
            </Card>
         </div>
      </section>

      <Separator />

      <section class="row-span-1 p-4">
         <div class="flex flex-col items-center justify-center">
            <TooltipProvider>
               <Tooltip>
                  <TooltipTrigger asChild>
                     <Button size="icon" variant="icon" @click="themeStore.toggleTheme">
                        <Icon icon="radix-icons:sun" 
                        class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 text-secondary-foreground transition-all dark:-rotate-90 dark:scale-0" />
                        <Icon icon="radix-icons:moon"
                        class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100 dark:text-primary" />
                     </Button>
                  </TooltipTrigger>
                  <TooltipContent>
                     <span>Toggle Theme</span>
                  </TooltipContent>
               </Tooltip>
            </TooltipProvider>
         </div>
      </section>
   </div>

</template>
