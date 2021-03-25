<template>
  <div class="">
      <v-container fluid class="white--text">

        <v-layout column align-center justify-center class="hidden-md-and-up mb-3">
            <v-flex>
                <v-card flat color="transparent">
                    <v-card-title class="white--text" primary-title>
                        <div class="text-xs-center">
                            <v-layout align-center fill-height justify-center class="mb-2">
                                <v-icon color="white" large>people</v-icon>
                            </v-layout>
                            <p class="headline text-capitalize mb-2">Social Networks</p>
                            <p class="subheading">Keep and manage all your social media accounts in one profile.</p>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>

            <v-flex>
                <v-card flat color="transparent">
                    <v-card-title class="white--text" primary-title>
                        <div class="text-xs-center">
                            <v-layout align-center fill-height justify-center class="mb-2">
                                <v-icon color="white" large>link</v-icon>
                            </v-layout>
                            <p class="headline mb-2">Tou.sh Links</p>
                            <p class="subheading">Create links to your profile that change how people interact with you.</p>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>

            <v-flex>
                <v-card flat color="transparent">
                    <v-card-title class="white--text" primary-title>
                        <div class="text-xs-center">
                            <v-layout align-center fill-height justify-center class="mb-2">
                                <v-icon color="white" large>highlight</v-icon>
                            </v-layout>
                            <p class="headline text-capitalize mb-2">Highlights</p>
                            <p class="subheading">Grab a snapshot of someone's day with Touchbase Highlights.</p>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>
        </v-layout>

          <v-layout align-center justify-center>
              <v-flex lg8>
                  <p class="display-1 font-weight-light mt-5 text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">Communication As A Product</p>
                  <p class="headline grey--text text--lighten-2 mt-4 text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">From preferred contact methods, to redirecting to other social media accounts a user has,
                 Touchbase ensures the best options and outlets for allowing users to get in contact with other
                 Touchbase users, all without being intrusive, evasive, or annoying.</p>
             </v-flex>
          </v-layout>

          <v-layout align-start justify-start class="mt-5">
              <v-layout align-center justify-center fill-height class="hidden-sm-and-down mt-5">
                  <v-layout align-center fill-height justify-center>
                      <v-flex lg4>
                          <div class="">
                              <v-layout align-center fill-height justify-center class="mb-3">
                                      <v-btn large fab outline color="primary"><v-icon>mdi-add_box</v-icon></v-btn>
                              </v-layout>
                              <v-flex lg6 offset-lg3>
                                  <p class="title font-weight-bold text-uppercase text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">Social Network Accounts</p>
                                  <p class="title grey--text text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">
                                      Keep and manage all your social media accounts in one configurable, convenient and customizable profile.
                                  </p>
                              </v-flex>
                          </div>
                      </v-flex>
                      <v-flex lg4>
                          <div class="mr-3">
                              <img src="/img/mockups/1.png"/>
                          </div>
                      </v-flex>
                 </v-layout>
              </v-layout>

              <v-layout class="hidden-md-and-up">
                  <v-layout align-center justify-center>
                      <div class="">
                          <v-layout align-center fill-height justify-center class="mb-3">
                                  <v-btn large fab outline color="primary"><v-icon>mdi-add_box</v-icon></v-btn>
                          </v-layout>
                          <p class="title font-weight-bold text-uppercase text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">Social Network Accounts</p>
                          <p class="title grey--text text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">
                              Keep and manage all your social media accounts in one configurable, convenient and customizable profile.
                          </p>
                          <v-img src="/img/mockups/1.png" width="275" class="mr-2"></v-img>
                      </div>
                  </v-layout>
              </v-layout>

          </v-layout>
      </v-container>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
    div {
        background-color: #212121;
    }
    img {
        max-width: 100%;
    }
</style>
