<template>
    <v-dialog v-model="dialog" fullscreen hide-overlay max-width="800px" transition="dialog-bottom-transition" class="mx-3">
        <v-btn slot="activator" large flat color="white" class="title font-weight-regular">Login</v-btn>
        <v-card class="login-box">
            <v-toolbar color="primary" card class="login-box-toolbar">
                <v-btn icon dark @click="dialog = false" class="ml-2 mr-3">
                    <v-icon>close</v-icon>
                </v-btn>
                <v-toolbar-title>
                    <span class="white--text headline">Login to Touchbase</span>
                </v-toolbar-title>
                
                <!-- x icon to exit card -->
            </v-toolbar>

            <v-card-text>
                <v-form class="px-3 login-form" ref="form">
                    <v-text-field box v-model="username" label="Username" prepend-icon="person"></v-text-field>
                    <v-text-field box v-model="password" label="Password" prepend-icon="lock"></v-text-field>

                    <v-spacer></v-spacer>

                    <v-btn flat @click="submit" class="success my-3 ml-3" :loading="loading">Login</v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            username: '',
            email: '',
            firstName: '',
            lastName: '',
            password: '',
            dialog: false,
        }
    }

}
</script>

<style>
/* .login-box {
    
} */

.login-form {
    max-width: 500px;
}

</style>