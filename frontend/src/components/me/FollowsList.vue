<template>
<v-layout row fill-height align-center justify-center v-if="$apollo.loading || loading">
    <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
</v-layout>

<!-- exclusive OR to ensure only one is given -->
<v-flex class="home-div mt-5" v-else-if="(followers.length > 0) != (following.length > 0)">
    <v-list two-line class="py-0 elevation-2" style="border-radius: 10px;">
        <!-- <v-divider></v-divider> -->
        <template v-for="(person, index) in people">
            <v-list-tile @click="followLoad ? null : $router.push(`/${person.username}`)" :key="person.username" avatar ripple>
                <v-list-tile-avatar size="53" color="primary" class="pr-4">
                    <img :src="person.profilePic" alt="">
                    <!-- :src="person.avatak111bh00r" -->
                </v-list-tile-avatar>
                <v-list-tile-content>
                    <v-list-tile-title>
                        <span>{{ person.firstName }} </span>
                        <span>{{ person.lastName }}</span>
                    </v-list-tile-title>
                    <v-list-tile-sub-title class="ml-2">@{{ person.username }}</v-list-tile-sub-title>
                    <!-- if they already follow, unfollow button, else follow button -->
                </v-list-tile-content>
                <v-list-tile-action v-if="ownFollowing.includes(person.username)">
                    <v-btn depressed @click="followLoad = true; unfollow(person.username)" small color="primary">
                        <v-icon small class="mx-2">person_add_disabled</v-icon>
                        <span class="font-weight-regular caption mr-2">Unfollow</span>
                    </v-btn>
                </v-list-tile-action>
                <v-list-tile-action v-else>
                    <v-btn depressed @click="followLoad = true; follow(person.username)" small color="primary">
                        <v-icon small class="mx-2">person_add</v-icon>
                        <span class="font-weight-regular caption mr-2">Follow</span>
                    </v-btn>
                </v-list-tile-action>
            </v-list-tile>
            <!-- v-if="index + 1 < persons.length" -->
            <v-divider v-if="index + 1 != people.length" :key="index"></v-divider>
        </template>
    </v-list>
</v-flex>

<v-flex v-else class="text-xs-center">
    <v-icon color="grey lighten-1" class="mb-3" size="70">hourglass_empty</v-icon> <br/>
    <span class="display-3 font-weight-light grey--text text--lighten-1">Nothing here...</span>
</v-flex>
</template>

<script>
import { FOLLOW_USER_MUTATION } from '@/graphql/mutations/follow'
import { UNFOLLOW_USER_MUTATION } from '@/graphql/mutations/unfollow'

export default {
    name: 'FollowsList',
    props: {
        ownFollowing: {
            type: Array,
            default: () => { return [] }
        },
        following: {
            type: Array,
            default: () => { return [] }
        },
        followers: {
            type: Array,
            default: () => { return [] }
        },
        public: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            people: [],
            loading: true,
            followLoad: false,
        }
    },
    // mounted() {
    //     if (this.followers.length > 0) {
    //         this.people = this.followers
    //     } else if (this.following.length > 0) {
    //         this.people = this.following
    //     }
    // },
    watch: {
        followers() {
            if (this.followers.length > 0) this.people = this.followers
            this.loading = false
        },
        following() {
            if (this.following.length > 0) this.people = this.following
            this.loading = false
        },
    },
    methods: {
        follow(usernameFollowee) {
            this.$apollo.mutate({
                mutation: FOLLOW_USER_MUTATION,
                variables: {
                    usernameFollowee
                }
            }).then(result => {
                if (result.data.follow) {
                    if (result.data.follow.success) {
                        // NOTE: UPDATE TO QUERY REFETCH AND NOT PAGE RELOAD
                        // this.loading = false
                        location.reload()
                    } else {
                        alert("Error - Could not follow user. \n FYI - You cannot follow yourself.")
                    }
                }
            }).catch(err => {
                console.log(err)
                this.feedback = true
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
                        location.reload()
                    } else {
                        alert('Error - Could not unfollow user')
                    }
                }
            }).catch(err => {
                console.log(err)
                this.feedback = true
                // this.loading = false
            })
        },
    },
}
</script>

<style>
.follows-list-action {
    z-index: 999;
}
</style>