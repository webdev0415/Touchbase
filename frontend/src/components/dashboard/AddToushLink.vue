<template>
<div>
    <v-dialog lazy :max-width="dialogWidth" v-model="dialog" scrollable>
        <v-btn slot="activator" flat large color="primary" class="animated-box in font-weight-medium subheading">
            New Toush Link
        </v-btn>
        <v-card style="border-radius: 25px;">
            <v-card-text>
                <v-form class="pr-4 pl-2" ref="makeToushForm" lazy-validation>
                    <span class="caption grey--text mt-1">* Beta</span>
                    <v-select
                        :items="itemsPef"
                        v-model="typeOfLink"
                        outline
                        prepend-inner-icon="link"
                    >
                        <span slot="label">Type of Link</span>
                    </v-select>
                    <v-divider class="mt-0 mb-4"></v-divider>
                    <v-layout row wrap justify-space-between>
                        <v-flex xs12 md6>
                            <v-text-field class="my-0"
                                outline
                                clearable
                                label="Message"
                                prepend-inner-icon="message"
                                v-model="message"
                                counter="128"
                                hint="A custom message for your tou.sh link!"
                            ></v-text-field>
                        </v-flex>
                        <!-- :placeholder="'A custom message for my tou.sh ' + itemsPefPos + ' link'" -->
                        <v-flex xs12 md5>
                            <v-text-field class="my-0"
                                label="Custom Link"
                                outline
                                counter="20"
                                v-model="customLink"
                                clearable
                                hint="Custom link - ex. memes would result in tou.sh/memes"
                                prepend-inner-icon="lock"
                            ></v-text-field>
                        </v-flex>
                    </v-layout>
                    <v-divider></v-divider>
                    <p class="text-uppercase grey--text mt-1">Expire After</p>
                    <v-layout row wrap justify-space-around>
                        <v-flex xs12 sm6>
                            <v-layout class="mr-2" row justify-center>
                                <v-checkbox class="shrink mt-2 mr-2" v-model="hoursEnabled" color="success" hide-details></v-checkbox>
                                <v-text-field class="my-0" :disabled="!hoursEnabled" v-model="lifespan" label="Number of hours"></v-text-field>
                            </v-layout>
                        </v-flex>
                        <v-flex xs12 sm6>
                            <v-layout row justify-center>
                                <v-checkbox class="shrink mt-2 mr-2" v-model="maxCountEnabled" color="success" hide-details></v-checkbox>
                                <v-text-field class="my-0" :disabled="!maxCountEnabled" v-model="maxCount" label="Max views"></v-text-field>
                            </v-layout>
                        </v-flex>
                    </v-layout>
                    <v-divider></v-divider>
                    <p class="text-uppercase grey--text mt-1">Link Permissions</p>
                    <v-layout align-center justify-space-around row fill-height>
                        <v-btn large outline round color="primary" class="mt-1" @click="profileDialog = !profileDialog">Profile</v-btn>
                        <v-btn large outline round color="primary" class="mt-1" @click="accountsDialog = !accountsDialog">Accounts</v-btn>
                    </v-layout>
                    
                    <!-- <v-btn round color="primary">Other</v-btn> -->
                </v-form>
                <!-- <p v-if="feedback" class="red--text text-xs-center">Please enter valid credentials.</p> -->
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-btn primary block large dark depressed round color="primary" class="my-3 mx-4 subheading" @click="submit" :loading="loading">Create</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
    <v-dialog v-model="profileDialog" :max-width="dialogWidth">
        <v-card style="border-radius: 25px;">
          <v-card-title class="justify-center">
            <span class="font-weight-light grey--text headline">What To Display On My Tou.sh Link</span>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
              <v-layout class="ml-3 text-xs-center" wrap align-center justify-space-around row fill-height>
                <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Link Back To My Profile?" v-model="linkToProfile"></v-checkbox></v-flex>
                <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Username" v-model="username"></v-checkbox></v-flex>
                <v-flex xs6 sm6 md4><v-checkbox color="primary" label="First Name" v-model="firstName"></v-checkbox></v-flex>
                <v-flex xs6 sm6 md4><v-checkbox color="primary" label="Last Name" v-model="lastName"></v-checkbox></v-flex>
                <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Contact Email" v-model="contactEmail"></v-checkbox></v-flex>
                <v-flex xs6 sm6 md4><v-checkbox color="primary" label="Contact Phone" v-model="contactPhone"></v-checkbox></v-flex>
              </v-layout>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" block flat @click="profileDialog=false"><v-icon>check</v-icon></v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="accountsDialog" :max-width="dialogWidth">
        <v-card style="border-radius: 25px;">
          <v-card-title class="justify-center">
            <v-toolbar card color="white">
                <template v-if="$vuetify.breakpoint.lgAndUp"> 
                    <v-toolbar-side-icon class="primary--text ml-1">
                        <v-icon>people</v-icon>
                    </v-toolbar-side-icon>
                    <v-toolbar-title class="font-weight-light primary--text">
                        <!-- <div class="headline">
                            <span>Accounts To Show On My Tou.sh Link</span>
                        </div> -->
                        <span>Accounts To Show</span>
                    </v-toolbar-title>

                    <v-spacer></v-spacer>
                </template>

                <v-toolbar dense flat class="sb-toush mx-2" color="grey lighten-4">
                    <v-text-field
                        label="Search"
                        background-color="grey lighten-4"
                        flat
                        solo
                        v-model="searchInput"
                        hide-details
                        clearable
                        prepend-inner-icon="search"
                    >
                    </v-text-field>
                </v-toolbar>

            </v-toolbar>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text style="min-height: 50vh; max-height: 50vh; overflow: auto;">
              <v-list dense>
                  <v-list-tile class="mx-1 my-2" v-for="service in filteredAccounts" :key="service">
                      <v-list-tile-action>
                          <v-checkbox color="success" v-model="selectedServices" :value="service"></v-checkbox>
                          <!-- :v-model="`services.find(x => x.service === {service}).value`" -->
                      </v-list-tile-action>
                      <v-list-tile-content>
                          <v-list-tile-title>{{ service.substring(0, service.indexOf('.')) }}</v-list-tile-title>
                          <v-list-tile-sub-title>{{ service }}</v-list-tile-sub-title>
                      </v-list-tile-content>
                  </v-list-tile>
              </v-list>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" block flat @click="accountsDialog=false"><v-icon>check</v-icon></v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>

</div>
</template>

<script>
import { CREATE_TOUSHLINK_MUTATION } from '@/graphql/mutations/createToushLink'
import {ALL_ACCOUNTS_QUERY } from '@/graphql/queries/accounts'

export default {
    name: 'AddToushLink',
    data() {
        return {
            loading: false,
            ownAccounts: [],
            dialog: false,
            itemsPef: ['Profile'], // , 'Account List', 'Event', 'Feed'
            hoursEnabled: false,
            maxCountEnabled: false,
            profileDialog: false,
            accountsDialog: false,
            searchInput: '',
            typeOfLink: 'Profile',

            itemsPefPos: 'Profile',
            isToushProfile: true,
            isToushFeed: false,
            isToushEvent: false,
            lifespan: null,  // int
            maxCount: null,  // int
            linkToProfile: true, // bool
            username: true,  // bool
            firstName: true,  // bool
            lastName: true,  // bool
            contactEmail: true,  // bool
            contactPhone: true,  // bool
            message: '',  // string
            link: '', // string - use for tou.sh/AfeFh1 >> twitter.com/memes
            customLink: '',  // string
            accountsList: null, // JSON.stringify - JSONString

            selectedServices: [],


            // rules: {
            //     username: v => /^[\w.]+$/.test(v) || 'Letters, numbers, . or _',
            //     password: v => v.length >= 8 || 'Password should be 8 or more characters'
            // },
        }
    },
    computed: {
        // accountList() {
        //     return this.$store.state.accountList
        // },
        filteredAccounts() {
            if (!this.$apollo.loading && this.ownAccounts) {
                // use one-liner instead
                // accounts.filter(a => a.name.toLowerCase().includes(this.searchTerm.toLowerCase()))
                return this.ownAccounts.filter(account => {
                    return account.substring(0, account.indexOf('.')).match(this.searchInput)
                })
            } else {
                return []
            }
        },
        dialogWidth() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return '98vw'
                case 'sm': return '75vw'
                case 'md': return '60vw'
                case 'lg': return '50vw'
                case 'xl': return '45vw'
            }
        }
    },
    methods: {
        submit() {
            // console.log('memes')
            // console.log(this.accountList)
            // console.log(this.selectedServices)
            if (this.$refs.makeToushForm.validate()) {
                this.loading = true
                let { 
                    typeOfLink,
                    isToushProfile,
                    isToushFeed,
                    isToushEvent,
                    lifespan,  // int
                    maxCount,  // int
                    linkToProfile, // bool
                    username,  // bool
                    firstName,  // bool
                    lastName,  // bool
                    contactEmail,  // bool
                    contactPhone,  // bool
                    message,  // string
                    link, // string - use for tou.sh/AfeFh1 >> twitter.com/memes
                    customLink,  // string
                    accountsList, // JSON.stringify - JSONString
                    selectedServices
                } = this.$data
                // if (typeOfLink === 'Profile') {
                //     isToushProfile = true
                //     isToushFeed = false
                //     isToushEvent = false
                // } else if (typeOfLink === 'Account List') {
                //     isToushProfile = true
                //     isToushFeed = false
                //     isToushEvent = false
                // } else if (typeOfLink === 'Event') {
                //     isToushProfile = false
                //     isToushFeed = false
                //     isToushEvent = true
                // } else if (typeOfLink === 'Feed') {
                //     isToushProfile = false
                //     isToushFeed = true
                //     isToushEvent = false
                // } else {
                //     isToushProfile = false
                //     isToushFeed = false
                //     isToushEvent = false
                // }
                if (!maxCount) maxCount = -1
                if (!lifespan) lifespan = -1
                accountsList = { "services": [] }
                selectedServices.forEach(service => {
                    accountsList["services"].push(service)
                })
                function jsFriendlyJSONStringify (s) {
                    return JSON.stringify(s).
                        replace(/\u2028/g, '\\u2028').
                        replace(/\u2029/g, '\\u2029')
                }
                let accountsListEscaped = jsFriendlyJSONStringify(accountsList)
                //let testJSON = "{ \"services\": [ \"facebook.com\" ] }"
                console.log(accountsListEscaped)
                this.$apollo.mutate({
                    mutation: CREATE_TOUSHLINK_MUTATION,
                    variables: {
                        isToushEvents: isToushEvent, 
                        isToushFeed: isToushFeed,
                        isToushProfile: isToushProfile,
                        message: message,
                        link: link,
                        lifespan: lifespan,
                        maxCount: maxCount,
                        customLink: customLink,
                        linkToProfile: linkToProfile,
                        username: username,
                        firstName: firstName,
                        lastName: lastName,
                        contactPhone: contactPhone,
                        contactEmail: contactEmail,
                        //accountsListEscaped,
                        accountsList: accountsListEscaped
                    }
                }).then(result => {
                    this.loading = false
                    this.dialog = false
                    this.$emit('linksUpdate')
                }).catch(err => {
                    console.log(err)
                    //this.feedback = true
                    this.loading = false
                })
                
            }

            
        },
    },
    apollo: {
        ownAccounts: {
            query: ALL_ACCOUNTS_QUERY,
            result({ data, loading }) {
                if (!loading) {
                    if (data.ownAccounts) {
                        for (let i = 0; i < this.ownAccounts.length; i++) {
                            this.ownAccounts[i] = this.ownAccounts[i].service
                        }
                    }
                }
            }
        }
    }

}
</script>


<style>
.sb-toush {
    border-radius: 30px;
    max-width: 420px;
}
</style>
