<template>
    <div class="home-div">
        <!-- <v-layout> -->
            <!-- <v-card flat width="2920px" height="990px" class="mx-auto"> -->
        <div style="height: 100vh; min-width: 100vw;">
            <div style="position: absolute; top: 0; z-index: 1; width: 100vw;">
                <CarouselItem/>
            </div>
            <div>
                <!-- <div style="min-height: 7vh;" class="primary">
                    <v-layout row style="min-height: 7vh;" class="white--text" align-center>
                        <v-flex>
                            <span class="ml-5">Touchbase | Hioz LLC</span>
                        </v-flex>
                        
                    </v-layout>
                </div> -->
                <v-carousel class="elevation-0" cycle continuous hide-controls hide-delimiters height="100vh">
                        <!-- <v-carousel-item src="https://i.imgur.com/ibUD4Kx.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/eEBGWbU.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/ibUD4Kx.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/eEBGWbU.jpg"></v-carousel-item> -->
                        <!-- <v-carousel-item src="https://i.imgur.com/ZvTDmVQ.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/IjfKhoh.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/ZvTDmVQ.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/IjfKhoh.jpg"></v-carousel-item> -->
                        <v-carousel-item src="https://i.imgur.com/w3EtHMa.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/1tTQ64a.png"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/w3EtHMa.jpg"></v-carousel-item>
                        <v-carousel-item src="https://i.imgur.com/1tTQ64a.png"></v-carousel-item>
                </v-carousel>
                
            </div>
            
        </div>
        
            <!-- </v-card> -->
        <!-- </v-layout> -->
        <div id="subsection">
            <div id="features">

            </div>
        </div>
    </div>
</template>

<script>
    import CarouselItem from '@/components/landing/CarouselItem'
    // const CarouselItem = () => import('./CarouselItem.vue')

    export default {
        name: 'App',
        components: { CarouselItem },
    }
</script>

<style scoped>
    #subsection {
        background-color: #262626;
        padding-top: 3rem;
        padding-bottom: 2rem;
    }
    >>>.title {
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

</style>
