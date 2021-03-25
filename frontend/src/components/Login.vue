<template>
  <div class="auth-main white--text">
    <div class="limiter">
      <div class="container-login100" :style="`background-image: url('${bgImage}');`">
        <div class="wrap-login100 opacity-half">
          <h1 class="display-1 white--text mb-1 font-weight-medium">Login</h1>
          <p class="white--text font-weight-light">Login to Touchbase with Alias</p>
          <v-form ref="loginForm">
              <v-text-field
                v-model="username"
                class="mt-5"
                dark
                color="white"
                prepend-icon="person_pin"
                label="Username"
                @keyup.enter="submit()"
                :rules="[rules.username]"
              >
                <!-- <v-icon slot="prepend" color="white">person_pin</v-icon>
                <span slot="label" class="white--text font-weight-light">Username</span> -->
              </v-text-field>
              <!-- </v-col> -->

              <!-- <v-col cols="12" sm="12"> -->
              <v-text-field
                v-model="password"
                @keyup.enter="submit()"
                class="mt-3"
                dark
                color="white"
                prepend-icon="lock"
                label="Password"
                type="password"
                :rules="[rules.password]"
              >
                <!-- <v-icon slot="prepend" color="white">lock</v-icon>
                <span slot="label" class="white--text font-weight-light">Password</span> -->
              </v-text-field>
              <p style="cursor: pointer" class="mt-2 mb-4 font-weight-light">Forgot your password?</p>
              <v-flex class="text-xs-right">
                <v-btn @click="submit"  class="login-button" outline style="border-radius: 5px;" color="white" :loading="loading">
                  <span class="ml-1">Login</span>
                  <v-icon size="20" class="ml-2 mr-0 pr-0" color="white">keyboard_arrow_right</v-icon>
                </v-btn>
              </v-flex>
              <p v-if="feedback" class="red--text text-xs-center mt-3">Please enter valid credentials.</p>
          </v-form>
          
          
          <!-- <hr class="mt-4 mb-2" style="background-color: grey;"/> -->
          <hr class="mb-3 mt-5"/>
          <div class="text-center">
            <v-layout row justify-center>
              <span class="white--text title font-weight-light">Powered by Alias</span>
              <!-- <v-avatar size="25" class="ml-2 pb-1"><img src="/img/alias.png" alt="alias_logo"></v-avatar> -->
            </v-layout>
          </div>
        </div>
        <v-container>
          <p class="font-weight-light subheading">
            <span>Don't have an Alias Account? </span>
            <router-link tag="a" to="signup" class="white--text" href>Sign Up!</router-link>
          </p>
          <v-flex xs12 class="white--text caption font-weight-light mt-2">
            Background taken from
            <a class="white--text" style="text-decoration: none;" href="#">Joseph Hayes</a>
          </v-flex>
        </v-container>
      </div>
    </div>
  </div>
</template>

<script>
import { LOGIN_USER_MUTATION } from '@/graphql/mutations/login'
import { onLogin } from '@/apollo'

const images = ['/img/background_slider_01.jpg', '/img/background_slider_02.jpg']
export default {
  data() {
    return {
      checkbox: false,
      username: '',
      password: '',
      feedback: false,
      loading: false,

      rules: {
        username: v => /^[\w.]+$/.test(v) || 'Letters, numbers, . or _',
        password: v => v.length >= 8 || 'Password should be 8 or more characters'
      }
    }
  },
  computed: {
    bgImage () {
      var min=0; 
      var max=images.length;  
      var random = 
      Math.floor(Math.random() * (+max - +min)) + +min;
      return images[random] 
    }
  },
  methods: {
    submit() {
        if (this.$refs.loginForm.validate()) {
            this.loading = true
            const { username, password } = this.$data
            this.$apollo.mutate({
                mutation: LOGIN_USER_MUTATION,
                variables: {
                    username,
                    password
                }
            }).then(result => {
                if (result.data.login.token && result.data.login.refreshToken) {
                    onLogin(this.$apollo.provider.defaultClient, username)
                    // this.loading = false
                    location.href = '/'
                } else {
                    console.log("you\'re fake")
                }
            }).catch(err => {
                console.log(err)
                this.feedback = true
                this.loading = false
            })
            
        }
    },
  }
};
</script>

<style scoped>
.auth-main {
  text-align: center;
}
.opacity-half {
  opacity: 0.8;
}

* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}

body,
html {
  height: 100%;
}

.limiter {
  width: 100%;
  margin: 0 auto;
}

.container-login100 {
  width: 100%;
  min-height: 100vh;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 15px;

  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  position: relative;
  z-index: 1;
}

.container-login100::before {
  content: "";
  display: block;
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: rgb(70, 95, 117, 0.3);
}

.wrap-login100 {
  width: 400px;
  overflow: hidden;
  padding: 15px 55px 37px 55px;
  background-color: rgb(45, 57, 64, 0.75);
}

/**************************/

label-v-label.theme--dark {
  color: white;
  font-weight: 200 !important;
}

.auth-main .theme--light.v-input:not(.v-input--is-disabled) input,
.theme--light.v-input:not(.v-input--is-disabled) textarea {
  color: white;
}

.login-button {
  font-size: 15px;
  letter-spacing: 1px;
  width: 40%;
}
</style>