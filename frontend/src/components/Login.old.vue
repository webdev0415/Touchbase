<template>
    <v-layout fill-height align-center justify-center>
        <v-flex xs12 sm7 md5 lg3 style="max-width: 420px;">
            <v-card class="elevation-10">
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
                            <span class="display-1 font-weight-bold">Login to Touchbase</span>
                        </v-flex>
                    </v-layout>
                </v-card-title>

                <v-card-text>
                    <v-form class="px-4" ref="loginForm">
                        <v-text-field @keyup.enter="submit()" box v-model="username" label="Username" prepend-icon="person" class="my-2" color="alias" validate-on-blur :rules="[rules.username]"></v-text-field>
                        <v-text-field @keyup.enter="submit()" box v-model="password" type="password" label="Password" prepend-icon="lock" class="my-2" validate-on-blur color="alias" :rules="[rules.password]"></v-text-field>
                    </v-form>
                    <p v-if="feedback" class="red--text text-xs-center">Please enter valid credentials.</p>
                </v-card-text>

                <v-card-actions>
                    <v-btn primary block large dark depressed round color="alias" class="ma-3 subheading" @click="submit" :loading="loading">Login</v-btn>
                </v-card-actions>

                <!-- <p>Don't have an account? Sign up</p> -->
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
import { LOGIN_USER_MUTATION } from '@/graphql/mutations/login'
import { onLogin } from '@/apollo'

export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            feedback: false,
            loading: false,
            rules: {
                username: v => /^[\w.]+$/.test(v) || 'Letters, numbers, . or _',
                password: v => v.length >= 8 || 'Password should be 8 or more characters'
            }
        }
    },
    methods: {
        submit() {
            if (this.$refs.loginForm.validate()) {
                this.loading = true
                const { username, password } = this.$data
                this.$apollo.mutate({
                    mutation: LOGIN_USER_MUTATION,
                    variables: {
                        username,
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
                    this.feedback = true
                    this.loading = false
                })
                
            }
        },
    }
}
</script>
