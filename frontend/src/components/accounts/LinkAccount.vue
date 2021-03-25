<template>
<v-dialog scrollable lazy v-model="show">
    <v-layout row justify-center>
        <v-flex xs12 md8 lg4 xl3>
            <v-card style="border-radius: 18px;">
                <v-card-text>
                    <v-form class="pr-4 pl-2" lazy-validation ref="linkAccountForm">
                        <span class="subheading">Link 
                            <v-avatar size="27" class="pb-1 ml-1">
                                <img :src="service.logo" :alt="service.name">
                            </v-avatar>
                            <span class="font-weight-medium title mr-1"> {{ service.name }}</span>
                             to Touchbase</span>
                        <v-text-field class="mt-4"
                            outline
                            clearable
                            v-if="!isSupported"
                            label="Username/Email"
                            v-model="username"
                            prepend-inner-icon="person"
                            counter="128"
                            hint="The username/email/phone number of the account you want to link."
                        ></v-text-field>
                        <div v-if="isSupported" class="mt-3">
                            <!-- <v-divider class="mt-1 mb-3"></v-divider> -->
                            <p class="text-uppercase grey--text mb-1">Sign In Securely</p>
                            <v-layout justify-center>
                                <!-- tooltip that says touchbase cannot see or store your credentials -->
                                <v-btn round @click="signIn" large outline color="primary">Sign In With {{ service.name }}</v-btn>
                            </v-layout>
                            <v-layout justify-center align-center>
                                <v-flex style="max-width: 250px;">
                                    <v-tooltip bottom>
                                        <p slot="activator" class="text-xs-center grey--text my-2">Secured with OAuth technology. 🔒</p>
                                        <span>Touchbase can't see or store your credentials.</span>
                                    </v-tooltip>
                                </v-flex>
                            </v-layout>
                            <template v-if="service != 'Steam'">
                                <v-divider class="mt-1 mb-3"></v-divider>
                                <p class="text-uppercase grey--text mb-1">Options</p>
                                <v-layout class="mr-2" row justify-center>
                                    <v-checkbox class="shrink mt-2 mr-2" v-model="shareSPF" :label="OAFLabel" color="success" hide-details></v-checkbox>
                                </v-layout>
                            </template>
                            
                        </div>
                    </v-form>
                    <!-- <p v-if="feedback" class="red--text text-xs-center">Please enter valid credentials.</p> -->
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-btn primary large flat color="grey" class="my-2 ml-4 subheading" @click="reset">Close</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn primary large dark outline color="primary" class="my-2 mr-4 subheading" @click="submit" :loading="loading">
                        <span>Link It</span>
                        <v-icon class="ml-2">keyboard_arrow_right</v-icon>
                    </v-btn>
                </v-card-actions>
                <p v-if="feedback" class="red--text text-xs-center">Please double check the form.</p>
                <p v-if="oauthFeedback" class="ogSuccess--text text-xs-center">Click to finish linking {{ service.name }}.</p>
            </v-card>
        </v-flex>
    </v-layout>
    
</v-dialog>
</template>

<script>
import { LINK_ACCOUNT_MUTATION } from '@/graphql/mutations/linkAccount'
import JQuery from 'jquery'
let $ = JQuery
var gapi = window.gapi;

export default {
    data() {
        return {
            show: false,
            username: '',
            service: {},
            shareSPF: false,
            loading: false,
            oauthFeedback: false,
            feedback: false,
            spfIdentifier: '',
        }
    },
    computed: {
        OAFLabel() {
            return `Share highlights of my posts on ${this.service.name} to my Touchbase followers`
        },
        isSupported() {
            if (this.$store.state.supportedAccounts.includes(this.service.name)) {
                return true
            } else {
                return false
            }
        },
    },
    mounted() {
        this.$root.$on('openLinkAccountDialog', account => {
            this.service = account
            this.show = true
        })
    },
    beforeRouteEnter (to, from, next) {
        next(vm => {
            if (!vm.loggedIn) {
                vm.$router.replace('/login')
            }
        })
    },
    methods: {
        reset() {
            this.show = false
            // smoother transition ???
            setTimeout(() => {
                this.username = ''
                this.service = {}
                this.shareSPF = false
                this.loading = false
                this.oauthFeedback = false
                this.feedback = false
                this.spfIdentifier = ''
            }, 300)
        },
        signIn() {
            switch (this.service) {
                case 'Youtube':
                    var SCOPE = 'https://www.googleapis.com/auth/youtube.readonly'
                    var GoogleAuth
                    var that = this
                    function initYoutube() {
                        gapi.client.init({
                            'apiKey': 'AIzaSyAh_Sla-sKuxfpjn36YKd9DRTpzkelwd4M',
                            'discoveryDocs': ['https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest'],
                            'clientId': '197733516305-j7sn6j8gm3utu9bea2ickufbmp3ouia3.apps.googleusercontent.com',
                            'scope': SCOPE
                        }).then(() => {
                            
                            GoogleAuth = gapi.auth2.getAuthInstance()
                            // console.log('memes2', GoogleAuth.isSignedIn.get())
                            GoogleAuth.signIn().then((GoogleUser) => {
                                if (GoogleUser) {
                                    var request = gapi.client.youtube.channels.list({'part': 'id', 'mine': 'true'});
                                    request.execute((res) => {
                                        that.spfIdentifier = res.items[0].id
                                        that.oauthFeedback = true
                                    })
                                } else {
                                    console.log('error')
                                }
                            })
                            GoogleAuth.disconnect()
                            
                        })
                    }
                    gapi.load('client:auth2', initYoutube)
                    break;

                case 'Steam':
                    let link = 'https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=http%3A%2F%2F192.168.0.26:8000%2Faccounts&openid.realm=http%3A%2F%2F192.168.0.26:8000&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select'
                    window.location.replace(link)
                    break;
                default:
                    console.log('You broke something')
                    break;
            }
        },
        submit() {
            if (this.$refs.linkAccountForm.validate()) {
                this.loading = true
                let { username, shareSPF, spfIdentifier } = this.$data
                let service = this.service.url
                
                if (this.isSupported) {
                    username = ''
                }
                console.log(username, service, shareSPF, spfIdentifier)
                this.$apollo.mutate({
                    mutation: LINK_ACCOUNT_MUTATION,
                    variables: {
                        identifier: username,
                        service: service,
                        shareSPF: shareSPF,
                        spfIdentifier: spfIdentifier
                    }
                }).then(result => {
                    if (result.data.linkAccount) {
                        if (result.data.linkAccount.success) {
                            this.loading = false
                            this.$emit('accountsUpdate')
                            this.show = false
                        }
                    }
                }).catch(err => {
                    console.log(err)
                    this.feedback = true
                    this.loading = false
                })
                
            }
        },
    }, 
    created() {
        let r = this.$route.query
        // NOTE: localhost, change to touchbase.id for prod
        if (r['openid.claimed_id'] && r['openid.assoc_handle'] && r['openid.signed'] && r['openid.sig'] && r['openid.mode'] && r['openid.response_nonce'] && r['openid.op_endpoint'] === "https://steamcommunity.com/openid/login" && r['openid.return_to'] === "http://192.168.0.26:8000/accounts") {
            this.spfIdentifier = r['openid.claimed_id'].split('/').pop()
            console.log(this.spfIdentifier)
            this.service = 'Steam'
            this.oauthFeedback = true
            this.dialog = true
        }
    },
}
</script>

<style>
.v-dialog {
    -webkit-box-shadow: none; 
    box-shadow: none;
}
</style>