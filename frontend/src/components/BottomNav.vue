<template>
    <div>
        <v-bottom-nav :height="responsiveDimHeight" :active.sync="bottomNav" app :value="true" color="primary">
            <!-- <v-flex xs12 class="text-xs-center">
                <v-btn color="primaryComp" :value="bottomNav" v-slot="activator" flat @click="sheet = true" class="ma-0 pa-0">
                    <v-icon color="primaryComp">keyboard_arrow_up</v-icon>
                </v-btn>
                <v-divider></v-divider>
            </v-flex> -->
            <v-btn to="/" color="primaryComp" flat class="mt-0 pt-0 pb-0">
                <span v-if="bottomNav === 0" class="caption">Home</span>
                <v-icon>home</v-icon>
            </v-btn>
            <v-btn to="/explore" color="primaryComp" flat class="mt-0 pt-0 pb-0">
                <span v-if="bottomNav === 1" class="caption">Explore</span>
                <v-icon>dashboard</v-icon>
            </v-btn>
            <v-btn to="/me" color="primaryComp" flat class="mt-0 pt-0 pb-0">
                <span v-if="bottomNav === 2" class="caption">Me</span>
                <v-icon>person</v-icon>
            </v-btn>
        </v-bottom-nav>
        <!-- <v-bottom-sheet full-width hide-overlay v-model="sheet" class="sheet">
            <v-card class="text-xs-center">
                <v-card-actions>
                    <v-btn color="primary" @click="sheet = false" block flat>
                        <v-icon>keyboard_arrow_down</v-icon>
                        <span class="text-uppercase">Close</span>
                        <v-icon>keyboard_arrow_down</v-icon>
                    </v-btn>
                </v-card-actions>
                <v-divider></v-divider>
                <v-card-text>
                    <v-layout row class="text-xs-center" wrap>
                        <v-flex xs6>
                            <v-btn large outline round color="primary">Followers</v-btn>
                        </v-flex>
                        <v-flex xs6>
                            <v-btn large outline round color="primary">Following</v-btn>
                        </v-flex>
                        <v-flex xs6>
                            <v-btn large outline round color="primary">My Links</v-btn>
                        </v-flex>
                        <v-flex xs6>
                            <v-btn large outline round color="primary">Settings</v-btn>
                        </v-flex>
                    </v-layout>
                </v-card-text>
                <v-divider></v-divider>
                <span class="grey--text ma-2">-- Hioz LLC --</span>
            </v-card>
        </v-bottom-sheet> -->
    </div>
</template>

<script>
export default {
    name: 'BottomNav',
    data() {
        return {
            bottomNav: '',
            sheet: false,
        }
    },
    computed: {
        responsiveDimHeight() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 50
                case 'sm': return 55
            }
        },
        // iconSizeA() {
        //     if (this.bottomNav != 0) {
                
        //     }
        // },
        // iconSizeB() {
        //     if (this.bottomNav != 0) {
                
        //     }
        // },
        // iconSizeC() {
        //     if (this.bottomNav != 0) {
                
        //     }
        // }
    },
}
</script>

<style>

.bot-nav {
    position: fixed;
    bottom: 0px;
    /* width: 100%; */
}

/* .sheet {
    position: fixed;
    bottom: 108px;
    width: 100%;
    height: 45vh;
} */

</style>