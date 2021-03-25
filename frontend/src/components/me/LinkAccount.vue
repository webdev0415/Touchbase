<template>
    <v-dialog
        lazy max-width="50vw" v-model="dialog" scrollable
    >
        <v-btn large flat slot="activator" class="animated-box in font-weight-medium subheading" color="primary">Link an Account </v-btn>
        <v-card style="border-radius: 25px;">
            <v-card-text>
                <v-form class="pr-4 pl-2" lazy-validation ref="linkAccountForm">
                    <v-autocomplete
                        :items="accountList"
                        label="Service"
                        outline
                        clearable
                        v-model="service"
                        prepend-inner-icon="link"
                    ></v-autocomplete>
                    <v-divider class="mt-1 mb-3"></v-divider>
                    <!-- accounts user has linked -->
                    <!-- If categories are wanted for account selection, sort it in accountList with -->
                    <!-- "-----" break items. have custom scoped-slot="item" and if break, put -->
                    <!-- divider and respective category. Color code? -->
                    
                    <v-text-field class="my-0"
                        outline
                        clearable
                        v-if="!isSupported"
                        label="Username/Email"
                        v-model="username"
                        prepend-inner-icon="person"
                        counter="128"
                        hint="The username/email/phone number of the account you want to link."
                    ></v-text-field>
                    <div v-if="isSupported">
                        <!-- <v-divider class="mt-1 mb-3"></v-divider> -->
                        <p class="text-uppercase grey--text mb-1">Sign In Securely</p>
                        <v-layout justify-center>
                            <!-- tooltip that says touchbase cannot see or store your credentials -->
                            <v-btn round @click="signIn" large outline color="primary">Sign In With {{ service }}</v-btn>
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
                    
                    <!-- <v-btn round color="primary">Other</v-btn> -->
                </v-form>
                <!-- <p v-if="feedback" class="red--text text-xs-center">Please enter valid credentials.</p> -->
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-btn primary block large dark depressed round color="primary" class="my-3 mx-4 subheading" @click="submit" :loading="loading">Link It</v-btn>
            </v-card-actions>
            <p v-if="feedback" class="red--text text-xs-center">Please double check the form.</p>
            <p v-if="oauthFeedback" class="ogSuccess--text text-xs-center">Click to finish linking {{ service }}.</p>
        </v-card>
    </v-dialog>
</template>

<script>
import { LINK_ACCOUNT_MUTATION } from '@/graphql/mutations/linkAccount'
import JQuery from 'jquery'
let $ = JQuery
var gapi = window.gapi;

export default {
    name: 'LinkAccount',
    data() {
        return {
            username: '',
            service: '',
            shareSPF: true,
            loading: false,
            dialog: false,
            oauthFeedback: false,
            feedback: false,
            spfIdentifier: '',
        }
    },
    // props: ['accounts'],
    computed: {
        accountList() {
            let ac = this.$store.state.accountList
            let acNew = []
            for (let i = 0; i < ac.length; i++) {
                let thing = ac[i].substring(0, ac[i].indexOf('.'))
                if (thing === 'steamcommunity') {
                    acNew.push('Steam')
                } else {
                    acNew.push(thing.charAt(0).toUpperCase() + thing.slice(1))
                }
            }
            return acNew
        },
        OAFLabel() {
            return `Share highlights of my posts on ${this.service} to my Touchbase followers`
        },
        supported() {
            return this.$store.state.supportedAccounts
        },
        isSupported() {
            if (this.supported.includes(this.service)) {
                return true
            } else {
                return false
            }
        },
        loggedIn() {
            // make sure to validate the jwt-token with the verifyToken mutation!
            if (localStorage.getItem('jwt-token')) {
                return true
            } else {
                return false
            }
            // return this.$store.state.loggedIn
        },
    },
    beforeRouteEnter (to, from, next) {
        next(vm => {
            if (!vm.loggedIn) {
                vm.$router.replace('/login')
            }
        })
    },
    methods: {
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
                    console.log('gaben unCOOL')
                    break;
            

                default:
                    console.log('You broke something')
                    break;
            }
        },
        submit() {
            if (this.$refs.linkAccountForm.validate()) {
                this.loading = true
                let { username, service, shareSPF, spfIdentifier } = this.$data
                var ac = this.$store.state.accountList
                if (service === 'Steam') {
                    service = 'steamcommunity.com'
                    shareSPF = false
                } else {
                    service = service.toLowerCase()
                    // get it in the domain format
                    ac.forEach(function(a){if (typeof(a) == 'string' && a.indexOf(service)>-1) service = a})
                }
                
                if (this.isSupported) {
                    username = ''
                }
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
                            // console.log(this.$apollo.queries, 'memes3123')
                            // TODO: PASS APOLLO QUERIES AS PROP FROM PARENT COMPONENT, 
                            // THEN USE TO REFRESH OVER HERE
                            // location.href('/accounts')
                            // location.reload()
                            this.dialog = false
                            this.$emit('accountsUpdate')
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
.animated-box {
  position: relative;
  width: 270px;
}

.animated-box:after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 4px;
  background: linear-gradient(120deg, #FF7256, #FFCCB3, #FF7256);
  background-size: 300% 300%;
  clip-path: polygon(0% 100%, 3px 100%, 3px 3px, calc(100% - 3px) 3px, calc(100% - 3px) calc(100% - 3px), 3px calc(100% - 3px), 3px 100%, 100% 100%, 100% 0%, 0% 0%);
}

.animated-box.in:after {
  animation: frame-enter 1s forwards ease-in-out reverse, gradient-animation 4s ease-in-out infinite;
}

/* motion */
@keyframes gradient-animation {
  0% {
    background-position: 15% 0%;
  }
  50% {
    background-position: 85% 100%;
  }
  100% {
    background-position: 15% 0%;
  }
}

@keyframes frame-enter {
  0% {
    clip-path: polygon(0% 100%, 3px 100%, 3px 3px, calc(100% - 3px) 3px, calc(100% - 3px) calc(100% - 3px), 3px calc(100% - 3px), 3px 100%, 100% 100%, 100% 0%, 0% 0%);
  }
  25% {
    clip-path: polygon(0% 100%, 3px 100%, 3px 3px, calc(100% - 3px) 3px, calc(100% - 3px) calc(100% - 3px), calc(100% - 3px) calc(100% - 3px), calc(100% - 3px) 100%, 100% 100%, 100% 0%, 0% 0%);
  }
  50% {
    clip-path: polygon(0% 100%, 3px 100%, 3px 3px, calc(100% - 3px) 3px, calc(100% - 3px) 3px, calc(100% - 3px) 3px, calc(100% - 3px) 3px, calc(100% - 3px) 3px, 100% 0%, 0% 0%);
  }
  75% {
    -webkit-clip-path: polygon(0% 100%, 3px 100%, 3px 3px, 3px 3px, 3px 3px, 3px 3px, 3px 3px, 3px 3px, 3px 0%, 0% 0%);
  }
  100% {
    -webkit-clip-path: polygon(0% 100%, 3px 100%, 3px 100%, 3px 100%, 3px 100%, 3px 100%, 3px 100%, 3px 100%, 3px 100%, 0% 100%);
  }
}
</style>