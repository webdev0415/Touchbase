<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" style="min-width: 100%;" fullscreen hide-overlay transition="dialog-bottom-transition">
        <!-- <v-btn block flat dark><v-icon>search</v-icon></v-btn> -->
        <v-chip slot="activator" text-color="white" style="min-width: 100%;" class="subheading" color="grey lighten-4">
            <v-avatar
            >
                <!-- <vicon style="height: 40px; width: 40px;" src="/img/avatar-2.png" alt="profile picture"> -->
                <v-icon class="ml-3" color="grey darken-1">search</v-icon>
            </v-avatar>
            
            <span class="ml-1 grey--text text--darken-1">Search</span>
            
            <!-- <v-icon class="mr-3" style="position: absolute; right: 0;">exit_to_app</v-icon> -->
        </v-chip>
      
      <div class="grey lighten-4 ms-container">
        <v-toolbar dark color="primary">
          <v-btn icon dark @click="dialog = false">
            <v-icon>close</v-icon>
          </v-btn>
          <v-toolbar-title>Search</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark flat @click="dialog = false">Close</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-layout fill-height align-center column>
            <v-flex xs2 class="ms-flex-item pt-3 px-4">
                <v-layout justify-center row class="mb-2">
                    <span class="grey--text mb-1 font-weight-light text--darken-1">Search for a person or brand!</span>
                    <!-- Click the three dots for advanced search. -->
                </v-layout>
                <v-text-field
                    @keyup="search"
                    prepend-inner-icon="search"
                    label="Search"
                    outline
                    height="45"
                    v-model="value"
                ></v-text-field>
            </v-flex>
            <v-divider inset class="full-width mx-5 my-0 py-0"></v-divider>
            <template v-if="$vuetify.breakpoint.mdAndUp">
                <v-flex xs2 class="ms-flex-item pt-2">
                    <span class="grey--text ml-3 font-weight-light text-uppercase text--darken-1">Trending</span>
                </v-flex>
                <v-divider inset class="full-width mx-5 my-0 py-0"></v-divider>
            </template>
            <v-flex class="ms-flex-item pt-2">
                <span class="grey--text ml-3 font-weight-light text-uppercase text--darken-1">Results</span>
                <v-list two-line class="grey ms-results lighten-4 mt-2">
                    <v-layout row fill-height align-center justify-center v-if="loading">
                        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
                    </v-layout>
                    <template v-else-if="!loading && isResults">
                        <template v-for="(item, index) in items">
                            <v-list-tile @click="$router.push(`/${item.username}`)" :key="item.username" avatar ripple class="py-1">
                                <v-list-tile-avatar size="53" color="primary" class="pr-4">
                                    <img :src="item.profilePic" alt="">
                                    <!-- :src="item.avatar" -->
                                </v-list-tile-avatar>
                                <v-list-tile-content class="mr-3">
                                    <v-list-tile-title>
                                        <span>{{ item.firstName }} </span>
                                        <span>{{ item.lastName }}</span>
                                    </v-list-tile-title>
                                    <v-list-tile-sub-title class="ml-2">@{{ item.username }}</v-list-tile-sub-title>
                                    <!-- if they already follow, unfollow button, else follow button -->
                                </v-list-tile-content>
                                <v-list-tile-action v-if="ownFollowing.includes(item.username)">
                                    <v-btn depressed @click="unfollow(item.username)" small color="primary">
                                        <v-icon small class="mx-2">person_add_disabled</v-icon>
                                        <span class="font-weight-regular caption mr-2">Unfollow</span>
                                    </v-btn>
                                </v-list-tile-action>
                                <v-list-tile-action v-else>
                                    <v-btn depressed @click="follow(item.username)" small color="primary">
                                        <v-icon small class="mx-2">person_add</v-icon>
                                        <span class="font-weight-regular caption mr-2">Follow</span>
                                    </v-btn>
                                </v-list-tile-action>
                            </v-list-tile>
                            <v-divider v-if="index + 1 < items.length" :key="index"></v-divider>
                        </template>
                    </template>
                    
                </v-list>
            </v-flex>
        </v-layout>
      </div>
    </v-dialog>
  </v-layout>
</template>

<script>
import { BASIC_SEARCH_MUTATION } from '@/graphql/mutations/basicSearch'
import { OWN_FOLLOWING_QUERY } from '@/graphql/queries/ownFollowing'
import { FOLLOW_USER_MUTATION } from '@/graphql/mutations/follow'
import { UNFOLLOW_USER_MUTATION } from '@/graphql/mutations/unfollow'

export default {
    name: 'MobileSearch',
    data () {
        return {
            dialog: false,
            value: '',
            items: [],
            outputValue: '',
            // followLoad: false,
            ownFollowing: [],
            timeout: null,
            loading: false,
        }
    },
    computed: {
        isResults() {
            if (this.items.length >= 1) {
                return true
            } else {
                return false
            }
        },
    },
    methods: {
        search() {
            this.loading = true
            clearTimeout(this.timeout)
            
            this.timeout = setTimeout(() => {
                this.$apollo.mutate({
                    mutation: BASIC_SEARCH_MUTATION,
                    variables: {
                        term: this.value,
                        // possible data collection for analytics
                    }
                }).then(result => {
                    // let list = 
                    // normalization of list, for item.avatar, item.text, see vuetify
                    // set items to normalized list so vue can render it
                    this.items = result.data.basicSearch.results
                    this.items.forEach(obj => {
                        obj.disabled = true
                    })
                    console.log(this.items);
                    this.loading = false
                }).catch(err => {
                    console.log(err)
                    //this.feedback = true
                    this.loading = false
                })
            }, 500)
        },
        follow(usernameFollowee) {
            this.$apollo.mutate({
                mutation: FOLLOW_USER_MUTATION,
                variables: {
                    usernameFollowee
                }
            }).then(result => {
                if (result.data.follow) {
                    if (result.data.follow.success) {
                        // this.loading = false
                        this.$apollo.queries.ownFollowing.refetch() 
                    } else {
                        alert("Error - Could not follow user. \n FYI - You cannot follow yourself.")
                    }
                }
            }).catch(err => {
                console.log(err)
                // this.feedback = true
                // this.loading = false
            })
        },
        unfollow(usernameFollowee) {
            this.$apollo.mutate({
                mutation: UNFOLLOW_USER_MUTATION,
                variables: {
                    usernameFollowee
                }
            }).then(result => {
                if (result.data.unfollow) {
                    if (result.data.unfollow.success) {
                        // this.loading = false
                        this.$apollo.queries.ownFollowing.refetch() 
                    } else {
                        alert('Error - Could not unfollow user')
                    }
                }
            }).catch(err => {
                console.log(err)
                // this.feedback = true
                // this.loading = false
            })
        },
    },
    apollo: {
        ownFollowing: {
            query: OWN_FOLLOWING_QUERY,
            update(data) {
                let people = []
                if (data.ownFollowing) {
                    for (let i = 0; i < data.ownFollowing.length; i++) {
                        people.push(data.ownFollowing[i].username)
                    }
                } else {
                    alert('Something went wrong. Please try again later! ⏳')
                }
                return people  
            }
        }
    }

}
</script>

<style>
.ms-flex-item {
    width: 100%;
    height: 1000px;
}

.full-width {
    width: 100vw;
}

.ms-container {
    height: 100%; 
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
    top: 0;
    right: 0;
    overflow: hidden;
}

.ms-results {
    max-height: calc(calc(100vh / 12) * 8);
    overflow-y: auto;
    overflow-x: hidden;
}
</style>