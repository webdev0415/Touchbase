<template>
    <!-- THE OLD LAYOUT, http://prntscr.com/mx090o -->
    <!-- <v-container fluid fill-height>
        <v-layout wrap row align-end justify-space-around fill-height>
            <People />
            <Links />
            <Manage />
        </v-layout>
    </v-container> -->
    <v-layout row fill-height align-center justify-center v-if="$apollo.loading">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>

    <div v-else class="home-div">
        <v-layout align-end justify-space-around row fill-height class="pb-2" v-if="$vuetify.breakpoint.lgAndUp">
            <!-- here -->
            <!-- style="max-width: calc(100vw / 12 * 1.)" -->
            <!-- <v-flex md1 class="hidden-sm-and-down">
                <div class="home-whitespace"></div>
            </v-flex> -->

            <v-flex md12>
                <v-layout justify-end>
                    <!-- style="max-width: calc(100vw / 11.5);" -->
                    <v-flex lg3 class="hidden-md-and-down home-lsidebar elevation-3 mr-3">
                        <v-toolbar dense flat color="white">
                            <!-- WHo To Follow and Following Tabs -->
                            <v-toolbar-title class="font-weight-light text--darken-2 grey--text my-3">
                                <span>Who To Follow</span>
                            </v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-btn flat icon color="primary">
                                <v-icon>more_vert</v-icon>
                            </v-btn>
                        </v-toolbar>
                        <v-divider></v-divider>
                        <v-layout class="mcs-section" column justify-around align-center>
                            <v-flex style="width: 100%;" v-for="i in 20" :key="i">
                                <!-- <div> -->
                                <v-layout class="my-3" row wrap>
                                    <v-flex class="text-xs-center">
                                        <v-avatar
                                            size="75"
                                            color="primary"
                                            class="ml-3 mr-2"
                                        >
                                            <img src="img/avatar-2.png" alt="alt">
                                        </v-avatar>
                                    </v-flex>
                                    

                                    <v-layout column fill-height justify-center class="grey--text text-xs-center ml-1 text--darken-1">
                                        <v-flex class="title font-weight-light ml-2 pt-2">
                                            <!-- <v-layout row justify-space-between>
                                                <span>Hickory Doo</span>
                                                <span class="e-title body-2 font-weight-light pt-1 mr-3" @click="$router.push(`/${'toodaloo'}`)">@toodaloo</span>
                                            </v-layout> -->
                                            <v-flex>
                                                <span>Hickory Doo</span>
                                            </v-flex>
                                            <v-flex class="mt-1 ml-2">
                                                <span class="e-title body-2 font-weight-light" @click="$router.push(`/${'toodaloo'}`)">@toodaloo</span>
                                            </v-flex>
                                            <v-flex class="mt-2">
                                                <span class="subheading font-weight-light">"On this list bc I like cake"</span>
                                            </v-flex>
                                            
                                            
                                            <!-- <v-divider class="ocedlo-divs mx-3" inset vertical></v-divider> -->
                                            
                                        </v-flex>
                                        <!-- <v-flex class="mt-2 text-xs-center">
                                            Either occupation, location, bio snippet, or education, can be customized
                                            <span class="subheading font-weight-light">" Resident cool kid "</span>
                                        </v-flex> -->
                                        
                                        
                                    </v-layout>

                                    <!-- <v-flex class="text-xs-center"> -->
                                    <v-layout row justify-center>
                                        <v-btn class="ma-0 py-2" flat style="width: 100%; height: 120%;" color="primary">
                                            <v-icon>person_add</v-icon>
                                        </v-btn>
                                    </v-layout>
                                    
                                    <!-- </v-flex> -->
                                    

                                    <!-- <span class="title ml-1 pt-1 grey--text text--darken-3 font-weight-light">Hickory Doo</span>
                                    <v-spacer></v-spacer>
                                    <span class="e-title mr-3 grey--text text--darken-2 subheading font-weight-light" @click="$router.push(`/${post.user.username}`)">@toodaloo</span> -->
                                </v-layout>
                                <!-- <v-btn block flat class="my-0" color="primary">
                                    <span class="mr-2">Follow</span>
                                    <v-icon>person_add</v-icon>
                                </v-btn> -->
                                <!-- </div> -->
                                <v-divider></v-divider>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <!-- <v-flex class="home-section-divider">
                        <v-divider vertical></v-divider>
                    </v-flex> -->



                    <!-- <v-flex xs8 class="elevation-3 ml-3 db-card">
                        <v-toolbar dense flat class="db-card-top" color="white">
                            <v-toolbar-title class="font-weight-light text--darken-2 grey--text my-3">
                                <span>Hey Firstname! See your highlights.</span>
                            </v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-btn flat icon color="primary">
                                <v-icon>more_vert</v-icon>
                            </v-btn>
                        </v-toolbar>
                        <v-divider></v-divider> -->
                    <v-flex style="max-width: calc(calc(100vw / 12 * 9))">
                        <v-layout column class="db-card-bottom" style="padding: 20px 64px;">
                            <v-flex class="title my-1 ml-2">
                                <span class="font-weight-light text--darken-2 grey--text">Hey Firstname! See your highlights.</span>
                            </v-flex>
                            <!-- <v-flex v-for="(change, i) in publicChanges" :key="i" v-if="change.statement || change.service">
                                <v-card class="mcs-card elevation-3 my-3">
                                    <v-card-title @click="$router.push(`/${change.user.username}`)" class="grey--text text--darken-2 title font-weight-light pa-0">
                                        <v-avatar size="50" color="primary" class="ma-2"><img src="/img/avatar-2.png"></v-avatar>
                                        <span class="ml-1">{{ change.user.firstName }} {{ change.user.lastName }} - @{{ change.user.username }}</span>
                                        <v-spacer></v-spacer>
                                        <span v-if="change.service" class="mr-3">Added an account: {{ change.service.substring(0, change.service.indexOf('.')) }}</span>
                                        <span v-else class="mr-3">{{ change.statement }} <v-icon>dashboard</v-icon></span>
                                        <v-avatar v-if="change.service" size="32" class="mr-3"><img :src="`/img/${change.service.substring(0, change.service.indexOf('.'))}.png`"></v-avatar>
                                    </v-card-title>
                                    
                                </v-card>
                            </v-flex> -->
                            <v-flex v-for="(post, i) in all" :key="i">
                                <!-- IF SPF, THEN THIS OTHERWISE THAT -->
                                <v-card v-if="post.pdj" style="max-height: 297px;" :class="mcsCard">
                                    <v-layout row fill-height justify-center>
                                        <v-flex xs6>
                                            <v-layout row>
                                                <v-avatar
                                                    size="75"
                                                    class="ma-2 ml-3"
                                                    color="primary"
                                                >
                                                    <img :src="post.user.profilePic" alt="profile pic">
                                                </v-avatar>

                                                <v-layout column fill-height justify-center class="grey--text ml-3 text--darken-1">
                                                    <v-flex class="title font-weight-regular mt-3 mb-2">
                                                        <v-layout row justify-space-between>
                                                            <span>{{ post.user.firstName }} {{ post.user.lastName }}</span>
                                                            <span class="e-title subheading font-weight-light mr-3" @click="$router.push(`/${post.user.username}`)">@{{ post.user.username }}</span>
                                                        </v-layout>
                                                        
                                                        <!-- <v-divider class="ocedlo-divs mx-3" inset vertical></v-divider> -->
                                                        
                                                    </v-flex>
                                                    <v-flex class="mt-1">
                                                        <v-layout row justify-space-between>
                                                            <span class="subheading font-weight-light">
                                                                <span> Posted a {{ post.type }} on {{ post.service.charAt(0).toUpperCase() + post.service.slice(1) }}</span> 
                                                                <v-avatar size="30" class="ml-2 mb-1"><img :src="post.serviceLogo" :alt="post.service"></v-avatar>
                                                            </span>
                                                            <span class="text-capitalize font-weight-light mr-3">{{ post.created }}</span>
                                                        </v-layout>
                                                    </v-flex>
                                                    
                                                </v-layout>
                                            </v-layout>
                                            
                                            <v-divider></v-divider>
                                            <template v-if="post.service === 'youtube'">
                                                <v-layout v-if="post.pdj.id.kind === 'youtube#video'" style="height: 65%;" column class="mx-4 mt-3" align-center justify-space-between>
                                                    <v-flex>
                                                        <span class="title font-weight-light text-xs-center pb-1 spf-post-text">{{ post.pdj.snippet.title }}</span>
                                                    </v-flex>
                                                    
                                                    <v-flex>
                                                        <span class="spf-post-text" v-if="post.pdj.snippet.description">{{ post.pdj.snippet.description }}</span>
                                                    </v-flex>
                                                    <v-flex>
                                                        <span class="text-xs-center grey--text">
                                                            <span>Visit </span>
                                                            <a style="text-decoration: none;" target="_blank" :href="`http://${post.accountUrl}`">{{ post.user.firstName }}'s channel</a>
                                                            <span> on {{ post.service.charAt(0).toUpperCase() + post.service.slice(1) }}</span>
                                                        </span>
                                                    </v-flex>
                                                </v-layout>
                                            </template>
                                            

                                            <v-layout v-else style="height: 65%;" column class="mx-4 mt-3" align-center justify-space-between>
                                                <v-flex>
                                                    <span class="title font-weight-light text-xs-center pb-1 spf-post-text">a title or something</span>
                                                </v-flex>
                                            </v-layout>
                                            
                                            
                                        </v-flex>
                                        <!-- <v-divider vertical></v-divider> -->
                                        <v-flex xs6 v-if="post.service === 'youtube'">
                                            <v-img :src="post.pdj.snippet.thumbnails.high.url" style="border-radius: 0 10px 10px 0;" height="297px"></v-img>
                                        </v-flex>
                                        <v-flex xs6 v-else>
                                            <v-img src="/img/avatar-1.png" style="border-radius: 0 10px 10px 0;" height="297px"></v-img>
                                        </v-flex>
                                    </v-layout>
                                </v-card>
                                <v-card v-else class="mcs-card elevation-3 my-3">
                                    <v-card-title @click="$router.push(`/${post.user.username}`)" class="grey--text text--darken-2 title font-weight-light pa-0">
                                        <v-avatar size="50" color="primary" class="ma-2"><img :src="post.user.profilePic"></v-avatar>
                                        <span class="ml-1">{{ post.user.firstName }} {{ post.user.lastName }} - @{{ post.user.username }}</span>
                                        <v-spacer></v-spacer>
                                        <span v-if="post.service" class="mr-3">Added an account: {{ post.service.substring(0, post.service.indexOf('.')) }}</span>
                                        <span v-else class="mr-3">{{ post.statement.charAt(0).toUpperCase() + post.statement.slice(1) }} <v-icon>dashboard</v-icon></span>
                                        <v-avatar v-if="post.service" size="32" class="mr-3"><img :src="`/img/${post.service.substring(0, post.service.indexOf('.'))}.png`"></v-avatar>
                                    </v-card-title>
                                    
                                </v-card>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <!-- </v-flex> -->

                    <!-- <v-flex lg2 class="hidden-md-and-down db-card home-rsidebar elevation-3">
                        <v-toolbar dense class="db-card-top" flat color="white">
                            WHo To Follow and Following Tabs
                            <v-toolbar-title class="font-weight-light text--darken-2 grey--text my-3">
                                <span>What's New</span>
                            </v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-btn flat icon color="primary">
                                <v-icon>more_vert</v-icon>
                            </v-btn>
                        </v-toolbar>
                        <v-divider></v-divider>
                        <v-layout class="mcs-section" column justify-around align-center>
                            <v-flex style="width: 100%;" v-for="i in 20" :key="i">
                                <div class="py-3">
                                    <v-layout row wrap>
                                        

                                        <v-layout column fill-height justify-center class="grey--text text-xs-center ml-1 text--darken-1">
                                            <v-flex class="subheading font-weight-light ml-2">
                                                <v-layout row justify-space-between>
                                                    <span>Hickory Doo</span>
                                                    <span class="e-title body-2 font-weight-light pt-1 mr-3" @click="$router.push(`/${'toodaloo'}`)">@toodaloo</span>
                                                </v-layout>
                                                <v-flex>
                                                    <span>Hickory Doo</span>
                                                </v-flex>
                                                <v-flex class="ml-2 mb-2">
                                                    <span class="e-title body-2 font-weight-light" @click="$router.push(`/${'toodaloo'}`)">@toodaloo</span>
                                                </v-flex>
                                                <v-flex class="mx-3">
                                                    <span class="subheading font-weight-light">Added an account: Reddit </span>
                                                    <v-avatar size="28" class="ml-1"><img src="/img/reddit.png"></v-avatar>
                                                </v-flex>                                        
                                            </v-flex>
                                        </v-layout>
                                    </v-layout>
                                </div>
                                <v-divider></v-divider>
                            </v-flex>
                        </v-layout>
                    </v-flex> -->



                    <!-- <v-flex class="home-section-divider">
                        <v-divider vertical></v-divider>
                    </v-flex> -->
                    <!-- lg3 VVVV -->
                    <!-- <v-flex xs4 lg5 class="elevation-3 db-card"> 
                        <v-toolbar flat class="db-card-top" color="white">
                            <v-toolbar-title class="font-weight-light text--darken-2 grey--text my-1">
                                <span>Suggested</span>
                            </v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-btn flat icon color="primary">
                                <v-icon>more_vert</v-icon>
                            </v-btn>
                        </v-toolbar>
                        <v-divider></v-divider>
                        <v-layout row fill-height align-center justify-center v-if="$apollo.loading">
                            <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
                        </v-layout>
                        <v-layout v-else column align-around class="mcs-section db-card-bottom home-lsidebar" style="padding: 10px 30px;">
                            <v-flex v-for="(event, i) in memes.events" :key="i">
                                <v-card :class="mcsCard">
                                    <v-card-title class="mb-0 pb-2 pt-3" primary-title @click="open(event.url)">
                                        <span class="subheading mb-0 e-title"><v-icon>link</v-icon> {{ event.name.text }}</span>
                                    </v-card-title>
                                    <v-layout row justify-space-between>
                                        <span class="body-2 font-weight-regular ml-4 grey--text">{{ event.location }}</span>
                                        <span class="body-2 font-weight-regular text-uppercase mb-3 mr-4 grey--text">{{ event.start }}</span>
                                    </v-layout>
                                    
                                    <v-img
                                        contain
                                        width="auto"
                                        :src="event.image"
                                        class=""
                                        style="border-radius: 10px;"
                                    ></v-img>
                                </v-card>
                            </v-flex>
                        </v-layout>

                    </v-flex> -->
                </v-layout>
            </v-flex>
            <!-- here -->
            <!-- <v-flex md1 class="hidden-sm-and-down">
                <div class="home-whitespace"></div>
            </v-flex> -->
        </v-layout>

        <v-layout v-else justify-center column>
            
            <v-flex xs1>
                <v-layout row justify-center>
                    <v-flex xs12 class="my-4 px-2" style="width: 100%;">
                        <span class="font-weight-light title ml-2 text--darken-2 grey--text my-3">Who To Follow</span>
                        <!-- <v-select
                            :items="cSelect"
                            v-model="cSelectVal"
                        >
                            <template v-if="!cSelectVal" slot="label">
                                <span>{{ cSelectDef }}</span>
                            </template>
                        </v-select> -->
                        <v-card class="px-1 py-1 mt-2" style="border-radius: 8px;">
                            <RecommendedSlider :recommendeds="recommendeds" />
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-flex>


            <!-- SEE WHAT'S NEW -->


            <v-flex xs11>
                <v-layout align-center fill-height column>
                    <v-flex v-for="(post, i) in all" :key="i" class="mx-1" style="width: 100%;">
                        <v-card v-if="post.pdj" :class="mcsCard">
                            <v-layout column>
                                <v-flex style="width: 100%;">
                                    <v-layout row>
                                        <v-avatar
                                            size="80"
                                            class="mt-3 ml-2"
                                            color="primary"
                                        >
                                            <img :src="post.user.profilePic" alt="profile pic">
                                        </v-avatar>

                                        <v-layout column fill-height justify-center class="grey--text ml-2 text--darken-1">
                                            <v-flex class="title font-weight-regular mt-3 mb-2">
                                                <v-layout column align-center>
                                                    <span>{{ post.user.firstName }} {{ post.user.lastName }}</span>
                                                    <span class="e-title mt-1 subheading font-weight-light mr-3" @click="$router.push(`/${post.user.username}`)">@{{ post.user.username }}</span>
                                                    <span class="subheading mt-2 px-2 font-weight-light">
                                                        <span> Posted a {{ post.type }} on {{ post.service.charAt(0).toUpperCase() + post.service.slice(1) }}</span> 
                                                        <v-avatar size="26" class="ml-2 mb-1"><img :src="post.serviceLogo" :alt="post.service"></v-avatar>
                                                    </span>
                                                    <span class="body-1 text-capitalize font-weight-light mr-3">{{ post.created }}</span>
                                                </v-layout>
                                                
                                                <!-- <v-divider class="ocedlo-divs mx-3" inset vertical></v-divider> -->
                                                
                                            </v-flex>
                                            
                                            
                                        </v-layout>
                                    </v-layout>
                                </v-flex>
                                <!-- <v-flex class="mt-1">
                                    <v-layout row justify-space-between>
                                        
                                        
                                    </v-layout>
                                </v-flex> -->
                                <v-divider></v-divider>
                                <v-divider></v-divider>
                                <v-flex xs8>
                                    <template v-if="post.service === 'youtube'">
                                        <v-layout v-if="post.pdj.id.kind === 'youtube#video'" column class="mx-4 mt-3" align-center justify-space-between>
                                            <v-flex>
                                                <span class="title font-weight-light text-xs-center pb-1 spf-post-text">{{ post.pdj.snippet.title }}</span>
                                            </v-flex>
                                            
                                            <!-- <v-flex> -->
                                            <!-- <v-img :src="post.pdj.snippet.thumbnails.high.url" style="border-radius: 0 10px 10px 0;" height="200"></v-img> -->
                                            <!-- </v-flex> -->
                                            <!-- <v-flex>
                                                <span class="text-xs-center grey--text">
                                                    <span>Visit </span>
                                                    <a style="text-decoration: none;" target="_blank" :href="`http://${post.accountUrl}`">{{ post.user.firstName }}'s channel</a>
                                                    <span> on {{ post.service.charAt(0).toUpperCase() + post.service.slice(1) }}</span>
                                                </span>
                                            </v-flex> -->
                                        </v-layout>
                                    </template>
                                    <v-img :src="post.pdj.snippet.thumbnails.high.url" style="border-radius: 0 0 8px 8px;" height="25vh"></v-img>

                                    <!-- <v-layout v-else style="height: 65%;" column class="mx-4 mt-3" align-center justify-space-between>
                                        <v-flex>
                                            <span class="title font-weight-light text-xs-center pb-1 spf-post-text">a title or something</span>
                                        </v-flex>
                                    </v-layout> -->

                                </v-flex>
                            </v-layout>
                            <!-- <v-card v-if="post.location || post.location == ''" :class="mcsCard">
                                <v-card-title class="mb-0 pb-2 pt-3" primary-title @click="open(post.url)">
                                    <span class="subheading mb-0 e-title"><v-icon>link</v-icon> {{ post.name.text }}</span>
                                </v-card-title>
                                <v-layout row justify-space-between>
                                    <span class="body-2 font-weight-regular ml-4 grey--text">{{ post.location }}</span>
                                    <span class="body-2 font-weight-regular text-uppercase mb-3 mr-4 grey--text">{{ post.start }}</span>
                                </v-layout>
                                
                                <v-img
                                    contain
                                    height="auto"
                                    :src="post.image"
                                    class=""
                                    style="border-radius: 10px;"
                                ></v-img>
                            </v-card>
                            <v-card v-else :class="mcsCard">
                                <v-card-title class="pt-3" primary-title>
                                    <div>
                                        <h3 class="headline mb-0">{{ post.user.username }} posted on {{ post.service }}</h3>
                                        <div>description</div>
                                    </div>
                                </v-card-title>
                                <template v-if="post.service === 'youtube'">
                                    <template v-if="post.pdj.id.kind === 'youtube#video'">
                                        <v-img :src="post.pdj.snippet.thumbnails.high.url" width="100%"></v-img>
                                    </template>
                                </template>
                            </v-card> -->
                        </v-card>
                        <v-card v-else class="mcs-card elevation-3 my-3 mx-1">
                            <div @click="$router.push(`/${post.user.username}`)" class="grey--text subheading text--darken-2 font-weight-light pa-0">
                                <v-layout row align-center>
                                    <v-avatar size="60" color="primary" class="mx-2 mt-2"><img :src="post.user.profilePic"></v-avatar>
                                    <span class="ml-1 title font-weight-light">{{ post.user.firstName }} {{ post.user.lastName }} - @{{ post.user.username }}</span>
                                    <v-spacer></v-spacer>
                                    <span class="mr-1 subheading font-weight-light">{{ post.created }}</span>
                                    <!-- <br> -->
                                </v-layout>
                                
                                <v-layout row justify-center>
                                    <v-flex xs12 class="text-xs-center py-1">
                                        <span v-if="post.service">Added an account: {{ post.service.substring(0, post.service.indexOf('.')) }}</span>
                                        <span v-else class="mr-3">{{ post.statement.charAt(0).toUpperCase() + post.statement.slice(1) }} <v-icon>dashboard</v-icon></span>
                                        <v-avatar v-if="post.service" size="27" class="ml-3"><img :src="`/img/${post.service.substring(0, post.service.indexOf('.'))}.png`"></v-avatar>
                                    </v-flex>
                                </v-layout>
                            </div>
                            
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout> 

        <v-speed-dial
            :class="speedDial"
            style="position: fixed; bottom: 2em; right: 0;"
            direction="top"
            v-model="fab"
            transition="slide-y-reverse-transition"
        >
            <template slot="activator">
                <v-btn fab color="primary" dark v-model="fab">
                    <v-icon>more_horiz</v-icon>
                    <v-icon>keyboard_arrow_down</v-icon>
                </v-btn>
            </template>
            <v-btn fab small to="/me/edit" color="success">
                <v-icon>edit</v-icon>
            </v-btn>
            <v-btn fab dark small to="/settings" color="aliasAcc">
                <v-icon>settings</v-icon>
            </v-btn>
            <v-btn fab dark small to="/following" color="alias">
                <v-icon>person</v-icon>
            </v-btn>
            <v-btn fab dark small to="/followers" color="alias darken-1">
                <v-icon>person_add</v-icon>
            </v-btn>
        </v-speed-dial>
    </div>
    
    
</template>

<script>
import moment from 'moment'
import gql from 'graphql-tag'
// import Links from './dashboard/Links'
// import Manage from './dashboard/Manage'
// import People from './dashboard/People'
import { OWN_OAUTHS_QUERY } from '@/graphql/queries/ownOAuths'
import { OWN_CHANGES_QUERY } from '@/graphql/queries/publicChanges'
import RecommendedSlider from '@/components/dashboard/RecommendedSlider'

export default {
    name: 'Dashboard',
    components: {
        RecommendedSlider
    },
    data() {
        return {
            testCanada: '',
            fab: false,
            publicChanges: [],
            ownOauthPosts: [],
            oauthPosts: [],
            memes: {},
            cSelect: ['New', 'Trending', 'Suggested'],
            cSelectVal: '',
            recommendeds: [
                { firstName: 'Elon', lastName: 'Musk', username: 'muskboi' },
                { firstName: 'Thicc', lastName: 'Man', username: 'xd' },
                { firstName: 'Mark', lastName: 'Guy', username: 'lol' },
                { firstName: 'Scott', lastName: 'Cawthon', username: 'memes._' },
                { firstName: 'Jojo', lastName: 'HaYeZust', username: '123p' },
                { firstName: 'Sponge', lastName: 'Bob', username: 'eatit' },
                { firstName: 'Josh', lastName: 'Goodings', username: 'aahhh' },
                { firstName: 'Normal', lastName: 'Guy', username: 'yeghj' },
                { firstName: 'HDMI', lastName: 'Cable', username: 'qq' },
                { firstName: 'thikker', lastName: 'mans', username: 'uak' },
                { firstName: 'Elongated', lastName: 'Muskrat', username: 'moose' },
            ]
        }
    },
    computed: {
        mcsCard() {
            if (this.$vuetify.breakpoint.smAndDown) {
                return {
                    'mcs-card': true,
                    'mx-1': true,
                    'my-3': true,
                    'elevation-3': true,
                }
            } else {
                return {
                    'mcs-card': true,
                    'my-3': true,
                    'elevation-3': true,
                }
            }
        },
        speedDial() {
            if (this.$vuetify.breakpoint.smAndDown) {
                return { 'mb-4': true, 'mr-2': true }
            } else {
                return { 'mb-5': true, 'mr-3': true }
            }
        },
        all() {
            if (!this.$apollo.loading) {
                // TODO: SORT CHRONOLOGICALLY
                let arr = this.publicChanges.concat(this.oauthPosts)
                arr = arr.sort(() => Math.random() - 0.5)
                let shuffled = arr.sort(() => Math.random() - 0.5)
                return shuffled
            }
        }
    },
    methods: {
        open(url) {
            window.open(url)
        },
    },
    created() {
        this.$apollo.queries.oauthPosts.skip = false
        this.$apollo.queries.publicChanges.skip = false
        this.$apollo.queries.oauthPosts.refetch() 
        this.$apollo.queries.publicChanges.refetch() 
    },
    apollo: {
        // testCanada: {
        //     query: gql`query{  testCanada}`,
        //     result({ data, loading }) {
        //         if (!loading) {
        //             this.memes = JSON.parse(data.testCanada)
        //             this.memes.events.forEach((event, i) => {
        //                 this.memes.events[i].start = moment(event.start).format("MMM D, @ ha")
        //             })

        //             // console.log(data.testCanada)
        //         }
        //     }
        // },
        oauthPosts: {
            skip: true,
            query: OWN_OAUTHS_QUERY,
            update(data) {
                let resultOauthPosts = []
                if (data.ownOauthPosts) {
                    data.ownOauthPosts.forEach(post => {
                        post.pdj = JSON.parse(post.pdj)
                        // post.pdj.snippet.title = 'IoT Demonstration - Smart Cities Assignment IoT Demonstration - Smart Cities Assignment ABCDEFG XDX'
                        // post.pdj.snippet.description = 'TOUUCHHHHbbbbbbasseeee with MEEEEe Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlorTOUUCHHHHbbbbbbasseeee with MEEEEe Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlorTOUUCHHHHbbbbbbasseeee with MEEEEe Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlorTOUUCHHHHbbbbbbasseeee with MEEEEe Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlorTOUUCHHHHbbbbbbasseeee with MEEEEe Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor Lorem Ipsum dolor sit Amet Lorem Ipsum Dolor Sit Amet Lorem Ipsum DOlor'
                        if (post.pdj.snippet.description.length > 256) post.pdj.snippet.description = post.pdj.snippet.description.substring(0,256).concat('...')
                        if (!post.pdj.snippet.description) post.pdj.snippet.description = '...'
                        post.created = moment(post.created).fromNow()
                        if (post.service === 'youtube') post.type = 'video'; post.accountUrl = `youtube.com/channel/${post.pdj.snippet.channelId}`
                        var i = this.$store.state.accountList.findIndex(v => v.includes(post.service))
                        post.serviceLogo = this.$store.state.logoList[this.$store.state.accountList[i]]
                        if (post.pdj.id.kind === 'youtube#video') resultOauthPosts.push(post)
                    })
                } else {
                    alert('Something went wrong. Please try again later! ⏳')
                }
                return resultOauthPosts
            }
        },
        publicChanges: {
            skip: true,
            query: OWN_CHANGES_QUERY,
            // result({ data, loading }) {
            //     if (!loading) {
            //         data.publicChanges.forEach(post => {
                        
            //             post.created = moment(post.created, 'YYYY-MM-DD HH:mm').fromNow()
            //         })
            //     }
            // }
        }
    },
}
</script>

<style>

.db-card {
    border-radius: 10px;
    /* width: 30vw; */
    width: 100%;
}

.db-card-top {
    border-radius: 10px 10px 0 0;
    /* width: 30vw; */
}

.db-card-bottom {
    border-radius: 0 0 10px 10px;
    /* width: 30vw; */
}

.mcs-card {
    border-radius: 8px;
    /* border-style: solid; */
    /* min-width: 100%; */
}

/* .mcs-card-img {
    padding: 90vw;
} */

.mcs-section {
    overflow-y: auto;
    overflow-x: hidden;
    /* 88vh - 129px */
    max-height: calc(100vh - 162px);
    height: calc(100vh - 162px);
    /* min-width: 310px; */
    width: 100%;
    border-radius: 0 0 10px 10px;
    /* scrollbar-color: #aaa #ddd;
    scrollbar-width: thin; */
    background: white;
}

/* .mcs-section::-webkit-scrollbar {
    width: 11px;
}

.mcs-section::-webkit-scrollbar-track {
    background: #ddd;
}

.mcs-section::-webkit-scrollbar-thumb {
    background: #aaa;
} */

.mcs-section::-webkit-scrollbar {
    width: 0px;
}


.home-lsidebar {
    position: fixed;
    /* left: 30px; */
    left: 0px;
    width: 100%;
    /* margin: 25px 0; */
    /* max-height: calc(100vh - 200px); */
    
}

.home-rsidebar {
    position: fixed;
    right: 0px;
    /* right: 15px; */
    /* margin: 25px 0; */
    /* max-height: calc(100vh - 200px); */
}

.home-whitespace {
    /* BDBDBD */
    background: #fff;
    width: 100%;
    height: 100%;
}

.home-section-divider {
    max-height: calc(100vh - 64px);
}

.e-title:hover {
    color: #FF7256;
    cursor: pointer;
}

/* .home-main-border {
    -webkit-box-shadow: 0 11px 15px -7px rgba(0,0,0,.2), 0 24px 38px 3px rgba(0,0,0,.14), 0 9px 46px 8px rgba(0,0,0,.12);
    box-shadow: 0 11px 15px -7px rgba(0,0,0,.2), 0 24px 38px 3px rgba(0,0,0,.14), 0 9px 46px 8px rgba(0,0,0,.12);
} */

/* .home-sidebar-img {
    background-image: url("../../public/img/coral-pattern.jpg");
    -webkit-filter: blur(5px);
    -moz-filter: blur(5px);
    -o-filter: blur(5px);
    -ms-filter: blur(5px);
    filter: blur(5px);

    display: block;
    z-index: 10000;
    width: 100%;
    height: 100%;
}

.home-sidebar-content {
    overflow: auto;
    position: absolute;
    z-index: 999;
} */

/* .home-sidebar-content:before {
    background-image: url('../../public/img/coral-pattern.jpg');
    width: 100%;
    height: 100%;

    -webkit-filter: blur(5px);
    -moz-filter: blur(5px);
    -o-filter: blur(5px);
    -ms-filter: blur(5px);
    filter: blur(5px);
} */

.spf-post-text {
    text-overflow: ellipsis;
    /* white-space: nowrap; */
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

</style>
