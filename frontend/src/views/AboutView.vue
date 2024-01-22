<script setup lang="ts">
import { ref } from 'vue';
import type { Ref } from 'vue';
import Button from '@/components/core/Button.vue';
import router from '@/router';

function navigateToRegister() {
  router.push('/register');
}

</script>


<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-card id="card">
          <v-layout>
            <v-navigation-drawer floating permanent>
              <v-list density="compact" nav>

                <v-list-item title="About Game Night" value="About Game Night">
                 
                </v-list-item>

                <v-list-item title="Rules" value="rules"> 
                  
                </v-list-item>

                <v-list-item title="Game Features" value="Game Features">
                  
                </v-list-item>

                <v-list-item title="Community" value="Community"></v-list-item>
                <v-list-item title="Join" value="Join"></v-list-item>
              </v-list>
            </v-navigation-drawer>
            <v-main  id="main"></v-main>
          </v-layout>
        </v-card>
      </v-col>
      <v-divider vertical></v-divider>
      <v-col cols="8">
        <v-sheet class="pa-2 ma-2">
          <section id="sec1" class="about-section">
            <h1 class="font-weight-thin">About Game Night</h1>
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

          <section class="rules-section">
            <h2 id="sec3" class="font-weight-thin">Our Rules</h2>
            <h3 class="rules-aside">
              At Game Night, we believe in fair play, respect, and above all,
              fun! Here are a few guidelines to ensure everyone has a great
              time:
            </h3>
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

          <section class="games-section">
            <h2 id="sec2" class="font-weight-thin">Our Games</h2>
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

          <section class="community-section">
            <h2 class="font-weight-thin">Our Community</h2>
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

          <section class="join-section">
            <h2 class="font-weight-thin">How to Join</h2>
            <p>
              Joining our Game Night is easy! Simply fill out the form below and
              we'll send you an email with all the details you'll need to join
              us for our next Game Night. We look forward to seeing you there!
            </p>
            <button
              :text="'Click Here To Register'"
              @clicked="navigateToRegister"
            ></button>
          </section>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
  <section class="quote-section">
    <p class="quote">“Play is the highest form of research.” - Albert Einstein</p>
  </section>
</template>



<style scoped>
.quote {
  font-style: italic;
  text-align: center;
}
#main{
  height: 250px;
}
#card{
  position: fixed !important ;
}

</style>
