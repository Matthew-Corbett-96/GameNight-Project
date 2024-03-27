<script setup lang="ts">
import { AvatarRoot, type AvatarRootProps } from 'radix-vue'
import { avatarVariant, type AvatarVariantProps } from '.'
import { cn } from '../../../lib/utils'

interface Props extends AvatarRootProps {
  size?: AvatarVariantProps['size']
  shape?: AvatarVariantProps['shape']
  class?: string
}

const props = withDefaults(defineProps<Props>(), {
  size: 'sm',
  shape: 'circle',
})
</script>

<template>
  <AvatarRoot :class="cn(avatarVariant({ size, shape }), props.class)">
    <slot />
  </AvatarRoot>
</template>
