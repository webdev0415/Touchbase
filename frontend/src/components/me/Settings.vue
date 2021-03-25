<template>
    <v-layout row fill-height align-center justify-center v-if="$apollo.loading && !refetch">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>

    <div class="home-div" v-else style="overflow: hidden;">
        <!-- NOTE: MAX-HEIGHTS MUST BE ADJUSTED FOR MOBILE AND DESKTOP, DECIDE ON BOTTOMNAV OR NOT -->
        <v-layout fill-height row style="max-height: calc(100vh - 58px); overflow: hidden;">
            <!-- VVVVV PUT OVERFLOW SCROLL ON THIS -->
            <v-flex class="hidden-sm-and-down white" md3 style="min-width: 285px;">
                <v-layout fill-height column align-center justify-space-between class="pt-4">
                    <v-flex xs2 class="text-xs-center">
                        <!-- <v-btn large flat to="/me/edit" class="animated-box in font-weight-medium subheading" color="primary">Edit My Profile</v-btn> -->
                        <v-avatar color="primary" size="120">
                            <img src="/img/avatar-2.png" alt="">
                        </v-avatar>
                        <p class="text-xs-center font-weight-regular my-0 headline mt-2">Seneca Mans</p>
                        <span class="text-xs-center grey--text text--darken-1 subheading">@username</span>
                        <p class="primary--text title font-weight-regular mt-3" @click="$router.push('/me/edit')" style="cursor: pointer;">Edit</p>
                    </v-flex>
                    <!-- <v-flex>
                        <v-icon color="grey lighten-1" class="mb-0 pb-0">keyboard_arrow_up</v-icon>
                    </v-flex>
                    <v-flex>
                        <v-divider vertical class="ocedlo-divs"></v-divider>
                    </v-flex> -->
                    

                    <v-flex xs9 class="mt-1" style="width: 100%; overflow: hidden;" >
                        <!-- <v-divider></v-divider> -->
                        <!-- <v-list> -->
                        <div 
                            v-for="item in items" :key="item.title"
                            style="width: 100%;" class="my-1"
                        >
                            <v-layout row @click="selected=item.title" style="cursor: pointer;" :class="{ primaryLight: item.title === selected, 'settings-item-container': true }">
                                <div v-if="item.title === selected" style="min-height: 100%; min-width: 8px;" class="primary lighten-1"></div>
                                <!-- <v-btn flat large block class="text-xs-left" right color="primary"> -->
                                <v-layout align-center style="min-height: 100%;" class="settings-item-text">
                                    <v-flex style="width: 100%;" class="title">
                                        <v-icon color="grey darken-2" class="ml-3">{{ item.action }}</v-icon>
                                        <!-- <v-spacer></v-spacer> -->
                                        <span class="ml-2 text-capitalize font-weight-light">
                                            {{ item.title }}
                                        </span>
                                    </v-flex>
                                </v-layout>
                                
                                    <!-- <v-spacer></v-spacer> -->
                                <!-- </v-btn> -->
                                <v-btn v-if="!item.expanded" flat @click="item.expanded = true" icon large color="grey darken-2"><v-icon>keyboard_arrow_down</v-icon></v-btn>
                                <v-btn v-else flat @click="item.expanded = false" icon large color="grey darken-2"><v-icon>keyboard_arrow_up</v-icon></v-btn>
                            </v-layout>
                            
                            <v-layout v-if="item.items && item.expanded" class="pl-5 pb-2" column justify-space-around>
                                <!-- Security & Privacy -->
                                <!-- <template> -->
                                <v-flex v-for="(subItem, i) in item.items" :key="i" @click="selected = item.title; selectedSub = subItem.title" class="ml-2 mb-1 text-capitalize grey--text text--darken-1 font-weight-light">
                                    <v-icon color="primary">arrow_right</v-icon>
                                    <span class="e-title">{{ subItem.title }}</span>
                                </v-flex>
                                <!-- </template> -->
                                <!-- <template v-else-if="item.title === 'Preferences'">
                                    <div>
                                        
                                    </div>
                                </template>
                                <template v-else-if="item.title === 'Advertising'">
                                    <div>
                                        
                                    </div>
                                </template>
                                <template v-else-if="item.title === 'Security & Privacy'">
                                    <div>
                                        
                                    </div>
                                </template> -->
                            </v-layout>
                            <!-- <v-divider></v-divider> -->
                        </div>
                            <!-- <v-list-group
                                v-for="item in items"
                                v-model="item.active"
                                :key="item.title"
                                :prepend-icon="item.action"
                                no-action
                            >
                                <v-list-tile>
                                    <v-list-tile-content>
                                        <v-list-tile-title v-slot="activator">{{ item.title }}</v-list-tile-title>
                                    </v-list-tile-content>
                                </v-list-tile>

                                <v-list-tile
                                    v-for="subItem in item.items" :key="subItem.title"
                                >
                                    <v-list-tile-content>
                                        <v-list-tile-title>{{ subItem.title }}</v-list-tile-title>
                                    </v-list-tile-content>
                                </v-list-tile>

                            </v-list-group> -->
                        <!-- </v-list> -->
                        <!-- <v-layout fill-height justify-center class="text-xs-center">
                            <v-divider vertical style="height: 100vh;"></v-divider>
                        </v-layout> -->
                        
                    </v-flex>
                </v-layout>
            </v-flex>

            <v-divider vertical class="full-height hidden-sm-and-down"></v-divider>

            <v-flex xs12 style="max-height: calc(100vh - 58px); overflow-y: auto;">
                <!-- hidden-sm-and-down -->
                <v-layout column align-center justify-center class="py-5">
                    <v-card flat class="settings-card" :style="cardFlex">
                        <v-card-title class="justify-center">
                            <!-- perhaps put drop down select here? -->
                            <span class="display-2 grey--text text--darken-4 text-xs-center">{{ selected }}</span>
                        </v-card-title>
                        <v-divider></v-divider>
                        <v-card-text v-if="selected === 'Account & Profile'">
                            <Account :settings="ownSettings" @settingsUpdate="childUpdate"/>
                        </v-card-text>
                        <v-card-text v-else-if="selected === 'Preferences'">
                            <Preferences :settings="ownSettings" @settingsUpdate="childUpdate"/>
                        </v-card-text>
                        <v-card-text v-else-if="selected === 'Advertising'">
                            <Advertising :settings="ownSettings" @settingsUpdate="childUpdate"/>
                        </v-card-text>
                        <v-card-text v-else-if="selected === 'Security & Privacy'">
                            <SecurityPrivacy :settings="ownSettings" @settingsUpdate="childUpdate"></SecurityPrivacy>
                        </v-card-text>
                    </v-card>
                </v-layout>

                <!-- <v-layout style="overflow: hidden;" column justify-center align-center class="settings-main hidden-md-and-up pt-3">
                    <v-flex>
                        <v-select
                            outline
                            style="width: 95vw;"
                            :items="cSelect"
                            v-model="cSelectVal"
                            color="primary"
                        >
                            <span slot="label">Setting</span>
                        </v-select>
                    </v-flex>
                    <v-flex class="text-xs-center">
                        <v-btn large flat class="animated-box in font-weight-medium subheading" color="primary">Edit My Profile</v-btn>
                    </v-flex>

                    <v-flex class="mt-5">
                        memes
                    </v-flex>
                </v-layout> -->
            </v-flex>
        </v-layout>
        <v-btn @click="save()" :loading="loading" color="primary" fixed bottom class="mr-2" right style="height: 50px;">
            <span class="mr-2">Save</span>
            <v-icon>check</v-icon>
        </v-btn>
    </div>
</template>

<script>
import { EDIT_SETTINGS_MUTATION } from '@/graphql/mutations/editSettings'
import { OWN_SETTINGS_QUERY } from '@/graphql/queries/ownSettings'

import Account from '@/components/settings/Account'
import Preferences from '@/components/settings/Preferences'
import Advertising from '@/components/settings/Advertising'
import SecurityPrivacy from '@/components/settings/SecurityPrivacy'

export default {
    name: 'Settings',
    components: {
        Account, Preferences,
        Advertising, SecurityPrivacy,
    },
    data() {
        return {
            selected: 'Account & Profile',
            selectedSub: '',
            cSelect: ['Account & Profile', 'Preferences', 'Advertising', 'Security & Privacy'],
            cSelectVal: 'Account & Profile',
            items: [
                {
                    expanded: false,
                    action: 'assignment_ind',
                    title: 'Account & Profile',
                    active: true,
                    items: [
                        { title: 'TBD' },
                        { title: 'TBD' },
                    ]
                },
                {
                    expanded: false,
                    action: 'style',
                    title: 'Preferences',
                    items: [
                        { title: 'TBD' }
                    ]
                },
                {
                    expanded: false,
                    action: 'gradient',
                    title: 'Advertising',
                    items: [
                        { title: 'TBD' },
                        { title: 'TBD' },
                        { title: 'TBD' }
                    ]
                },
                {
                    expanded: false,
                    action: 'lock',
                    title: 'Security & Privacy',
                    items: [
                        { title: 'TBD' },
                        { title: 'TBD' }
                    ]
                }
            ],
            changed: {},
            loading: false,
            refetch: false,
            ownSettings: [],
            feedbackEmpty: false,
            // a means ANYONE
            // s means SOME/SELECT FEW
            // n means NO ONE
            // accountType: 'p',
            // notifsEnable: true,
            // notifsFollows: true,
            // notifsNewAccount: true,
            // notifsUpdates: true,
            // sponsoredRelevant: true,
            // privacyAccounts: 'a',
            // privacyFollows: 'a',
            // privateProfile: false,
        }
    },
    computed: {
        
        loggedIn() {
            // make sure to validate the jwt-token with the verifyToken mutation!
            if (localStorage.getItem('jwt-token')) {
                return true
            } else {
                return false
            }
            // return this.$store.state.loggedIn
        },
        cardFlex() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return { width: 'calc(100vw - 40px)', 'background-color': 'white' }
                case 'sm': return { width: 'calc(100vw - 40px)', 'background-color': 'white' }
                case 'md': return { width: 'calc(100vw / 12 * 8)', 'background-color': '#FAFAFA' }
                case 'lg': return { width: 'calc(100vw / 12 * 8)', 'background-color': '#FAFAFA' }
                case 'xl': return { width: 'calc(100vw / 12 * 8)', 'background-color': '#FAFAFA' }
            }
        }
    },
    methods: {
        childUpdate(change) {
            this.changed[Object.keys(change)[0]] = Object.values(change)[0]
        },
        save() {
            ////////////// ********** IMPORTANT NOTE: CHANGE ALL EDITS TO THIS LOGIC!!
            this.loading = true
            let variables = {}
            if (Object.keys(this.changed).length > 0) {
                for (let change in this.changed) {
                    if (this.changed[change] !== null && this.changed[change] !== '' && this.changed[change] != this.ownSettings[change]) variables[change] = this.changed[change]
                }
                this.$apollo.mutate({
                    mutation: EDIT_SETTINGS_MUTATION,
                    variables: variables
                }).then(result => {
                    if (result.data.editSettings.success) {
                        this.loading = false
                        this.refetch = true
                        this.$apollo.queries.ownSettings.refetch().then(() => {
                            console.log('done refetch')
                            this.refetch = false
                        })
                    } else {
                        this.loading = false
                        this.feedback = true
                    }
                }).catch(err => {
                    console.log(err)
                    this.feedback = true
                    this.loading = false
                })
            } else {
                this.feedbackEmpty = true
            }
            
        }
    },
    beforeRouteEnter (to, from, next) {
        next(vm => {
            if (!vm.loggedIn) {
                vm.$router.replace('/login')
            }
        })
    },
    apollo: {
        ownSettings: {
            query: OWN_SETTINGS_QUERY,
            result({ data }) {
                console.log(data.ownSettings)
            }
        }
    }
}
</script>

<style>

.primaryLight {
    background-color: #ffddd6;
}

.settings-container {
    overflow-y: auto;
    overflow-x: hidden;
    max-height: calc(100vh - 56px);
}

.settings-card {
    /* min-height: calc(100vh - 146px);
    height: 1200px;
    width: 80%; */
    /* border-radius: 20px; */
    border-radius: 9px;
    /* max-height: calc(100vh - 146px);
    overflow-y: auto; */
}

.settings-item-text {
    color: #424242;
    -webkit-transition: color 0.23s;
    transition: color 0.23s;
}

.settings-item-container:hover > .settings-item-text {
    color: #FF7256;
}
</style>