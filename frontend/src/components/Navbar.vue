<template>
    <div>
        <v-navigation-drawer disable-resize-watcher mobile-break-point=15000 app v-model="sideNav" width=400>
            <v-layout column align-center>
                <v-flex style="width: 100%;">
                    <v-btn @click="sideNav = false" flat block color="primary">
                        <v-spacer></v-spacer>
                        <span class="primary--text text-uppercase">Close</span>
                        <v-icon class="mx-2">close</v-icon>
                    </v-btn>
                </v-flex>
                <v-flex>
                    <v-avatar color="primary" size="100">
                        <img src="/img/avatar-2.png" alt="">
                    </v-avatar>
                    <p class="text-xs-center subheading mt-1">Username</p>
                </v-flex>
            </v-layout>
            <v-tabs grow mobile-break-point=1 optional slider-color="primaryComp" icons-and-text v-model="tab" color="white" dark>
                <v-tab to="/" class="primary--text">
                    <span class="title font-weight-regular text-capitalize">Home</span>
                    <v-icon color="primary">home</v-icon>
                </v-tab>
                <v-tab to="/explore" class="primary--text">
                    <span class="title font-weight-regular text-capitalize">Explore</span>
                    <v-icon color="primary">dashboard</v-icon>
                </v-tab>
                <v-tab to="/me" class="primary--text">
                    <v-menu offset-y>
                        <div slot="activator">
                            <v-icon color="primary">person</v-icon> <br>
                            <span class="title font-weight-regular text-capitalize">Me</span>
                        </div>
                        <v-list flat style="border-radius: 10px;">
                            <v-list-tile v-for="link in linksMe" :key="link.text" router :to="link.route">
                                <v-list-tile-action>
                                    <v-icon>{{ link.icon }}</v-icon>
                                </v-list-tile-action>
                                <v-list-tile-title>{{ link.text }}</v-list-tile-title>
                            </v-list-tile>
                        </v-list>
                    </v-menu>
                </v-tab>
            </v-tabs>
            <v-divider
                class="mt-2"
             >
             </v-divider>
             <!-- v-if="$route.path.includes('/me') || $route.path.includes('/links') || $route.path.includes('/accounts')" -->
            <v-tabs
                height="42"
                grow
                optional
                v-model="meTab"
                color="primaryComp"
                slider-color="primary"
                >
                <v-tab exact to="/me" class="primary--text">
                    <span class=" font-weight-regular text-capitalize">My Profile</span>
                </v-tab>
                <v-divider vertical></v-divider>
                <v-tab exact to="/links" class="primary--text">
                    <span class=" font-weight-regular text-capitalize">Links</span>
                </v-tab>
                <v-divider vertical></v-divider>
                <v-tab exact to="/accounts" class="primary--text">
                    <span class=" font-weight-regular text-capitalize">Accounts</span>
                </v-tab>
                <!-- <v-tab to="/settings" class="white--text">
                    <span class="title font-weight-regular text-capitalize">Settings</span>
                </v-tab> -->
            </v-tabs>
            <v-divider></v-divider>
            <v-list>
                <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-tile-action>
                        <v-icon class="grey--text text-darken-1">{{ link.icon }}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title class="grey--text text-darken-1">{{ link.text }}</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
            <div></div>
            <v-divider></v-divider>
            <v-btn flat block @click="logout" class="grey--text text-darken-1">
                <span>Sign Out</span>
                <v-icon right>exit_to_app</v-icon>
            </v-btn>
        </v-navigation-drawer>
        <v-toolbar color="primary" :height="isMeBar" :scroll-threshold="10" :scroll-off-screen="$vuetify.breakpoint.smAndDown" prominent tabs app>
            <v-toolbar-side-icon 
                class="white--text hidden-lg-and-up"
                @click.stop="sideNav = !sideNav"
            ></v-toolbar-side-icon>
            <v-toolbar-title class="headline font-weight-light white--text hidden-sm-and-down">
                Touchbase
            </v-toolbar-title>
            
            <v-layout row wrap justify-start align-center fill-height class="ml-2">
                <!-- <v-flex xs4 sm6 md1 class="mr-5 tlc">
                    
                </v-flex> -->

                <!-- xs4 sm6 md5 -->
                <v-spacer class="hidden-md-and-down"></v-spacer>



                <!-- <TabsContainer /> -->
                <v-flex xs5 class="tc hidden-md-and-down">
                    <v-tabs grow height="44" optional v-model="tab" color="primary" hide-slider>
                        <v-tab exact to="/" class="white--text">
                            <span class="headline font-weight-light text-capitalize">Home</span>
                        </v-tab>
                        <v-tab exact to="/explore" class="white--text">
                            <span class="headline font-weight-light text-capitalize">Explore</span>
                        </v-tab>
                        <v-tab exact to="/me" class="white--text">
                            
                            <v-menu open-on-hover offset-y>
                                <span slot="activator" class="headline font-weight-light text-capitalize">
                                    <span>Me</span>
                                    <v-icon v-show="$vuetify.breakpoint.lgAndUp" class="ml-1" color="white">keyboard_arrow_down</v-icon>
                                </span>
                                <v-list flat style="border-radius: 8px;">
                                    <v-list-tile v-for="link in linksMe" :key="link.text" router exact :to="link.route">
                                        <v-list-tile-action>
                                            <v-icon>{{ link.icon }}</v-icon>
                                        </v-list-tile-action>
                                        <v-list-tile-title>{{ link.text }}</v-list-tile-title>
                                    </v-list-tile>
                                </v-list>
                            </v-menu>
                        </v-tab>
                    </v-tabs>
                </v-flex>



                <!-- xs4 sm6 md4 -->
                <v-spacer class="hidden-sm-and-down"></v-spacer>



                <!-- <SearchBar /> -->
                <v-flex xs6 lg3 class="sbc hidden-sm-and-down" style="margin-bottom: 6px;">
                    <v-layout row fill-height justify-center align-center>
                        <v-toolbar height="35" flat class="searchbox-main" color="primaryComp">
                            <v-autocomplete
                                :loading="loading"
                                :search-input.sync="value"
                                @keyup="search"
                                label="Search"
                                flat
                                solo
                                no-filter
                                hide-details
                                no-data-text=""
                                prepend-inner-icon="search"
                            >
                                <!-- <v-icon class="text-xs-center" v-if="loading" slot="prepend-item">calendar_today</v-icon> -->
                                <v-layout justify-center v-if="loading" slot="prepend-item" class="mt-5">
                                    <v-progress-circular indeterminate color="primary"></v-progress-circular>
                                </v-layout>

                                <!-- <v-layout justify-center v-if="items.length >= 1" slot="prepend-item">
                                    <h2>memes</h2>
                                </v-layout> -->
                                <template v-if="isResults && !loading" slot="prepend-item">
                                    <v-list two-line>
                                        <template v-for="(item, index) in items">
                                            <v-list-tile @click="followLoad ? null : $router.push(`/${item.username}`)" :key="item.username" avatar ripple class="py-1">
                                                <v-list-tile-avatar size="53" color="primary" class="pr-4">
                                                    <img :src="item.profilePic" alt="">
                                                    <!-- :src="item.avatar" -->
                                                </v-list-tile-avatar>
                                                <v-list-tile-content class="mr-3">
                                                    <v-list-tile-title>
                                                        <span>{{ item.firstName }} </span>
                                                        <span>{{ item.lastName }}</span>
                                                    </v-list-tile-title>
                                                    <v-list-tile-sub-title class="ml-2">@{{ item.username }}</v-list-tile-sub-title>
                                                    <!-- if they already follow, unfollow button, else follow button -->
                                                </v-list-tile-content>
                                                <v-list-tile-action v-if="ownFollowing.includes(item.username)">
                                                    <v-btn depressed @click="followLoad = true; unfollow(item.username)" small color="primary">
                                                        <v-icon small class="mx-2">person_add_disabled</v-icon>
                                                        <span class="font-weight-regular caption mr-2">Unfollow</span>
                                                    </v-btn>
                                                </v-list-tile-action>
                                                <v-list-tile-action v-else>
                                                    <v-btn depressed @click="followLoad = true; follow(item.username)" small color="primary">
                                                        <v-icon small class="mx-2">person_add</v-icon>
                                                        <span class="font-weight-regular caption mr-2">Follow</span>
                                                    </v-btn>
                                                </v-list-tile-action>
                                            </v-list-tile>
                                            <!-- v-if="index + 1 < items.length" -->
                                            <v-divider :key="index"></v-divider>
                                        </template>
                                    </v-list>
                                </template>

                                <template v-if="isResults && !loading" slot="append-item">
                                    <v-layout fill-height justify-center align-center row>
                                        <v-flex class="text-xs-center">
                                            <span class="grey--text title font-weight-light">Touchbase</span>
                                            <v-divider class="ocedlo-divs mx-4" inset vertical></v-divider>
                                            <v-icon color="grey">dashboard</v-icon>
                                        </v-flex>
                                    </v-layout>
                                </template>

                                <template v-if="!loading && items <= 0" slot="no-data" class="text-xs-center">
                                    <div class="text-xs-center grey--text text--lighten-1 mb-3" style="max-width: 400px; overflow: auto;">
                                        <v-icon large class="mr-2">search</v-icon>
                                        <span class="headline">_</span>
                                        <span class="title">______</span>
                                        <v-icon>keyboard_arrow_right</v-icon>
                                    </div>
                                    <div class="text-xs-center">
                                        <span class="grey--text font-weight-light text--darken-1 mx-2">Search for a person or brand!</span> 
                                        <!-- <br/> -->
                                        <!-- <span class="grey--text font-weight-light text--darken-1 mx-2">Click the three dots for advanced search.</span> -->
                                    </div>
                                </template>
                            </v-autocomplete>
                        </v-toolbar>
                    </v-layout>
                    
                </v-flex>



                <v-spacer class="hidden-sm-and-down"></v-spacer>

                <!-- <p>Value: {{ outputValue }}</p> -->
                <v-spacer class="hidden-md-and-up"></v-spacer>
                <v-flex class="hidden-md-and-up" xs8>
                    <MobileSearch class="mr-1" />
                </v-flex>
                
                
                <v-flex xs3 md2 v-if="loggedIn"> 
                    <!-- <AccountMenu /> -->
                    <v-menu offset-y open-on-hover transition="slide-y-transition" class="mx-0">
                        <v-btn large flat slot="activator" color="primaryComp" class="mx-0">
                            <v-icon left class="pb-1">expand_more</v-icon>
                            <v-avatar :size="responsiveDimProfPic" :class="{'mx-0 pb-1': true }">
                                <img src="/img/avatar-2.png" alt="profile_pic">
                            </v-avatar>
                        </v-btn>

                        <v-list class="mx-0">
                            <span class="grey--text text-darken-2 mx-3 my-1">Hello, Firstname!</span>
                            <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                                <v-list-tile-action>
                                    <v-icon class="grey--text text-darken-1">{{ link.icon }}</v-icon>
                                </v-list-tile-action>
                                <v-list-tile-content>
                                    <v-list-tile-title class="grey--text text-darken-1">{{ link.text }}</v-list-tile-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-btn flat block @click="logout" class="grey--text text-darken-1">
                                <span>Sign Out</span>
                                <v-icon right>exit_to_app</v-icon>
                            </v-btn>
                        </v-list>          
                        
                    </v-menu>
                </v-flex>

                <!-- xs4 sm6 md2 -->
                <v-flex xs6 sm4 lg2 v-else>
                    <v-layout row justify-space-between align-center>
                        <v-flex xs6>
                            <v-btn block flat color="white" @click="signupRoute" class="title text-capitalize font-weight-regular">Signup</v-btn>
                        </v-flex>
                        <v-flex xs6>
                            <v-btn block flat color="white" @click="loginRoute" class="title text-capitalize font-weight-regular">Login</v-btn>
                        </v-flex>
                    </v-layout>
                </v-flex>
                <!-- <v-spacer></v-spacer> -->
                 <!-- style="max-width: calc(20vw + 450px);" -->
                <v-flex xs11 sm12 lg5 xl4 :class="{'sub-slider-margin': $vuetify.breakpoint.lgAndUp}" v-show="($route.path === '/me' || $route.path === '/me/edit' || $route.path === '/links' || $route.path === '/cliques' || $route.path === '/accounts' || $route.path === '/settings') || $vuetify.breakpoint.mdAndDown">
                    <v-layout row justify-center>
                        <v-tabs 
                            :height="subSliderHeight"
                            grow
                            optional
                            v-model="subTab"
                            color="primary"
                            hide-slider
                        >
                            <template v-if="$vuetify.breakpoint.lgAndUp">
                                <v-tab exact to="/me" class="white--text">
                                    <span :class="subSliderText">My Profile</span>
                                </v-tab>
                                <v-tab to="/links" class="white--text">
                                    <span :class="subSliderText">Links</span>
                                </v-tab>
                                <v-tab exact to="/cliques" class="white--text">
                                    <span :class="subSliderText">Cliques</span>
                                </v-tab>
                                <v-tab exact to="/accounts" class="white--text">
                                    <span :class="subSliderText">Accounts</span>
                                </v-tab>
                            </template>
                            <template v-else-if="$vuetify.breakpoint.mdAndDown">
                                <v-tab exact to="/" class="white--text">
                                    <span :class="subSliderText">Home</span>
                                </v-tab>
                                <v-tab exact to="/explore" class="white--text">
                                    <span :class="subSliderText">Explore</span>
                                </v-tab>
                                <v-tab to="/me" class="white--text">
                                    <span :class="subSliderText">Me</span>
                                </v-tab>
                                <!-- <v-tab to="/me" class="white--text">
                                    <span :class="subSliderText">Me</span>
                                </v-tab> -->
                            </template>
                            
                        </v-tabs>
                    </v-layout>
                    
                </v-flex>
            </v-layout>
        </v-toolbar>
    </div>
</template>

<script>
import { onLogout } from '@/apollo'
import { mapMutations } from 'vuex'
import MobileSearch from '@/components/MobileSearch'
import { BASIC_SEARCH_MUTATION } from '@/graphql/mutations/basicSearch'
import { OWN_FOLLOWING_QUERY } from '@/graphql/queries/ownFollowing'
import { FOLLOW_USER_MUTATION } from '@/graphql/mutations/follow'
import { UNFOLLOW_USER_MUTATION } from '@/graphql/mutations/unfollow'

export default {
  name: 'Navbar',
  components: {
      MobileSearch,
  },
  data() {
    return {
        sideNav: false,
        tab: null,
        meTab: null,
        subTab: null,
        value: '',
        items: [],
        outputValue: '',
        followLoad: false,
        ownFollowing: [],
        timeout: null,
        loading: false,
        links: [
            { icon: 'person', text: 'Alias', route: '/alias' },
            { icon: 'format_paint', text: 'Themes', route: '/themes' },
            { icon: 'map', text: 'Site Map', route: '/sitemap' },
            { icon: 'settings', text: 'Settings', route: '/settings' },
            { icon: 'domain', text: 'Legal', route: '/legal' },
            { icon: 'help', text: 'Support', route: '/support' },
        ],
        tabLinks: [
            { icon: 'home', text: 'Home', route: '/' },
            { icon: 'dashboard', text: 'Explore', route: '/explore' },
            { icon: 'person', text: 'Me', route: '/me' },
        ],
        linksMe: [
            { icon: 'person', text: 'My Profile', route: '/me' },
            { icon: 'link', text: 'Links', route: '/links' },
            { icon: 'supervisor_account', text: 'Cliques', route: '/cliques' },
            { icon: 'account_circle', text: 'Accounts', route: '/accounts' },
        ]
    }
  },
//   watch: {
//         subTab() {
//             console.log(typeof this.subTab, this.subTab, this.$route.path)
//             if (this.$route.path != this.subTab) {
//                 this.subTab = null
//             }
//         },
//     },
  computed: {
    subSliderText() {
        return { 'subheading': this.$vuetify.breakpoint.mdAndUp, 'subheading': this.$vuetify.breakpoint.smAndDown, 'font-weight-light text-capitalize': true }
    },
    subSliderHeight() {
        return this.$vuetify.breakpoint.smAndDown ? 22 : 24
    },
    responsiveDimProfPic() {
        switch (this.$vuetify.breakpoint.name) {
            case 'xs': return 44
            case 'sm': return 46
            // case 'md': return 120
            // case 'lg': return 135
            // case 'xl': return 150
        }
    },
    isResults() {
        if (this.items.length >= 1) {
            return true
        } else {
            return false
        }
    },
    isMeBar() {
        if ((this.$route.path === '/me' || this.$route.path === '/me/edit' || this.$route.path === '/cliques' || this.$route.path === '/links' || this.$route.path === '/accounts' || this.$route.path === '/settings') || this.$vuetify.breakpoint.mdAndDown) {
            return 80
        } else {
            return 50
        }
    },
    loggedIn() {
        return this.$loggedIn()
    }
  },
  methods: {
    loginRoute() {
        this.$router.push('/login')
    },
    signupRoute() {
        this.$router.push('/signup')
    },
    logout() {
        this.unsetToken()
        onLogout(this.$apollo.provider.defaultClient)
        .then(() => {
            location.href = '/'
        })
    },
    search() {
        this.loading = true
        clearTimeout(this.timeout)
        
        this.timeout = setTimeout(() => {
            this.$apollo.mutate({
                mutation: BASIC_SEARCH_MUTATION,
                variables: {
                    term: this.value,
                    // possible data collection for analytics
                }
            }).then(result => {
                // let list = 
                // normalization of list, for item.avatar, item.text, see vuetify
                // set items to normalized list so vue can render it
                this.items = result.data.basicSearch.results
                this.items.forEach(obj => {
                    obj.disabled = true
                })
                console.log(this.items);
                this.loading = false
            }).catch(err => {
                console.log(err)
                //this.feedback = true
                this.loading = false
            })
        }, 500)
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
                    // this.loading = false
                    this.$apollo.queries.ownFollowing.refetch() 
                } else {
                    alert("Error - Could not follow user. \n FYI - You cannot follow yourself.")
                }
            }
        }).catch(err => {
            console.log(err)
            // this.feedback = true
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
                    // this.loading = false
                    this.$apollo.queries.ownFollowing.refetch() 
                } else {
                    alert('Error - Could not unfollow user')
                }
            }
        }).catch(err => {
            console.log(err)
            // this.feedback = true
            // this.loading = false
        })
    },

    ...mapMutations([
        'unsetToken'
    ])
  },
  apollo: {
    ownFollowing: {
        query: OWN_FOLLOWING_QUERY,
        update(data) {
            let people = []
            if (data.ownFollowing) {
                for (let i = 0; i < data.ownFollowing.length; i++) {
                    people.push(data.ownFollowing[i].username)
                }
            } else {
                alert('Something went wrong. Please try again later! ⏳')
            }
            return people  
        }
        // result({ data, loading }) {
        //     if (!loading) {
        //         for (let i = 0; i < this.ownFollowing.length; i++) {
        //             this.pownFollowing.push(this.ownFollowing[i].username)
        //         }
        //     }
        // }
    }
  }
}
</script>


<style>

.searchbox {
  border-radius: 25px;
  max-width: 33vw;
}
.searchbox-main {
  border-radius: 25px;
}

.sub-slider-margin {
    margin-left: 10%;
}

.v-input__control, .v-input__slot {
  min-height: 30px !important;
}

.v-input__slot {
    align-items: center !important;
}

.v-input__prepend-inner {
    margin-top: 0px !important;
    align-self: auto !important;
}
/* .tc {
    min-width: calc(calc(100vw / 12) * 4);
    margin-right: 5%; 
    margin-left: 5%;
} */

/* .sbc {
    min-width: calc(calc(100vw / 12) * 4);
} */
</style>