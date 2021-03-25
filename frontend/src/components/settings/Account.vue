<template>
    <div>
        <!-- 
            Will have account type, verification status 
            (verified email and same verified v-chip from EditProfile),
            Reset Email, manage your links btn, to="/links"
         -->
        <v-form>
             <v-layout column align-center class="pb-5">
                <v-flex style="width: 100%;" class="mt-4 mb-4">
                    <!-- <v-badge right color="transparent">
                        <span style="font-size: 29px;" class="text-capitalize mr-1 font-weight-light grey--text text--darken-3 mt-1">Alias Account</span>
                        <v-avatar size="100%" slot="badge" class="mt-1"><img src="/img/alias.png"></img></v-avatar>
                    </v-badge> -->
                    <v-layout row align-center>
                        <span style="font-size: 29px;" class="text-capitalize mr-1 font-weight-light grey--text text--darken-4 mt-1">Alias Account</span>
                        <v-avatar size="37" class="ml-2 mt-1"><img src="/img/alias.png"></img></v-avatar>
                    </v-layout>
                    
                </v-flex>
                <v-flex style="width: 100%;">
                    <a href="https://alias.ac/dashboard" class="alias--text title font-weight-regular">Alias Dashboard</a>
                </v-flex>
                
                <v-flex style="width: 100%" class="mt-4">
                    <span class="subheading grey--text text--darken-2" style="cursor: pointer;">Learn more about Alias <span class="alias--text" @click="$router.push('/advertise')">here.</span></span>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <!-- <v-icon color="alias" class="ml-3 pb-2">help</v-icon> -->
                    </v-layout>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <span style="font-size: 29px;" class="text-capitalize font-weight-light grey--text text--darken-4 mt-1">Account Type</span>
                </v-flex>
                <v-flex style="width: 100%;">
                    <v-layout row justify-center align-center style="max-width: 600px;">
                        <!-- :depressed and :outline, the current account type has outline false and depressed true -->
                        <v-flex xs4>
                            <v-btn :outline="accountType != 'p'" :depressed="accountType === 'p'" round color="primary" @click="accountType = 'p'">Personal</v-btn>
                        </v-flex>
                        <v-flex xs4>
                            <v-btn :outline="accountType != 'b'" :depressed="accountType === 'b'" round color="primary" @click="haspBusiness ? accountType = 'b' : $router.push('/plans/business')">Business</v-btn>
                        </v-flex>
                        <v-flex xs4>
                            <!-- NOTE: change celeb to actual term -->
                            <v-btn :outline="accountType != 'c'" :depressed="accountType === 'c'" round color="primary" @click="haspCeleb ? accountType = 'c' : $router.push('/plans/celeb')">Celebrity</v-btn>
                        </v-flex>
                    </v-layout>
                </v-flex>
                
                <v-flex style="width: 100%" class="mt-5 ml-3">
                    <span class="subheading grey--text text--darken-2" >Learn more about account types <span style="cursor: pointer;" class="primary--text" @click="$router.push('/advertise')">here.</span></span>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <!-- <v-icon color="alias" class="ml-3 pb-2">help</v-icon> -->
                    </v-layout>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-4">
                    <span style="font-size: 29px;" class="text-capitalize font-weight-light grey--text text--darken-4 mt-1">Verification</span>
                </v-flex>
                <v-flex style="width: 100%;">
                    <v-layout row align-center wrap>
                        <span class="title font-weight-light grey--text text--darken-3 mb-2 mr-3">Email:</span>
                        <v-flex xs12 lg5 class="mb-2">
                            <v-text-field
                                outline
                                placeholder="memes@gmail.com"
                                disabled
                                class="mr-3"
                                single-line
                                hide-details
                                :append-icon="`${verifiedEmail ? 'check_circle_outline' : ''}`"
                                prepend-inner-icon="mail"
                            ></v-text-field>
                        </v-flex>
                        
                        <v-flex xs12 lg4 class="mb-2">
                            <v-layout row>
                                <v-btn class="ml-0" large color="primary">
                                    <!-- <span class="subheading font-weight-medium">Reset</span> -->
                                    Reset
                                </v-btn>
                                <v-btn large v-if="verifiedEmail" color="success darken-1">
                                    <span class="mr-2">Verified</span>
                                    <v-icon>check_circle_outline</v-icon>
                                </v-btn>
                                <v-btn large v-else color="success darken-1">
                                    <span class="mr-2">Verify</span>
                                    <v-icon>check_circle_outline</v-icon>
                                </v-btn>
                            </v-layout>
                        </v-flex>
                    </v-layout>
                </v-flex>
                
                <!-- <v-flex style="width: 100%" class="mt-5 ml-3">
                    <span class="subheading grey--text text--darken-2"><span class="ogSuccess--text">Verify</span> your email to finish setting up Touchbase.</span>
                </v-flex> -->
                <v-flex style="width: 100%" class="mt-5 ml-2">
                    <span class="title font-weight-light grey--text text--darken-3">Account: Unverified</span>
                </v-flex>
                <v-flex class="my-3" style="width: 100%;">
                    <v-chip style="width: 50%; min-width: 420px;" text-color="white" class="verified-chip elevation-2 subheading" color="aliasAcc" @click="$router.push('/plans/verified')">
                        <v-avatar
                            color="white"
                        >
                            <img style="height: 40px; width: 40px;" src="/img/avatar-2.png" alt="profile picture">
                        </v-avatar>
                        
                        <!-- <span class="ml-2">Memes Exdee</span> -->
                        <!-- <v-icon class="mr-2">close</v-icon> -->
                        <div style="position: absolute; left: 34%;">
                            <span class="mr-2">Get the Verified Tag</span>
                            <v-icon>verified_user</v-icon>
                        </div>
                        
                        <!-- <v-icon class="mr-3" style="position: absolute; right: 0;">exit_to_app</v-icon> -->
                    </v-chip>
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
    // NOTE: $EMIT BEFORE COMPONENT DESTROY AND ON SAVE BUTTON CLICK SO THAT SETTINGS.VUE
    // CAN HANDLE ALL THE DATA AND APOLLO STUFF IN ONE PLACE, MEANING ONE GLOBAL SAVE BUTTON!!!
    name: 'Account',
    props: ['settings'],
    data() {
        return {
            accountType: this.settings.accountType.toLowerCase(),
            haspBusiness: this.settings.haspBusiness, //
            haspCeleb: this.settings.haspCelebrity, //
            verifiedEmail: false, //
        }
    },
    watch: {
        accountType() {
            this.$emit('settingsUpdate', { 'accountType': this.accountType })
        },
    },
}
</script>

<style>
    
</style>