<template>
    <v-flex xs12 md6 lg4 order-md2 class="db-flex mb-5">
        <v-card flat color="grey lighten-4" class="db-card elevation-2">
            <v-card-title class="text-uppercase grey--text text--darken-1 justify-center">Links</v-card-title>
            
            <v-spacer></v-spacer>
            <v-divider></v-divider>
            <v-card-actions>
                <v-layout wrap align-center justify-space-around fill-height>
                    <!-- <v-flex xs12 sm6>
                        <v-btn to="/me/settings" round outline large color="primary">
                            <v-icon left>settings</v-icon>
                            <span>Settings</span>
                        </v-btn>
                    </v-flex>
                    <v-flex xs12 sm6>
                        <v-btn to="/me/settings" round outline large color="primary">
                            <v-icon left>settings</v-icon>
                            <span>Settings</span>
                        </v-btn>
                    </v-flex> -->
                    <AddToushLink />
                    <v-btn to="/links" round outline large color="primary" class="my-2">
                        <v-icon left>settings</v-icon>
                        <span>manage</span>
                    </v-btn>
                    <ToushLinkList />
                </v-layout>
            </v-card-actions>
        </v-card>
    </v-flex>
</template>

<script>
import AddToushLink from "./AddToushLink"
import ToushLinkList from "./ToushLinkList";

export default {
    name: 'Links',
    components: {
        AddToushLink,
        ToushLinkList
    }
}
</script>

<style>

</style>
