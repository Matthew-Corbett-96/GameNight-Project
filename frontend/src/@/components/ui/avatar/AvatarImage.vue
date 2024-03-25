<script setup lang="ts">
import { AvatarImage, type AvatarImageProps, type AvatarImageEmits } from 'radix-vue'

const props = defineProps<AvatarImageProps>()
// const { emit } = defineEmits<AvatarImageEmits>()
</script>

<template>
  <AvatarImage v-bind="props" class="h-full w-full object-cover" />
</template>
