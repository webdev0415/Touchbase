<template>
    <v-flex xs12 md6 lg4 order-md1 class="db-flex mb-5">
        <v-card flat color="grey lighten-4" class="db-card elevation-2">
            <v-card-title class="text-uppercase grey--text text--darken-1 justify-center">Manage</v-card-title>
            <v-spacer></v-spacer>
            <v-divider></v-divider>
            <v-card-actions>
                <v-layout align-center justify-space-around fill-height class="my-2">
                    <v-btn to="/me/settings" round outline large color="primary">
                        <v-icon left>settings</v-icon>
                        <span>Settings</span>
                    </v-btn>
                </v-layout>
            </v-card-actions>
        </v-card>
    </v-flex>
</template>

<script>
export default {
    name: 'Manage',
    data() {
        return {

        }
    }
}
</script>

<style>

</style>

