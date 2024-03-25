<script setup lang="ts">
import { AvatarRoot, type AvatarRootProps } from 'radix-vue'
import { avatarVariant } from '.'
import { cn } from '../../../lib/utils'
import type { VariantProps } from 'class-variance-authority';

interface AvatarVariantProps extends VariantProps<typeof avatarVariant> {}


// This may cause issue b/c I added AvatarRootProps as parent interface
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
  <AvatarRoot 
    :class="cn(avatarVariant({ size, shape }), props.class)">
    <slot />
  </AvatarRoot>
</template>
