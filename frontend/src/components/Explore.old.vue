<template>
<v-layout justify-center fill-height row class="px-3">
    <v-flex xs12 md10 lg9>
        <v-layout column>
            <span class="mt-5 mb-2 ml-2 title font-weight-light text-uppercase grey--text text--darken-1">
                <span class="mr-2">Trending</span>
                <!-- <v-icon class="mx-2">trending_up</v-icon> -->
                <span>🔥</span>
            </span>
            <v-card class="px-2 py-2" style="border-radius: 8px;">
                <RecommendedSlider :recommendeds="recommendeds" />
            </v-card>

            <!-- PUT SLIDER OF V-CHIPS OF CATEGORIES HERE -->
            <FilterSlider style="margin: 4.5vh 0;" />

            <v-container class="px-1" fluid>
                <v-layout v-for="(row, i) in items" :key="i" row>
                    

                    <v-flex style="margin-bottom: 6.5vh;" class="px-2" v-for="card in cards" :key="card.title" v-bind="{ [`${card.xs}`]: true, [`${card.lg}`]: true }">
                        <v-card style="border-radius: 8px;">
                            <!-- if news or event, do this else do profile view -->
                            <v-img v-if="card.plan" :src="card.src" height="25vh">
                                <v-container fill-height fluid class="pa-2">
                                    <v-layout fill-height>
                                        <v-flex xs12 align-end flexbox>
                                            <span class="headline font-weight-light explore-post-title white--text">{{ card.title }}</span>
                                        </v-flex>
                                    </v-layout>
                                </v-container>
                            </v-img>
                            <v-card-text v-else style="height: 25vh;">
                                <v-layout>
                                    memes
                                </v-layout>
                            </v-card-text>
                            <v-card-actions dense>
                                <v-spacer></v-spacer>
                                <v-btn flat icon color="primary">
                                    <v-icon>favorite</v-icon>
                                </v-btn>
                                <v-btn flat icon color="primary">
                                    <v-icon>share</v-icon>
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
            
        </v-layout>
    </v-flex>
</v-layout>
</template>

<script>
import { EXPLORE_QUERY } from '@/graphql/queries/explore'
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
            variables: {
                default: false
            },
            personDefault: {
                id: Math.floor(Math.random() * Math.floor(500)),
                username: 'thikkxd',
                firstName: 'th3icck',
                lastName: 'MANS'
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
                  
            },
            recommendeds: [
                { firstName: 'Elon', lastName: 'Musk', username: 'muskboi' },
                { firstName: 'Thicc', lastName: 'Man', username: 'xd' },
                { firstName: 'Mark', lastName: 'Guy', username: 'lol' },
                { firstName: 'Scott', lastName: 'Cawthon', username: 'memes._' },
                { firstName: 'Jojo', lastName: 'HaYeZust', username: '123p' },
                { firstName: 'Sponge', lastName: 'Bob', username: 'eatit' },
                { firstName: 'Josh', lastName: 'Goodings', username: 'aahhh' },
                { firstName: 'Normal', lastName: 'Guy', username: 'yeghj' },
                { firstName: 'HDMI', lastName: 'Cable', username: 'qq' },
                { firstName: 'thikker', lastName: 'mans', username: 'uak' },
                { firstName: 'Elongated', lastName: 'Muskrat', username: 'moose' },
            ],
            cardsFirstRow: [
                { first: true, title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs5', lg: 'lg4' },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs3', lg: 'lg2' },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs6' },
            ],
            filters: [],
            cards: [
                { title: 'Ping Pong Power', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs3', lg: 'lg2' },
                { title: 'Memes that are good', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs5', lg: 'lg5', plan: true, },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs4', lg: 'lg3', plan: true, },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs4', lg: 'lg2', plan: true, },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs5', lg: 'lg4', plan: true, },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs3', lg: 'lg2' },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs6', plan: true, },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs5', lg: 'lg4', plan: true, },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs3', lg: 'lg2' },
                { title: 'Reddit bans memes', src: 'https://images.unsplash.com/photo-1567449899307-e711e1bf9851?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80', xs: 'xs6', plan: true, },
            ]
        }
    },
    computed: {
        items() {
            return this.compileExplore()
        }
    },
    methods: {
        compileExplore() {
            if (!this.$apollo.loading) {
                // if (this.explore.people.length < 100 || this.explore.cliques.length < 50) const shortest = [this.explore.people, this.explore.cliques].sort((p, c) => p.length - c.length)[0]
                
                // if (shortest) {
                //     switch(shortest[0].__typename) {
                //         case 'CliqueType':
                //             this.explore.cliques.splice(this.explore.people.length * 2 - 1)
                //         case 'PeopleType':
                //             this.explore.people.splice(this.explore.cliques.length / 2 - 1)
                //         // brands
                //     }
                // }

                // counters. clique uses i counter
                let people_index = 0
                let brands_index = 0
                console.log(this.explore)
                this.explore.cliques.length < this.explore.people.length / 2 ? this.explore.cliques.splice(this.explore.people.length * 2 - 1) : this.explore.people.splice(this.explore.cliques.length / 2 - 1)
                let exploreList = []

                if (this.$vuetify.breakpoint.lgAndUp) {
                    // 50 rows
                    for (let i = 0; i < 50; i++) {
                        // const brand = Math.random() < 0.5
                        const brand = i % 2 === 0
                        let row = []
                        if (brand) {
                            let perm = this.permutations.desktopBrand[Math.floor(Math.random() * this.permutations.desktopBrand.length)]
                            // for each letter of perm, add correct thing to row
                            console.log(perm.length)
                            for (let type of perm) {
                                switch (type) {
                                    case 'p':
                                        row.push(this.explore.people[people_index] ? this.explore.people[people_index] : this.personDefault)
                                        people_index++
                                        break;
                                    case 'b':
                                        row.push(this.explore.brands[brands_index])
                                        brands_index++
                                        break;
                                    case 'c':
                                        row.push(this.explore.cliques[i] ? this.explore.cliques[i] : this.cliqueDefault)
                                }
                            }
                        }
                        else {
                            let perm = this.permutations.desktop[Math.floor(Math.random() * this.permutations.desktop.length)]
                            // for each letter of perm, add correct thing to row
                            for (let type of perm) {
                                switch (type) {
                                    case 'p':
                                        row.push(this.explore.people[people_index] ? this.explore.people[people_index] : this.personDefault)
                                        people_index++
                                        break;
                                    case 'c':
                                        row.push(this.explore.cliques[i] ? this.explore.cliques[i] : this.cliqueDefault)
                                }
                            }
                        }
                        exploreList.push(row)
                    }
                    // exploreList.push(...w(fours, threes))
                }
                else if (this.$vuetify.breakpoint.mdOnly) {
                    console.log(shortest)
                }
                else if (this.$vuetify.breakpoint.smAndDown) {
                    console.log(shortest)
                }
                console.log(exploreList)
                return exploreList
            } else {
                return []
            }
            
        }
    },
    apollo: {
        explore: {
            query: EXPLORE_QUERY,
            variables() {
                return this.variables
            },
            result() {
                console.log(this.items)
            },
            update(data) {
                if (data.explore) {
                    data.explore.brands = [
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                        { name: 'Hioz LLC', caption: 'We like memes!', },
                    ]
                } else {
                    alert('Something went wrong. Please try again later! ⏳')
                } 
                return data.explore
            }
        }
    }
}
</script>

<style>

.explore-post-title {

}

</style>