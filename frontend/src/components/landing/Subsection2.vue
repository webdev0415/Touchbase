<template>
  <div class="">
      <v-container fluid class="white--text">
           <v-layout align-center justify-center>
               <v-flex lg8>
                  <hr>
              </v-flex>
           </v-layout>
           <v-layout class="mt-5">
               <v-layout align-start justify-start class="mt-5">
                   <v-layout align-center justify-center fill-height class="hidden-sm-and-down">
                       <v-layout align-center fill justify-center>
                           <v-flex lg4>
                               <div class="ml-3">
                                   <img src="/img/mockups/2.png"/>
                               </div>
                           </v-flex>

                           <v-flex lg4>
                               <div class="">
                                   <v-layout align-center fill-height justify-center class="mb-3">
                                           <v-btn large fab outline color="primary"><v-icon>mdi-add_box</v-icon></v-btn>
                                   </v-layout>
                                   <v-flex lg6 offset-lg3>
                                       <p class="title font-weight-bold text-uppercase text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">Customizable Profile Links</p>
                                       <p class="title grey--text text-md-center text-sm-center text-lg-center text-xl-center text-xs-center">
                                           Create up to 2 links to your Touchbase page that dictate how visitors interact with your profile, from account visibility to a custom description.
                                       </p>
                                   </v-flex>
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
                               <v-img src="/img/mockups/2.png" width="275" class="ml-2"></v-img>
                           </div>
                       </v-layout>
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
    hr {
        border-width: 1px;
    }
</style>
