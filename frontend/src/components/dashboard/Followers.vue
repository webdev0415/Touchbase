<template>
    <v-dialog lazy max-width="800px" v-model="dialog" scrollable>
        <v-btn slot="activator" large round depressed outline color="primary">Followers</v-btn>
        <v-card class="followers-box">
            <v-toolbar color="primary" card>
                <v-toolbar-side-icon class="white--text ml-2">
                    <v-icon large>people</v-icon>
                </v-toolbar-side-icon>
                <v-toolbar-title class="text-uppercase white--text pr-5">
                    <div class="headline">
                        <span>Followers</span>
                    </div>
                </v-toolbar-title>

                <v-spacer></v-spacer>

                <v-toolbar dense flat class="searchbox mr-5" color="primaryComp">
                    <v-text-field
                        label="Search"
                        flat
                        solo
                        hide-details
                        clearable
                        prepend-inner-icon="search"
                    >
                    </v-text-field>
                </v-toolbar>

            </v-toolbar>
            <v-card-text style="max-height: 400px;">
                <v-card flat>
                    <v-list two-line>
                        <!-- use router prop with to="" for links. Replaces router-link -->
                        <v-list-tile v-for="person in followers" :key="person.id">
                            <v-list-tile-action>
                                <v-icon class="grey--text text--darken-2">account_circle</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content>
                                <v-list-tile-title class="grey--text text--darken-2">{{ person.firstName }} {{ person.lastName }}</v-list-tile-title>
                                <v-list-tile-sub-title class="grey--text text--darken-1">@{{ person.username }}</v-list-tile-sub-title>

                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list>
                </v-card>
            </v-card-text>
        </v-card>
    </v-dialog>


</template>

<script>
import { ALL_FOLLOWERS_QUERY } from '@/graphql/queries/followers'

export default {
    name: 'Followers',
    data() {
        return {
            followers: [],
            loading: 0,
            dialog: false,
        }
    },
    apollo: {
        followers: {
            query: ALL_FOLLOWERS_QUERY
        }
    }
}

// [
//                 {'id': 1, 'username': 'memes._34', 'firstName': 'Jahseh', 'lastName': 'Onfroy'},
//                 {'id': 2, 'username': 'tho.tdestroyer_', 'firstName': 'Meme', 'lastName': 'Extravaganza'},
//                 {'id': 3, 'username': 'stokeley', 'firstName': 'Jack', 'lastName': 'the Nibber'},
//                 {'id': 4, 'username': 'ski.mask', 'firstName': 'smd', 'lastName': 'jk'},
//             ],
</script>


<style>
.followers-box {
    border-radius: 20px;
}
</style>
