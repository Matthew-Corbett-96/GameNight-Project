import { cva, type VariantProps } from 'class-variance-authority';

export { default as GameCard } from './gamecard.vue';


export const gameCardVariants = cva(
    '',
    {
        variants: {
            variant: {
                default:
                    'bg-button text-primary-foreground hover:bg-button/90',
            },
            size: {
                md: 'h-10 px-4 py-2',
                sm: 'h-9 rounded-md px-3',
                lg: 'h-11 rounded-md px-8',
            },
        },
        defaultVariants: {
            variant: 'default',
            size: 'md',
        },
    },
)

export interface GameCardVariantProps extends VariantProps<typeof gameCardVariants> { }