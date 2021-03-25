<template>
<v-expansion-panel expand flat style="-webkit-box-shadow: none;">
    <v-expansion-panel-content
        v-for="account in accounts" :key="account.service"
         class="mb-1 py-0" 
        style="border: none; border-radius: 8px; border: 1px solid #EEEEEE;"
    >
        <v-layout style="max-height: 35px;" slot="header" align-center justify-space-around row fill-height>
            <v-avatar size="32" class="mr-4"><img class="elevation-1" :src="$store.state.logoList[account.service]" :alt="account.service"></v-avatar>
            <span class="text-capitalize grey--text text--darken-4">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
            <template v-if="account.service.substring(0, account.service.indexOf('.')) === 'youtube'"></template>
            <template v-else>
                <v-icon class="mx-4" color="grey">compare_arrows</v-icon>
                <span class="font-weight-light body-1 grey--text text--darken-2">@{{ account.identifier }}</span>
            </template>
            <v-spacer></v-spacer>
            <v-btn flat :href="account.url" icon color="primary" class="mr-4 hidden-sm-and-down">
                <v-icon>exit_to_app</v-icon>
            </v-btn>
        </v-layout>
        <v-card style="border-radius: 8px;">
            <v-card-text class="grey--text text--darken-2 font-weight-light">
                <v-layout align-center justify-space-between row fill-height>
                    <span class="ml-2">Linked {{ account.created }}</span>
                    <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                </v-layout>
            </v-card-text>
            <!-- <v-divider></v-divider> -->
            <div style="height: 1px; width: 100%; background-color: #EEEEEE"></div>
            <v-card-actions class="pa-1">
                <v-btn @click="openProfile(account.url)" flat color="primary" class="ml-2">
                    <span class="text-capitalize font-weight-regular">Go To Profile</span>
                    <v-icon class="ml-2">link</v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn v-if="!account.remove" @click="account.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">remove</span><v-icon>delete</v-icon></v-btn>
                <v-btn v-else-if="account.remove && !account.confirmedRemove" :loading="deleteLoading" @click="account.confirmedRemove=true; removeAccount(account.service)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-2">Confirm?</span><v-icon>check</v-icon></v-btn>
                <span class="success--text" v-if="account.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span>
            </v-card-actions>
        </v-card>

    </v-expansion-panel-content>
</v-expansion-panel>
</template>

<script>
export default {
    name: 'AccountList',
    props: ['accounts'],
    data() {
        return {
            deleteLoading: false,
        }
    },
    methods: {
        openProfile(url) {
            window.open(url)
        },
        removeAccount(service) {
            this.deleteLoading = true
            console.log(service)
            this.deleteLoading = false
            location.reload()
        }
    },
}
</script>

<style>
.v-expansion-panel__header {
    padding: 0px 24px;
}
</style>