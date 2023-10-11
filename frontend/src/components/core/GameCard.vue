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
   <div class="game-box">
      <div class="game-info">
         <h3 class="game-item name "> {{ game.name }} </h3>
         <p class="game-item description"> {{ game.description }} </p>
         <p class="game-item min-player"> {{ 'Min Players:' + game.min_players }} </p>
         <p class="game-item max-player"> {{ 'Max Players:' + game.max_players }} </p>
      </div>
      <div class="bottom-bar">
         <Button @clicked="deleteGame" :text="'Delete'" class="btn" />
         <Button @clicked="updateGame" :text="'Update'" class="btn" />
      </div>
   </div>
</template>

<style scoped>


.game-box {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: rgb(255, 255, 255);
  border-radius: 0.5rem;
}

.game-item {
  margin: 0.5rem;
}

.game-item.name {
  font-size: 1.5rem;
}

.game-item.description {
  font-size: 1rem;
}

.game-item.min-player {
  font-size: 0.8rem;
}

.game-item.max-player {
  font-size: 0.8rem;
}

.bottom-bar {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

</style>