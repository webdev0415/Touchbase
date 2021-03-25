<template>
    <v-layout row fill-height align-center justify-center v-if="$apollo.loading">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>

    <v-layout v-else column align-center class="pt-2">
        <v-flex style="width: 100%;">
            <v-layout row justify-center align-center fill-height class="my-4">
                <v-flex xs6 md3 class="text-xs-center">
                    <span class="text-uppercase font-weight-medium grey--text text--darken-2">Linked Accounts</span> <br/>
                    <span class="display-1 font-weight-medium">{{ accounts.length }}</span>
                </v-flex>
                <v-flex xs6 md3 class="text-xs-center">
                    <span class="text-uppercase font-weight-medium grey--text text--darken-2">Total Account Views</span> <br/>
                    <span class="display-1 font-weight-bold">4093</span>
                </v-flex>
            </v-layout>
            <v-divider v-show="$vuetify.breakpoint.smAndDown"></v-divider>
        </v-flex>
        <v-layout row justify-center style="width: 100%;" wrap>
            <v-flex xs12 md4 lg3 :order-xs2="$vuetify.breakpoint.smAndDown" :class="{'pb-2': $vuetify.breakpoint.smAndDown, 'mr-4': $vuetify.breakpoint.mdAndUp }" v-show="!searchTerm">
                <v-layout row align-center fill-height>
                    <v-btn small flat @click="showLinked = true; showNotLinked = true" class="my-0" color="grey darken-1" :block="$vuetify.breakpoint.smAndDown">All <v-icon class="ml-2">view_carousel</v-icon></v-btn>
                    <v-btn small flat @click="showLinked = true; showNotLinked = false" class="my-0" color="grey darken-1" :block="$vuetify.breakpoint.smAndDown">Linked <v-icon class="ml-2">link</v-icon></v-btn>
                    <v-btn small flat @click="showLinked = false; showNotLinked = true" class="my-0" color="grey darken-1" :block="$vuetify.breakpoint.smAndDown">Not Linked <v-icon class="ml-2">link_off</v-icon></v-btn>
                </v-layout>
            </v-flex>
            <v-flex xs12 md4 lg4 :class="{ 'pr-2': $vuetify.breakpoint.mdAndUp, 'px-3 pt-3': $vuetify.breakpoint.smAndDown }">
                <v-text-field
                    prepend-icon="search"
                    label="Search for an account"
                    v-model="searchTerm"
                ></v-text-field>
            </v-flex>
        </v-layout>

        <!-- <v-flex style="width: 100%;">
            <v-layout row justify-center>
                <v-flex xs12 md8 xl7 :class="{'px-1': $vuetify.breakpoint.smAndDown, 'my-2 ml-2': true}">
                    <span class="text-uppercase grey--text">My Accounts</span>
                </v-flex>
            </v-layout>
        </v-flex> -->
        
        <v-flex v-show="!searchTerm && showLinked">
            <v-layout row justify-center>
                <v-flex xs12 md8 xl7 :class="{'px-1': $vuetify.breakpoint.smAndDown}">
                    <AccountList :accounts="accounts" />
                </v-flex>
            </v-layout>
        </v-flex>
        <v-flex style="width: 100%;" v-show="!searchTerm && showNotLinked">
            <v-layout row justify-center>
                <v-flex xs12 md8 xl7 :class="{'px-1': $vuetify.breakpoint.smAndDown, 'my-2 ml-2': true}">
                    <span class="text-uppercase grey--text">All Available</span>
                </v-flex>
            </v-layout>
        </v-flex>
        <v-flex style="width: 100%;" v-show="!searchTerm && showNotLinked">
            <v-layout row justify-center>
                <v-flex xs12 md8 xl7 :class="{'px-1': $vuetify.breakpoint.smAndDown}">
                    <!-- fill array with true values to keep open by default -->
                    <v-expansion-panel :value="Array(categories.length).fill(true)" expand flat style="-webkit-box-shadow: none;">
                        <AccountCategory v-for="(category, i) in categories" :key="i" :category="category" />
                    </v-expansion-panel>
                </v-flex>
            </v-layout>
        </v-flex>
        <v-flex v-show="searchTerm" style="width: 100%;">
            <v-layout row justify-center>
                <v-flex xs12 md8 xl7 :class="{'px-1': $vuetify.breakpoint.smAndDown}">
                    <AccountGrid :accounts="filteredAccounts" />
                </v-flex>
            </v-layout>
        </v-flex>
        
        <LinkAccount/>
    </v-layout>
</template>

<script>
import moment from 'moment'
import { ALL_ACCOUNTS_QUERY } from '@/graphql/queries/accounts'
// import LinkAccount from '@/components/me/LinkAccount'
import AccountList from '@/components/accounts/AccountList'
import AccountCategory from '@/components/accounts/AccountCategory'
import AccountGrid from '@/components/accounts/AccountGrid'
import LinkAccount from '@/components/accounts/LinkAccount'

export default {
    name: 'Accounts',
    components: {
        LinkAccount,
        AccountList,
        AccountCategory,
        AccountGrid,
        LinkAccount
    },
    data() {
        return {
            accounts: [],
            searchTerm: '',
            showLinked: true,
            showNotLinked: true,
        }
    },
    computed: {
        categories() {
            return this.$store.state.categories
        },
        filteredAccounts() {
            let accounts = []
            this.categories.forEach(cat => {
                // merge and store in local var accounts
                Array.prototype.push.apply(accounts, cat.accounts)
            })
            let arr = accounts.filter(a => a.name.toLowerCase().includes(this.searchTerm.toLowerCase()))
            return arr.filter((v,i,a)=>a.findIndex(t=>(t.logo === v.logo && t.name===v.name))===i)
        },
    },
    beforeRouteEnter (to, from, next) {
        next(vm => {
            if (!vm.$loggedIn()) {
                vm.$router.replace('/login')
            }
        })
    },
    apollo: {
        accounts: {
            query: ALL_ACCOUNTS_QUERY,
            update(data) {
                if (data.ownAccounts) {
                    data.ownAccounts.forEach(account => {
                        if (account.service === 'steamcommunity.com') account.service = 'steam.com'
                        account.created = moment(account.created).fromNow()
                        account.dialog = false
                        account.confirmedRemove = false
                        account.remove = false
                    })
                }
                return data.ownAccounts          
            }
        }
    }
}
</script>