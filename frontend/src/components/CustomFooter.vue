<script setup lang="ts">

const links = [
  'About Us',
  'Contact Us',
  'Legal',
  'Privacy Policy',
  'Terms of Use'
]

</script>


<template>
  <v-footer class="bg-grey-lighten-1">
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="link in links"
        :key="link"
        color="primary"
        variant="text"
        class="mx-2"
        rounded="xl"
      >
        {{ link }}
      </v-btn>
      <v-col class="text-center mt-4" cols="12">
        {{ new Date().getFullYear() }} — <strong>White Fence Gang LLC</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>


<style scoped>

.container {
   max-width: 100vw;
   background-color: aqua;
}

</style>