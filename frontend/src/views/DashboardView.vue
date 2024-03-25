<script setup lang="ts">
// import avatar component 
import { Avatar, AvatarImage, AvatarFallback } from '../@/components/ui/avatar'
import { AlertDialogRoot, AlertDialogTrigger, AlertDialogPortal, AlertDialogOverlay, AlertDialogContent, AlertDialogTitle, AlertDialogDescription, AlertDialogCancel, AlertDialogAction } from 'radix-vue';
import { Button } from '../@/components/ui/button'
import { Checkbox } from '../@/components/ui/checkbox'

</script>

<template>
  <h1>
    Dashboard
  </h1>
  <Avatar shape="square" size="lg">
    <AvatarImage src="../assets/logoo.jpg">
      <AvatarFallback>
        <span>JD</span>
      </AvatarFallback>
    </AvatarImage>
  </Avatar>

  <!-- IDEA: lets make our own component of this and only give them access to the props they need to give us the words  -->
  <AlertDialogRoot>
    <AlertDialogTrigger >
      <Button>Open Dialog</Button>
    </AlertDialogTrigger>
    <AlertDialogPortal>
      <AlertDialogOverlay />
      <AlertDialogContent>
        <AlertDialogTitle >
          Delete your account
        </AlertDialogTitle>
        <AlertDialogDescription class="text-center text-base">
          Are you sure you want to delete your account? All of your data will be permanently removed. This action cannot be undone.
        </AlertDialogDescription>
        <div class="flex justify-center mt-4">
          <AlertDialogCancel >
            <Button>Cancel</Button>
          </AlertDialogCancel>
          <AlertDialogAction >
            <Button :variant="'destructive'">Delete</Button>
          </AlertDialogAction>
        </div>
      </AlertDialogContent>
    </AlertDialogPortal>
  </AlertDialogRoot>

  <div class="flex flex-col gap-2.5">
    <label class="flex flex-row gap-4 items-center [&>.checkbox]:hover:bg-neutral-100">
      <Checkbox
        v-model:checked="checkboxOne"
      >
      </Checkbox>
      <span class="select-none text-white">Accept terms and conditions.</span>
    </label>
  </div>

</template>

<style scoped></style>
