<template>
    <v-layout row fill-height align-center justify-center v-if="$apollo.loading">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>
    <v-layout v-else-if="expired" row>
        This toush link has expired.
    </v-layout>
    <div class="home-div" v-else>
        <ToushProfile v-if="expand.item.isToushProfile" :toushLink="expand"/>
        <ToushFeed v-else-if="expand.item.isToushFeed" :toushLink="expand"/>
        <ToushEvents v-else-if="expand.item.isToushEvents" :toushLink="expand"/>
    </div>
</template>

<script>
import { RESOLVE_TOUSH_QUERY } from '@/graphql/queries/resolveToush'
import ToushProfile from '@/components/toush/ToushProfileComponent'
import ToushFeed from '@/components/toush/ToushFeedComponent'
import ToushEvents from '@/components/toush/ToushEventsComponent'

export default {
    name: 'Toush',
    props: ['toushString'],
    components: {
        ToushProfile,
        ToushFeed,
        ToushEvents
    },
    data() {
        return {
            loading: 0,
            expand: {},
            expired: false,
        }
    },
    apollo: {
        expand: {
            query: RESOLVE_TOUSH_QUERY,
            variables() {
                return {
                    shortUrl: this.toushString,
                    edit: false
                }
            },
            error(err) {
                console.log(err)
                this.expired = true
            },
            // update(data) {
            //     return data.toushLinkType
            // }
            result({ data, loading }) {
                if (!loading) {
                    console.log(data)
                }
                
            }
        }
    },
    computed: {
        computedToushString() {
            if (this.$route.query.redirect) {
                // console.log(this.$route.query.redirect)
                return this.$route.query.redirect
            } else {
                return ''
            }
        }
    },

}
</script>
