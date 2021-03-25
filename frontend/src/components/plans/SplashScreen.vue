<template>
    <div>
        <section>
            <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg" height="600">
                <v-layout row fill-height
                 align-center justify-center
                 class="white--text"
                >
                    <v-flex>
                        <h1 class="white--text mb-4 display-4 text-xs-center font-weight-thin">Parallax Template</h1>
                        <div class="headline font-weight-light text-xs-center" style="margin-bottom: 70px;">Powered by Vuetify</div>
                        <v-layout row justify-center>
                            <!-- PayPal Buy Button -->
                            <v-flex xs8 sm6 md4 lg3>
                                <div style="max-width: 420px;" id="plans-ss-buy"></div>
                            </v-flex>
                        </v-layout>
                        
                    </v-flex>
                </v-layout>
            </v-parallax>
        </section>

        <section>
            <v-layout column class="my-5" align-center wrap>
                <v-flex xs12 sm4 class="my-3">
                    <div class="text-xs-center">
                        <h2 class="headline">The best way to start developing</h2>
                        <span>
                            Cras facilisis mi vitae nunc 
                        </span>
                    </div>
                </v-flex>
                <v-flex xs12>
                    <v-container grid-list-xl>
                        <v-layout row wrap align-center>
                            <v-flex xs12 md4>
                                <v-card class="elevation-0 transparent">
                                    <v-card-text class="text-xs-center">
                                        <v-icon x-large color="primary">dashboard</v-icon>
                                    </v-card-text>
                                    <v-card-title primary-title class="layout justify-center">
                                        <div class="headline text-xs-center">Material Design</div>
                                    </v-card-title>
                                    <v-card-text>
                                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare. 
                                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
                                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti. 
                                    </v-card-text>
                                </v-card>
                            </v-flex>
                            <v-flex xs12 md4>
                                <v-card class="elevation-0 transparent">
                                    <v-card-text class="text-xs-center">
                                        <v-icon x-large color="primary">person</v-icon>
                                    </v-card-text>
                                    <v-card-title primary-title class="layout justify-center">
                                        <div class="headline text-xs-center">Fast Development</div>
                                    </v-card-title>
                                    <v-card-text>
                                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare. 
                                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
                                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti. 
                                    </v-card-text>
                                </v-card>
                            </v-flex>
                            <v-flex xs12 md4>
                                <v-card class="elevation-0 transparent">
                                    <v-card-text class="text-xs-center">
                                        <v-icon x-large color="primary">build</v-icon>
                                    </v-card-text>
                                    <v-card-title primary-title class="layout justify-center">
                                        <div class="headline text-xs-center">Get Promoted</div>
                                    </v-card-title>
                                    <v-card-text>
                                        Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare. 
                                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
                                        Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti. 
                                    </v-card-text>
                                </v-card>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-flex>
            </v-layout>
        </section>
        
        <section>
            <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" height="380">
                <v-layout column align-center justify-center>
                    <div class="headline white--text mb-3 text-xs-center">Web development has never been easier</div>
                    <em>Kick-start your application today</em>
                    <v-btn class="primary mt-5" @click="$vuetify.goTo('#plans-ss-buy', {duration: 1400, offset: -500, easing: 'easeOutQuad'})" dark large round >
                        Buy Now
                    </v-btn>
                </v-layout>
            </v-parallax>
        </section>
        
        <section>
            <v-container grid-list-xl>
                <v-layout row wrap justify-center class="my-5">
                    <v-flex xs12 sm4>
                        <v-card class="elevation-0 transparent">
                            <v-card-title primary-title class="layout justify-center">
                                <div class="headline">Company info</div>
                            </v-card-title>
                            <v-card-text>
                                Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam in aliquet odio. Aliquam eu est vitae tellus bibendum tincidunt. Suspendisse potenti.
                            </v-card-text>
                        </v-card>
                    </v-flex>
                    <v-flex xs12 sm4 offset-sm1>
                        <v-card class="elevation-0 transparent">
                            <v-card-title primary-title class="layout justify-center">
                                <div class="headline">Contact us</div>
                            </v-card-title>
                            <v-card-text>
                                Cras facilisis mi vitae nunc lobortis pharetra. Nulla volutpat tincidunt ornare.
                            </v-card-text>
                            <v-list class="transparent">
                                <v-list-tile>
                                    <v-list-tile-action>
                                        <v-icon color="primary">phone</v-icon>
                                    </v-list-tile-action>
                                    <v-list-tile-content>
                                        <v-list-tile-title>777-867-5309</v-list-tile-title>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile>
                                    <v-list-tile-action>
                                        <v-icon color="primary">place</v-icon>
                                    </v-list-tile-action>
                                    <v-list-tile-content>
                                        <v-list-tile-title>Chicago, US</v-list-tile-title>
                                    </v-list-tile-content>
                                </v-list-tile>
                                <v-list-tile>
                                    <v-list-tile-action>
                                        <v-icon color="primary">email</v-icon>
                                    </v-list-tile-action>
                                    <v-list-tile-content>
                                        <v-list-tile-title>john@vuetifyjs.com</v-list-tile-title>
                                    </v-list-tile-content>
                                </v-list-tile>
                            </v-list>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </section>
        <v-footer color="blue lighten-1">
            <v-layout row wrap align-center justify-center>
                <div class="white--text ml-3">
                    &copy; Hioz LLC
                </div>
            </v-layout>
        </v-footer>

        <v-snackbar
            bottom right
            v-model="paymentDone"
            :timeout="3500"
        >
            <v-icon color="success">check</v-icon>
            Your payment has gone through!
            <v-btn flat color="primary" @click.native="paymentDone = false; router.replace('/')">Close</v-btn>
        </v-snackbar>

    </div>
</template>

<script>
import { SEND_TRANSACTION_MUTATION } from '@/graphql/mutations/ptc'

export default {
    name: 'SplashScreen',
    data() {
        return {
            paymentConfirmed: false,
            paymentDone: false,
        }
    },
    methods: {
        sendTransaction(orderId, phone) {
            this.loading = true
            this.$apollo.mutate({
                mutation: SEND_TRANSACTION_MUTATION,
                variables: {
                    orderId,
                    phone
                }
            }).then(result => {
                this.loading = false
                if (result.data.ptc.success) {
                    this.paymentDone = true
                }
            }).catch(err => {
                console.log(err)
                this.loading = false
            })
        }
    },
    mounted() {
        let that = this
        paypal.Buttons({
            style: {
                color:  'gold',
                // shape:  'pill',
                label:  'pay',
                height: 50,
            },

            // Set up the transaction
            createOrder: function(data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value: '29.99'
                        }
                    }]
                });
            },

            // Finalize the transaction
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(details) {
                    // Show a success message to the buyer
                    that.paymentConfirmed = true
                    // that.paymentDone = true
                    // console.log(details)
                    // console.log(details.payer, details.payer.phone.phone_number.national_number)
                    that.sendTransaction(details.id, '1234567890')
                    // alert('Transaction completed by ' + details.payer.name.given_name + '!');
                });
            }
        }).render('#plans-ss-buy')
    },
}
</script>

<style>
    
</style>