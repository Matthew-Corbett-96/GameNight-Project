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
   <main>
      <div class="container">
         <header>
            <h1>Notes</h1>
            <button>+</button>
         </header>
         <div class="card-container">
            <div class="card">
               <p class="main-text"></p>
               <p class="date"></p>
            </div>
         </div>
      </div>
   </main>

   <!-- <div>
      <input type="text" v-model="tempNote" />
      <button @click="add()">Submit</button>
      <ul>
         <div v-for="note in notes" :key="note">
            <li>{{ note }}</li>
            <button @click="removeNote(note)">Done</button>
         </div>
      </ul>
   </div> -->
</template>

<style scoped>

main {
   height: 100vh;
   widows: 100vw;
   margin: 40px 0 0;
}

.container {
   max-width: 1000px;
   margin: 0 auto;
   padding: 10px;
}

header {
   display: flex;
   justify-content: space-between;
   align-items: center;
}

h1 {
   font-size: 75px;
   font-weight: bold;
   color: #333;
   margin-bottom: 20px;
}

button {
   border: none;
   padding: 10px;
   width: 50px;
   height: 50px;
   cursor: pointer;
   background-color: rgb(21, 20, 20);
   border-radius: 100%;
   color: white;
   font-size: 20px;
}

.card {
   width: 225px;
   height: 225px;
   background-color: rgb(237, 182, 44);
   display: flex;
   flex-direction: column;
   justify-content: center;
   margin-right: 20px;
   margin-left: 20px;
}
</style>
