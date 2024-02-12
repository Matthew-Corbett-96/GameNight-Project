<script setup lang="ts">
import { ref, type Ref } from 'vue';
import { RouterLink } from 'vue-router';
import {Button} from '../@/components/ui/button';
import { useAuthStore } from '../store/auth';
import { Separator } from '../@/components/ui/separator';




const authStore = useAuthStore();

function navigateToRegister(): void {
  authStore.Register();
}

</script>


<template>
  <!-- <div class="bg-[url('src/assets/boardgameImg.jpg')] bg-cover">
    <div class=" backdrop-blur-xl bg-white/30"> -->
      <div class="grid grid-cols-6 gap-20 prose prose-slate mx-auto base:prose-base">
  <div class="col-start-1 col-end-2  sticky top-0 py-10 -mx-20 flex flex-col  ">
    <div class="fixed drop-shadow-md hover:drop-shadow-xl">
      <a href="#sec-about-gamenight" class="block text-black py-1 px-2 no-underline hover:bg-gray-300">About</a>
    <a href="#sec-rules" class="block text-black no-underline py-1 px-2 hover:bg-gray-300">Rules</a>
    <a href="#sec-games" class="block text-black no-underline py-1 px-2 hover:bg-gray-300">Games</a>
    <a href="#sec-community" class="block text-black no-underline py-1 px-2 hover:bg-gray-300">Community</a>
    <a href="#sec-join" class="block text-black no-underline py-1 px-2 hover:bg-gray-300">Join</a>
    </div>  
  </div>
  
  <div class="col-start-2 col-end-2 top-0 py-6 flex flex-col  ">
  <Separator orientation="vertical" class="my-4"/>
  </div>

  <div class="col-start-3 col-end-10 -mx-16">
    <div id="sec-about-gamenight"></div>
    <section  class="about">
      <h3 >About Game Night</h3>
      <p>
        Welcome to our Game Night, a cherished tradition where friends,
        family, and fellow game enthusiasts gather to explore worlds,
        build empires, and create cherished memories! Our Game Nights are
        not just an event but a community where we celebrate camaraderie,
        friendly competition, and the joy of gaming. Whether you're a
        seasoned gamer or a newcomer eager to dive into the exciting world
        of board games, card games, and more, our Game Night is a space
        where you'll always find a warm welcome and a seat at the table.
      </p>
      <p>
        In a world that often rushes by, Game Night is our way of taking a
        pause, connecting with others, and indulging in the simple
        pleasures of play. It's where strategies are formed, alliances are
        forged, and occasionally, where friendly rivalries are born.
        Through every roll of the dice, shuffle of the cards, and
        triumphant victory cheer, we create moments that linger, stories
        that are retold, and friendships that are deepened.
      </p>
    </section>
    <br>

    <div id="sec-rules"></div>
    <section class="rules-section">
      <h3>Our Rules</h3>
      <p class="lead">
        At Game Night, we believe in fair play, respect, and above all,
        fun! Here are a few guidelines to ensure everyone has a great
        time:
      </p>
      <ul class="rules-list rules-list-header">
        <li>Rule 1</li>
        <li>Rule 2</li>
        <li>Rule 3</li>
        <li>Rule 4</li>
        <li>Rule 5</li>
        <li>Rule 6</li>
      </ul>
    </section>
    <br>

    <div id="sec-games"></div>
    <section class="games-section">
      <h2>Our Games</h2>
      <p>
        Our Game Night features a wide variety of games, from classic
        favorites to the latest releases. We have games for every age and
        skill level, so whether you're a seasoned gamer or a newcomer
        eager to dive into the exciting world of board games, card games,
        and more, our Game Night is a space where you'll always find a
        warm welcome and a seat at the table.
      </p>
    </section>
    <br>

    <div id="sec-community"></div>
    <section class="community-section">
      <h2>Our Community</h2>
      <p>
        Our Game Night is not just an event but a community where we
        celebrate camaraderie, friendly competition, and the joy of
        gaming. In a world that often rushes by, Game Night is our way of
        taking a pause, connecting with others, and indulging in the
        simple pleasures of play. It's where strategies are formed,
        alliances are forged, and occasionally, where friendly rivalries
        are born. Through every roll of the dice, shuffle of the cards,
        and triumphant victory cheer, we create moments that linger,
        stories that are retold, and friendships that are deepened.
      </p>
    </section>
    <br>

    <section id="sec-join" class="grid grid-flow-row gap-3">
      <h2>How to Join</h2>
      <p>
        Joining our Game Night is easy! Simply fill out the form below and
        we'll send you an email with all the details you'll need to join
        us for our next Game Night. We look forward to seeing you there!
      </p>
    </section>
    <Button variant="default" size="sm" @clicked="navigateToRegister" class="mx-52">
        Click Here To Register
      </Button>
    <section class="quote-section">
      <blockquote>
        <p>Play is the highest form of research.</p>
      </blockquote>
      <p>- Albert Einstein</p>
      
    </section>
  </div>
</div>
    <!-- </div>
</div> -->
</template>

<style scoped>
</style>
