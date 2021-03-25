<template>
    <div>
        <!-- 
            Change or Edit my Interests btn /me/edit,
            TCSS uses your given interests to serve content do you want to opt-out of TCSS?,
            Advertising Dashboard coming soon
         -->
        <v-form>
             <v-layout column align-center class="pb-5">
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <span style="font-size: 29px;" class="text-capitalize mr-1 font-weight-light grey--text text--darken-4 mt-1">Interests</span>
                </v-flex>
                <v-flex style="width: 100%;">
                    <v-btn @click="$router.push('/me/edit')" depressed class="mx-0" color="primary">Change Interests</v-btn>
                </v-flex>
                
                <!-- <v-flex style="width: 100%" class="mt-4">
                    <span class="subheading grey--text text--darken-2">Learn more about Alias <span  style="cursor: pointer;" class="primary--text" @click="$router.push('/advertise')">here.</span></span>
                </v-flex> -->
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <!-- <v-icon color="alias" class="ml-3 pb-2">help</v-icon> -->
                    </v-layout>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-2">
                    <span style="font-size: 29px;" class="text-capitalize font-weight-light grey--text text--darken-4 mt-1">Sponsored</span>
                </v-flex>
                <v-flex style="width: 100%;">  
                    <v-switch v-model="sponsoredRelevant" color="primary">
                        <template slot="prepend">
                            <span class="grey--text text--darken-2 mt-1 mr-2">Serve sponsored content that's more relevant to me.</span>
                        </template>
                    </v-switch>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <!-- <v-icon color="alias" class="ml-3 pb-2">help</v-icon> -->
                    </v-layout>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <span style="font-size: 29px;" class="text-capitalize font-weight-light grey--text text--darken-4 mt-1">Manage</span>
                </v-flex>
                <v-flex style="width: 100%;">  
                    <span class="grey--text subheading text--darken-2 mt-1">To promote and use ads on Touchbase, check out our <span style="cursor: pointer;" class="primary--text" @click="$router.push('/advertise')">Advertiser Platform.</span></span>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <!-- <v-icon color="alias" class="ml-3 pb-2">help</v-icon> -->
                    </v-layout>
                </v-flex>
            </v-layout>
        </v-form>
    </div>
</template>

<script>
export default {
    name: 'Advertising',
    props: ['settings'],
    data() {
        return {
            sponsoredRelevant: this.settings.sponsoredRelevant,
        }
    },
    watch: {
        sponsoredRelevant() {
            this.$emit('settingsUpdate', { 'sponsoredRelevant': this.sponsoredRelevant })
        },
    },
}
</script>

<style>
    
</style>