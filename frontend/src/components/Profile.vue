<template>
    <!-- <v-layout v-if="notFound" row justify-center align-center fill-height>
        <v-flex class="text-xs-center">
            404, can't find em
        </v-flex>
    </v-layout> -->
    <!-- 404 component -->
    <NotFound v-if="notFound"/>

    <v-layout row fill-height align-center justify-center v-else-if="$apollo.loading && !refetch">
        <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
    </v-layout>

    <v-layout v-else-if="$vuetify.breakpoint.mdAndUp">
        <v-flex xs5>
                
            <v-container class="profile-side">
                <v-layout row justify-space-between>
                    <v-flex>
                        <template v-if="isFollowing">
                            <v-btn @click="unfollow(username)" outline round color="primary" class="mt-0 px-4">
                                <span class="mr-3 ml-1">Unfollow</span>
                                <v-icon>person_add_disabled</v-icon>
                            </v-btn>
                        </template>
                        <template v-else-if="!isFollowing && $username() && username != $username()">
                            <v-btn @click="follow(username)" outline round color="primary" class="mt-0 px-4">
                                <span class="mr-3 ml-1">Follow</span>
                                <v-icon>person_add</v-icon>
                            </v-btn>
                        </template>
                        <v-btn outline icon color="primary" class="mt-0">
                            <v-icon>share</v-icon>
                        </v-btn>
                    </v-flex>
                    <v-flex class="grey--text text-xs-right text--darken-3 subheading text-uppercase">
                        <span>{{ profile.viewCount }} </span> <span class="caption grey--text text--darken-1"> Views</span>
                    </v-flex>
                </v-layout>
                
                <v-layout column align-center>
                    <v-flex class="mt-0 text-xs-center">
                        <v-avatar color="primary" :size="responsiveDimProfPic">
                            <img :src="profile.user.profilePic" alt="">
                        </v-avatar>
                    </v-flex>

                    <v-flex>
                        <div class="mt-3 mb-0">
                            <span v-if="profile.isCompany || profile.isVerified || profile.isBusiness || profile.isCelebrity" class="grey--text pl-5 text--darken-3 title">{{ profile.user.firstName }} {{ profile.user.lastName }}</span>
                            <span v-else class="grey--text text--darken-3 title">{{ profile.user.firstName }} {{ profile.user.lastName }}</span>
                            <v-icon v-if="profile.isVerified" class="mb-1 ml-1" color="success">verified_user</v-icon> 
                            <v-icon v-if="profile.isCompany" class="mb-1" color="grey darken-2">turned_in</v-icon> 
                            <v-icon v-if="profile.isBusiness" class="mb-1" color="grey darken-2">domain</v-icon>
                            <v-icon v-if="profile.isCelebrity" class="mb-1" color="grey darken-2">record_voice_over</v-icon> 
                        </div>
                        <p class="grey--text text-xs-center text--darken-1 subheading mt-1 mb-0">@{{ profile.user.username }}</p>
                    </v-flex>

                    <v-flex class="grey--text text-xs-center mb-3 text--darken-3 subheading text-uppercase">
                        <v-layout class="pt-3" :key="followCountKey" row align-end justify-space-between>
                            <template>
                                <ApolloQuery
                                    
                                    deep
                                    :query="require('@/graphql/queries/followerCount.gql')"
                                    :variables="{ username }"
                                >
                                    <template slot-scope="{ result: { loading, error, data } }">
                                        <template v-if="!loading && data && !error && !(data.followerCount < 0)">
                                            <template v-if="data.followerCount > 0">
                                                <span class="e-title" @click="$router.push(`/${username}/followers`)"><span>{{ data.followerCount }} </span> <span class="caption grey--text text--darken-1"> Followers</span></span>
                                            </template>
                                            <template v-else>
                                                <span>0 </span> <span class="caption grey--text text--darken-1"> Followers</span>
                                            </template>
                                        </template>
                                        <template v-else-if="error">
                                            <span>You broke it: {{ error }}</span>
                                        </template>
                                    </template>
                                </ApolloQuery>
                            </template>
                            
                            <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                            <template>
                                <ApolloQuery
                                    deep
                                    :query="require('@/graphql/queries/followingCount.gql')"
                                    :variables="{ username }"
                                >
                                    <template slot-scope="{ result: { loading, error, data } }">
                                        <template v-if="!loading && data && !error && !(data.followingCount < 0)">
                                            <template v-if="data.followingCount > 0">
                                                <span class="e-title" @click="$router.push(`/${username}/following`)"><span >{{ data.followingCount }} </span> <span class="caption grey--text text--darken-1"> Following</span></span>
                                            </template>
                                            <template v-else>
                                                <span>0 </span> <span class="caption grey--text text--darken-1"> Following</span>
                                            </template>
                                            
                                        </template>
                                        <template v-else-if="error">
                                            <span>You broke it: {{ error }}</span>
                                        </template>
                                    </template>
                                </ApolloQuery>
                            </template>
                        </v-layout>
                        
                    </v-flex>
                    
                    <template v-if="profile.occupation || profile.location || profile.education">
                        <!-- <v-flex class="mt-1 mb-2">
                            <v-divider vertical style="height: 15px;"></v-divider>
                        </v-flex> -->

                        <v-flex class="mb-1 mt-2">
                            <v-layout row justify-center class="text-uppercase grey--text text--darken-2">
                                <template v-if="profile.occupation">
                                    <v-layout column align-center>
                                        <span class="caption grey--text mb-1">Occupation</span>
                                        <span>{{ profile.occupation }}</span>
                                    </v-layout>
                                    
                                    <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                                </template>
                                <template v-if="profile.location">
                                    <v-layout column align-center>
                                        <span class="caption grey--text mb-1">Location</span>
                                        <span>{{ profile.location }}</span>
                                    </v-layout>

                                    <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                                </template>
                                <v-layout v-if="profile.education" column align-center>
                                    <span class="caption grey--text mb-1">Education</span>
                                    <span>{{ profile.education }}</span>
                                </v-layout>
                            </v-layout>
                        </v-flex>

                        <v-flex class="my-1">
                            <v-divider vertical style="height: 15px;"></v-divider>
                        </v-flex>
                    </template>

                    <v-flex class="my-2 text-xs-center">
                        <span class="grey--text caption text-uppercase">Biography</span> <br>
                        <v-card class="bio-box" flat color="transparent">
                            <v-card-text class="text-xs-center font-weight-light pt-1" style="width: 30vw; font-size: 1.25em;">
                                <span>{{ profile.bio }}</span> 
                            </v-card-text>
                        </v-card>
                    </v-flex>

                    <v-flex class="my-1" v-if="profile.website">
                        <v-divider vertical style="height: 15px;"></v-divider>
                    </v-flex>

                    <v-flex class="my-1 text-xs-center" v-if="profile.website">
                        <span class="grey--text caption text-uppercase">Website</span> <br>
                        <a :href="profile.website" style="font-size: 18px;">{{ profile.website }}</a>
                    </v-flex>

                    <v-flex class="my-1" v-if="profile.website">
                        <v-divider vertical style="height: 15px;"></v-divider>
                    </v-flex>

                    <v-flex class="my-1 grey--text text--darken-3 font-weight-light">

                        <v-layout wrap row class="pl-5">
                            <v-flex xs12 class="pl-5">
                                <v-tooltip bottom v-if="profile.contactEmail">
                                    <v-btn outline slot="activator" fab :href="'mailto:' + profile.contactEmail" color="primary"> 
                                        <v-icon>mail</v-icon>
                                    </v-btn>
                                    <span>{{ profile.contactEmail }}</span>
                                </v-tooltip>
                                <span>{{ profile.contactEmail }}</span>
                            </v-flex>
                            
                            <v-flex xs12 class="pl-5">
                                <v-tooltip bottom v-if="profile.contactPhone">
                                    <v-btn outline slot="activator" fab :href="'tel:' + this.profile.contactPhone" color="primary"> 
                                        <v-icon>phone</v-icon>
                                    </v-btn>
                                    <span>{{ profile.contactPhone }}</span>
                                </v-tooltip>
                                <span>{{ profile.contactPhone }}</span>
                            </v-flex>
                        </v-layout>
                        
                    </v-flex>
                    
                </v-layout>
            </v-container>     
            
            <!-- <div class="me-footer">
                <v-divider></v-divider>
                <v-layout align-center justify-center style="height: 99%;">
                    <v-flex xs8>
                    <v-card flat color="#EEEEEE">
                        <v-card-text class="text-xs-center">
                            <v-layout align-start justify-space-around row fill-height>
                                <v-flex>
                                    <span class="font-weight-bold">Followers</span>  <br>
                                    <span>354</span>
                                </v-flex>

                                <v-flex>
                                    <v-divider class="ffv-divs" inset vertical></v-divider>
                                </v-flex>

                                <v-flex>
                                    <span class="font-weight-bold">Following</span> <br>
                                    <span>423</span>
                                </v-flex>

                                <v-flex>
                                    <v-divider class="ffv-divs" inset vertical></v-divider>
                                </v-flex>
                                
                                <v-flex>
                                    <span class="font-weight-bold">Views</span> <br>
                                    <span>1.6k</span>
                                </v-flex>
                            </v-layout>
                            
                        </v-card-text>
                    </v-card>
                    </v-flex>

                    <v-flex xs4>
                        <v-layout wrap>
                            <v-flex xs12 sm6 class="text-xs-center">
                                <v-btn color="primary" @click="test">Follow</v-btn>
                            </v-flex>

                            <v-flex xs12 sm6>
                                <v-btn color="primary" @click="test">Stuff</v-btn>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    
                    

                </v-layout>
            </div>     -->
            
        </v-flex>
        
        <v-divider vertical class="full-height-nme"></v-divider>

        <v-flex xs7>
            <v-tabs grow v-model="tabs" class="mt-2">
                <v-tabs-slider color="primary"></v-tabs-slider>
                <v-tab class="grey--text">
                    <span style="font-size: 20px;" class="font-weight-light">Accounts</span>
                </v-tab>
                <v-divider vertical></v-divider>
                <v-tab class="grey--text">
                    <span style="font-size: 20px;" class="font-weight-light">Gallery</span>
                </v-tab>
                <!-- <v-tab class="grey--text">
                    <span class="headline font-weight-regular text-uppercase">Something</span>
                </v-tab> -->
            </v-tabs>
            <v-divider></v-divider>

            <v-tabs-items
                mandatory
                v-model="tabs"
            >
                <v-tab-item class="home-div">
                    <template v-if="accounts.length > 0">
                        <v-container fluid class="ac-accounts-scroll">

                            <v-expansion-panel popout v-if="!grid">
                                <v-expansion-panel-content
                                    v-for="account in accounts" :key="account.service"
                                    expand-icon="arrow_drop_down"
                                >
                                    <div slot="header">
                                        <v-layout align-center justify-space-around row fill-height>
                                            <v-avatar :size="responsiveDimSize" class="mr-4"><img :src="$store.state.logoList[account.service]" alt=""></v-avatar>
                                            <span class="text-capitalize">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                            <template v-if="account.service.substring(0, account.service.indexOf('.')) === 'youtube'"></template>
                                            <template v-else>
                                                <v-icon class="mx-4">compare_arrows</v-icon>
                                                <span>@{{ account.identifier }}</span>
                                            </template>
                                            <v-spacer></v-spacer>
                                            <v-btn flat :href="account.url" icon color="primary" class="mr-4 hidden-sm-and-down">
                                                <v-icon size="32">exit_to_app</v-icon>
                                            </v-btn>
                                        </v-layout>
                                        
                                    </div>
                                    <v-card>
                                        <v-card-text class="grey lighten-4">
                                            <v-layout align-center justify-space-between row fill-height>
                                                <span class="ml-2">Linked {{ account.created }}</span>
                                                <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                                            </v-layout>
                                        </v-card-text>
                                        <v-divider></v-divider>
                                        <v-card-actions class="pa-3">
                                            <v-btn @click="openProfile(account.url)" round outline color="primary">Go To Profile</v-btn>
                                        </v-card-actions>
                                    </v-card>

                                </v-expansion-panel-content>
                            </v-expansion-panel>

                            <v-container class=" ac-accounts-grid pa-0 ma-0" fluid grid-list-sm v-else>
                                <v-layout row wrap>
                                    <v-flex v-for="account in accounts" class="mt-2 mb-5" :key="account.service" md6 lg4>
                                        <v-layout justify-center align-center column>
                                            <v-dialog flat :v-model="account.dialog" max-width="450">
                                                <template slot="activator">
                                                    <v-img :src="$store.state.logoList[account.service]" color="primary" :alt="account.service" :width="responsiveDim" :height="responsiveDim" ></v-img>
                                                </template>

                                                <v-card flat style="border-radius: 30px;">
                                                    <v-card-title class="text-capitalize title">
                                                        <img :src="$store.state.logoList[account.service]" alt="lorem" width="70" height="70">
                                                        <span class="ml-4">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                                    </v-card-title>
                                                    <v-card-text>
                                                        <v-layout wrap align-center justify-space-between row fill-height>
                                                            <span class="ml-2">Linked {{ account.created }}</span>
                                                            <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                                                        </v-layout>
                                                    </v-card-text>
                                                    <v-divider></v-divider>
                                                    <v-card-actions class="pa-3">
                                                        <v-btn @click="account.dialog=false; openProfile(account.url)" round outline color="primary">Go To Profile</v-btn>
                                                        <!-- <v-spacer></v-spacer>
                                                        <v-btn v-if="!account.remove" @click="account.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">remove</span><v-icon>delete</v-icon></v-btn>
                                                        <v-btn v-else-if="account.remove && !account.confirmedRemove" @click="account.confirmedRemove=true; removeAccount(account.service)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">Confirm?</span><v-icon>check</v-icon></v-btn>
                                                        <span class="success--text" v-if="account.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->
                                                    </v-card-actions>                              
                                                </v-card>
                                                
                                            </v-dialog>
                                            <v-badge class="mt-2 mr-1" right color="transparent">
                                                <span class="text-capitalize title font-weight-light grey--text text--darken-3">
                                                    {{ account.service.substring(0, account.service.indexOf('.')) }}
                                                </span>
                                                <v-icon @click="openProfile(account.url)" slot="badge" color="primary">open_in_new</v-icon>
                                            </v-badge>
                                        </v-layout>
                                        
                                    </v-flex>
                                </v-layout>
                            </v-container>

                        </v-container>
                        <v-btn 
                            v-if="!grid" color="primary"
                            @click="grid = !grid"
                            fab fixed
                            bottom right
                            class="mr-2"
                            style="margin-bottom: 5vh;"
                        >
                            <v-icon>dashboard</v-icon>
                        </v-btn>

                        <v-btn 
                            v-else color="primary"
                            @click="grid = !grid"
                            fab fixed
                            bottom right
                            class="mr-2"
                            style="margin-bottom: 5vh;"
                        >
                            <v-icon>list</v-icon>
                        </v-btn>
                    </template>
                    

                    <v-layout v-else row style="height: calc(100vh - 116px);" justify-center align-center>
                        <v-flex class="text-xs-center">
                            <v-icon color="grey lighten-1" class="mb-3" size="70">perm_identity</v-icon> <br/>
                            <!-- <v-icon color="grey lighten-1" class="mb-3" size="50">hourglass_empy</v-icon> <br/> -->
                            <span class="display-1 font-weight-light grey--text text--lighten-1">{{ profile.user.firstName }} has no accounts linked!</span>
                        </v-flex>
                    </v-layout>
                </v-tab-item>

                <v-tab-item class="home-div">
                    <v-layout row style="height: calc(100vh - 114px);" justify-center align-center>
                        <v-flex class="text-xs-center">
                            <v-icon color="grey lighten-1" class="mb-3" size="70">timer</v-icon> <br/>
                            <span class="display-3 font-weight-light grey--text text--lighten-1">Coming Soon!</span>
                        </v-flex>
                    </v-layout>
                </v-tab-item>
            </v-tabs-items>
            
        </v-flex>
    </v-layout>

    <div v-else class="home-div" style="overflow-y: auto;">
        <v-layout style="height: calc(calc(100vh / 12) * 8);" column align-center>
            <v-flex xs5 style="width: 100%;">
                <v-layout fill-height row class="pt-2 pb-1">
                    <v-flex xs4>
                        <v-layout row wrap fill-height align-content-space-between>
                            <v-flex xs12 class="mt-3">
                                <v-layout row justify-center>
                                    <v-avatar color="primary" :size="responsiveDimProfPic">
                                        <img :src="profile.user.profilePic" alt="">
                                    </v-avatar>
                                </v-layout>
                            </v-flex> 
                            <v-flex xs12 class="mb-2 grey--text text-xs-center text--darken-3 subheading text-uppercase">
                                <span>{{ profile.viewCount }} </span> <span class="caption grey--text text--darken-1"> Views</span>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <v-flex xs8>
                        <v-layout fill-height align-center column>
                            <v-flex class="pt-2">
                                <!-- <span v-if="profile.isCompany || profile.isVerified || profile.isBusiness || profile.isCelebrity" class="grey--text text--darken-3 title">{{ profile.user.firstName }} {{ profile.user.lastName }}</span> -->
                                <span class="grey--text pr-1 text--darken-3 title">{{ profile.user.firstName }} {{ profile.user.lastName }}</span>
                                <!-- #fbca09 check_circle -->
                                <v-icon v-if="profile.isVerified" class="mb-1" color="success">verified_user</v-icon> 
                                <v-icon v-if="profile.isCompany" class="mb-1" color="grey darken-2">turned_in</v-icon> 
                                <v-icon v-if="profile.isBusiness" class="mb-1" color="grey darken-2">domain</v-icon>
                                <v-icon v-if="profile.isCelebrity" class="mb-1" color="grey darken-2">record_voice_over</v-icon> 
                            </v-flex>
                            <v-flex>
                                <span class="grey--text text-xs-center text--darken-1 subheading pr-2">@{{ profile.user.username }}</span>
                            </v-flex>
                            <v-flex class="mt-1 grey--text text-xs-center text--darken-3 subheading">
                                <!-- <v-layout row fill-height justify-center align-end>
                                    <v-flex class="mr-1">
                                        <v-btn class="mx-1" outline round small block color="primary">
                                            <span>Follow</span>
                                        </v-btn>
                                    </v-flex>
                                    <v-flex class="ml-1">
                                        <v-btn class="mx-1" outline round small block color="primary">
                                            <span>Share</span>
                                        </v-btn>
                                    </v-flex>
                                </v-layout> -->
                                <v-layout row fill-height justify-space-between align-end>
                                    <v-flex xs9>
                                        <template v-if="isFollowing">
                                            <v-btn @click="unfollow(username)" outline round small block color="primary">
                                                <span class="mx-5">Unfollow</span>
                                            </v-btn>
                                        </template>
                                        <template v-else-if="!isFollowing && $username() && username != $username()">
                                            <v-btn @click="follow(username)" outline round small block color="primary">
                                                <span class="mx-5">Follow</span>
                                            </v-btn>
                                        </template>
                                    </v-flex>
                                    <v-flex xs3>
                                        <v-btn outline icon small color="primary">
                                            <v-icon small>share</v-icon>
                                        </v-btn>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                            <v-flex class="grey--text text-xs-center text--darken-3 subheading text-uppercase">
                                <v-layout class="pt-3" :key="followCountKey" row align-end justify-space-between>
                                    <template>
                                        <ApolloQuery
                                            deep
                                            :query="require('@/graphql/queries/followerCount.gql')"
                                            :variables="{ username }"
                                        >
                                            <template slot-scope="{ result: { loading, error, data } }">
                                                <template v-if="!loading && data && !error && !(data.followerCount < 0)">
                                                    <template v-if="data.followerCount > 0">
                                                        <span class="e-title" @click="$router.push(`/${username}/followers`)"><span>{{ data.followerCount }} </span> <span class="caption grey--text text--darken-1"> Followers</span></span>
                                                    </template>
                                                    <template v-else>
                                                        <span>0 </span> <span class="caption grey--text text--darken-1"> Followers</span>
                                                    </template>
                                                </template>
                                                <template v-else-if="error">
                                                    <span>You broke it: {{ error }}</span>
                                                </template>
                                            </template>
                                        </ApolloQuery>
                                    </template>
                                    
                                    <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                                    <template>
                                        <ApolloQuery
                                            deep
                                            :query="require('@/graphql/queries/followingCount.gql')"
                                            :variables="{ username }"
                                        >
                                            <template slot-scope="{ result: { loading, error, data } }">
                                                <template v-if="!loading && data && !error && !(data.followingCount < 0)">
                                                    <template v-if="data.followingCount > 0">
                                                        <span class="e-title" @click="$router.push(`/${username}/following`)"><span >{{ data.followingCount }} </span> <span class="caption grey--text text--darken-1"> Following</span></span>
                                                    </template>
                                                    <template v-else>
                                                        <span>0 </span> <span class="caption grey--text text--darken-1"> Following</span>
                                                    </template>
                                                    
                                                </template>
                                                <template v-else-if="error">
                                                    <span>You broke it: {{ error }}</span>
                                                </template>
                                            </template>
                                        </ApolloQuery>
                                    </template>
                                </v-layout>
                                
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-layout>
            </v-flex>

            <v-flex xs7 style="width: 100%;">
                <v-divider></v-divider>
                <v-layout column fill-height align-center class="pt-3">
                    <v-flex v-if="profile.occupation || profile.location || profile.education">
                        <v-layout row justify-center class="mt-1 text-uppercase grey--text text--darken-2">
                            <template v-if="profile.occupation">
                                <v-layout column align-center>
                                    <span class="caption grey--text mb-1">Occupation</span>
                                    <span>{{ profile.occupation }}</span>
                                </v-layout>
                                
                                <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                            </template>
                            <template v-if="profile.location">
                                <v-layout column align-center>
                                    <span class="caption grey--text mb-1">Location</span>
                                    <span>{{ profile.location }}</span>
                                </v-layout>

                                <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                            </template>
                            <v-layout v-if="profile.education" column align-center>
                                <span class="caption grey--text mb-1">Education</span>
                                <span>{{ profile.education }}</span>
                            </v-layout>
                        </v-layout>
                    </v-flex>
                    <!-- <v-flex class="grey--text caption text-uppercase">
                        <span>occupation</span>
                        <span class="mx-4">location</span>
                        <span>education</span>
                    </v-flex> -->

                    <v-flex class="text-xs-center">
                        <span class="grey--text caption text-uppercase">Biography</span> <br>
                        <v-card class="bio-box" flat color="transparent">
                            <v-card-text class="text-xs-center font-weight-light pt-1" style="width: 80vw; font-size: 1.25em;">
                                <span>{{ profile.bio }}</span> 
                            </v-card-text>
                        </v-card>
                    </v-flex>

                    <v-flex v-if="profile.website || profile.contactEmail || profile.contactPhone">
                        <template v-if="profile.contactEmail">
                            <v-btn class="mb-0" large flat slot="activator" icon :href="'mailto:' + profile.contactEmail" color="primary"> 
                                <v-icon>mail</v-icon>
                            </v-btn>
                            <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                        </template>
                        <template v-if="profile.website">
                            <v-btn :href="profile.website" flat color="primary">
                                <v-icon>link</v-icon>
                                <!-- <span>Website</span> -->
                            </v-btn>
                            <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                        </template>
                        <v-btn v-if="profile.contactPhone" class="mt-0" flat large slot="activator" icon :href="'tel:' + this.profile.contactPhone" color="primary"> 
                            <v-icon>phone</v-icon>
                        </v-btn>
                    </v-flex>

                    <!-- <v-flex class="text-xs-center" v-if="profile.website">
                        <span class="grey--text caption text-uppercase">Website</span> <br>
                        <a :href="profile.website" style="font-size: 18px;">{{ profile.website }}</a>
                    </v-flex>

                    <v-flex style="max-height: 100px;" class="mt-2">
                        <v-layout row fill-height justify-space-around align-center>
                            <v-flex xs5 style="white-space: nowrap; text-overflow: ellipsis;" v-if="profile.contactEmail" class="font-weight-light">
                                <v-btn class="mb-0" large flat slot="activator" icon :href="'mailto:' + profile.contactEmail" color="primary"> 
                                    <v-icon>mail</v-icon>
                                </v-btn>
                                <span>{{ profile.contactEmail }}</span>
                            </v-flex>
                            
                            <v-flex xs5 style="white-space: nowrap; text-overflow: ellipsis;" v-if="profile.contactPhone" class="font-weight-light">
                                <v-btn class="mt-0" flat large slot="activator" icon :href="'tel:' + this.profile.contactPhone" color="primary"> 
                                    <v-icon>phone</v-icon>
                                </v-btn>
                                <span>{{ profile.contactPhone }}</span>
                            </v-flex>
                        </v-layout>
                        
                    </v-flex> -->
                </v-layout>
            </v-flex>
            
        </v-layout>
        <v-divider></v-divider>
        <p class="grey--text caption text-xs-center text-uppercase mt-3">Accounts</p>
        
        <v-container fluid>
            <v-expansion-panel popout v-if="!grid">
                <v-expansion-panel-content
                    v-for="account in accounts" :key="account.service"
                    expand-icon="arrow_drop_down"
                >
                    <div slot="header">
                        <v-layout align-center justify-space-around row fill-height>
                            <v-avatar :size="responsiveDimSize" class="mr-4"><img :src="$store.state.logoList[account.service]" alt=""></v-avatar>
                            <span class="text-capitalize">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                            <template v-if="account.service.substring(0, account.service.indexOf('.')) === 'youtube'"></template>
                            <template v-else>
                                <v-icon class="mx-4">compare_arrows</v-icon>
                                <span>@{{ account.identifier }}</span>
                            </template>
                            <v-spacer></v-spacer>
                            <v-btn flat :href="account.url" icon color="primary" class="mr-4 hidden-sm-and-down">
                                <v-icon size="32">exit_to_app</v-icon>
                            </v-btn>
                        </v-layout>
                        
                    </div>
                    <v-card>
                        <v-card-text class="grey lighten-4">
                            <v-layout align-center justify-space-between row fill-height>
                                <span class="ml-2">Linked {{ account.created }}</span>
                                <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                            </v-layout>
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions class="pa-3">
                            <v-btn @click="openProfile(account.url)" round outline color="primary">Go To Profile</v-btn>
                        </v-card-actions>
                    </v-card>

                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-container class="ac-accounts-grid pa-0 ma-0" fluid grid-list-sm v-else>
                <v-layout row wrap >
                    <v-flex v-for="account in accounts" class="mt-2 mb-5" :key="account.service" xs6>
                        <v-layout justify-center align-center column>
                            <v-dialog flat :v-model="account.dialog" max-width="450">
                                <template slot="activator">
                                    <v-img :src="$store.state.logoList[account.service]" color="primary" :alt="account.service" :width="responsiveDim" :height="responsiveDim" ></v-img>
                                </template>

                                <v-card flat style="border-radius: 30px;">
                                    <v-card-title class="text-capitalize title">
                                        <img :src="$store.state.logoList[account.service]" alt="lorem" width="70" height="70">
                                        <span class="ml-4">{{ account.service.substring(0, account.service.indexOf('.')) }}</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-layout wrap align-center justify-space-between row fill-height>
                                            <span class="ml-2">Linked {{ account.created }}</span>
                                            <span class="mr-2">Full URL: <a :href="account.url" class="ml-2">{{ account.url }}</a></span>
                                        </v-layout>
                                    </v-card-text>
                                    <v-divider></v-divider>
                                    <v-card-actions class="pa-3">
                                        <v-btn @click="account.dialog=false; openProfile(account.url)" round outline color="primary">Go To Profile</v-btn>
                                        <!-- <v-spacer></v-spacer>
                                        <v-btn v-if="!account.remove" @click="account.remove=true" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">remove</span><v-icon>delete</v-icon></v-btn>
                                        <v-btn v-else-if="account.remove && !account.confirmedRemove" @click="account.confirmedRemove=true; removeAccount(account.service)" flat color="primary" class="text-capitalize font-weight-regular"><span class="mr-1">Confirm?</span><v-icon>check</v-icon></v-btn>
                                        <span class="success--text" v-if="account.confirmedRemove">Done <v-icon class="ml-2" color="success">check</v-icon></span> -->
                                    </v-card-actions>                              
                                </v-card>
                                
                            </v-dialog>
                            <v-badge class="mt-2 mr-1" right color="transparent">
                                <span class="text-capitalize title font-weight-light grey--text text--darken-3">
                                    {{ account.service.substring(0, account.service.indexOf('.')) }}
                                </span>
                                <v-icon @click="openProfile(account.url)" slot="badge" color="primary">open_in_new</v-icon>
                            </v-badge>
                        </v-layout>
                        
                    </v-flex>
                </v-layout>
            </v-container>
        </v-container>

        <v-btn 
            v-if="!grid" color="primary"
            @click="grid = !grid"
            fab fixed
            bottom right
            class="mr-2"
            style="margin-bottom: 50px;"
        >
            <v-icon>dashboard</v-icon>
        </v-btn>

        <v-btn 
            v-else color="primary"
            @click="grid = !grid"
            fab fixed
            bottom right
            class="mr-2"
            style="margin-bottom: 50px;"
        >
            <v-icon>list</v-icon>
        </v-btn>
    </div>
</template>


<script>
import moment from 'moment'
import NotFound from '@/components/NotFound'

import { PUBLIC_PROFILE_QUERY } from '@/graphql/queries/publicProfile'
import { PUBLIC_ACCOUNTS_QUERY } from '@/graphql/queries/publicAccounts'

import { FOLLOW_USER_MUTATION } from '@/graphql/mutations/follow'
import { UNFOLLOW_USER_MUTATION } from '@/graphql/mutations/unfollow'
import { IS_FOLLOWING_QUERY } from '@/graphql/queries/isFollowing'

 export default {
     name: 'Profile',
     //props: ['username'],
     components: {
        NotFound
     },
     data() {
        return {
            profile: {},
            tabs: 0,
            accounts: [],
            followCountKey: 0,
            refetch: false,
            isFollowing: null,
            dialog: false,
            loading: 0,
            grid: true,
            notFound: false,
        }
    },
     methods: {
        openProfile(url) {
            window.open(url)
        },
        follow(usernameFollowee) {
            this.$apollo.mutate({
                mutation: FOLLOW_USER_MUTATION,
                variables: {
                    usernameFollowee
                }
            }).then(result => {
                if (result.data.follow) {
                    if (result.data.follow.success) {
                        this.refetch = true
                        this.$apollo.queries.isFollowing.refetch().then(() => {
                            this.followCountKey++
                            this.refetch = false
                        })
                    } else {
                        alert("Error - Could not follow user. \n FYI - You cannot follow yourself.")
                    }
                }
            }).catch(err => {
                this.feedback = true
                // this.loading = false
            })
        },
        unfollow(usernameFollowee) {
            this.$apollo.mutate({
                mutation: UNFOLLOW_USER_MUTATION,
                variables: {
                    usernameFollowee
                }
            }).then(result => {
                if (result.data.unfollow) {
                    if (result.data.unfollow.success) {
                        this.refetch = true
                        this.$apollo.queries.isFollowing.refetch().then(() => {
                            this.followCountKey++
                            this.refetch = false
                        })
                    } else {
                        alert('Error - Could not unfollow user')
                    }
                }
            }).catch(err => {
                console.log(err)
                this.feedback = true
                // this.loading = false
            })
        },
     },
     computed: {
        username() {
            return this.$route.path.replace(/\//g,'')
        },
        responsiveDim() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 80
                case 'sm': return 95
                case 'md': return 90
                case 'lg': return 105
                case 'xl': return 120
            }
        },
        responsiveDimSize() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 35
                case 'sm': return 40
                case 'md': return 45
                case 'lg': return 50
                case 'xl': return 55
            }
        },
        responsiveDimProfPic() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 90
                case 'sm': return 110
                case 'md': return 120
                case 'lg': return 135
                case 'xl': return 150
            }
        },
    },
    apollo: {
        profile: {
            query: PUBLIC_PROFILE_QUERY,
            variables() {
                return {
                    username: this.username
                }
            },
            error() {
                this.notFound = true
            }
        },
        theAccounts: {
            query: PUBLIC_ACCOUNTS_QUERY,
            variables() {
                return {
                    username: this.username
                }
            },
            update({ data }) {
                if (data.accounts) {
                    data.accounts.forEach(account => {
                        if (account.service === 'steamcommunity.com') account.service = 'steam.com'
                        account.created = moment(account.created).fromNow(),
                        account.dialog = false
                    })
                } else {
                    alert('Something went wrong. Please try again later! ⏳')
                }
                return data.accounts
            }
        },
        isFollowing: {
            query: IS_FOLLOWING_QUERY,
            variables() {
                return {
                    // username follower, username followee
                    unFollower: this.$username(),
                    unFollowee: this.username,
                }
            }
        }
    },
}
</script>

<style>
.full-height-nme {
    height: calc(100vh - 58px);
}
</style>
 