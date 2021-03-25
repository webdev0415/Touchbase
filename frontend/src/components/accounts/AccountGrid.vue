<template>
<v-container grid-list-lg class="px-2" fluid>
    <v-layout row wrap>
        <v-flex xs3 md2 class="text-xs-center mb-1" v-for="(account, i) in accounts" :key="i" @click="$root.$emit('openLinkAccountDialog', account)" style="cursor: pointer;">
            <!-- <v-layout column align-center justify-center class="text-xs-center"> -->
                <v-avatar :size="$vuetify.breakpoint.mdAndUp ? 58 : 44"><img class="account-category-logo" :src="account.logo" :alt="account.name"></v-avatar> <br/>
                <span class="text-capitalize font-weight-light caption grey--text text--darken-3">{{ account.name }}</span>
            <!-- </v-layout> -->
        </v-flex>
    </v-layout>
</v-container>
</template>

<script>
export default {
    props: ['accounts',]
}
</script>