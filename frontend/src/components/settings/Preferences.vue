<template>
    <div>
        <!-- 
            Notifications, <-- move notifs to account and then say: 
            Preferences nd Customization for Touchbase is coming soon OR simply:
            Coming Soon (code icon)
         -->
        <v-form>
             <v-layout column align-center class="pb-5">
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <span style="font-size: 29px;" class="text-capitalize mr-1 font-weight-light grey--text text--darken-4 mt-1">Notifications</span>
                </v-flex>
                <v-flex style="width: 100%;">  
                    <v-switch v-model="notifsEnable" color="primary">
                        <template slot="prepend">
                            <span class="grey--text text--darken-2 mt-1 mr-2 ml-1">All Notifications</span>
                        </template>
                    </v-switch>
                </v-flex>
                <v-flex style="width: 100%;" class="ml-5">  
                    <v-checkbox :disabled="!notifsEnable" label="Follows *" v-model="notifsFollows" color="primary"></v-checkbox>
                </v-flex>
                <v-flex style="width: 100%;" class="ml-5">  
                    <v-checkbox :disabled="!notifsEnable" label="New Account Support *" v-model="notifsNewAccount" color="primary"></v-checkbox>
                </v-flex>
                <v-flex style="width: 100%;" class="ml-5">  
                    <v-checkbox :disabled="!notifsEnable" label="Updates *" v-model="notifsUpdates" color="primary"></v-checkbox>
                </v-flex>
                <span style="width: 100%" class="ml-2 my-2 grey--text text--darken-3"> * Coming Soon <v-icon>timer</v-icon></span>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                    </v-layout>
                </v-flex>
            </v-layout>
        </v-form>
    </div>
</template>

<script>
export default {
    name: 'Preferences',
    props: ['settings'],
    data() {
        return {
            notifsEnable: this.settings.notifsEnable,
            notifsFollows: this.settings.notifsFollows,
            notifsNewAccount: this.settings.notifsNewAccount,
            notifsUpdates: this.settings.notifsUpdates,
        }
    },
    watch: {
        notifsEnable() {
            this.$emit('settingsUpdate', { 'notifsEnable': this.notifsEnable })
        },
        // notifsFollows() {
        //     this.$emit('settingsUpdate', { 'notifsFollows': this.notifsFollows })
        // },
        // notifsNewAccount() {
        //     this.$emit('settingsUpdate', { 'notifsNewAccount': this.notifsNewAccount })
        // },
        // notifsUpdates() {
        //     this.$emit('settingsUpdate', { 'notifsUpdates': this.notifsUpdates })
        // }
    },
}
</script>

<style>
    
</style>