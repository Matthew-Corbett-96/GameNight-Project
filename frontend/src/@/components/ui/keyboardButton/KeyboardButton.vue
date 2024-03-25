<script setup lang="ts">
import type { VariantProps } from 'class-variance-authority'
import { Primitive, type PrimitiveProps } from 'radix-vue'
import { buttonVariants } from '.'
import { cn } from '../../../lib/utils'

interface ButtonVariantProps extends VariantProps<typeof buttonVariants> {}

interface Props extends PrimitiveProps {
  color?: ButtonVariantProps['color']
  size?: ButtonVariantProps['size']
  as?: 'a'
  href?: string
}

const props = withDefaults(defineProps<Props>(), {
  as: 'a',
})
</script>

<template>
  <Primitive
    v-bind="props"
    :class="cn(buttonVariants({ color, size }))"
  >
    <slot />
  </Primitive>
</template>
