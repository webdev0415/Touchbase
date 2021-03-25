<template>
    <v-flex xs12 md6 lg4 order-md2 class="db-flex px-3 mb-5">
        <v-card flat color="grey lighten-4" class="db-card elevation-2">
            <v-card-title class="text-uppercase grey--text text--darken-1 justify-center">People</v-card-title>
            <v-divider></v-divider>
            <v-card-text>
                <div class="people-recommended mb-2">
                    <span class="grey--text text--darken-3">Recommended For You</span>
                    <!-- <div class="swiper-container">
                    <v-layout align-center justify-space-around fill-height class="swiper-wrapper">
                        <v-flex xs6 sm4 md3 class="people-content swiper-slide text-xs-center mt-3" v-for="person in recommendeds" :key="person.name">
                            <v-badge overlap>
                                <v-icon slot="badge" dark>check</v-icon>

                                <v-avatar size="70" color="primary" class="mb-1">
                                    <img src="img/avatar-2.png"/>
                                </v-avatar><br>
                            </v-badge>
                            <span>{{ person.name }}</span>
                        </v-flex>
                    </v-layout>
                    </div> -->
                    <!-- @transitionEnd="transitionEnd" -->
                    <!-- <custom-component
                        :recommendeds="recommendeds"
                    /> -->
                    <RecommendedSlider :recommendeds="recommendeds" />

                    <!-- overflow it with a max-width so it's draggable on mobile -->
                    <!-- <div @click="recPageNum"> 
                        <v-btn small icon>
                            <v-icon>arrow_left</v-icon>
                        </v-btn>
                    </div> -->
                    
                </div>
                <!-- <v-divider class="my-2"></v-divider> -->
                <!-- <div class="people-recommended mb-2"> -->
                    <!-- <span class="grey--text text--darken-3">Trending</span> -->
                    <!-- <v-layout class="mt-3" align-center justify-space-around fill-height>
                        <v-flex xs3 class="people-content text-xs-center" v-for="person in recommendeds" :key="person.name">
                            <v-badge overlap>
                                <v-icon slot="badge" dark>check</v-icon>

                                <v-avatar size="65" color="grey darken-1" class="mb-1">
                                    <v-icon large dark>person</v-icon>
                                </v-avatar>
                            </v-badge> <br>
                            <span>{{ person.name }}</span>
                        </v-flex>
                    </v-layout> -->
                <!-- </div> -->
                
            </v-card-text>
            <v-spacer></v-spacer>
            <v-divider></v-divider>
            <v-card-actions>
                <v-layout wrap align-center justify-space-around fill-height>
                    <Followers class="my-2" />
                    <Following class="my-2" />
                </v-layout>
            </v-card-actions>
            
        </v-card>
    </v-flex>
</template>

<script>
import RecommendedSlider from './RecommendedSlider'
import Followers from './Followers'
import Following from './Following'

export default {
    name: 'People',
    components: {
        Followers,
        Following,
        RecommendedSlider
    },
    data() {
        return {
            recPage: 1,
            recommendeds: [
                { name: 'Elon Musk' },
                { name: 'Mr. Obama' },
                { name: 'Pewdiepie' },
                { name: 'Donald J. Trump' },
                { name: 'Boi' },
                { name: 'Big' },
                { name: 'xd' },
            ]
        }
    },
}
</script>
