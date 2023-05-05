<script lang="ts" setup>
import { Ref, ref } from 'vue'

const tempNote: Ref<string> = ref('')
const notes: Ref<string[]> = ref([])

function add (): void {
  notes.value.push(tempNote.value)
  tempNote.value = ''
}

function removeNote (note: string): void {
  const index = notes.value.indexOf(note)
  notes.value.splice(index, 1)
}

</script>

<template>
   <h1>Notes</h1>

   <div>
      <input type="text" v-model="tempNote" />
      <button @click="add()">Submit</button>
      <ul>
         <div v-for="note in notes" :key="note">
            <li>{{ note }}</li>
            <button @click="removeNote(note)">Done</button>
         </div>
      </ul>
   </div>
</template>

<style scoped>
h3 {
   margin: 40px 0 0;
}
</style>
