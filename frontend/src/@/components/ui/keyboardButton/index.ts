import { cva } from 'class-variance-authority'

export { default as KeyboardButton } from './KeyboardButton.vue'

export const buttonVariants = cva(
  "inline-block text-white font-bold border-b-4 inline-flex items-center justify-center ring-offset-background transition-colors ",
  {
    variants: {
      color: {
        purple: 
          "bg-purple-700 hover:bg-purple-600 border-purple-900 hover:border-purple-700",
        green:
          "bg-green-500 hover:bg-green-400 border-green-700 hover:border-green-500",
        red:
          "bg-red-500 hover:bg-red-400 border-red-700 hover:border-red-500",
        pink:
          "bg-pink-600 hover:bg-pink-500 border-pink-800 hover:border-pink-600",
        gray:
          "bg-gray-500 hover:bg-gray-400 border-gray-700 hover:border-gray-500",
        yellow:
          "bg-yellow-500 hover:bg-yellow-400 border-yellow-700 hover:border-yellow-500",
        blue:
          "bg-blue-500 hover:bg-blue-400 border-blue-700 hover:border-blue-500",
      },
      size: {
        md: 'h-10 px-4 py-2 rounded',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
      },
    },
    defaultVariants: {
      color: 'blue',
      size: 'md',
    },
  },
)
