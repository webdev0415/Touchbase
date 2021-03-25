<template>
    <v-dialog max-width="800px" v-model="dialog" scrollable>
        <v-btn slot="activator" icon outline large color="primary" class="my-2">
            <v-icon>link</v-icon>
        </v-btn>
        <v-card style="border-radius: 25px;">
            <v-toolbar color="primary">
                <v-toolbar-side-icon class="white--text ml-2">
                    <v-icon large>link</v-icon>
                </v-toolbar-side-icon>
                <v-toolbar-title class="text-uppercase white--text pr-5">
                    <div class="headline">
                        <span>My Links</span>
                    </div>
                </v-toolbar-title>

                <!-- <v-toolbar dense flat class="searchbox mr-5" color="primaryComp">
                    <v-text-field
                        label="Search"
                        flat
                        solo
                        hide-details
                        clearable
                        prepend-inner-icon="search"
                    >
                    </v-text-field>
                </v-toolbar> -->

            </v-toolbar>
            <v-card-text style="max-height: 75vh;">
                <v-layout align-center justify-space-around row>
                    <span class="mr-5">Link</span>
                    <span class="ml-5">Message</span>
                    <span>Views</span>
                </v-layout>
                
                <v-expansion-panel popout>
                    <!-- use router prop with to="" for links. Replaces router-link -->
                    <v-expansion-panel-content v-for="(link, i) in ownLinks" :key="i" expand-icon="arrow_drop_down">
                        <!-- basic info abt link -->
                        <div slot="header">
                            <v-layout align-center justify-start row fill-height>
                                <!-- <v-avatar size="40" class="mr-4"><img src="/img/avatar-2.png" alt=""></v-avatar> -->
                                <a :href="'https://tou.sh/' + link.shortUrl" class="text-capitalize">tou.sh/{{ link.shortUrl }}</a>
                                <v-icon class="mx-4">link</v-icon>
                                <span v-if="link.item.isToushProfile">Profile</span>
                                <span v-if="link.item.isToushFeed">Feed</span>
                                <span v-if="link.item.isToushEvent">Event</span>
                                <v-spacer></v-spacer>
                                <span>{{ link.item.message }}</span>
                                <v-spacer></v-spacer>
                                <div class="text-xs-center">
                                    <v-chip>{{ link.usageCount }}</v-chip>
                                </div>
                            </v-layout>
                        </div>
                        <v-card>
                            <v-card-text class="grey lighten-4">
                                <v-layout align-center justify-space-between row fill-height>
                                    <span class="ml-2">Created {{ link.momentCreated }}</span>
                                    <span class="mr-2">
                                        
                                        <span v-if="toushLink.lifespan != -1">Expires {{ link.expiry }}</span>
                                        <!-- <span v-else>Expires Never</span> -->
                                    </span>
                                </v-layout>
                                <v-layout wrap justify-space-between row>
                                    <v-checkbox disabled color="primary" label="Link To My Profile" v-model="link.item.linkToProfile"></v-checkbox>
                                    <div style="margin-right: 100%;"></div>
                                    <v-checkbox disabled color="primary" label="Username" v-model="link.item.username"></v-checkbox>
                                    <v-checkbox disabled color="primary" label="First Name" v-model="link.item.username"></v-checkbox>
                                    <v-checkbox disabled color="primary" label="Last Name" v-model="link.item.username"></v-checkbox>
                                    <v-checkbox disabled color="primary" label="Contact Email" v-model="link.item.username"></v-checkbox>
                                    <v-checkbox disabled color="primary" label="Contact Phone" v-model="link.item.username"></v-checkbox>
                                </v-layout>
                                <!-- <v-card v-if="link.item.isToushProfile"> -->
                                    <!-- add close prop for editing -->
                                <div v-if="link.item.isToushProfile">
                                    <v-chip class="grey lighten-2" v-for="service in link.item.accountListJSON.services" :key="service">
                                        <v-avatar><v-icon>person</v-icon></v-avatar>
                                        <span class="text-capitalize">{{ service.substring(0, service.indexOf('.')) }}</span>
                                    </v-chip>
                                </div>
                                
                                <!-- </v-card> -->
                            </v-card-text>
                            <v-divider></v-divider>
                            <v-card-actions>
                                <v-btn @click="openToush(link.shortUrl)" color="primary">Go To Link</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-expansion-panel-content>
                </v-expansion-panel>
            </v-card-text>
            
        </v-card>
    </v-dialog>


</template>

<script>
import { OWN_LINKS_QUERY } from '@/graphql/queries/ownLinks'
import moment from 'moment'

export default {
    name: 'ToushLinkList',
    data() {
        return {
            ownLinks: [],
            loading: 0,
            dialog: false
        }
    },
    methods: {
        openToush(shortUrl) {
            let url = 'https://tou.sh/' + shortUrl
            window.open(url)
        }
    },
    // apollo: {
    //     ownLinks: {
    //         query: OWN_LINKS_QUERY,
    //         result({ data, loading }) {
    //             if (!loading) {
    //                 // console.log(data.ownLinks[0].usageCount)
    //                 // console.log(data.ownLinks[0].item.accountsList)
    //                 data.ownLinks.forEach(link => {
    //                     // if (link.lifespan === -1) {
    //                     //     link.momentExpired = 'never'
    //                     // } else {
    //                     //     link.momentCreated = moment(link.created).fromNow()
    //                     //     //link.momentExpired = moment(link.expired).fromNow(true) + ' from now'
    //                     //     //link.momentExpired = `in ${link.lifespan} hours`
    //                     //     let diff = moment(link.expired).diff(moment(link.created))
    //                     //     let diffDuration = moment.duration(diff)
    //                     //     link.momentExpired = `${diffDuration.days()} days, ${diffDuration.hours()} hours`
    //                     //     if (moment(link.created).diff(moment(link.expired), 'seconds', true) === 0) {
    //                     //         link.momentExpired = 'Expired'
    //                     //     }
    //                     //     if (moment(link.created).diff(moment(link.expired), 'hours', true) <= 1) {
    //                     //         link.momentExpired = 'soon'
    //                     //     }

    //                     //     // if (moment(link.expired).diff(moment(link.created), 'seconds', true) === 0) {
    //                     //     //     link.momentExpired = 'Expired'
    //                     //     // } else if (moment(link.expired).diff(moment(link.created), 'hours') <= 1) {
    //                     //     //     link.momentExpired = 'soon'
    //                     //     // } else {
    //                     //         // let diff = moment(link.expired).diff(moment(link.created))
    //                     //         // let diffDuration = moment.duration(diff)

    //                     //         // link.momentExpired = `${diffDuration.days()} days, ${diffDuration.hours()} hours`
    //                     //     // }
    //                     // }

    //                     // PROPER THINGY
    //                     link.momentCreated = moment(link.created).fromNow()
    //                     link.expiry = moment(link.expired).fromNow()
    //                     console.log(link, 'MEMEMEMEMS')

    //                     link.item.accountListJSON = JSON.parse(link.item.accountsList)
    //                     // console.log(link.item.accountListJSON)
    //                     // for updating
    //                     //link.updatedLinkToProfile = link.linkToProfile
    //                     // THING
    //                     // TAKE LIFESPAN VAL AND EVALUATE THE EXPIRY DATE FROM LINK.CREATED
    //                     //
    //                 })
    //             }
                
    //         }
    //     }
    // }
}
</script>


<style>

</style>
