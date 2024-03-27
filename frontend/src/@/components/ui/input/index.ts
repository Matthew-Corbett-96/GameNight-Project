export { default as Input } from './Input.vue'
import type { VariantProps } from 'class-variance-authority';
import { cva } from 'class-variance-authority'

export const inputVariants = cva(
  `flex w-full rounded-md border border-input bg-background
   ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground 
   focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 
   disabled:cursor-not-allowed disabled:opacity-50`,
  {
    variants: {
      variant: {
        default: 'text-primary-foreground focus-visible:ring-primary',
        destructive: 'text-destructive-foreground',
        secondary: 'text-secondary-foreground',
        ghost: 'text-accent-foreground',
      },
      size: {
        sm: 'h-9 px-3 text-sm',
        md: 'h-10 px-3 py-2 text-md',
        lg: 'h-11 px-5 py-2 text-lg',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'md',
    },
  },
)

export interface InputVariantProps extends VariantProps<typeof inputVariants> {}