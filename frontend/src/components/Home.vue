<template>
  <div class="home-div" v-if="toushLink">
    <Toush :toush-string="this.$route.query.redirect" />
  </div>
  <div class="home-div" v-else-if="loggedIn">
    <Dashboard />
  </div>
  <div class="home-div" v-else>
    <Landing />
  </div>
</template>

<script>
import Dashboard from '@/components/Dashboard'
import Landing from '@/components/Landing'
import Toush from '@/components/Toush'

  export default {
    components: {
      Dashboard,
      Landing,
      Toush
    },
    data() {
      return {
        
      }
    },
    computed: {
    loggedIn() {
      // make sure to validate the jwt-token with the verifyToken mutation!
      if (localStorage.getItem('jwt-token')) {
        return true
      } else {
        return false
      }
        // return this.$store.state.loggedIn
    },
    toushLink() {
      if (this.$route.query.redirect) {
        return true
      } else {
        return false
      }
    }
  },
  }
</script>

<style>
.home-div {
  width: 100%;
  height: 100%;
}
</style>
