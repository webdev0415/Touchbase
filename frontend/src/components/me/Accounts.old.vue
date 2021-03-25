<template>
    <div style="height: 100%;">
        <v-layout class="pt-5" column align-center>
            <v-flex class="text-xs-center">
                <LinkAccount :key="linkAccountKey" @accountsUpdate="$apollo.queries.ownAccounts.refetch(); linkAccountKey++"/>
            </v-flex>

            <v-flex class="ac-accounts mt-5">
                <v-expansion-panel style="max-width: 95vw;" class="mb-5" popout v-if="!grid">
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
                                <v-btn v-if="!account.remove" @click="account.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn>
                                <v-btn v-else-if="account.remove && !account.confirmedRemove" :loading="deleteLoading" @click="account.confirmedRemove=true; removeAccount(account.service)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Confirm?</span><v-icon>check</v-icon></v-btn>
                                <span class="success--text" v-if="account.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span>
                            </v-card-actions>
                        </v-card>

                    </v-expansion-panel-content>
                </v-expansion-panel>

                <v-container class=" ac-accounts-grid pa-0 ma-0" fluid grid-list-sm v-else>
                    <v-layout row wrap>
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
                                            <v-btn v-if="!account.remove" @click="account.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn>
                                            <v-btn :loading="deleteLoading" v-else-if="account.remove && !account.confirmedRemove" @click="account.confirmedRemove=true; removeAccount(account.service)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Confirm?</span><v-icon>check</v-icon></v-btn>
                                            <span class="success--text" v-if="account.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span>
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
        </v-layout>
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
        </div>
</template>

<script>
import moment from 'moment'
import {ALL_ACCOUNTS_QUERY } from '@/graphql/queries/accounts'
import LinkAccount from '@/components/me/LinkAccount'

export default {
    name: 'Accounts',
    components: {
        LinkAccount
    },
    data() {
        return {
            linkAccountKey: 0,
            ownProfile: {},
            accounts: [],
            dialog: false,
            loading: 0,
            deleteLoading: false,
            grid: true,
        }
    },
    methods: {
        test() {
            console.log(this.ownProfile.user.username, this.accounts[0].url)
        },
        openProfile(url) {
            window.open(url)
        },
        removeAccount(service) {
            this.deleteLoading = true
            console.log(service)
            this.deleteLoading = false
            location.reload()
        }
    },
    computed: {
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
    beforeRouteEnter (to, from, next) {
        next(vm => {
            if (!vm.$loggedIn()) {
                vm.$router.replace('/login')
            }
        })
    },
    created() {
        this.$apollo.queries.accounts.skip = false
        this.$apollo.queries.accounts.refetch() 
    },
    apollo: {
        accounts: {
            skip: true,
            query: ALL_ACCOUNTS_QUERY,
            update(data) {
                if (data.ownAccounts) {
                    data.ownAccounts.forEach(account => {
                        if (account.service === 'steamcommunity.com') account.service = 'steam.com'
                        account.created = moment(account.created).fromNow()
                        account.dialog = false
                        account.confirmedRemove = false
                        account.remove = false
                    })
                } else {
                    alert('Something went wrong. Please try again later! ⏳')
                }
                return data.ownAccounts          
            }
        }
    }
}
</script>

<style>
.ac-accounts {
    width: calc(50vw + 300px);
}

.ac-accounts-grid {
    /* height: 100vh; */
    /* max-height: calc(30vh + 350px); */
}

.ac-accounts-scroll {
    overflow: auto;
}
</style>