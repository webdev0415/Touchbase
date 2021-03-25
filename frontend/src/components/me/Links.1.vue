<template>
<!-- TODO: MOVE ALL DIALOGS TO THEIR OWN COMPONENT TO FIX ISSUES -->
    <div style="height: 100%;">
        <v-layout column align-center style="overflow: hidden;">
            <v-flex class="text-xs-center mt-3">
                <AddToushLink />
            </v-flex>
            <v-flex :class="{ 'ln-align-bottom': $vuetify.breakpoint.mdAndUp, 'ln-scroll': true, 'ln-grid': true, }">
                <v-layout fill-height row justify-center align-center>
                    <v-layout fill-height align-center column class="ln-links">
                        <v-flex v-for="(link, i) in ownLinks" :key="i" class="my-3">
                            <v-badge overlap left color="primary">
                                <span slot="badge">{{ i + 1 }}</span> <!--slot can be any component-->
                                <v-card flat style="border-radius: 25px; min-width: 350px; width: 42vw;">
                                    <v-card-title class="text-capitalize title">
                                        <img class="mr-4" src="/img/avatar-2.png" alt="lorem" width="70" height="70">
                                        <span v-if="link.item.isToushProfile">Profile</span>
                                        <span v-if="link.item.isToushFeed">Feed</span>
                                        <span v-if="link.item.isToushEvent">Event</span>
                                        <v-spacer></v-spacer>
                                        <!-- <v-tooltip bottom max-width="100%">
                                            <template slot="activator"> -->
                                        <v-text-field
                                            class="hidden-sm-and-down"
                                            @click="copyToush(makeToush(link.shortUrl))"
                                            style="max-width: 40%;"
                                            :placeholder="makeToush(link.shortUrl)"
                                            readonly
                                            prepend-icon="link"
                                        ></v-text-field>
                                        <v-text-field
                                            class="hidden-md-and-up"
                                            @click="copyToush(makeToush(link.shortUrl))"
                                            style="max-width: 80%;"
                                            :placeholder="makeToush(link.shortUrl)"
                                            readonly
                                            prepend-icon="link"
                                        ></v-text-field>
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
                                            <v-divider class="hidden-md-and-up my-2" inset></v-divider>
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
                                        <v-layout class="grey--text text-uppercase mt-1" wrap align-end justify-space-between row fill-height>
                                            <span class="ml-2 caption">
                                                <span>Created {{ link.created }}</span>
                                                <template v-if="link.lifespan != -1">
                                                    <v-divider class="links-date-divs mx-3" inset vertical></v-divider>
                                                    <!-- <span v-if="link.momentExpired!='Expired'"> | Expires {{ link.momentExpired }}</span> -->
                                                    <span>Expiry:  {{ link.expiry }}</span>
                                                </template>
                                            </span>
                                            <span class="mr-2">{{ link.usageCount }} Views</span>
                                        </v-layout>
                                    </v-card-text>
                                    <v-divider></v-divider>
                                    <v-layout row justify-center align-center fill-height>
                                        <v-dialog
                                            v-model="link.optionsDialog"
                                            :max-width="dialogWidth"
                                        >
                                            <v-card-actions slot="activator">
                                                <!-- <v-layout justify-center align-center> -->
                                                
                                                
                                                <v-btn style="min-width: 350px; width: 42vw;" flat block color="primary">
                                                    <span>Configure</span>
                                                </v-btn>
                                                <!-- </v-layout> -->
                                                <!-- <v-spacer></v-spacer>
                                                <v-btn flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">remove</span><v-icon>delete</v-icon></v-btn> -->
                                            </v-card-actions>  
                                            <v-card style="border-radius: 25px;" class="pb-1">
                                                <v-card-text>
                                                    <v-layout column fill-height>
                                                        <v-flex>
                                                            <span class="text-uppercase grey--text mt-1">Edit</span>
                                                        </v-flex>
                                                        <v-divider class="mt-1 mb-3"></v-divider>

                                                        <v-form class="px-3" ref="editToushForm" lazy-validation>
                                                            <v-layout row wrap justify-space-between class="mb-3">
                                                                <v-flex xs12 md6>
                                                                    <v-text-field class="my-0"
                                                                        outline
                                                                        clearable
                                                                        label="Message"
                                                                        prepend-inner-icon="message"
                                                                        v-model="link.editMessage"
                                                                        counter="128"
                                                                    ></v-text-field>
                                                                </v-flex>
                                                                <v-flex xs12 md5>
                                                                    <v-text-field class="my-0"
                                                                        label="Custom Link"
                                                                        outline
                                                                        counter="20"
                                                                        v-model="link.editCustomLink"
                                                                        clearable
                                                                        prepend-inner-icon="lock"
                                                                    ></v-text-field>
                                                                </v-flex>
                                                            </v-layout>
                                                            <!-- <v-divider inset class="mt-4 mx-5"></v-divider> -->
                                                            <span class="text-capitalize grey--text ml-2">Permissions</span>
                                                            <v-layout class="mt-1" align-center justify-space-around row fill-height>
                                                                <v-dialog
                                                                    v-model="link.editProfileDialog"
                                                                    :max-width="dialogWidth"
                                                                >
                                                                    <v-btn slot="activator" large outline round color="primary" class="mt-1">Profile</v-btn>
                                                                
                                                                    <v-card style="border-radius: 25px;">
                                                                        <v-card-title class="justify-center">
                                                                            <span class="font-weight-light grey--text headline">What To Display On My Tou.sh Link</span>
                                                                        </v-card-title>
                                                                        <v-divider></v-divider>
                                                                        <v-card-text>
                                                                            <v-layout class="ml-3 text-xs-center" wrap align-center justify-space-around row fill-height>
                                                                                <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Link Back To My Profile?" v-model="link.editLinkToProfile"></v-checkbox></v-flex>
                                                                                <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Username" v-model="link.editUsername"></v-checkbox></v-flex>
                                                                                <v-flex xs6 sm6 md4><v-checkbox color="primary" label="First Name" v-model="link.editFirstName"></v-checkbox></v-flex>
                                                                                <v-flex xs6 sm6 md4><v-checkbox color="primary" label="Last Name" v-model="link.editLastName"></v-checkbox></v-flex>
                                                                                <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Contact Email" v-model="link.editContactEmail"></v-checkbox></v-flex>
                                                                                <v-flex xs6 sm6 md4><v-checkbox color="primary" label="Contact Phone" v-model="link.editContactPhone"></v-checkbox></v-flex>
                                                                            </v-layout>
                                                                        </v-card-text>
                                                                        <!-- <v-divider></v-divider>
                                                                        <v-card-actions>
                                                                            <v-spacer></v-spacer>
                                                                            <v-btn color="primary" block flat @click="link.editProfileDialog=false"><v-icon>check</v-icon></v-btn>
                                                                            <v-spacer></v-spacer>
                                                                        </v-card-actions> -->
                                                                    </v-card>
                                                                </v-dialog>
                                                                



                                                                <v-dialog v-model="link.editAccountsDialog" :max-width="dialogWidth">
                                                                    <v-btn large outline slot="activator" round color="primary" class="mt-1">Accounts</v-btn>

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
                                                                                        <v-checkbox color="success" v-model="link.selectedServices" :value="service"></v-checkbox>
                                                                                        <!-- :v-model="`services.find(x => x.service === {service}).value`" -->
                                                                                    </v-list-tile-action>
                                                                                    <v-list-tile-content>
                                                                                        <v-list-tile-title>{{ service.substring(0, service.indexOf('.')) }}</v-list-tile-title>
                                                                                        <v-list-tile-sub-title>{{ service }}</v-list-tile-sub-title>
                                                                                    </v-list-tile-content>
                                                                                </v-list-tile>
                                                                            </v-list>
                                                                        </v-card-text>
                                                                        <!-- <v-divider></v-divider>
                                                                        <v-card-actions>
                                                                            <v-spacer></v-spacer>
                                                                            <v-btn color="primary" block flat @click="link.editAccountsDialog=false"><v-icon>check</v-icon></v-btn>
                                                                            <v-spacer></v-spacer>
                                                                        </v-card-actions> -->
                                                                    </v-card>
                                                                </v-dialog>   
                                                                
                                                            </v-layout>
                                                        </v-form>

                                                        <v-flex class="mt-3">
                                                            <span class="text-uppercase grey--text">Delete</span>
                                                        </v-flex>
                                                        <v-divider class="mt-1 mb-3"></v-divider>
                                                        <div class="px-3">
                                                            <span class="grey--text text--darken-2 mr-3">Delete this toush link:</span>
                                                            <!-- <v-btn large flat class="ml-3" icon color="primary">
                                                                <v-icon>delete</v-icon>
                                                            </v-btn> -->
                                                            <!-- <v-btn v-if="!link.remove" @click="link.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn>
                                                            <v-btn v-else-if="link.remove && !link.confirmedRemove" @click="link.confirmedRemove=true; removeLink(link)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Confirm?</span><v-icon>check</v-icon></v-btn>
                                                            <span class="success--text" v-if="link.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->

                                                            <!-- <v-btn v-if="!link.remove" @click="link.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn>
                                                            <v-btn :loading="deleteLoading" v-else-if="link.remove && !link.confirmedRemove" @click="link.confirmedRemove=true; removeLink(link)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Confirm?</span><v-icon>check</v-icon></v-btn>
                                                            <span class="success--text" v-if="link.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->

                                                            <!-- <v-btn v-if="!link.remove" @click="link.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn> -->
                                                            <v-layout row align-center>
                                                                <v-switch color="primary" append-icon="arrow_right_alt" class="ml-3" v-model="deleteSwitch">
                                                                    <!-- <v-icon slot="label">arrow_right_alt</v-icon> -->
                                                                </v-switch>
                                                                <v-btn style="margin-right: 80%;" :disabled="!deleteSwitch" :loading="deleteLoading" @click="link.confirmedRemove=true; removeLink(link)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Delete</span><v-icon>delete</v-icon></v-btn>
                                                                
                                                            </v-layout>
                                                            
                                                            
                                                            <!-- <span class="success--text" v-if="link.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->
                                                        </div>
                                                    </v-layout>
                                                    
                                                </v-card-text>
                                                <v-divider></v-divider>
                                                <v-card-actions>
                                                    <v-btn @click="edit(link)" :loading="editLoading" flat block color="primary">
                                                        <span>Save</span>
                                                        <v-icon class="ml-2">check</v-icon>
                                                    </v-btn>
                                                </v-card-actions>
                                                <p v-if="feedback" class="red--text text-xs-center">Something went wrong. Double check the form please.</p>
                                            </v-card>   
                                        </v-dialog>
                                        
                                    </v-layout>
                                                         
                                </v-card>
                            </v-badge>
                        </v-flex>
                    </v-layout>
                </v-layout>
                    
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import AddToushLink from "@/components/dashboard/AddToushLink"
import { OWN_LINKS_QUERY } from '@/graphql/queries/ownLinks'
import { ALL_ACCOUNTS_QUERY } from '@/graphql/queries/accounts'
import { EDIT_TOUSHLINK_MUTATION } from '@/graphql/mutations/editToushLink'
import moment from 'moment'

export default {
    name: 'Advertising',
    data() {
        return {
            ownLinks: [],
            deleteSwitch: false,
            ownAccounts: [],
            loading: 0,
            dialog: false,
            snackbar: false,
            searchInput: '',
            deleteLoading: false,

            editLoading: false,
            feedback: '',

            // message: '',
            // customLink: '',
            // linkToProfile: true, // bool
            // username: true,  // bool
            // firstName: true,  // bool
            // lastName: true,  // bool
            // contactEmail: true,  // bool
            // contactPhone: true,  // bool
            
        }
    },
    methods: {
        removeLink(link) {
            this.deleteLoading = true
            console.log(link)
            this.deleteLoading = false
            location.reload()
        },
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

        edit(link) {
            // if (this.$refs.editToushForm.validate()) {
            this.editLoading = true
            let accountsListEscaped = '{}'
            if (link.selectedServices != link.item.accountListJSON.services) {
                let accountsList = { "services": [] }
                link.selectedServices.forEach(service => {
                    accountsList["services"].push(service)
                })
                function jsFriendlyJSONStringify (s) {
                    return JSON.stringify(s).
                        replace(/\u2028/g, '\\u2028').
                        replace(/\u2029/g, '\\u2029')
                }
                accountsListEscaped = jsFriendlyJSONStringify(accountsList)
            }

            let changed = []

            if (link.editMessage != '') changed.push('message')
            if (link.editCustomLink != '') changed.push('custom_link')
            if (link.editLinkToProfile != link.item.linkToProfile) changed.push('link_to_profile')
            if (link.editUsername != link.item.username) changed.push('username')
            if (link.editFirstName != link.item.firstName) changed.push('first_name')
            if (link.editLastName != link.item.lastName) changed.push('last_name')
            if (link.editContactEmail != link.item.contactEmail) changed.push('contact_email')
            if (link.editContactPhone != link.item.contactPhone) changed.push('contact_phone')

            // const changedSafe = JSON.stringify(changed)

            console.log(changed, accountsListEscaped, link.shortUrl,
                link.editMessage,
                link.editCustomLink,
                link.editLinkToProfile,
                link.editUsername,
                link.editFirstName,
                link.editLastName,
                link.editContactEmail, 
                link.editContactPhone, 
            )

            const toushString = link.shortUrl
            const message = link.editMessage
            const customLink  = link.editCustomLink
            const linkToProfile = link.editLinkToProfile
            const username = link.editUsername
            const firstName = link.editFirstName
            const lastName = link.editLastName
            const contactEmail = link.editContactEmail
            const contactPhone = link.editContactPhone

            this.$apollo.mutate({
                mutation: EDIT_TOUSHLINK_MUTATION,
                variables: {
                    toushString: toushString,
                    changed: changed,
                    customLink: customLink,
                    message: message,
                    linkToProfile: linkToProfile,
                    username: username,
                    firstName: firstName,
                    lastName: lastName,
                    contactEmail: contactEmail,
                    contactPhone: contactPhone,
                    accountsList:  accountsListEscaped
                }
            }).then(result => {
                if (result.data.editToushLink.success) {
                    this.editLoading = false
                    location.reload()
                } else {
                    this.editLoading = false
                    this.feedback = true
                    console.log(result.data.editToushLink.errors)
                }
            }).catch(err => {
                console.log(err)
                this.feedback = true
                this.editLoading = false
            })
            
            // }
            
        }
    },
    components: {
        AddToushLink,
    },
    computed: {
        filteredAccounts() {
            return this.ownAccounts.filter(account => {
               return account.substring(0, account.indexOf('.')).match(this.searchInput)
            })
        },
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
    apollo: {
        ownLinks: {
            query: OWN_LINKS_QUERY,
            result({ data, loading }) {
                if (!loading) {
                    data.ownLinks.forEach(link => {
                        link.expiry = moment(link.expired).fromNow()
                        link.created = moment(link.created).fromNow()
                        link.accounts = []
                        link.accountDialog = false
                        link.optionsDialog = false
                        link.item.accountListJSON = JSON.parse(link.item.accountsList)
                        
                        link.editAccountsDialog = false
                        link.editProfileDialog = false
                        link.confirmedRemove = false
                        link.remove = false

                        // fields that can edited
                        link.selectedServices = []
                        link.selectedServices = link.selectedServices.concat(link.item.accountListJSON.services)
                        link.editMessage = ''
                        link.editCustomLink = ''
                        link.editLinkToProfile = link.item.linkToProfile
                        link.editUsername = link.item.username
                        link.editFirstName = link.item.firstName
                        link.editLastName = link.item.lastName
                        link.editContactEmail = link.item.contactEmail 
                        link.editContactPhone = link.item.contactPhone
                    })
                }
                
            }
        },
        ownAccounts: {
            query: ALL_ACCOUNTS_QUERY,
        }
    }
}
</script>

<style>
.ln-align-bottom {
    position: fixed;
    bottom: 0;
}

.ln-links {
    /* width: calc(20vw + 400px); */
}

.ln-grid {
    height: calc(100% - 184px);
    /* max-height: calc(100vh - 210px); */
    width: calc(100% - 10px);
}

.ln-scroll {
    overflow: auto;
}

.links-date-divs {
    height: 20px;
}

</style>