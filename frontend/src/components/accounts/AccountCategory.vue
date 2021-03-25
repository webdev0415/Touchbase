<template>
<v-expansion-panel-content
    expand-icon="" class="my-1 py-0"
    style="border: none; border-radius: 8px; border: 1px solid #EEEEEE;"
>
    <v-layout slot="header">
        <span class="title grey--text text--darken-3">{{ category.name }}</span>
        <v-icon class="ml-2" color="grey darken-3">{{ category.icon }}</v-icon>
    </v-layout>

    <v-card style="border-radius: 8px;">
        <div style="height: 1px; width: 100%; background-color: #EEEEEE"></div>
        <AccountGrid :accounts="category.accounts" />
    </v-card>

</v-expansion-panel-content>
</template>

<script>
import AccountGrid from '@/components/accounts/AccountGrid'

export default {
    name: 'AccountCategory',
    components: {
        AccountGrid
    },
    props: ['category'],
    data() {
        return {
            
        }
    },
}
</script>

<style>
.account-category-logo {
    transition: box-shadow .3s;
}
.account-category-logo:hover {
  box-shadow: 0 0 15px rgba(33,33,33,.2); 
}
</style>