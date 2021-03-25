<template>
<v-layout row fill-height align-center justify-center v-if="$apollo.loading">
    <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
</v-layout>

<v-layout v-else row class="px-4" justify-center fill-height>
    <v-flex xs12 sm8 md6 lg5>
        <v-layout column align-center fill-height class="pb-5">
            <v-flex>
                <p class="display-1 font-weight-light grey--text text--darken-2 mt-5">
                    <span @click="$router.push({ path: `/${username}`, name: 'Profile' })" class="e-title">@{{ username }} </span>
                    <span>- Following</span>
                </p>
            </v-flex>
            <FollowsList :ownFollowing="pownFollowing" :following="following" public />
        </v-layout>
    </v-flex>
</v-layout>
</template>

<script>
import { ALL_FOLLOWING_QUERY } from '@/graphql/queries/following'
import { OWN_FOLLOWING_QUERY } from '@/graphql/queries/ownFollowing'
import FollowsList from '@/components/me/FollowsList'

export default {
    name: 'Following',
    data() {
        return {
            following: [],
            ownFollowing: [],
            pownFollowing: [],
        }
    },
    components: {
        FollowsList
    },
    computed: {
        username() {
            return this.$route.params.username
        },
        // if ends with s, append ' otherwise append 's
        usernamePunct() {
            if (this.username[this.username.length - 1] === 's') {
                return this.username + "'"
            } else {
                return this.username + "'s"
            }
        }
    },
    apollo: {
        following: {
            query: ALL_FOLLOWING_QUERY,
            variables() {
                // console.log(this.$route)
                return {
                    username: this.username
                }
                
            },
            // result({ data, loading }) {
            //     if (!loading) {
            //         console.log(data)
            //     }
            // }
        },
        ownFollowing: {
            query: OWN_FOLLOWING_QUERY,
            result({ data, loading }) {
                if (!loading) {
                    for (let i = 0; i < this.ownFollowing.length; i++) {
                        this.pownFollowing.push(this.ownFollowing[i].username)
                    }
                }
            }
        }
    }
}
</script>