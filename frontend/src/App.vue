<template>
  <v-app class="grey lighten-4">

    <Navbar v-if="!navRoute"></Navbar>

    <v-content>
      <router-view></router-view>
    </v-content>
    <!-- <v-bottom-nav v-if="!navRoute" class="hidden-md-and-up" height="108" fixed :active.sync="bottomNav" :value="true" shift color="primary lighten-1">
        <v-layout row justify-space-around align-center wrap>
            <v-flex xs12 class="text-xs-center">
                <v-btn color="primaryComp" :value="bottomNav" v-slot="activator" flat @click="sheet = true" class="ma-0 pa-0">
                    <v-icon color="primaryComp">keyboard_arrow_up</v-icon>
                </v-btn>
                <v-divider></v-divider>
            </v-flex>
            <v-btn to="/" color="primaryComp" flat value="home" style="max-height:64px;" class="mt-0 pt-0">
                <span>Home</span>
                <v-icon large>home</v-icon>
            </v-btn>
            <v-btn to="/explore" color="primaryComp" flat value="explore" style="max-height:64px;" class="mt-0 pt-0">
                <span>Explore</span>
                <v-icon large>dashboard</v-icon>
            </v-btn>
            <v-btn to="/me" color="primaryComp" flat value="me" style="max-height:64px;" class="mt-0 pt-0">
                <span>Me</span>
                <v-icon large>person</v-icon>
            </v-btn>
        </v-layout>
    </v-bottom-nav> -->
    <!-- <BottomNav v-if="!navRoute && $vuetify.breakpoint.smAndDown"></BottomNav> -->
    <v-footer
        v-if="homeRoute && $vuetify.breakpoint.mdAndUp && loggedIn"
        app
        color="primary"
        height="55px"
        dark
    >
        <v-spacer></v-spacer>
        <v-btn flat round class="mx-2" to="contact" color="primaryComp">Contact Us</v-btn>
        <v-btn flat round class="mx-2" to="help" color="primaryComp">Help</v-btn>
        <v-btn flat round class="mx-2" to="advertise" color="primaryComp">Advertise</v-btn>
        <v-icon large class="mx-4" color="white">dashboard</v-icon>
        <v-btn flat round class="mx-2" to="changelog" color="primaryComp">Changelog</v-btn>
        <v-btn flat round class="mx-2" to="/legal/terms" color="primaryComp">Terms</v-btn>
        <v-btn flat round class="mx-2" to="/legal/privacy" color="primaryComp">Privacy</v-btn>
        <v-spacer></v-spacer>
    </v-footer>

  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
import BottomNav from '@/components/BottomNav'
import { CREATE_SITEVISIT_MUTATION } from '@/graphql/mutations/createSiteVisit'
import { CREATE_PROFILEVISIT_MUTATION } from '@/graphql/mutations/createProfileVisit'

export default {
  name: 'App',
  components: { Navbar, BottomNav },
  data () {
    return {
      isProfile: false,
    }
  },
  computed: {
    navRoute() {
      // console.log(this.$route)
      return this.$route.path === '/signup' || this.$route.path === '/login' || (this.homeRoute && !this.loggedIn) || (this.$route.query.redirect && !this.loggedIn)
    },
    homeRoute() {
      return this.$route.fullPath === '/'
    },
    loggedIn() {
        // NOTE: make sure to validate the jwt-token with the verifyToken mutation!
        if (localStorage.getItem('jwt-token')) {
            return true
        } else {
            return false
        }
    },
  },
  methods: {
    createProfileVisit(viewee) {
      if (this.loggedIn) {
        this.$apollo.mutate({
          mutation: CREATE_PROFILEVISIT_MUTATION,
          variables: {
            viewee
          }
        }).then(result => {
          if (result.data.createProfileVisit.success) {
            console.log('good memes have occurred')
          } else {
            console.log("authenticate yo anon ass!")
          }
        }).catch(err => {
          console.log("authenticate yo anon ass!")
        })
      }
    },
    createSiteVisit(page) {
      if (this.loggedIn) {
        this.$apollo.mutate({
          mutation: CREATE_SITEVISIT_MUTATION,
          variables: {
            page
          }
        }).then(result => {
          if (result.data.createSiteVisit.success) {
            console.log('good memes have occurred')
          } else {
            console.log("authenticate yo anon ass!")
          }
        }).catch(err => {
          console.log("authenticate yo anon ass!")
        })
      }
    }
  },
  created() {
    // if (this.loggedIn) {
    //   console.log('memes, 123')
    // } else {
    //   console.log('123, memes')
    // }
    if (this.loggedIn) {
      if (this.$route.name === 'Profile') {
        // viewer (current user), viewee (params.username), timestamp, interest_tags of viewee
        /*
          Script like spf for Who To Follow, SELECT all users where amount of ProfileVisit > 10
          then for each user go through ProfileVisit's and find repeated interest tags. If same
          interest tag appears >=40% of the time, and the user does not already have it, add it.
          ALSO, if same user appears more than once and IT matches viewer IT, add to list of
          candidates for Who To Follow, store in database.
          
          backup -> At end of pass, must be minimum of 100 candidates at a time. If not 100,
          select popular users who have similar interest tags and get to 100.

          When db queried, select top 10 at a time, display in shuffled order on frontend. (paginated)

          if each user in in this list takes 1 second (no idea how long in reality) and we have 
          40k users, one pass of this algo will take ~12hrs, meaning candidates can get frequent
          updates.
        */
       // NOTE: don't store usernames as strings in db as they can be changed!!
        // NOTE: link analytics: not going to store analytics as strings in the DB. When someone clicks the analytics button on their link, all of that will be processed then to avoid old nonsense data in db
        // console.log(this.$route.params.username, 'ProfileVisit object gets made')
        this.createProfileVisit(this.$route.params.username)
      } else {
        // stores timestamp, user, and page. Number of SiteVisit where page=page is click count
        // console.log(this.$route.name, 'SiteVisit object, +1 clicks on whatever page it is')
        if (!this.$route.query.redirect) {
          this.createSiteVisit(this.$route.name)
        }
      }
    }
    
  },
  watch: {
    $route (to, from) {
      if (to.name === 'Profile') {
        // console.log(to.params.username, 'ProfileVisit object gets made watch')
        this.createProfileVisit(to.params.username)
      } else {
        // console.log(to.name, 'SiteVisit object, +1 clicks on whatever page it is watch')
        if (!to.query.redirect) {
          this.createSiteVisit(to.name)
        }
      }
    }
  },
}
</script>

<style>
html {
  overflow-y: auto;
  scrollbar-color: #aaa #ddd;
  scrollbar-width: thin;
}

::-webkit-scrollbar {
    width: 9px;
}

::-webkit-scrollbar-track {
  /* -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); */
  /* -webkit-border-radius: 10px; */
  /* border-radius: 10px; */
  background: rgba(221, 221, 221, 1);
}

::-webkit-scrollbar-thumb {
  -webkit-border-radius: 10px;
  border-radius: 10px;
  background: #aaa;
}
</style>