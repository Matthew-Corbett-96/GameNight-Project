<script lang="ts" setup>
import { Ref, ref } from 'vue'

const msg: Ref<string> = ref('')
const counter: Ref<number> = ref(0)

function add (): void {
  counter.value++
}

function sub (): void {
  counter.value--
}

</script>

<template>
  <div class="hello">
    <h1>{{ counter }}</h1>

    <input type="text" v-model="msg" />
    <h2 class="message1"> {{ msg }}</h2>

    <div>
      <h2 v-if="counter > 0">Posative Number</h2>
      <h2 v-else-if="counter < 0">Negative Number</h2>
      <h2 v-else>Zero</h2>
    </div>

    <div class="btn-wrapper">
      <button id="btn-add" @click="add">Add</button>
      <button id="btn-sub" @click="sub">Sub</button>
    </div>

  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.btn-wrapper {
  margin-top: 40px;
}

#btn-add {
  margin-right: 10px;
  background-color: #42b983;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

#btn-add:hover {
  background-color: #3da370;
}

#btn-add:disabled {
  background-color: #e0e0e0;
  color: #a4a4a4;
  cursor: not-allowed;
}

#btn-sub {
  margin-left: 10px;
  background-color: #42b983;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

#btn-sub:hover {
  background-color: #3da370;
}

#btn-sub:disabled {
  background-color: #e0e0e0;
  color: #a4a4a4;
  cursor: not-allowed;
}

</style>
