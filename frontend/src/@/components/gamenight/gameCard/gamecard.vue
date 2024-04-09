<script setup lang="ts">
import type { Game } from 'src/main';
import { type GameCardVariantProps } from './index';
import type { PrimitiveProps } from 'radix-vue';
import { type HTMLAttributes } from 'vue';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '../../ui/card';
import { Button } from '../../ui/button';
import { Dialog, DialogClose, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger, DialogFooter } from '../../ui/dialog';
import { Input } from '../../ui/input';
import { Label } from '../../ui/label';
import { toTypedSchema } from '@vee-validate/zod';
import zod from 'zod';
import { useForm, useField } from 'vee-validate';


interface Props extends PrimitiveProps {
    variant?: GameCardVariantProps['variant']
    size?: GameCardVariantProps['size']
    class?: HTMLAttributes['class']
    game: Game
}

const props = defineProps<Props>();

const emits = defineEmits<{
    delete: [game: Game],
    update: [values: any]
}>();

// schema for game form 
const schema = toTypedSchema(zod.object({
    name: zod.string().min(2).max(50),
    description: zod.string().min(2).max(1000),
    min_players: zod.number().min(1).max(20),
    max_players: zod.number().min(1).max(20),
}));

const { handleReset, errors, handleSubmit } = useForm({
    validationSchema: schema,
    initialValues: {
        name: props.game.name,
        description: props.game.description,
        min_players: props.game.min_players,
        max_players: props.game.max_players
    }
});

const { value: name } = useField('name');
const { value: description } = useField('description');
const { value: min_players } = useField('min_players');
const { value: max_players } = useField('max_players');

// function to submit form
const onSubmit = handleSubmit((values) => {
    emits('update', values);
});

function cancel() {
    handleReset();
}

</script>

<template>
    <div class="flex flex-col items-center">
        <Card class=" bg-blue-200 bg-opacity-10 p-4 rounded-lg shadow-md mb-5 mt-5">
            <CardHeader>
                <CardTitle>{{ props.game.name }}</CardTitle>
                <CardDescription>{{ props.game.description }}</CardDescription>
            </CardHeader>
            <CardContent>
                <p>Min Players: {{ props.game.min_players }}</p>
                <p>Max Players: {{ props.game.max_players }}</p>
            </CardContent>
            <CardFooter>
                <div class="flex space-x-2">
                    <Dialog class="items-center mb-5 flex space-x-2">
                        <div class="flex items-center justify-center">
                            <DialogTrigger asChild>
                                <Button class="out">Update</Button>
                            </DialogTrigger>
                        </div>
                        <DialogContent>
                            <DialogHeader>
                                <DialogTitle>Update Game</DialogTitle>
                                <DialogDescription>
                                    Make changes to game here. Click save when you're done.
                                </DialogDescription>
                            </DialogHeader>
                            <div>
                                <form @submit="onSubmit">
                                    <div class="mb-5">
                                        <Label for="name">Name</Label>
                                        <input v-model="name"
                                            class="mt-1 flex w-full rounded-md border border-input bg-background ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 text-primary-foreground focus-visible:ring-primary h-10 px-3 py-2 text-md" />
                                        <span class="text-destructive"> {{ errors.name }} </span>
                                    </div>
                                    <div class="mb-5 flex items-center space-x-2">
                                        <div class="w-50">
                                            <Label for="description">Description</Label>
                                            <input v-model="description"
                                                class="mt-1 flex w-full rounded-md border border-input bg-background ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 text-primary-foreground focus-visible:ring-primary h-10 px-3 py-2 text-md">
                                            <span class="text-destructive"> {{ errors.description }} </span>
                                        </div>
                                        <div class="w-50">
                                            <Label for="min_players">min_players</Label>
                                            <input v-model="min_players" type="number"
                                                class="mt-1 flex w-full rounded-md border border-input bg-background ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 text-primary-foreground focus-visible:ring-primary h-10 px-3 py-2 text-md">
                                            <span class="text-destructive"> {{ errors.min_players }} </span>
                                        </div>
                                        <div class="w-50">
                                            <Label for="max_players">max_players</Label>
                                            <input v-model="max_players" type="number"
                                                class="mt-1 flex w-full rounded-md border border-input bg-background ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 text-primary-foreground focus-visible:ring-primary h-10 px-3 py-2 text-md">
                                            <span class="text-destructive"> {{ errors.max_players }} </span>
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <DialogClose>
                                <Button @click="cancel" variant="outline" class="m-2">Cancel</Button>
                                <Button @click="onSubmit">Save</Button>
                            </DialogClose>
                        </DialogContent>
                    </Dialog>
                    <Button class="fill" @click="emits('delete', props.game)">Delete</Button>
                </div>
            </CardFooter>
        </Card>
    </div>
</template>

<style scoped>
.out {
    background: transparent;
    color: rgba(0, 212, 255, 0.9);
    border: 1px solid rgba(0, 212, 255, 0.6);
    transition: all .3s ease;

}

.out:hover {
    transform: scale(1.125);
    color: rgba(255, 255, 255, 0.9);
    border-color: rgba(255, 255, 255, 0.9);
    transition: all .3s ease;
}
</style>