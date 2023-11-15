<script setup lang="ts">
import { defineProps, ref, type Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import { type Game } from '@/main';

const emit = defineEmits(['delete', 'update']);

const props = defineProps({
   game: {
      type: Object as () => Game,
      required: true
   }
});

function updateGame() {
   emit('update', props.game);
}

function deleteGame() {
   emit('delete', props.game);
}

</script>

<template>
   <v-card class="mt-2 ml-2 mr-2">

         <v-card-item class="text-center" >
            <v-card-title> {{ game.name }} </v-card-title>
            <v-card-subtitle> {{ game.description }}</v-card-subtitle>
         </v-card-item>

         <v-divider></v-divider>

         <v-expansion-panels>
            <v-expansion-panel>

               <v-expansion-panel-title>
                 <p class="text-body1 font-weight-medium"> more info . . .  </p>
               </v-expansion-panel-title>
               
               <v-expansion-panel-text>
                  <v-card-subtitle> {{ 'ID:' + game.id }} </v-card-subtitle>
                  
                  <v-card-item>
                     <v-card-subtitle> {{ 'Created:' + game.created_on }} </v-card-subtitle>
                  </v-card-item>

                  <v-card-item>
                     <v-card-subtitle> {{ 'Updated:' + game.updated_on }} </v-card-subtitle>
                  </v-card-item>

                  <v-card-item>
                     <v-card-subtitle> {{ 'Min Players:' + game.min_players }} </v-card-subtitle>
                  </v-card-item>

                  <v-card-item>
                     <v-card-subtitle> {{  'Max Players:' + game.max_players }} </v-card-subtitle>
                  </v-card-item>
               </v-expansion-panel-text>

            </v-expansion-panel>
         </v-expansion-panels>

      <v-divider></v-divider>         

      <v-card-actions>
         <v-row>
            <v-col cols="12" sm="6">
               <Button @clicked="deleteGame" text="Delete" />
            </v-col>
            <v-col cols="12" sm="6">
               <Button @clicked="updateGame" text="Update" />
            </v-col>
         </v-row>
      </v-card-actions>

   </v-card>
</template>