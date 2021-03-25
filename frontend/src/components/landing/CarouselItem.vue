<template>
    <div class="home-div" style="min-width: 100vw;">

        <!-- <v-layout align-right fill-height justify-end class="hidden-sm-and-down">
                <v-btn flat round id="login" to='/login' class="font-weight-bold mt-5 mr-5">login</v-btn>
        </v-layout> -->

        <!-- <v-layout align-right fill-height justify-end class="hidden-md-and-up">
                <v-btn flat round id="login" to='/login' class="font-weight-bold">login</v-btn>
        </v-layout> -->

        <!-- <v-container fluid class="hidden-sm-and-down hidden-md-only">
            <v-layout justify-space-around align-center>
                <v-flex lg1 class="ml-5 pl-2">
                    <v-img src="/img/logo_home.png" alt="logo" height="90px" width="90px" class="mt-5"></v-img>
                </v-flex>
            </v-layout>
        </v-container>

        <v-container fluid class="hidden-md-and-up">
            <v-layout align-center fill-height justify-center>
                <v-flex xs6 offset-xs2 class="">
                    <v-img src="/img/logo_home.png" alt="logo" height="90px" width="90px" class="mt-5"></v-img>
                </v-flex>
            </v-layout>
        </v-container>

        <v-container fluid class="hidden-sm-and-down hidden-lg-and-up">
            <v-layout align-center fill-height justify-center>
                <v-flex xs3 offset-xs2 class="">
                    <v-img src="/img/logo_home.png" alt="logo" height="90px" width="90px" class="mt-5"></v-img>
                </v-flex>
            </v-layout>
        </v-container> -->

        <v-layout align-center column style="margin-top: 10vh; background-color: red;" justify-center>
            <v-img src="/img/logo_home.png" alt="logo" height="120px" width="120px"></v-img>
            <div class="white--text mb-5 mt-4">
                <v-layout row>
                    
                    <p class="display-4 font-weight-medium text-xs-center">Touchbase</p>
                </v-layout>
                
                <p class="display-1 mt-4 font-weight-light text-xs-center">The Online Rolodex</p>
                <v-layout justify-space-around>
                    <p class="font-weight-light text-uppercase font-weight-black title text-xs-center">Available on
                        <img class="ml-2" src="/img/icon_apple.png" alt="">
                        <img class="ml-2" src="/img/icon_android.png" alt="">
                        <img class="ml-2 mr-2" src="/img/icon_windows.png" alt="">
                        For free, forever
                    </p>
                </v-layout>
                <v-layout justify-center align-center :class="{'mt-5': true, 'mt-3': $vuetify.breakpoint.mdAndUp}">
                    <v-btn color="primary" raised to='/signup' class="landing-btn elevation-3 mx-4">Signup</v-btn>
                    <v-btn color="primary" rasied outline to='/login' class="landing-btn elevation-3 mx-4">Login</v-btn>
                </v-layout>
            </div>

            <v-layout align-center fill-height wrap justify-center :class="{'hidden-sm-and-down': true, 'mt-5': $vuetify.breakpoint.lgAndUp, 'mt-3': $vuetify.breakpoint.mdOnly}">
                <v-flex xs12 md3>
                    <v-card flat color="transparent">
                        <v-card-title class="white--text" primary-title>
                            <div class="text-xs-center">
                                <v-layout align-center fill-height justify-center class="mb-2">
                                    <v-icon color="white" large>people</v-icon>
                                </v-layout>
                                <p class="headline text-capitalize mb-2">Social Networks</p>
                                <p class="subheading">Keep and manage all your social media accounts in one profile.</p>
                            </div>
                        </v-card-title>
                    </v-card>
                </v-flex>

                <v-flex xs12 md3 class="ml-4">
                    <v-card flat color="transparent">
                        <v-card-title class="white--text" primary-title>
                            <div class="text-xs-center">
                                <v-layout align-center fill-height justify-center class="mb-2">
                                    <v-icon color="white" large>link</v-icon>
                                </v-layout>
                                <p class="headline mb-2">Tou.sh Links</p>
                                <p class="subheading">Create links to your profile that change how people interact with you.</p>
                            </div>
                        </v-card-title>
                    </v-card>
                </v-flex>

                <v-flex xs12 md3 class="ml-4">
                    <v-card flat color="transparent">
                        <v-card-title class="white--text" primary-title>
                            <div class="text-xs-center">
                                <v-layout align-center fill-height justify-center class="mb-2">
                                    <v-icon color="white" large>highlight</v-icon>
                                </v-layout>
                                <p class="headline text-capitalize mb-2">Highlights</p>
                                <p class="subheading">Grab a snapshot of someone's day with Touchbase Highlights.</p>
                            </div>
                        </v-card-title>
                    </v-card>
                </v-flex>
            </v-layout>


        </v-layout>

    </div>
</template>

<script>
export default {

}
</script>

<style lang="css" scoped>
    #title {
        color: white;
        opacity: 0.5;
    }
    >>>.display-2 {
        opacity: 0.7;
    }
    /* >>>.v-btn {
        background-color: #8E24AA!important;
    } */
    img {
        width: 1.25rem;
    }
    #login {
        opacity: 0.7;
        background-color: transparent!important;
    }
    #login >>>.v-btn__content:hover {
        color: #2196f3;
    }
    .v-btn:hover:before{
        background-color: transparent!important;
    }

    @media screen and (max-width: 960px) {
        >>>.title {
            font-size: 28px!important;
        }
    }

.landing-btn {
    height: 50px;
    width: 150px;
    border-radius: 8px;
    font-size: 1.25rem;
    letter-spacing: 2px;
}

</style>
