<script setup lang="ts">
import { defineProps, ref, type Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import { watch } from 'vue';
import { type FormData } from '@/main';
import { type FormField } from '@/main';


const emit = defineEmits(['cancel', 'submit']);

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
   formFields: {
      type: Array as () => Array<FormField>, 
      required: true 
   },
   formData: {
      type: Object as () => FormData,
      default: {},
      required: false
   }
});

const formData: Ref<FormData>  = ref({...props.formData});

watch(() => props.formData, (newFormData) => {
   Object.assign(formData.value, newFormData);
});

function submitForm() {
   emit('submit', formData.value);
   formData.value = {};
}

</script>

<template>
   <div v-if="show" class="popup-background">
      <div class="popup-main-content">

         <h1 class="title"> {{ title }}</h1>

         <section class="main-form">
            <form  @submit.prevent="submitForm" class="form">
               <div v-for="field in formFields" :key="field.label" class="form-items">
                  <label :for=field.label class="form-label"> {{ field.label + ' ' }} </label>
                  <input 
                  :type="field.type" 
                  :name=field.label 
                  :id=field.label 
                  v-model="formData[field.label]"
                  required 
                  class="form-input"
                  />
               </div>
            </form>
         </section>

         <div class="footer">
            <Button text="Submit" @clicked="submitForm" />
            <Button text="Cancel" @clicked="emit('cancel')" />
         </div>

      </div>
   </div>
</template>

<style scoped>
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
.popup-main-content {
   background-color: white;
   padding: 1.5rem;
   border-radius: 5px;
   box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.title {
   display: flex;
   justify-content: center;
   align-items: center;
}

.main-form {
   display: flex;
   justify-content: center;
   align-items: center;
}


.form-lables {
   margin-top: 1rem;
   padding: 0.5rem;
   border: none;
   border-radius: 0.25rem;
   box-shadow: 0 0.25rem 0.5rem rgba(0, 0, 0, 0.1);
}

.form {
   display: grid;
   grid-template-columns: 1fr 1fr;
   grid-gap: 1rem;
   margin-top: 1rem;
   padding: 0.5rem;
}

.form-input {
   margin-top: 1rem;
   padding: 0.5rem;
   border: none;
   border-radius: 0.25rem;
   box-shadow: 0 0.25rem 0.5rem rgba(0, 0, 0, 0.1);
}

.footer {
   display: grid;
   grid-template-columns: 1fr 1fr;
   grid-gap: 1rem;
   margin-top: 1rem;
   padding: 0.5rem;
}
</style>