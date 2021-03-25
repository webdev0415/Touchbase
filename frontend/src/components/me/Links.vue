<template>
<!-- NOTE: MOVE ALL DIALOGS TO THEIR OWN COMPONENT TO FIX ISSUES -->
    <v-layout row fill-height align-center justify-center v-if="$apollo.loading">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>

    <div v-else style="height: 100%;">
        <v-layout column align-center style="overflow: hidden;">
            <v-flex class="text-xs-center mt-3">
                <AddToushLink :key="addLinkKey" @linksUpdate="$apollo.queries.ownLinks.refetch(); addLinkKey++"/>
            </v-flex>
            <v-flex class="ln-scroll ln-grid">
                <v-layout fill-height row justify-center align-center>
                    <v-flex xs12 sm10 md8 lg6 xl5 class="px-3 pt-3">
                        <v-layout fill-height align-center column>
                            <v-flex v-for="(link, i) in ownLinks" :key="i" style="width: 100%;" class="my-3">
                                <v-badge style="width: 100%;" overlap left color="primary">
                                    <span slot="badge">{{ i + 1 }}</span> <!--slot can be any component-->
                                    <!--  min-width: 350px; width: 42vw; -->
                                    <v-card style="border-radius: 10px; width: 100%;">
                                        <v-card-title class="text-capitalize title">
                                            <!-- NOTE: if profile, show user profile pic, if feed, feed icon, if event, show event icon -->
                                            <img class="mr-4" src="/img/avatar-2.png" alt="lorem" width="70" height="70">
                                            <span v-if="link.item.isToushProfile">Profile Type</span>
                                            <span v-if="link.item.isToushFeed">Feed</span>
                                            <span v-if="link.item.isToushEvent">Event</span>
                                            <v-spacer></v-spacer>
                                            <!-- <v-tooltip bottom max-width="100%">
                                                <template slot="activator"> -->
                                            <v-text-field
                                                class="hidden-sm-and-down toush-text"
                                                @click="copyToush(makeToush(link.shortUrl))"
                                                style="max-width: 40%;"
                                                :value="makeToush(link.shortUrl)"
                                                readonly
                                                prepend-icon="link"
                                            ></v-text-field>
                                            <v-text-field
                                                class="hidden-md-and-up toush-text"
                                                @click="copyToush(makeToush(link.shortUrl))"
                                                style="max-width: 80%;"
                                                :value="makeToush(link.shortUrl)"
                                                readonly
                                                prepend-icon="link"
                                            ></v-text-field>
                                            <v-btn class="mr-0" @click="openToush(link.shortUrl)" flat icon color="primary">
                                                <v-icon>exit_to_app</v-icon>
                                            </v-btn>
                                                <!-- </template>
                                                <span>Click to copy! 📋</span>
                                            </v-tooltip> -->
                                        </v-card-title>
                                        <!-- color="green lighten-1" -->
                                        <v-snackbar
                                            bottom right
                                            v-model="snackbar"
                                            :timeout="3500"
                                        >
                                            Copied to clipboard!
                                            <v-btn dark flat @click="snackbar = false">Close</v-btn>
                                        </v-snackbar>
                                        <v-card-text class="pt-0">
                                            <v-layout justify-space-around row wrap>
                                                <v-flex xs12 md5 class="text-xs-center">
                                                    <v-layout align-center column>
                                                        <span class="grey--text text--darken-2 mb-1">Analytics</span>
                                                        <v-spacer></v-spacer>
                                                        <!-- <v-btn small class="text-capitalize font-weight-regular" depressed color="primary">View</v-btn> -->
                                                        <v-chip outline color="primary">
                                                            <span>Coming Soon</span>
                                                            <v-icon right class="pr-1">code</v-icon>
                                                        </v-chip>
                                                        <v-spacer></v-spacer>
                                                    </v-layout>
                                                </v-flex>
                                                <v-divider class="hidden-sm-and-down" inset vertical></v-divider>
                                                <v-divider class="hidden-md-and-up my-2 mr-5" inset></v-divider>
                                                <v-flex xs12 md5 class="text-xs-center">
                                                    <v-layout align-center column>
                                                        <span class="grey--text text--darken-2  mb-1">Accounts</span>
                                                        
                                                        <v-dialog
                                                            v-model="link.accountDialog"
                                                            :max-width="dialogWidth"
                                                        >
                                                            <v-btn slot="activator" small class="text-capitalize font-weight-regular" depressed color="primary">View</v-btn>
                                                            <v-card style="border-radius: 25px;">
                                                                <v-card-title class="justify-center">
                                                                    <span class="display-1 font-weight-light text-capitalize grey--text text--darken-2">Accounts for {{ link.shortUrl }}</span>
                                                                </v-card-title>
                                                                <v-card-text style="max-height: 65vh; overflow: auto;">
                                                                    <v-layout column class="pl-4">
                                                                        <v-flex class="my-2" v-for="service in link.item.accountListJSON.services" :key="service">
                                                                            <v-avatar :size="responsiveDimSize" class="mr-4"><img :src="$store.state.logoList[service]" alt=""></v-avatar>
                                                                            <v-chip label outline class="grey lighten-4">
                                                                                <span class="text-capitalize">{{ service.substring(0, service.indexOf('.')) }}</span>
                                                                            </v-chip>
                                                                        </v-flex>
                                                                    </v-layout>
                                                                    
                                                                </v-card-text>
                                                            </v-card>
                                                        </v-dialog>
                                                        
                                                    
                                                    
                                                    </v-layout>
                                                </v-flex>
                                            </v-layout>
                                            <v-layout row justify-end>
                                                <span class="grey--text text--darken-3 subheading text-uppercase mt-2 mr-2">{{ link.usageCount }} Views</span>
                                            </v-layout>
                                            <v-layout class="grey--text text-uppercase caption mt-2 pl-1" align-end wrap justify-space-between row fill-height>
                                                <!-- <span class="ml-2 caption"> -->
                                                <v-flex xs12 md6><span>Created {{ link.created }}</span></v-flex>
                                                <v-flex xs12 md6 :class="{ 'mt-2': true, 'text-xs-right': $vuetify.breakpoint.mdAndUp }" v-if="link.lifespan != -1">
                                                    <span>Expiry:  {{ link.expiry }}</span>
                                                </v-flex>
                                                <!-- </span> -->
                                                
                                            </v-layout>
                                            
                                            
                                        </v-card-text>
                                        <v-divider></v-divider>
                                        <v-layout row justify-center align-center fill-height>
                                            <!-- <v-dialog
                                                v-model="link.optionsDialog"
                                                :max-width="dialogWidth"
                                            > -->
                                                <v-card-actions>
                                                    <!-- <v-layout justify-center align-center> -->
                                                    
                                                    
                                                    <v-btn :to="`/links/${link.shortUrl}/edit`" flat block color="primary">
                                                        <span>Configure</span>
                                                    </v-btn>
                                                    <!-- </v-layout> -->
                                                    <!-- <v-spacer></v-spacer>
                                                    <v-btn flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">remove</span><v-icon>delete</v-icon></v-btn> -->
                                                </v-card-actions>   
                                            <!-- </v-dialog> -->
                                            
                                        </v-layout>
                                                            
                                    </v-card>
                                </v-badge>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    
                </v-layout>
                    
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import AddToushLink from "@/components/dashboard/AddToushLink"
import { OWN_LINKS_QUERY } from '@/graphql/queries/ownLinks'
import { ALL_ACCOUNTS_QUERY } from '@/graphql/queries/accounts'

import moment from 'moment'

export default {
    name: 'Advertising',
    data() {
        return {
            ownLinks: [],
            addLinkKey: 0,
            ownAccounts: [],
            loading: 0,
            dialog: false,
            snackbar: false,
            
        }
    },
    methods: {
        openToush(shortUrl) {
            let url = 'https://tou.sh/' + shortUrl
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
        },

    },
    components: {
        AddToushLink,
    },
    computed: {
        dialogWidth() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return '98vw'
                case 'sm': return '75vw'
                case 'md': return '60vw'
                case 'lg': return '50vw'
                case 'xl': return '45vw'
            }
        },
        responsiveDimSize() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 35
                case 'sm': return 40
                case 'md': return 45
                case 'lg': return 50
                case 'xl': return 55
            }
        },
    },
    beforeRouteEnter (to, from, next) {
        next(vm => {
            if (!vm.$loggedIn()) {
                vm.$router.replace('/login')
            }
        })
    },
    created() {
        this.$apollo.queries.ownLinks.skip = false
        this.$apollo.queries.ownLinks.refetch() 
    },
    apollo: {
        ownLinks: {
            skip: true,
            query: OWN_LINKS_QUERY,
            update(data) {
                if (data.ownLinks) {
                    data.ownLinks.forEach(link => {
                        link.expiry = moment(link.expired, 'YYYY-MM-DD HH:mm').fromNow()
                        link.created = moment(link.created, 'YYYY-MM-DD HH:mm').fromNow()
                        link.accounts = []
                        link.accountDialog = false
                        link.item.accountListJSON = JSON.parse(link.item.accountsList)
                    })
                } 
                // else {
                //     alert('Something went wrong. Please try again later! ⏳')
                // }
                return data.ownLinks
            }
        },
    }
}
</script>

<style scoped>
.toush-text >>> .v-text-field__slot input {
    color: #9E9E9E !important;
    font-weight: 400 !important;
}

.ln-align-bottom {
    position: fixed;
    bottom: 0;
}

.ln-grid {
    height: calc(100% - 184px);
    /* max-height: calc(100vh - 210px); */
    width: calc(100% - 10px);
}

.ln-scroll {
    overflow-y: auto;
    overflow-x: hidden;
}

.links-date-divs {
    height: 20px;
}

</style>