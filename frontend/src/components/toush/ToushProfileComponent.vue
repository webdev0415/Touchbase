<template>
    <!-- <h1>{{ toushLink.item.accountsList }}</h1> -->
    
    <!-- <h2 class="ml-5" v-for="account in accountList.services" :key="account">{{ account }}</h2> -->
    <v-layout row fill-height align-center justify-center v-if="$apollo.loading">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>
    <!-- <div v-else>

        <div>
            <span>{{ toushLink.usageCount }} Views</span>
        </div>

        <div v-if="toushLink.lifespan != -1">
            <span>Expires {{ expiry }}</span>
        </div>

        <div v-if="toushLink.item.username">
            <span>@{{ toushLink.item.user.username }}</span>
        </div>
        <div v-if="toushLink.item.firstName && toushLink.item.lastName">
            <span>{{ toushLink.item.user.firstName }} </span>
            <span>{{ toushLink.item.user.lastName }}</span>
        </div>
        <div v-else-if="toushLink.item.lastName && !toushLink.item.firstName">
            <span>{{ toushLink.item.user.lastName }}</span>
        </div>
        <div v-else-if="toushLink.item.firstName && !toushLink.item.lastName">
            <span>{{ toushLink.item.user.firstName }}</span>
        </div>
        <ApolloQuery v-if="toushLink.item.contactEmail || toushLink.item.contactPhone"
            :query="require('@/graphql/queries/cEmailcPhone.gql')"
            :variables="{ username }"
        >
            <template slot-scope="{ result: { loading, error, data } }">
                <div v-if="!loading && data && !error">
                    <span>{{ data.profile.contactEmail }}</span> <br>
                    <span>{{ data.profile.contactPhone }}</span>
                </div>
                <div v-else-if="error">
                    <span>You broke it: {{ error }}</span>
                </div>
            </template>
        </ApolloQuery>

        <div v-if="toushLink.item.message">
            <span>{{ toushLink.item.message }}</span>
        </div>

        <v-layout class="tpc-account-box" justify-center align-center>
            <v-flex xs12 md6 v-if="!grid">
                <v-expansion-panel popout>
                    <v-expansion-panel-content
                        v-for="account in theAccounts" :key="account.service"
                        expand-icon="arrow_drop_down"
                    >
                        <div slot="header">
                            <v-layout align-center justify-start row fill-height>
                                <v-avatar size="40" class="mr-4"><img src="/img/avatar-2.png" alt=""></v-avatar>
                                <span class="text-capitalize">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                <v-icon class="mx-4">compare_arrows</v-icon>
                                <span>@{{ account.identifier }}</span>
                                <v-spacer></v-spacer>
                                <v-btn flat :href="account.url" icon color="primary" class="mr-4">
                                    <v-icon size="32">exit_to_app</v-icon>
                                </v-btn>
                            </v-layout>
                            
                        </div>
                        <v-card>
                            <v-card-text class="grey lighten-4">
                                <v-layout align-center justify-space-between row fill-height>
                                    <span class="ml-2">Linked {{ account.created }}</span>
                                    <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                                </v-layout>
                            </v-card-text>
                            <v-divider></v-divider>
                            <v-card-actions>
                                <v-btn @click="openProfile(account.url)" color="primary">Go To Profile</v-btn>
                            </v-card-actions>
                        </v-card>

                    </v-expansion-panel-content>
                </v-expansion-panel>
            </v-flex>

            <v-flex xs12 sm8 md6 v-else>
                <v-container fluid grid-list-lg class="ma-0 pa-0">
                    <v-layout row wrap>
                        <v-flex v-for="account in theAccounts" :key="account.service" xs6 md4 lg3>
                            <v-dialog flat :v-model="account.dialog" max-width="450" style="height: 25vh;">
                                <div class="text-xs-center" slot="activator">
                                    <img src="/img/avatar-2.png" alt="lorem" width="100%" height="100%" style="padding-right: 39px;"> <br>
                                    <span class="text-capitalize">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                    <v-btn small icon :href="account.url">
                                        <v-icon small color="primary">exit_to_app</v-icon>
                                    </v-btn>
                                </div>

                                <v-card flat style="border-radius: 30px;">
                                    <v-card-title class="text-capitalize title">
                                        <img src="/img/avatar-2.png" alt="lorem" width="70" height="70">
                                        <span class="ml-4">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-layout wrap align-center justify-space-between row fill-height>
                                            <span class="ml-2">Linked {{ account.created }}</span>
                                            <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                                        </v-layout>
                                    </v-card-text>
                                    <v-divider></v-divider>
                                    <v-card-actions class="py-3">
                                        <v-layout justify-center align-center>
                                            <v-btn @click="account.dialog = false; openProfile(account.url)" color="primary">Go To Profile</v-btn>
                                        </v-layout>
                                        
                                    </v-card-actions>                              
                                </v-card>
                                
                            </v-dialog>
                            
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-flex>
        </v-layout>
        <div class="tpc-grid-switch">
            <v-btn 
                v-if="!grid" color="primary"
                @click="grid = !grid"
                fab fixed
                bottom right
                style="margin-bottom: 100px;"
            >
                <v-icon>dashboard</v-icon>
            </v-btn>

            <v-btn 
                v-else color="primary"
                @click="grid = !grid"
                fab fixed
                bottom right
                style="margin-bottom: 100px;"
            >
                <v-icon>list</v-icon>
            </v-btn>
        </div>

    </div> -->
    <v-layout v-else row fill-height justify-center>
        <v-flex xs12>
            <section>
                <!-- NOTE: change the background parallax image to our own -->
                <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg" style="border-radius: 0 0 13px 13px; height: calc(20vh + 400px);">
                    <v-layout row justify-start>
                        <v-flex xs9 sm5 md4 lg3 >
                            <v-text-field
                                @click="copyToush(makeToush(toushLink.shortUrl))"
                                style="margin-top: 85px;"
                                readonly
                                height="20"
                                box
                                dark
                                hide-details
                                color="primary"
                            >
                                <v-icon class="white--text" slot="prepend">link</v-icon>
                                <span slot="prepend-inner" class="title font-weight-light white--text">{{ makeToush(toushLink.shortUrl) }}</span>
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
                                <span v-if="toushLink.item.firstName">{{ toushLink.item.user.firstName }}</span>
                                <span v-if="toushLink.item.lastName"> {{ toushLink.item.user.lastName }}</span>
                            </p>
                            <p v-if="toushLink.item.username" class="mb-4 title font-weight-light text-xs-center">@{{ toushLink.item.user.username }}</p>
                            <ApolloQuery v-if="toushLink.item.contactEmail || toushLink.item.contactPhone"
                                :query="require('@/graphql/queries/cEmailcPhone.gql')"
                                :variables="{ username }"
                            >
                                <template slot-scope="{ result: { loading, error, data } }">
                                    <template v-if="!loading && data && !error">
                                        <p v-if="data.profile.contactEmail && toushLink.item.contactEmail" class="title font-weight-light text-xs-center">{{ data.profile.contactEmail }}</p>
                                        <p v-if="data.profile.contactPhone && toushLink.item.contactPhone" class="title font-weight-light text-xs-center">{{ data.profile.contactPhone }}</p>
                                    </template>
                                    <template v-else-if="error">
                                        <span>You broke it: {{ error }}</span>
                                    </template>
                                </template>
                            </ApolloQuery>
                        </v-flex>
                    </v-layout>
                </v-parallax>
            </section>
            
            <section style="margin-bottom: 15vh;">
                <v-layout column fill-height align-center>
                    <v-flex class="mt-2 mb-4 subheading text-uppercase grey--text text--darken-2 font-weight-light">
                        <!-- <v-layout align-center row justify-center>
                            <v-flex class="text-xs-center">
                                <template v-if="toushLink.lifespan != -1">
                                <span class="subheading text-uppercase grey--text text--darken-2 font-weight-light">Expires {{ expiry }}</span>
                                </template>
                            </v-flex>
                            <v-flex class="text-xs-center">
                                <span class="subheading text-uppercase grey--text text--darken-2 font-weight-light">{{ toushLink.usageCount }} Views</span>
                            </v-flex>
                        </v-layout> -->
                        <template v-if="toushLink.lifespan != -1">
                            <span>Expires {{ expiry }}</span>
                            <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                        </template>
                        <span>{{ toushLink.usageCount }} Views</span>
                    </v-flex>
                    <v-flex v-if="toushLink.item.message">
                        <p class="display-1 font-weight-light">{{ toushLink.item.message }}</p>
                    </v-flex>
                    <v-flex class="ac-accounts mt-5">
                        <v-expansion-panel style="max-width: 95vw;" popout v-if="!grid">
                            <v-expansion-panel-content
                                v-for="account in accounts" :key="account.service"
                                expand-icon="arrow_drop_down"
                            >
                                <div slot="header">
                                    <v-layout align-center justify-space-around row fill-height>
                                        <v-avatar :size="responsiveDimSize" class="mr-4"><img :src="$store.state.logoList[account.service]" alt=""></v-avatar>
                                        <span class="text-capitalize">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                        <template v-if="account.service.substring(0, account.service.indexOf('.')) === 'youtube'"></template>
                                        <template v-else>
                                            <v-icon class="mx-4">compare_arrows</v-icon>
                                            <span>@{{ account.identifier }}</span>
                                        </template>
                                        <v-spacer></v-spacer>
                                        <v-btn flat :href="account.url" icon color="primary" class="mr-4 hidden-sm-and-down">
                                            <v-icon size="32">exit_to_app</v-icon>
                                        </v-btn>
                                    </v-layout>
                                    
                                </div>
                                <v-card>
                                    <v-card-text class="grey lighten-4">
                                        <v-layout align-center justify-space-between row fill-height>
                                            <span class="ml-2">Linked {{ account.created }}</span>
                                            <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                                        </v-layout>
                                    </v-card-text>
                                    <v-divider></v-divider>
                                    <v-card-actions class="pa-3">
                                        <v-btn @click="openProfile(account.url)" round outline color="primary">Go To Profile</v-btn>
                                        <v-spacer></v-spacer>
                                        <!-- <v-btn v-if="!account.remove" @click="account.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">remove</span><v-icon>delete</v-icon></v-btn>
                                        <v-btn v-else-if="account.remove && !account.confirmedRemove" @click="account.confirmedRemove=true; removeAccount(account.service)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">Confirm?</span><v-icon>check</v-icon></v-btn>
                                        <span class="success--text" v-if="account.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->
                                    </v-card-actions>
                                </v-card>

                            </v-expansion-panel-content>
                        </v-expansion-panel>

                        <v-container class=" ac-accounts-grid pa-0 ma-0" fluid grid-list-sm v-else>
                            <v-layout row wrap class="ac-accounts-scroll">
                                <v-flex v-for="account in accounts" class="mt-2 mb-5" :key="account.service" xs6 md4>
                                    <v-layout justify-center align-center column>
                                        <v-dialog flat :v-model="account.dialog" max-width="450">
                                            <template slot="activator">
                                                <v-img :src="$store.state.logoList[account.service]" color="primary" :alt="account.service" :width="responsiveDim" :height="responsiveDim" ></v-img>
                                            </template>

                                            <v-card flat style="border-radius: 30px;">
                                                <v-card-title class="text-capitalize title">
                                                    <img :src="$store.state.logoList[account.service]" alt="lorem" width="70" height="70">
                                                    <span class="ml-4">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                                </v-card-title>
                                                <v-card-text>
                                                    <v-layout wrap align-center justify-space-between row fill-height>
                                                        <span class="ml-2">Linked {{ account.created }}</span>
                                                        <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                                                    </v-layout>
                                                </v-card-text>
                                                <v-divider></v-divider>
                                                <v-card-actions class="pa-3">
                                                    <v-btn @click="account.dialog=false; openProfile(account.url)" round outline color="primary">Go To Profile</v-btn>
                                                    <v-spacer></v-spacer>
                                                    <!-- <v-btn v-if="!account.remove" @click="account.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">remove</span><v-icon>delete</v-icon></v-btn>
                                                    <v-btn v-else-if="account.remove && !account.confirmedRemove" @click="account.confirmedRemove=true; removeAccount(account.service)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">Confirm?</span><v-icon>check</v-icon></v-btn>
                                                    <span class="success--text" v-if="account.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->
                                                </v-card-actions>                              
                                            </v-card>
                                            
                                        </v-dialog>
                                        <v-badge class="mt-2 mr-1" right color="transparent">
                                            <span class="text-capitalize title font-weight-light grey--text text--darken-3">
                                                {{ account.service.substring(0, account.service.indexOf('.')) }}
                                            </span>
                                            <v-icon @click="openProfile(account.url)" slot="badge" color="primary">open_in_new</v-icon>
                                        </v-badge>
                                    </v-layout>
                                    
                                </v-flex>
                            </v-layout>
                        </v-container>
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
import { TOUSH_ACCOUNTS_QUERY } from '@/graphql/queries/toushAccounts'

export default {
    name: 'ToushProfile',
    props: ['toushLink'],
    data() {
        return {
            accounts: [],
            loading: 0,
            grid: true,
        }
    },
    computed: {
        username() {
            // console.log(this.toushLink)
            return this.toushLink.item.user.username
        },
        expiry() {
            // return moment(this.toushLink.expired).fromNow(true) + ' from now'
            return moment(this.toushLink.expired).fromNow()
            // return this.toushLink.expired
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
    methods: {
        test() {
            console.log(this.profile.user.username, this.theAccounts[0].url)
        },
        openProfile(url) {
            window.open(url)
        },
        makeToush(shortUrl) {
            return `https://tou.sh/${shortUrl}`
        },
        copyToush(url) {
            const el = document.createElement('textarea');  // Create a <textarea> element
            el.value = url                                 // Set its value to the string that you want copied
            el.setAttribute('readonly', '')                // Make it readonly to be tamper-proof
            el.style.position = 'absolute'                 
            el.style.left = '-9999px'                      // Move outside the screen to make it invisible
            document.body.appendChild(el)                  // Append the <textarea> element to the HTML document
            const selected =            
                document.getSelection().rangeCount > 0        // Check if there is any content selected previously
                ? document.getSelection().getRangeAt(0)     // Store selection if found
                : false                                    // Mark as false to know no selection existed before
            el.select()                                    // Select the <textarea> content
            document.execCommand('copy')                   // Copy - only works as a result of a user action (e.g. click events)
            document.body.removeChild(el)                  // Remove the <textarea> element
            if (selected) {                                 // If a selection existed before copying
                document.getSelection().removeAllRanges();    // Unselect everything on the HTML document
                document.getSelection().addRange(selected);   // Restore the original selection
            }
            this.snackbar = true
        }
    },
    // computed: {
    //     accountList() {
    //         return JSON.parse(this.toushLink.item.accountsList)
    //     }
    // },


    apollo: {
        accounts: {
            query: TOUSH_ACCOUNTS_QUERY,
            variables() {
                return {
                    shortUrl: this.toushLink.shortUrl
                }
                
            },
            update(data) {
                if (data.toushAccounts) {
                    data.toushAccounts.forEach(account => {
                        account.created = moment(account.created).fromNow()
                        account.dialog = false
                    })
                } else {
                    alert('Something went wrong. Please try again later! ⏳')
                }
                return data.toushAccounts
                
            }
        }
    }
}
</script>

<style>
.tpc-account-box {
    width: 98vw;
    max-height: 50vh;
    overflow: auto;
}
</style>