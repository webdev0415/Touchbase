<template>
    <v-layout class="signup-splash" fill-height align-center justify-center>
        <v-flex xs8 sm6 md4 lg3>
            <v-card color="transparent" class="elevation-0">
                <v-card-title>
                    <v-layout wrap>
                        <v-flex xs12 class="text-xs-center my-2">
                            <span class="headline">Powered By Alias</span>
                        </v-flex>
                        <v-flex xs12 class="text-xs-center my-2">
                            <v-avatar size="100"><img src="/img/alias.png" alt="memess"></v-avatar>
                        </v-flex>
                        <v-flex xs12 class="text-xs-center my-2">
                            <v-divider></v-divider>
                        </v-flex>
                        <v-flex xs12 class="text-xs-center my-3">
                            <span class="display-1 font-weight-bold">Signup for Touchbase</span>
                        </v-flex>
                    </v-layout>
                </v-card-title>

                <v-card-text>
                    <v-form class="px-4" ref="signupForm">
                        <v-text-field dark solo-inverted v-model="username" label="Username" append-icon="person" class="my-2" color="alias" validate-on-blur :rules="[rules.username]"></v-text-field>
                        <v-text-field dark solo-inverted v-model="email" type="email" label="Email" append-icon="mail" class="my-2" color="alias" validate-on-blur></v-text-field>
                        <v-text-field dark solo-inverted v-model="firstName" label="First Name" append-icon="list" class="my-2" color="alias" validate-on-blur :rules="[rules.name]"></v-text-field>
                        <v-text-field dark solo-inverted v-model="lastName" label="Last Name" append-icon="list" class="my-2" color="alias" validate-on-blur :rules="[rules.name]"></v-text-field>
                        <v-text-field dark solo-inverted v-model="password" type="password" label="Password" append-icon="lock" class="my-2" validate-on-blur color="alias" :rules="[rules.password]"></v-text-field>
                    </v-form>
                </v-card-text>

                <v-card-actions>
                    <v-btn primary block large dark depressed round color="alias" class="ma-3 subheading" @click="submit" :loading="loading">Signup</v-btn>
                </v-card-actions>

                <!-- <p>Don't have an account? Sign up</p> -->
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
import { REGISTER_USER_MUTATION } from '@/graphql/mutations/register'
import { onLogin } from '@/apollo'

export default {
    name: 'Signup',
    data() {
        return {
            username: '',
            password: '',
            firstName: '',
            lastName: '',
            email: '',
            loading: false,
            rules: {
                username: v => /^[\w.]+$/.test(v) || 'Letters, numbers, . or _',
                password: v => v.length >= 8 || 'Password should be 8 or more characters',
                name: v => /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/.test(v) || 'Letters with - \' . , only'
            }
        }
    },
    methods: {
        submit() {
            if (this.$refs.signupForm.validate()) {
                this.loading = true
                const { username, email, firstName, lastName, password } = this.$data
                this.$apollo.mutate({
                    mutation: REGISTER_USER_MUTATION,
                    variables: {
                        username,
                        email,
                        firstName,
                        lastName,
                        password
                    }
                }).then(result => {
                    if (result.data.login.token && result.data.login.refreshToken) {
                        onLogin(this.$apollo.provider.defaultClient, username)
                        this.loading = false
                        location.href = '/'
                    } else {
                        console.log("you\'re fake")
                    }
                }).catch(err => {
                    console.log(err)
                    this.loading = false
                })
                
            }
        },
    }
}
</script>

<style>
    .signup-splash {
        background-image: url("https://cdn.pixabay.com/photo/2014/10/30/21/36/niagara-falls-509747_960_720.jpg");
        background-repeat: no-repeat;
        background-size: 100vw 120vh;
    }
</style>