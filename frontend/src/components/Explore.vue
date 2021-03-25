<template>
<v-layout row fill-height align-center justify-center v-if="$apollo.queries.explore.loading && !fetchMoreLoading">
    <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
</v-layout>

<v-layout v-else justify-center fill-height row>
    <v-flex xs12 md10 xl9>
        <v-layout column>
            <v-layout row :class="{'mt-5': $vuetify.breakpoint.mdAndUp, 'mt-4': $vuetify.breakpoint.smAndDown}" justify-space-between>
                <v-flex class="mb-2 ml-3 title font-weight-light text-uppercase grey--text text--darken-1">
                    <span class="mr-2">Trending</span>
                    <v-progress-circular class="ml-2 my-0" v-if="trendingLoadMoreLoading" indeterminate size="20" color="primary"></v-progress-circular>
                    <span v-else>🔥</span>
                </v-flex>
                <v-flex class="text-xs-right" v-if="!moreTrendingItems" :key="trendingEndMessageKey">
                    <span class="mt-3 mr-1 primary-fade font-weight-light">Come back later for more.</span>
                </v-flex>
            </v-layout>
            
            <v-card class="py-2 explore-slider-margin mx-1" style="border-radius: 8px;">
                <!-- <span>{{ items.length }}</span> -->
                <RecommendedSlider @sliderEnd="trendingLoadMore" v-if="trending" :recommendeds="trending" :usersPerPage="usersPerPage" :page="trendingPage" :previousIndex="previousIndex" :key="trendingKey" />
                <!-- <v-layout row fill-height align-center justify-center v-else>
                    <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
                </v-layout> -->
            </v-card>
            

            <!-- PUT SLIDER OF V-CHIPS OF CATEGORIES HERE -->
            <!-- <FilterSlider style="margin: 7.5vh 0;" /> -->

            <v-container fluid class="mx-0 px-0">
                <v-layout v-for="(row, i) in items" :key="i" row>
                    <!-- { [`${card.lg}`]: true } -->
                    <v-flex style="margin-bottom: 12.5vh;" :class="{'mx-1': $vuetify.breakpoint.smAndDown, 'mx-2': $vuetify.breakpoint.mdAndUp}" v-for="(item, j) in row" :key="j" v-bind="cardSize(item.__typename, row.length)">
                        <v-card style="border-radius: 8px;">
                            <!-- if news or event, do this else do profile view -->
                            <template v-if="['CliqueType', 'BrandType'].includes(item.__typename)">
                                <v-img :src="cliqueOrBrandImage(item.__typename)" height="25vh">
                                    <v-container fill-height fluid class="pa-2">
                                        <v-layout fill-height>
                                            <v-flex xs12 align-end flexbox>
                                                <span class="headline font-weight-light explore-post-title white--text">{{ item.name }}</span>
                                            </v-flex>
                                        </v-layout>
                                    </v-container>
                                </v-img>
                                
                                <v-card-actions class="py-0 my-0" dense>
                                    <v-spacer></v-spacer>
                                    <v-btn flat icon :class="{'mr-2': $vuetify.breakpoint.lgAndUp}" :loading="followOrJoinLoading" @click="followOrJoin(type=item.__typename, name=item.name)" color="primary">
                                        <v-icon size="20">person_add</v-icon>
                                        <!-- <span class="font-weight-regular caption mr-2">Follow</span> -->
                                    </v-btn>
                                    <v-btn flat icon size="20" color="primary">
                                        <v-icon size="20">share</v-icon>
                                    </v-btn>
                                </v-card-actions>
                            </template>
                            
                            <template v-else>
                                <v-card-text style="min-height: 25vh; max-height: 25vh;">
                                    <v-layout column fill-height align-center justify-center>
                                        <v-avatar
                                            :size="profileSize"
                                            color="primary"
                                            :class="{ 'my-2': $vuetify.breakpoint.lgAndUp, 'mb-1': true }"
                                        >
                                            <img :src="item.profilePic" alt="profile_picture">
                                        </v-avatar>
                                        <template v-if="$vuetify.breakpoint.mdAndUp">
                                            <v-flex class="grey--text text-xs-center text--darken-2 ">
                                                <p class="subheading single-line-name font-weight-light my-0 py-0">{{ item.firstName }} {{ item.lastName }}</p>
                                                <span class="font-weight-light">@{{ item.username }}</span>
                                            </v-flex>
                                        </template>
                                        <template v-else>
                                            <v-flex class="grey--text text-xs-center text--darken-2">
                                                <p class="single-line-name font-weight-light my-0 py-0">{{ item.firstName }} {{ item.lastName }}</p>
                                                <span class="caption font-weight-light">@{{ item.username }}</span>
                                            </v-flex>
                                        </template>
                                    </v-layout>
                                </v-card-text>
                                <v-divider v-if="$vuetify.breakpoint.mdAndUp"></v-divider>
                                <v-card-actions class="py-0 my-0 justify-center" dense>
                                    <v-btn flat :class="{'mr-2': $vuetify.breakpoint.lgAndUp}" icon :loading="followOrJoinLoading" @click="followOrJoin(item.__typename, username=item.username)" color="primary">
                                        <v-icon size="20">person_add</v-icon>
                                        <!-- <span class="font-weight-regular caption mr-2">Follow</span> -->
                                    </v-btn>
                                    <v-btn flat icon color="primary">
                                        <v-icon size="20">share</v-icon>
                                    </v-btn>
                                </v-card-actions>
                            </template>
                        </v-card>
                    </v-flex>
                </v-layout>
                <v-layout row justify-center fill-height align-center>
                    <v-btn v-if="moreExploreItems" large @click="fetchMoreLoading=true; loadMore()" :loading="fetchMoreLoading" class="mt-0" color="primary">See More</v-btn>
                    <template v-else>
                        <span class="font-weight-light">Come back later for more content.</span>
                    </template>
                </v-layout>
                
            </v-container>
            
        </v-layout>
    </v-flex>
</v-layout>

</template>

<script>
import { EXPLORE_QUERY } from '@/graphql/queries/explore'
import { TRENDING_QUERY } from '@/graphql/queries/trending'
import RecommendedSlider from '@/components/dashboard/RecommendedSlider'
import FilterSlider from '@/components/dashboard/FilterSlider'

// let w = (a, b) => a.length ? [a[0], ...w(b, a.slice(1))] : b

export default {
    name: 'Explore',
    components: {
        RecommendedSlider,
        FilterSlider
    },
    data() {
        return {
            explore: {},
            trendingPage: 0,
            trendingEndMessageKey: 0,
            moreTrendingItems: true,
            trendingLoadMoreLoading: false,
            followOrJoinLoading: false,
            previousIndex: null,
            trendingKey: 0,
            usersPerPage: 10,
            items: [],
            fetchMoreLoading: false,
            page: 1,
            followLoad: false,
            personDefault: {
                id: Math.floor(Math.random() * Math.floor(500)),
                username: 'thikkxd',
                firstName: 'th3icck',
                lastName: 'MANS',
                __typename: "UserType",
            },
            cliqueDefault: {
                caption: "my thicc storytime",
                created: "2019-09-04 23:35+0000",
                id: Math.floor(Math.random() * Math.floor(500)),
                name: "JoJo's Bizarre Adventures",
                thumbnail: "memes",
                viewCount: 0,
                __typename: "CliqueType",
            },
            permutations: { 
                desktopBrand: [
                    'pbcp', 'pcbp',
                    'bpcp', 'cpbp',
                    'pbcp', 'pcpb'
                ],
                desktop: [
                    'pcp', 'cpp',
                    'ppc', 
                ],
                tablet: [
                    'pcp', 'cpp',
                    'ppc', 
                ],
                tabletBrand: [
                    'b'
                ],
                phoneBrand: [
                    'pb', 'bp'
                ],
                  
            },
            moreExploreItems: true,
        }
    },
    computed: {
        profileSize() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 90
                case 'sm': return 120
                case 'md': return 120
                case 'lg': return 120
                case 'xl': return 130
            }
        },
        exploreDefault() {
            return this.page >= 1
        }
    },
    methods: {
        trendingLoadMore(previousIndex) {
            let xd = JSON.stringify(this.items)
            console.log(xd, 'length')
            if (this.moreTrendingItems) {
                this.trendingLoadMoreLoading = true
                let count = this.usersPerPage
                let skip = this.usersPerPage * this.trendingPage
                this.$apollo.queries.trending.fetchMore({
                    variables: {
                        count,
                        skip
                    },
                    updateQuery: (previousResult, { fetchMoreResult }) => {
                        // console.log('trending newly fetched:', fetchMoreResult, count, skip)
                        // this.moreTrendingItems = fetchMoreResult.trending.length > 0 ? true : false
                        
                        if (fetchMoreResult.trending.length > 0) {
                            this.moreTrendingItems = true
                        } else {
                            this.trendingEndMessageKey++
                            this.moreTrendingItems = false
                        }
                        
                        if (!fetchMoreResult.trending) {
                            return previousResult
                        }
                        
                        return {
                            trending: [...previousResult.trending, ...fetchMoreResult.trending],
                        }
                        console.log(this.items, 'length:', this.items.length)
                    }
                })
                .then(() => {
                    // console.log(previousIndex)
                    
                    if (this.moreTrendingItems) {
                        this.previousIndex = previousIndex
                        
                        this.trendingKey++
                        setTimeout(() => {
                            this.trendingLoadMoreLoading = false
                        }, 500)   
                    } else {
                        this.trendingLoadMoreLoading = false
                    }
                    
                    // this.previousIndex = previousIndex + 1
                    // this.trendingKey++
                    // this.moreTrendingItems ? setTimeout(() => { this.trendingLoadMoreLoading = false }, 500) : this.trendingLoadMoreLoading = false
                    
                })
            } else {
                this.trendingEndMessageKey++
                this.moreTrendingItems = false
            }
        },
        cliqueOrBrandImage(type) {
            return type === 'BrandType' ? "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80" : "https://images.unsplash.com/photo-1511988617509-a57c8a288659?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80"
        },
        loadMore() {
            // this.fetchMoreLoading = true
            this.page++
            this.$apollo.queries.explore.fetchMore({
                variables: {
                    page: this.page - 1,
                    // default: this.exploreDefault
                    // pageSize: this.itemsPerPage
                },
                updateQuery: (previousResult, { fetchMoreResult }) => {
                    // console.log('newly fetched:', fetchMoreResult)
                    if (!fetchMoreResult.explore) {
                        return previousResult
                    }
                    let itemsBefore = this.items.length
                    this.compileExplore(fetchMoreResult.explore)
                    if (this.items.length = itemsBefore) this.moreExploreItems = false
                    this.fetchMoreLoading = false
                    // return {
                    //     explore: {
                    //         __typename: previousResult.explore.__typename,
                    //         people: [...previousResult.explore.people, ...fetchMoreResult.explore.people],
                    //         cliques: [...previousResult.explore.cliques, ...fetchMoreResult.explore.cliques],
                    //         brands: [...previousResult.explore.brands, ...fetchMoreResult.explore.brands],
                    //     }
                    // }
                }
            })
            // .then((memes) => {
            //     this.fetchMoreLoading = false
            //     this.compileExplore(this.explore)
            // })
            
        },
        cardSize(type, rowLength) {
            if (this.$vuetify.breakpoint.lgAndUp) {
                if (rowLength <= 3) {
                    return type === "CliqueType" ? { lg6: true } : { lg3: true }
                } else {
                    return ["CliqueType", "BrandType"].includes(type) ? { lg4: true } : { lg2: true }
                }
            } else if (this.$vuetify.breakpoint.mdOnly) {
                if (rowLength === 1) {
                    return  { md12: true }
                } else {
                    return type === "CliqueType" ? { md6: true } : { md3: true }
                }
            } else if (this.$vuetify.breakpoint.smAndDown) {
                if (rowLength === 1) {
                    return  { xs12: true }
                } else {
                    return { xs6: true }
                }
            }
            
        },
        compileExplore(explore) {
            // counters. clique uses i counter
            let peopleIndex = 0
            let brandsIndex = 0
            let cliquesIndex = 0
            // fixes ratio
            const diff = explore.people.length - explore.cliques.length
            if (diff < (explore.people.length / 2)) {
                explore.cliques.length = explore.people.length / 2
            } else if (diff > (explore.people.length / 2)) {
                explore.people.length = explore.cliques.length * 2
            }
            const requiredBrandLen = explore.cliques.length / 2
            if (explore.brands.length > explore.cliques.length / 2) explore.brands.length = requiredBrandLen < 1 ? Math.ceil(requiredBrandLen) : Math.round(requiredBrandLen)

            if (this.$vuetify.breakpoint.lgAndUp) {
                // 20 rows
                for (let i = 0; i < 20 * this.page; i++) {
                    // const brand = Math.random() < 0.5
                    const brand = i % 2 === 0
                    let row = []
                    if (brand) {
                        let perm = this.permutations.desktopBrand[Math.floor(Math.random() * this.permutations.desktopBrand.length)]
                        // for each letter of perm, add correct thing to row
                        for (let type of perm) {
                            switch (type) {
                                case 'p':
                                    // row.push(this.explore.people[peopleIndex] ? this.explore.people[peopleIndex] : this.personDefault)
                                    if (explore.people[peopleIndex]) row.push(explore.people[peopleIndex])
                                    peopleIndex++
                                    break;
                                case 'b':
                                    if (explore.brands[brandsIndex]) row.push(explore.brands[brandsIndex])
                                    brandsIndex++
                                    break;
                                case 'c':
                                    // row.push(this.explore.cliques[i] ? this.explore.cliques[i] : this.cliqueDefault)
                                    if (explore.cliques[i]) row.push(explore.cliques[i])
                            }
                        }
                    }
                    else {
                        let perm = this.permutations.desktop[Math.floor(Math.random() * this.permutations.desktop.length)]
                        // for each letter of perm, add correct thing to row
                        for (let type of perm) {
                            switch (type) {
                                case 'p':
                                    // row.push(this.explore.people[peopleIndex] ? this.explore.people[peopleIndex] : this.personDefault)
                                    if (explore.people[peopleIndex]) row.push(explore.people[peopleIndex])
                                    peopleIndex++
                                    break;
                                case 'c':
                                    // row.push(this.explore.cliques[i] ? this.explore.cliques[i] : this.cliqueDefault)
                                    if (explore.cliques[i]) row.push(explore.cliques[i])
                            }
                        }
                    }
                    if (row.length > 0) this.items.push(row)
                }
            }

            else if (this.$vuetify.breakpoint.mdOnly) {
                // 30 rows, 20 3 items, 10 1 items
                for (let i = 1; i < 20 * this.page + 1; i++) {
                    const brand = i % 3 === 0
                    let row = []
                    if (brand) {
                        // row.push(this.explore.brands[brandsIndex])
                        if (explore.brands[brandsIndex]) row.push(explore.brands[brandsIndex])
                        brandsIndex++
                    }
                    else {
                        let perm = this.permutations.tablet[Math.floor(Math.random() * this.permutations.tablet.length)]
                        // for each letter of perm, add correct thing to row
                        for (let type of perm) {
                            switch (type) {
                                case 'p':
                                    // row.push(this.explore.people[peopleIndex] ? this.explore.people[peopleIndex] : this.personDefault)
                                    if (explore.people[peopleIndex]) row.push(explore.people[peopleIndex])
                                    peopleIndex++
                                    break;
                                case 'c':
                                    if (explore.cliques[i]) row.push(explore.cliques[i])
                                    // row.push(this.explore.cliques[i] ? this.explore.cliques[i] : this.cliqueDefault)
                            }
                        }
                    }
                    if (row.length > 0) this.items.push(row)
                }
            }

            else if (this.$vuetify.breakpoint.smAndDown) {
                // 50 rows, 20 (2) profile items, 20 (1) clique items, 10 brand items
                for (let i = 1; i < 50 * this.page + 1; i++) {
                    const brand = i % 5 === 0
                    const fullbrand = brandsIndex % 2 === 0
                    let row = []
                    if (brand) {
                        if (fullbrand) {
                            // row.push(this.explore.brands[brandsIndex])
                            if (explore.brands[brandsIndex]) row.push(explore.brands[brandsIndex])
                            brandsIndex++
                        } else {
                            let perm = this.permutations.phoneBrand[Math.floor(Math.random() * this.permutations.phoneBrand.length)]
                            // for each letter of perm, add correct thing to row
                            for (let type of perm) {
                                switch (type) {
                                    case 'p':
                                        // row.push(this.explore.people[peopleIndex] ? this.explore.people[peopleIndex] : this.personDefault)
                                        if (explore.people[peopleIndex]) row.push(explore.people[peopleIndex])
                                        peopleIndex++
                                        break;
                                    case 'b':
                                        // row.push(this.explore.brands[brandsIndex])
                                        if (explore.brands[brandsIndex]) row.push(explore.brands[brandsIndex])
                                        brandsIndex++
                                }
                            }
                        }
                    }
                    else {
                        const people = i % 2 === 0
                        if (people) {
                            // row.push(this.explore.people[peopleIndex] ? this.explore.people[peopleIndex] : this.personDefault)
                            if (explore.people[peopleIndex]) row.push(explore.people[peopleIndex])
                            peopleIndex++
                            // row.push(this.explore.people[peopleIndex] ? this.explore.people[peopleIndex] : this.personDefault)
                            if (explore.people[peopleIndex]) row.push(explore.people[peopleIndex])
                            peopleIndex++
                        } else {
                            // row.push(this.explore.cliques[cliquesIndex] ? this.explore.cliques[cliquesIndex] : this.cliqueDefault)
                            if (explore.cliques[i]) row.push(explore.cliques[i])
                            cliquesIndex++
                        }
                    }
                    if (row.length > 0) this.items.push(row)
                }
            }
        },
        followOrJoin(type, username=null, name=null) {
            this.followOrJoinLoading = true
            if (['UserType', 'BrandType'].includes(type)) {
                console.log(type, name, username)
            } else if (type === 'CliqueType') {
                console.log(type, name)
            }
            this.followOrJoinLoading = false
        },
    },
    apollo: {
        explore: {
            query: EXPLORE_QUERY,
            variables: {
                page: 0
            },
            result({data}) {
                this.compileExplore(data.explore)
            }
        },
        trending: {
            query: TRENDING_QUERY,
            variables() {
                return {
                    count: this.usersPerPage,
                    skip: 0,
                }
            },
            result({data, loading}) {
                if (!loading) {
                    this.trendingPage++
                    // console.log(data.trending, this.trendingPage, this.trending)
                }
            }
        }
    },
    beforeRouteEnter (to, from, next) {
        next(vm => {
            if (!vm.$loggedIn()) {
                vm.$router.replace('/login')
            }
        })
    },
}
</script>

<style>
.primary-fade {
    -webkit-animation: primaryFade 0.65s forwards;
    animation: primaryFade 0.65s forwards;
}

.explore-slider-margin {
    margin-bottom: 8.3vh;
}

@keyframes primaryFade {
    0% {opacity: 0;}
    65% {opacity: 1; color: #FF7256;}
    100% {color: #000}
}

@-webkit-keyframes primaryFade {
    0% {opacity: 0;}
    65% {opacity: 1; color: #FF7256;}
    100% {color: #000}
}
</style>