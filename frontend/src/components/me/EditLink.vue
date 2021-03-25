<template>
<v-layout row fill-height align-center justify-center v-if="$apollo.loading || expiry === null">
    <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
</v-layout>
<v-layout v-else-if="expired && expired != 'no'" align-center justify-space-around fill-height column>
    <p class="display-2 font-weight-light grey--text text--darken-1">Can't edit expired link.</p>
    <v-btn to="/links" class="mb-5" color="primary" style="top: 0; left: 0;" round outline asbolute small>
        <v-icon class="mr-2">arrow_back</v-icon>
        <span class="text-capitalize">Go Back</span>
    </v-btn>
    <v-flex xs5>
        <span class="grey--text text--darken-2 mr-3">Delete this toush link:</span>
        <v-layout row align-center>
            <v-switch color="primary" append-icon="arrow_right_alt" class="ml-3" v-model="deleteSwitch"></v-switch>
            <v-btn style="margin-right: 80%;" :disabled="!deleteSwitch" :loading="deleteLoading" @click="confirmedRemove=true; removeLink()" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Delete</span><v-icon>delete</v-icon></v-btn>
        </v-layout>
        
    </v-flex>
</v-layout>
<v-layout class="px-4" fill-height row justify-center align-center v-else-if="expired === 'no'">
    <v-flex xs12 md6 lg4>
        <v-btn to="/links" class="mb-5" color="primary" style="top: 0; left: 0;" round outline asbolute small>
            <v-icon class="mr-2">arrow_back</v-icon>
            <span class="text-capitalize">Go Back</span>
        </v-btn>
        <v-card class="pb-1 edit-link-card">
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
                                    v-model="editMessage"
                                    counter="128"
                                ></v-text-field>
                            </v-flex>
                            <v-flex xs12 md5>
                                <v-text-field class="my-0"
                                    label="Custom Link"
                                    outline
                                    counter="20"
                                    v-model="editCustomLink"
                                    clearable
                                    prepend-inner-icon="lock"
                                ></v-text-field>
                            </v-flex>
                        </v-layout>
                        <!-- <v-divider inset class="mt-4 mx-5"></v-divider> -->
                        <span class="text-capitalize grey--text ml-2">Permissions</span>
                        <v-layout class="mt-1" align-center justify-space-around row fill-height>
                            <v-dialog
                                v-model="editProfileDialog"
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
                                            <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Link Back To My Profile?" v-model="editLinkToProfile"></v-checkbox></v-flex>
                                            <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Username" v-model="editUsername"></v-checkbox></v-flex>
                                            <v-flex xs6 sm6 md4><v-checkbox color="primary" label="First Name" v-model="editFirstName"></v-checkbox></v-flex>
                                            <v-flex xs6 sm6 md4><v-checkbox color="primary" label="Last Name" v-model="editLastName"></v-checkbox></v-flex>
                                            <v-flex xs12 sm6 md4><v-checkbox color="primary" label="Contact Email" v-model="editContactEmail"></v-checkbox></v-flex>
                                            <v-flex xs6 sm6 md4><v-checkbox color="primary" label="Contact Phone" v-model="editContactPhone"></v-checkbox></v-flex>
                                        </v-layout>
                                    </v-card-text>
                                    <v-divider></v-divider>
                                    <v-card-actions>
                                        <!-- <v-spacer></v-spacer> -->
                                        <v-btn color="primary" block flat @click="editProfileDialog=false"><v-icon>check</v-icon></v-btn>
                                        <!-- <v-spacer></v-spacer> -->
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                            



                            <v-dialog v-model="editAccountsDialog" :max-width="dialogWidth">
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
                                        <!-- <v-spacer></v-spacer> -->
                                        <v-btn color="primary" block flat @click="editAccountsDialog=false"><v-icon>check</v-icon></v-btn>
                                        <!-- <v-spacer></v-spacer> -->
                                    </v-card-actions>
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

                        <v-btn v-if="!remove" @click="remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn>
                        <v-btn :loading="deleteLoading" v-else-if="remove && !confirmedRemove" @click="confirmedRemove=true; removeLink()" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Confirm?</span><v-icon>check</v-icon></v-btn>
                        <span class="success--text" v-if="confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span>

                        <!-- <v-btn v-if="!link.remove" @click="link.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn> -->
                        
                        <!-- <v-layout row align-center>
                            <v-switch color="primary" append-icon="arrow_right_alt" class="ml-3" v-model="deleteSwitch">
                            </v-switch>
                            <v-btn style="margin-right: 80%;" :disabled="!deleteSwitch" :loading="deleteLoading" @click="link.confirmedRemove=true; removeLink()" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Delete</span><v-icon>delete</v-icon></v-btn>
                            
                        </v-layout> -->
                        
                        
                        <!-- <span class="success--text" v-if="link.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->
                    </div>
                </v-layout>
                
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-btn @click="edit()" :loading="editLoading" flat block color="primary">
                    <span>Save</span>
                    <v-icon class="ml-2">check</v-icon>
                </v-btn>
            </v-card-actions>
            <p v-if="feedback" class="red--text text-xs-center">Something went wrong. Double check the form please.</p>
            <p v-if="feedbackEmpty" class="red--text text-xs-center">Please make an edit before saving.</p>
        </v-card> 
    </v-flex>
    
</v-layout>
     
</template>

<script>
import { RESOLVE_TOUSH_QUERY } from '@/graphql/queries/resolveToush'
import { EDIT_TOUSHLINK_MUTATION } from '@/graphql/mutations/editToushLink'
import { ALL_ACCOUNTS_QUERY } from '@/graphql/queries/accounts'

export default {
    name: 'EditLink',
    
    data() {
        return {
            expand: {},
            ownAccounts: [],
            feedback: false,
            feedbackEmpty: false,
            editLoading: false,
            deleteLoading: false,
            deleteSwitch: false,
            searchInput: '',
            expired: null,
            
            remove: false,
            editAccountsDialog: false,
            editProfileDialog: false,
            confirmedRemove: false,

            selectedServices: [],
            editMessage: '',
            editCustomLink: '',
            editLinkToProfile: null,
            editUsername: null,
            editFirstName: null,
            editLastName: null,
            editContactEmail: null,
            editContactPhone: null,
        }
    },
    computed: {
        filteredAccounts() {
            if (!this.$apollo.loading && this.ownAccounts) {
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
    methods: {
        removeLink() {
            this.deleteLoading = true
            console.log(this.$route.params.toushString)
            this.deleteLoading = false
            this.$router.push({ name: 'Links' })
        },
        edit() {
            if (this.$refs.editToushForm.validate()) {
                this.editLoading = true
                let changed = []

                let accountsListEscaped = '{}'
                if (this.selectedServices != this.accountListJSON.services) {
                    let accountsList = { "services": [] }
                    this.selectedServices.forEach(service => {
                        accountsList["services"].push(service)
                    })
                    function jsFriendlyJSONStringify (s) {
                        return JSON.stringify(s).
                            replace(/\u2028/g, '\\u2028').
                            replace(/\u2029/g, '\\u2029')
                    }
                    accountsListEscaped = jsFriendlyJSONStringify(accountsList)
                    changed.push('accounts_list')
                }

                if (this.editMessage != '') changed.push('message')
                if (this.editCustomLink != '') changed.push('custom_link')
                if (this.editLinkToProfile != this.expand.item.linkToProfile) changed.push('link_to_profile')
                if (this.editUsername != this.expand.item.username) changed.push('username')
                if (this.editFirstName != this.expand.item.firstName) changed.push('first_name')
                if (this.editLastName != this.expand.item.lastName) changed.push('last_name')
                if (this.editContactEmail != this.expand.item.contactEmail) changed.push('contact_email')
                if (this.editContactPhone != this.expand.item.contactPhone) changed.push('contact_phone')

                // if (link.editMessage != '') changed.push('message')
                // if (link.editCustomLink != '') changed.push('custom_link')
                // if (link.editLinkToProfile != link.item.linkToProfile) changed.push('link_to_profile')
                // if (link.editUsername != link.item.username) changed.push('username')
                // if (link.editFirstName != link.item.firstName) changed.push('first_name')
                // if (link.editLastName != link.item.lastName) changed.push('last_name')
                // if (link.editContactEmail != link.item.contactEmail) changed.push('contact_email')
                // if (link.editContactPhone != link.item.contactPhone) changed.push('contact_phone')

                // const changedSafe = JSON.stringify(changed)

                // console.log(changed, accountsListEscaped, this.expand.shortUrl,
                //     this.editMessage,
                //     this.editCustomLink,
                //     this.editLinkToProfile,
                //     this.editUsername,
                //     this.editFirstName,
                //     this.editLastName,
                //     this.editContactEmail, 
                //     this.editContactPhone, 
                // )

                const toushString = this.expand.shortUrl
                const message = this.editMessage
                const customLink  = this.editCustomLink
                const linkToProfile = this.editLinkToProfile
                const username = this.editUsername
                const firstName = this.editFirstName
                const lastName = this.editLastName
                const contactEmail = this.editContactEmail
                const contactPhone = this.editContactPhone

                if (changed.length > 0) {
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
                            // this.$router.push({ name: 'Links' })
                            // location.href = `${location}`
                            this.$router.go(-1)
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
                } else {
                    this.editLoading = false
                    this.feedbackEmpty = true
                }
                
            
            }
            
        }
    },
    apollo: {
        expand: {
            query: RESOLVE_TOUSH_QUERY,
            variables() {
                return {
                    shortUrl: this.$route.params.toushString,
                    edit: true
                }
            },
            result({ data, loading }) {
                if (!loading && data.expand) {
                    this.expired = 'no'
                    this.accountListJSON = JSON.parse(data.expand.item.accountsList)
                    this.selectedServices = this.selectedServices.concat(this.accountListJSON.services)
                    this.editMessage = ''
                    this.editCustomLink = ''
                    this.editLinkToProfile = data.expand.item.linkToProfile
                    this.editUsername = data.expand.item.username
                    this.editFirstName = data.expand.item.firstName
                    this.editLastName = data.expand.item.lastName
                    this.editContactEmail = data.expand.item.contactEmail
                    this.editContactPhone = data.expand.item.contactPhone
                }
            },
            error(err) {
                console.log(err)
                this.expired = true
            }
        },
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
    },
}
</script>


<style>
.edit-link-card {
    border-radius: 17px;
    width: 100%;
}
</style>