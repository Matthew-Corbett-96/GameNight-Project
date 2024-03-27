<script setup lang="ts">
import { AvatarImage, type AvatarImageProps, type AvatarImageEmits, useForwardPropsEmits } from 'radix-vue'

const props = defineProps<AvatarImageProps>();
const emit = defineEmits<AvatarImageEmits>();
const forwarded = useForwardPropsEmits(props, emit);
</script>

<template>
  <AvatarImage v-bind="forwarded" class="h-full w-full object-cover" />
</template>
