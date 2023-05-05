<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import NotesPage from '@/components/NotesPage.vue' // @ is an alias to /src

@Options({
  components: {
    NotesPage
  }
})
export default class NotesView extends Vue { }
</script>

<template>
   <div class="notes">
      <NotesPage />
   </div>
</template>
