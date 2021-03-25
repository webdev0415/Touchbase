<template>
    <NotFound v-if="notFound"/>

    <v-layout row fill-height align-center justify-center v-else-if="$apollo.loading">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>

    <v-layout v-else row fill-height justify-center>
        <v-flex xs12>
            <section>
                <!-- NOTE: change the background parallax image to our own -->
                <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg" style="border-radius: 0 0 13px 13px; height: calc(20vh + 400px);">
                    <v-layout row justify-start>
                        <v-flex xs9 sm5 md4 lg3 >
                            <v-text-field
                                style="margin-top: 85px;"
                                readonly
                                height="20"
                                box
                                dark
                                hide-details
                                color="primary"
                            >
                                <v-icon class="white--text" slot="prepend">link</v-icon>
                                <span slot="prepend-inner" class="title font-weight-light white--text">xd</span>
                            </v-text-field>
                        </v-flex>
                    </v-layout>
                    <v-layout column fill-height 
                    align-center
                    class="white--text"
                    >
                        <v-avatar class="text-xs-center" style="margin-top: 50px;" color="primary" size="150">
                            <img src="/img/avatar-2.png" alt="">
                        </v-avatar>
                        <v-flex class="mt-3">
                            <!-- <h1 class="white--text mb-4 display-4 text-xs-center font-weight-thin">Parallax Template</h1> -->
                            <p class="mb-2 display-1 font-weight-light text-xs-center">
                                <span>My Memes Clique!</span>
                            </p>
                            <!-- <p class="mb-4 title font-weight-light text-xs-center"></p> -->
                        </v-flex>
                    </v-layout>
                </v-parallax>
            </section>
            
            <section style="margin-bottom: 15vh;">
                <v-layout column fill-height align-center>
                    <v-flex class="mt-2 mb-4 subheading text-uppercase grey--text text--darken-2 font-weight-light">
                        <template>
                            <span>Expires </span>
                            <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                        </template>
                        <span>10 Views</span>
                    </v-flex>
                    <v-flex>
                        <p class="display-1 font-weight-light">A message for all</p>
                    </v-flex>
                    <v-flex>
                        column memes
                    </v-flex>
                    <v-btn 
                        v-if="!grid" color="primary"
                        @click="grid = !grid"
                        fab fixed
                        bottom right
                        class="mr-2"
                        style="margin-bottom: calc(3vh + 30px);"
                    >
                        <v-icon>dashboard</v-icon>
                    </v-btn>

                    <v-btn 
                        v-else color="primary"
                        @click="grid = !grid"
                        fab fixed
                        bottom right
                        class="mr-2"
                        style="margin-bottom: calc(3vh + 30px);"
                    >
                        <v-icon>list</v-icon>
                    </v-btn>
                </v-layout>
            </section>
        </v-flex>
    </v-layout>
</template>


<script>
import moment from 'moment'
import NotFound from '@/components/NotFound'

export default {
    name: 'Clique',
    data() {
        return {
            accounts: [],
            loading: 0,
            grid: true,
        }
    },
    computed: {
        username() {
            return this.$route.path.replace(/\//g,'')
        },
        responsiveDim() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 80
                case 'sm': return 95
                case 'md': return 110
                case 'lg': return 125
                case 'xl': return 140
            }
        },
        responsiveDimSize() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 50
                case 'sm': return 55
                case 'md': return 60
                case 'lg': return 65
                case 'xl': return 70
            }
        }
    },
    // apollo: {
    //     profile: {
    //         query: PUBLIC_PROFILE_QUERY,
    //         variables() {
    //             return {
    //                 username: this.username
    //             }
    //         },
    //         error() {
    //             this.notFound = true
    //         }
    //     },
    // }
}
</script>

<style>
.tpc-account-box {
    width: 98vw;
    max-height: 50vh;
    overflow: auto;
}
</style>