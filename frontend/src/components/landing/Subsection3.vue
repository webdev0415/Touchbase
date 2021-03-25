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
                       <v-layout align-center fill-height justify-center>
                           <v-flex lg3>
                               <div class="pb-3">
                                   <v-flex lg6 offset-lg3>
                                       <p class="title font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Trending Users 🔥</p>
                                       <p class="title grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                           Stay in the loop about people gaining traction! 🆙
                                       </p>
                                   </v-flex>
                               </div>

                               <div class="mt-5">
                                 <v-flex lg6 offset-lg3>
                                       <p class="title font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Events Near You 📅</p>
                                       <p class="title grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                           Be the first to know of any concerts, raves, or get-togethers near you! 📣
                                       </p>
                                 </v-flex>
                              </div>

                           </v-flex>


                           <v-flex lg3>
                               <div class="">
                                   <img src="/img/mockups/3.png"/>
                               </div>
                           </v-flex>

                           <v-flex lg3>
                               <div class="pb-3">
                                   <v-flex lg6 offset-lg3>
                                       <p class="title font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Suggested Users 📝</p>
                                       <p class="title grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                           Get suggestions on who to follow based on your unique interests! 📲
                                       </p>
                                   </v-flex>
                               </div>

                               <div class="mt-5"> 
                                 <v-flex lg6 offset-lg3>
                                       <p class="title font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Online Highlights ✨</p>
                                       <p class="title grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                           Stay up-to-date with many online highlights from everyone you follow! 🔔
                                       </p>
                                 </v-flex>
                              </div>

                           </v-flex>

                      </v-layout>
                   </v-layout>
                   <v-layout class="hidden-md-and-up">
                       <v-layout align-center justify-center fill-height>
                           <div class="">
                               <v-img src="/img/mockups/3.png" width="275" class="ml-2"></v-img>
                               <v-layout row justify-space-between class="mt-5 ml-2">
                                   <v-flex xs5>
                                       <div class="pb-3">
                                           <v-flex lg6>
                                               <p class="font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Trending Users 🔥</p>
                                               <p class="grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                                   Stay in the loop about people gaining traction! 🆙
                                               </p>
                                           </v-flex>
                                       </div>
                                   </v-flex>

                                   <v-flex xs5>
                                       <div>
                                         <v-flex lg6>
                                               <p class="font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Events Near You 📅</p>
                                               <p class="grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                                   Be the first to know of any concerts, raves, or get-togethers near you! 📣
                                               </p>
                                         </v-flex>
                                      </div>
                                   </v-flex>
                               </v-layout>

                               <v-layout row justify-space-between fill-height class="mt-5 mb-4 ml-2">
                                   <v-flex xs5>
                                       <div class="pb-3">
                                           <v-flex lg6>
                                               <p class="font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Suggested Users 📝</p>
                                               <p class="grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                                   Get suggestions on who to follow based on your unique interests! 📲
                                               </p>
                                           </v-flex>
                                       </div>
                                   </v-flex>

                                   <v-flex xs5>
                                       <div>
                                         <v-flex lg6>
                                               <p class="font-weight-bold text-uppercase text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">Online Highlights ✨</p>
                                               <p class="grey--text text-md-left text-sm-left text-lg-left text-xl-left text-xs-left">
                                                   Stay up-to-date with many online highlights from everyone you follow! 🔔
                                               </p>
                                         </v-flex>
                                      </div>
                                   </v-flex>
                               </v-layout>

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
