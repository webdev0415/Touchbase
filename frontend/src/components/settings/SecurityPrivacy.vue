<template>
    <div>
        <!-- 
            2FA, sign me out everywhere, Reset Password, accounts privacy,
            followers privacy, full private profile (like steam)
         -->
        <v-form>
             <v-layout column align-center class="pb-5">
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <span style="font-size: 29px;" class="text-capitalize mr-1 font-weight-light grey--text text--darken-4 mt-1">Two-Factor Login (2FA)</span>
                    <span class="ml-2 grey--text text--darken-3"> - Coming Soon <v-icon>timer</v-icon></span>
                </v-flex>
                <v-flex style="width: 100%;">  
                    <span class="grey--text subheading text--darken-2 mt-1">Add extra security with <a href="https://en.wikipedia.org/wiki/Multi-factor_authentication" style="text-decoration: none;">two-factor authentication.</a></span>
                </v-flex>
                <v-flex class="mt-3" style="width: 100%;">
                    <v-btn depressed class="mx-0" color="primary">
                        <span class="mr-2">Setup Now</span>
                        <v-icon>phonelink_lock</v-icon>
                    </v-btn>
                </v-flex>

                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                    </v-layout>
                </v-flex>

                <v-flex style="width: 100%;" class="mt-4 mb-2">
                    <span style="font-size: 29px;" class="text-capitalize font-weight-light grey--text text--darken-4 mt-1">Password</span>
                </v-flex>
                <v-flex style="width: 100%;">  
                    <span class="grey--text subheading text--darken-2 mt-1">Changing your password requires you to login again.</span>
                </v-flex>
                <v-flex class="mt-3" style="width: 100%;">
                    <v-btn depressed class="mx-0" color="primary">
                        <span class="mr-2">Change</span>
                        <v-icon>vpn_key</v-icon>
                    </v-btn>
                </v-flex>

                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                    </v-layout>
                </v-flex>

                <v-flex style="width: 100%;" class="mt-4 mb-2">
                    <span style="font-size: 29px;" class="text-capitalize font-weight-light grey--text text--darken-4 mt-1">Devices</span>
                </v-flex>
                <v-flex class="mt-3" style="width: 100%;">
                    <v-btn depressed @click="signOutAll" :loading="signOutAllLoading" class="mx-0" color="primary">
                        <span class="mr-2">Sign Out All Devices</span>
                        <v-icon>devices</v-icon>
                    </v-btn>
                </v-flex>
                <v-flex v-if="signOutAllFeedback" style="width: 100%" class="mt-4 ml-4">
                    <span class="title font-weight-light red--text">Error signing out your devices. Please try again.</span>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                    </v-layout>
                </v-flex>

                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <span style="font-size: 29px;" class="text-capitalize font-weight-light grey--text text--darken-4 mt-1">Privacy</span>
                </v-flex>
                <v-flex style="width: 100%;" class="mb-2">  
                    <span class="grey--text subheading text--darken-2 mt-1">Who can see what parts of your account.</span>
                </v-flex>
                <v-flex style="width: 100%" class="mt-4 ml-4">
                    <span class="title font-weight-light grey--text text--darken-3">Accounts</span>
                </v-flex>
                <v-flex style="width: 100%;" class="ml-5">
                    <v-radio-group v-model="privacyAccounts" row>
                        <v-radio class="mr-4" label="Anyone" value="a" color="primary"></v-radio>
                        <v-radio class="mr-4" label="Toush Links Only" value="s" color="primary"></v-radio>
                        <v-radio class="mr-4" label="Private" value="n" color="primary"></v-radio>
                    </v-radio-group>
                </v-flex>
                <v-flex style="width: 100%;" class="mb-2">  
                    <span class="grey--text ml-4 subheading text--darken-2 mt-1">* Accounts can still be individually privated.</span>
                </v-flex>
                <v-flex style="width: 100%" class="mt-4 ml-4">
                    <span class="title font-weight-light grey--text text--darken-3">Follows</span>
                </v-flex>
                <v-flex style="width: 100%" class="ml-5">
                    <v-radio-group v-model="privacyFollows" row>
                        <v-radio class="mr-4" label="Anyone" value="a" color="primary"></v-radio>
                        <v-radio class="mr-4" label="Followers Only" value="s" color="primary"></v-radio>
                        <v-radio label="Private" value="n" color="primary"></v-radio>
                    </v-radio-group>
                </v-flex>
                
                <v-flex style="width: 100%" class="mt-4 ml-4">
                    <span class="title font-weight-light grey--text text--darken-3">Profile</span>
                </v-flex>
                <v-flex style="width: 100%;" class="ml-4">  
                    <v-switch v-model="privateProfile" color="primary">
                        <template slot="prepend">
                            <span class="grey--text text--darken-2 mt-1 mr-2">Private my whole profile.</span>
                        </template>
                    </v-switch>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                    </v-layout>
                </v-flex>
                
            </v-layout>
        </v-form>
    </div>
</template>

<script>
import { SIGN_OUT_ALL_MUTATION } from '@/graphql/mutations/signOutAll'
import { onLogout } from '@/apollo'
import { mapMutations } from 'vuex'

export default {
    name: 'SecurityPrivacy',
    props: ['settings'],
    data() {
        return {
            privacyAccounts: this.settings.privacyAccounts.toLowerCase(),
            privacyFollows: this.settings.privacyFollows.toLowerCase(),
            privateProfile: this.settings.privateProfile,
            signOutAllFeedback: false,
            signOutAllLoading: false,
        }
    },
    methods: {
        logout() {
            this.unsetToken()
            onLogout(this.$apollo.provider.defaultClient)
            .then(() => {
                location.href = '/'
            })
        },
        signOutAll() {
            this.signOutAllLoading = true
            this.$apollo.mutate({
                mutation: SIGN_OUT_ALL_MUTATION
            }).then(result => {
                if (result.data.signOutAll.success) {
                    this.signOutAllLoading = false
                    this.logout()
                } else {
                    this.signOutAllLoading = false
                    this.signOutAllFeedback = true
                }
            }).catch(err => {
                console.log(err)
                this.signOutAllFeedback = true
                this.signOutAllLoading = false
            })
        },
        ...mapMutations([
            'unsetToken'
        ])
    },
    watch: {
        privacyAccounts() {
            this.$emit('settingsUpdate', { 'privacyAccounts': this.privacyAccounts })
        },
        privacyFollows() {
            this.$emit('settingsUpdate', { 'privacyFollows': this.privacyFollows })
        },
        privateProfile() {
            this.$emit('settingsUpdate', { 'privateProfile': this.privateProfile })
        }
    },
}
</script>

<style>
    
</style>