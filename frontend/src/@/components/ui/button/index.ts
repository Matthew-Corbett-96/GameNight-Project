import { cva, type VariantProps } from 'class-variance-authority'

export { default as Button } from './Button.vue'

export const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 
          'bg-button text-primary-foreground hover:bg-button/90',
        destructive:
          'bg-destructive text-destructive-foreground hover:bg-destructive/80',
        outline:
          'border border-input bg-background hover:bg-accent hover:text-accent-foreground',
        secondary:
          'bg-button-secondary text-secondary-foreground hover:bg-button-secondary/90',
        ghost: 
          'hover:bg-accent hover:text-accent-foreground',
        link: 
          'text-primary underline-offset-4 hover:underline',
        icon:
          'bg-button-icon hover:bg-accent hover:text-accent-foreground text-secondary-forward  hover:dark:bg-button-icon/80',
      },
      size: {
        md: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'md',
    },
  },
)

export interface ButtonVariantProps extends VariantProps<typeof buttonVariants> {}