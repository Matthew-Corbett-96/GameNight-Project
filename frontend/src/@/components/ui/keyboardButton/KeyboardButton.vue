<script setup lang="ts">
import type { VariantProps } from 'class-variance-authority'
import { Primitive, type PrimitiveProps, useForwardPropsEmits } from 'radix-vue'
import { keyboardButtonVariants, type KeyboardButtonVariantProps } from '.'
import { cn } from '../../../lib/utils'

interface Props extends PrimitiveProps {
  color?: KeyboardButtonVariantProps['color']
  size?: KeyboardButtonVariantProps['size']
  as?: string
  href?: string
}

const emits = defineEmits(['click']);

const props = withDefaults(defineProps<Props>(), {
  as: 'a',
})

const forwarded = useForwardPropsEmits(props, emits);

</script>

<template>
  <Primitive
    v-bind="forwarded"
    :class="cn(keyboardButtonVariants({ color, size }))"
  >
    <slot />
  </Primitive>
</template>
