<template>
  <div class="auth-main white--text">
    <div class="limiter">
      <div class="container-login100" :style="`background-image: url('${bgImage}');`">
        <div class="wrap-login100 opacity-half">
          <h1 class="display-1 mb-0 pb-0 font-weight-medium white--text">Register</h1>
          <p class="white--text mt-1 pt-0 font-weight-light">Register for Touchbase with Alias</p>

          <!-- ****************************** -->
          <v-form ref="signupForm">
              <v-stepper v-model="e1">
                <v-stepper-header class="hidden-md-and-up hidden-sm-and-down">
                <v-stepper-step step="1"></v-stepper-step>

                <v-stepper-step step="2"></v-stepper-step>

                <v-stepper-step step="3"></v-stepper-step>
                </v-stepper-header>

                <v-stepper-items>
                <v-stepper-content step="1" class="pa-0">
                    <v-container>
                        <p class="font-weight-light text-left mb-0 white--text">What is your name?</p>

                        <v-text-field
                        v-model="firstName"
                        dark
                        @keyup.enter="e1++"
                        color="white"
                        label="First Name"
                        :rules="[rules.name, rules.required]"
                        validate-on-blur
                        ></v-text-field>

                        <v-text-field
                        v-model="lastName"
                        dark
                        @keyup.enter="e1++"
                        color="white"
                        label="Last Name"
                        :rules="[rules.name, rules.required]"
                        validate-on-blur
                        ></v-text-field>
                        <!-- <v-btn color="white" outlined @click="e1 = 2">Next</v-btn> -->
                    </v-container>
                </v-stepper-content>

                <v-stepper-content step="2" class="pa-0">
                    <v-container>
                        <p class="font-weight-light text-left mb-0 white--text">Some info about you</p>

                        <v-select
                        dark
                        color="white"
                        @keyup.enter="e1++"
                        v-model="country"
                        :items="countriesList"
                        label="Country"
                        :rules="[rules.required]"
                        validate-on-blur
                        ></v-select>

                        <v-select
                        dark
                        color="white"
                        v-model="language"
                        @keyup.enter="e1++"
                        :items="languagesList"
                        label="Language"
                        :rules="[rules.required]"
                        validate-on-blur
                        ></v-select>

                        <v-menu
                            ref="menu"
                            v-model="menu"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            lazy
                            transition="scale-transition"
                            offset-y
                            full-width
                            min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="birthday"
                                dark
                                @keyup.enter="e1++"
                                color="white"
                                :rules="[rules.required]"
                                label="Birthday"
                                readonly
                                validate-on-blur
                                v-on="on"
                            ></v-text-field>
                            </template>
                            <!-- color="blue-grey darken-1" -->
                            <v-date-picker
                                ref="picker"
                                dark
                                color="grey"
                                v-model="birthday"
                                :max="new Date().toISOString().substr(0, 10)"
                                min="1950-01-01"
                                @change="$refs.menu.save(birthday)"
                            ></v-date-picker>
                        </v-menu>

                    </v-container>
                </v-stepper-content>

                <v-stepper-content step="3" class="pa-0">
                    <v-container class="ma-0">
                        <p class="font-weight-light text-left mb-0 white--text">Your account details</p>

                        <v-text-field
                        v-model="username"
                        dark
                        color="white"
                        @keyup.enter="e1++"
                        @keyup="unique('u')"
                        :error="uniqueUsernameError"
                        :error-messages="uniqueUsernameErrorMessages"
                        label="Username"
                        :rules="[rules.username, rules.required]"
                        validate-on-blur
                        ></v-text-field>

                        <v-text-field
                        v-model="email"
                        dark
                        @keyup.enter="e1++"
                        @keyup="unique('e')"
                        :error="uniqueEmailError"
                        :error-messages="uniqueEmailErrorMessages"
                        color="white"
                        label="Email"
                        :rules="[rules.required]"
                        validate-on-blur
                        ></v-text-field>

                        <v-text-field
                        v-model="password"
                        dark
                        @keyup.enter="e1++"
                        color="white"
                        label="Password"
                        type="password"
                        :rules="[rules.password, rules.required]"
                        validate-on-blur
                        ></v-text-field>

                        <v-text-field
                        v-model="verifyPassword"
                        dark
                        @keyup.enter="e1++"
                        color="white"
                        label="Verify Password"
                        type="password"
                        class="mb-0"
                        :rules="[rules.verifyPassword, rules.required]"
                        hint="Enter password again"
                        persistent-hint
                        validate-on-blur
                        ></v-text-field>
                        
                    </v-container>
                </v-stepper-content>

                <v-stepper-content step="4" class="pa-0">
                    <v-container class="ma-0">
                        <p class="font-weight-light text-left mb-3 white--text">Your profile picture</p>
                        
                        <img-inputer v-if="!cropping && !cropped" icon="img" class="mb-1" accept="image/*" :maxSize="1024" @onExceed="exceedHandler" @onChange="fileChange"
                          no-mask no-multiple-text="Only one image" exceed-size-text="Too large! File size must be below "
                          placeholder="Drag and drop a picture or click to browse" style="background-color: rgba(0, 0, 0, 0.15); max-height: 100%; max-width: 100%;"
                        />
                        <template
                          v-if="cropping && !cropped"
                        >
                          <Cropper
                            ref="cropper"
                            :stencil-props="{
                              aspectRatio: 1
                            }"
                            classname="crop-img"
                            :src="file"
                          />
                          <v-layout row>
                            <v-btn @click="resetImage" block color="white" flat>
                              <v-icon>close</v-icon>
                            </v-btn>
                            <v-btn @click="crop" block color="white" flat>
                              <v-icon>check</v-icon>
                            </v-btn>
                          </v-layout>
                        </template>
                        <!-- <img-inputer v-if="cropped" class="mb-1" no-mask readonly :imgSrc="fileUrl"
                          placeholder="Drag and drop a picture or click to browse" style="background-color: rgba(0, 0, 0, 0.15);"
                        /> -->
                        <v-badge v-if="cropped" color="grey darken-3" overlap>
                          <v-icon style="cursor: pointer;" @click="resetImage" dark slot="badge">close</v-icon>
                          <img class="elevation-3" style="border-radius: 10px;" :src="fileUrl"></img>
                        </v-badge>
                        
                        
                        
                        <!-- <FileUpload ref="signupDropzone" id="signupDropzone" :options="dropzoneOptions" includeStyling /> -->
                        <!-- <v-avatar
                          size="100"
                          color="primary"
                        >
                          <img ref="profilePicturePreview" src="/img/avatar-1.png" alt="alt">
                        </v-avatar> -->
                        <!-- <ImageUpload 
                          @finished="saveClicked"
                          :width="400"
                          :height="400"
                        />
                        <img ref="image"> -->
                        <!-- <v-btn color="white" outline @click="saveClicked">
                          <span>Done</span>
                          <v-icon>check</v-icon>
                        </v-btn> -->
                    </v-container>
                </v-stepper-content>

                <v-btn v-if="e1 > 1" text flat color="white" class="mb-5 mt-0" @click="e1--" style="border-radius: 4px;">Back</v-btn>
                <v-btn v-if="e1 < 4"color="white" class="mb-5 mt-0" outline @click="e1++" style="border-radius: 4px;">Next</v-btn>
                <!-- <v-btn v-else color="white" class="mb-5 mt-0" outline @click="submit" style="border-radius: 4px;">Register</v-btn> -->
                <v-btn v-else color="white" class="mb-5 mt-0" outline @click="submit" :loading="loading" style="border-radius: 4px;">
                    <span class="ml-1">Register</span>
                    <v-icon size="20" class="ml-2 mr-0 pr-0" color="white">keyboard_arrow_right</v-icon>
                </v-btn>
                <p v-if="feedback" class="red--text">Please fill out the form.</p>
                </v-stepper-items>
            </v-stepper>
          </v-form>
          
          <!--------------------------------------------------------------------->
            <!-- <p>
              Already have an account?
              <router-link tag="a" to="login" class="white--text" href>Login!</router-link>
            </p> -->

          <hr />
          <div class="text-center mt-4">
            <span class="white--text title font-weight-light">Powered by Alias</span>
          </div>
        </div>
        <v-container>
            <p class="font-weight-light subheading">
                <span>Already have an Account? </span>
                <router-link tag="a" to="login" class="white--text" href>Login!</router-link>
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
// import ImageUpload from '@/components/ImageUpload'
import { Cropper } from 'vue-advanced-cropper'
import { REGISTER_USER_MUTATION } from '@/graphql/mutations/register'
import { UNIQUE_EMAIL_QUERY } from '@/graphql/queries/uniqueEmail'
import { UNIQUE_USERNAME_QUERY } from '@/graphql/queries/uniqueUsername'
import { onLogin } from '@/apollo'
const images = ['/img/background_slider_01.jpg', '/img/background_slider_02.jpg']

export default {
  components: {
    Cropper
  },
  data() {
    return {
      e1: 0,
      cropping: false,
      cropped: false,
      feedback: false,
      file: null,
      fileUrl: null,
      countriesList: ["USA", "Pakistan"],
      languagesList: ["English", "Urdu"],
        timeout: null,
        uniqueUsernameError: false,
        uniqueEmailError: false,
        uniqueEmailErrorMessages: [],
        uniqueUsernameErrorMessages: [],

        firstName: null,
        lastName: null,
        loading: false,
        
        country: null,
        language: null,
        username: null,
        password: null,
        verifyPassword: null,
        email: null,
        birthday: null,
        menu: false,
      rules: {
        username: v => /^[\w.]+$/.test(v) || 'Letters, numbers, . or _',
        password: v => v.length && v.length >= 8 || 'Password should be 8 or more characters',
        verifyPassword: v => v === this.password || 'Password must match',
        name: v => /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/.test(v) || 'Letters with - \' . , only',
        required: v => !!v || "Required.",
        // uniqueEmail: v => this.unique('e') || 'A user with this email already exists',
        // uniqueUsername: v => await this.unique('u') || 'This username is already taken',
        
      }
    }
  },
  watch: {
      menu (value) {
          value && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
      }
  },
  computed: {
    bgImage() {
      var min = 0;
      var max = images.length;
      var random = Math.floor(Math.random() * (+max - +min)) + +min;
      return images[random];
    },
  },
  methods: {
    // saveClicked(img) {
        // console.log(img, img.toDataURL())
        // this.$refs.image.src = img.toDataURL()
    // },
    // NOTE:::::::::: DATA URL WORKS, HOWEVER BROKEN IN BRAVE
    resetImage() {
      this.cropping = false
      this.cropped = false
      this.file = null
      this.fileUrl = null
    },
    crop() {
      const { coordinates, canvas, } = this.$refs.cropper.getResult()
      // console.log('memes2', canvas, canvas.toDataURL())
      this.fileUrl = canvas.toDataURL('image/jpeg', 0.8)
      this.cropping = false
      this.cropped = true
    },
    fileChange(file, name) {
      console.log("File --> ", file)
      console.log("FileName -->", name)
      let r = new FileReader()
      r.onload = (e) => {
        this.file = e.target.result
        this.cropping = true
      }
      r.readAsDataURL(file)
    },
    onErr(err, file) {
      console.log("​onErr -> file", file);
      console.log("​onErr -> err", err);
    },
    exceedHandler(file) {
      console.warn("onExceed -> file", file);
    },
    submit() {
        // NOTE: TODO: ADD USERNAME EXISTS CHECKER
        let valid
        try {
          valid = this.$refs.signupForm.validate()
        } catch (err) {
          this.feedback = true
        }
        
        if (valid && this.fileUrl) {
            this.loading = true
            const { username, email, firstName, lastName, language, country, birthday, password } = this.$data
            const file = this.fileUrl
            this.$apollo.mutate({
                mutation: REGISTER_USER_MUTATION,
                variables: {
                    username,
                    email,
                    firstName,
                    lastName,
                    language,
                    country,
                    birthday,
                    password,
                    file
                },
                context: {
                  hasUpload: true
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
                this.loading = false
            })
            
        } else {
          this.feedback = true
        }
    },
    // isUnique(t) {
    //     console.log('xd')
    //     if (t === 'e' && this.email) {
    //         this.$apollo.query({
    //             query: UNIQUE_EMAIL_QUERY,
    //             variables: { email: this.email }
    //         }).then((result) => {
    //             console.log('xd', result.data.uniqueEmail)
    //             return result.data.uniqueEmail
    //         }).catch((err) => {
    //             console.log(err)
    //         })
    //     } else if (t === 'u' && this.username) {
    //         this.$apollo.query({
    //             query: UNIQUE_USERNAME_QUERY,
    //             variables: { username: this.username }
    //         }).then((result) => {
    //             console.log('xd', result.data.uniqueUsername)
    //             return result.data.uniqueUsername
    //         }).catch((err) => {
    //             console.log(err)
    //         })
    //     } else {
    //         console.log('something went wrong')
    //         return false
    //     }
    // },
    unique(t) {
        clearTimeout(this.timeout)
        this.timeout = setTimeout(() => {
            let unique

            if (t === 'e' && this.email) {
                this.$apollo.query({
                    query: UNIQUE_EMAIL_QUERY,
                    variables: { email: this.email }
                }).then((result) => {
                    console.log('xd', result.data.uniqueEmail)
                    if (result.data.uniqueEmail) {
                        this.uniqueEmailError = false
                        this.uniqueEmailErrorMessages = []
                    } else {
                        this.uniqueEmailError = true
                        this.uniqueEmailErrorMessages = ['A user with this email already exists']
                    }
                }).catch((err) => {
                    console.log(err)
                })
            } else if (t === 'u' && this.username) {
                this.$apollo.query({
                    query: UNIQUE_USERNAME_QUERY,
                    variables: { username: this.username }
                }).then((result) => {
                    console.log('xd', result.data.uniqueUsername)
                    if (result.data.uniqueUsername) {
                        this.uniqueUsernameError = false
                        this.uniqueUsernameErrorMessages = []
                    } else {
                        this.uniqueUsernameError = true
                        this.uniqueUsernameErrorMessages = ['This username is already taken']
                    }
                }).catch((err) => {
                    console.log(err)
                })
            }

            // console.log(unique, this.uniqueEmailError, this.uniqueUsernameError)

            // if (unique) {
            //     if (t === 'e') {
            //         this.uniqueEmailError = false
            //         this.uniqueEmailErrorMessages = []
            //     } else if (t === 'u') {
            //         this.uniqueUsernameError = false
            //         this.uniqueUsernameErrorMessages = []
            //     }
            // } else {
            //     if (t === 'e') {
            //         this.uniqueEmailError = true
            //         this.uniqueEmailErrorMessages = ['A user with this email already exists']
            //     } else if (t === 'u') {
            //         this.uniqueUsernameError = true
            //         this.uniqueUsernameErrorMessages = ['This username is already taken']
            //     }
            // }
        }, 500)
    },


    // return new Promise(resolve => {
    //     if (t === 'e' && this.email) {
    //         this.$apollo.query({
    //             query: UNIQUE_EMAIL_QUERY,
    //             variables: { email: this.email }
    //         }).then((result) => {
    //             resolve( result.data.uniqueEmail )
    //         }).catch((err) => {
    //             console.log(err)
    //         })
    //     } else if (t === 'u' && this.username) {
    //         this.$apollo.query({
    //             query: UNIQUE_USERNAME_QUERY,
    //             variables: { username: this.username }
    //         }).then((result) => {
    //             resolve( result.data.uniqueUsername )
    //         }).catch((err) => {
    //             console.log(err)
    //         })
    //     } else {
    //         resolve( true )
    //     }
    // })
  },
}
</script>

<style>

.crop-img {
  width: 100%;
  height: 100%;
}

.auth-main {
  text-align: center;
}
.opacity-half {
  opacity: 0.8;
}
/*//////////////////////////////////////////////////////////////////
[ RESTYLE TAG ]*/

* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}

body,
html {
  height: 100%;
}

/*//////////////////////////////////////////////////////////////////
[ login ]*/

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

.auth-main .theme--light.v-label,
.auth-main .theme--light.v-icon {
  color: white;
  font-weight: 300;
}

.auth-main .theme--light.v-input:not(.v-input--is-disabled) input,
.theme--light.v-input:not(.v-input--is-disabled) textarea {
  color: white;
}

.v-stepper.theme--light {
  background-color: transparent !important;
  box-shadow: none !important;
}
</style>