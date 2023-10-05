<script setup lang="ts">
import { defineProps } from 'vue';
import Button from '@/components/core/Button.vue';
import type { StringArray, FormData } from '@/components/core/shared/models';
import 

const emit = defineEmits(['close', 'submit']);
const props = defineProps({
   show: {
      type: Boolean,
      default: false,
      required: true
   },
   title: {
      type: String,
      required: true
   },
   lables: {
      type: Array as () => StringArray,
      required: true
   },
   url: {
      type: String,
      required: true
   }
});

function submitForm() {

   let formdata: FormData = {};

   props.lables.forEach((item) => {
      formdata[item] = document.getElementById("form").value ? document.getElementById("form").value : '';
   });

   emit('submit');
}

</script>

<template>
   <div v-if="show" class="popup-background">
      <div class="popup-main-content">
         <h1 class="title"> {{ title }}</h1>
         <section class="form-lables">
            <form action="post" @submit.prevent="submitForm" id="form">
               <div v-for="item of lables">
                  <label for=item> {{ item + ' ' }} </label>
                  <input type="text" name=item id=item />
               </div>
            </form>
         </section>
         <div class="footer">
            <Button text="Submit" @clicked="submit" />
            <Button text="Close" @clicked="emit('close')" />
         </div>
      </div>
   </div>
</template>

<style>
.popup-background {
   position: fixed;
   top: 0;
   left: 0;
   width: 100%;
   height: 100%;
   background-color: rgba(0, 0, 0, 0.5);
   display: flex;
   justify-content: center;
   align-items: center;
}

.title {
   display: flex;
   justify-content: center;
   align-items: center;
}

.popup-main-content {
   background-color: white;
   padding: 1.5rem;
   border-radius: 5px;
   box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.form-lables {
   display: grid;
   grid-template-columns: 1fr;
   grid-gap: 1rem;
   margin-top: 1rem;
   padding: 0.5rem;
}

.footer {
   display: grid;
   grid-template-columns: 1fr 1fr;
   grid-gap: 1rem;
   margin-top: 1rem;
   padding: 0.5rem;
}
</style>