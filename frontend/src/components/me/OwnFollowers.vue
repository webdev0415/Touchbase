<template>
<v-layout row fill-height align-center justify-center v-if="$apollo.loading">
    <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
</v-layout>

<v-layout v-else row class="px-4" justify-center fill-height>
    <v-flex xs12 sm8 md6 lg5>
        <v-layout column align-center fill-height class="pb-5">
            <v-flex>
                <p class="display-1 font-weight-light grey--text text--darken-2 mt-5">
                    <span>My Followers</span>
                </p>
            </v-flex>
            <FollowsList :ownFollowing="pownFollowing" :followers="ownFollowers" />
        </v-layout>
    </v-flex>
</v-layout>
</template>

<script>
import { OWN_FOLLOWERS_QUERY } from '@/graphql/queries/ownFollowers'
import { OWN_FOLLOWING_QUERY } from '@/graphql/queries/ownFollowing'
import FollowsList from '@/components/me/FollowsList'

export default {
    name: 'OwnFollowers',
    data() {
        return {
            ownFollowers: [],
            ownFollowing: [],
            pownFollowing: [],
        }
    },
    components: {
        FollowsList
    },
    apollo: {
        ownFollowers: {
            query: OWN_FOLLOWERS_QUERY,
            result({ data, loading }) {
                if (!loading) {
                    console.log(data)
                }
            }
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