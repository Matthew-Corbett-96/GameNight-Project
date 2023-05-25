<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'


function expandNav() {

}

</script>

<template>
   <div class="nav-container">
      <nav>
         <ul>
            <li>
               <RouterLink class="item" to="/">Dashboard</RouterLink>
            </li>
            <li>
               <RouterLink class="item" to="/about">About</RouterLink>
            </li>
            <li>
               <RouterLink class="item" to="/games">Games</RouterLink>
            </li>
            <li>
               <RouterLink class="item" to="/login">Login</RouterLink>
            </li>
            <li>
               <RouterLink class="item" to="/register">Register</RouterLink>
            </li>
         </ul>
      </nav>
   </div>
</template>

<style scoped>

.nav-container {

}

nav {
   color: black;
   background-color: antiquewhite;
   padding: 1rem 0;
}

nav ul {
   display: flex;
   justify-items: stretch;
   /* align-items: center; */
   list-style: none;
   margin: 0;
   padding: 0;
}

nav li {
   margin: 0;
   padding: 0;
}

nav .item {
   color: black;
   text-decoration: none;
   font-weight: bold;
   padding: 1.25rem 2.55rem;
   background-color: aqua;
}

nav .item:hover {
   color: #ccccccf9;
   background-color: aquamarine;
}

nav .item:active {
   color: #d11515;
}

</style>