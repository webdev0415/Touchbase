<template>
    <div id="wrapper">
        <v-layout row wrap class="advertise-main">
            <v-flex md6 class="hidden-md-and-down advertise-left">
                <v-layout fill-height justify-space-between>
                    <!-- <v-timeline dense class="advertise-timeline pl-5">
                        <v-timeline-item color="primary" small right>
                            <h1 class="display-4">Touchbase With Your Audience</h1>
                            <p class="display-1">Good memes to help you in your advertising.</p>
                        </v-timeline-item>
                        <v-timeline-item color="success" small left>
                            <h1 class="display-2">more stuff</h1>
                            <p class="display-1">Good memes to help you in your advertising.</p>
                        </v-timeline-item>
                    </v-timeline> -->
                    <v-flex style="padding-top: 25vh;" class="mr-4">
                        <v-layout column wrap>
                            <v-flex class="text-xs-right">
                                <h1 class="display-4 font-weight-medium grey--text text--darken-3">Touchbase</h1>
                                <h2 class="display-3 font-weight-medium grey--text text--darken-3">With Your Audience.</h2>
                                <br> <br>
                                <!-- only show checkbox if they isPotentialAdvertiser is false -->
                                <v-checkbox color="success" @change="potentialFunc" :disabled="potentialLoading" style="position: absolute; right: 60vw;" v-model="isPotentialAdvertiser">
                                    <template slot="label">
                                        <span v-if="potentialLoading" class="headline text-uppercase font-weight-light grey--text text--darken-3" style="margin-right: 175px;">Thanks for your input.</span>
                                        <v-progress-circular v-if="isPotentialAdvertiser && !potentialLoading" :indeterminate="!potentialLoading" size="24" class="ml-4" style="margin-right: 416px;"></v-progress-circular>
                                        <span v-else-if="!isPotentialAdvertiser" class="headline text-uppercase font-weight-light grey--text text--darken-3">I'm interested in being an advertiser.</span>
                                    </template>
                                </v-checkbox>
                                <v-layout>
                                    <v-spacer></v-spacer>
                                    <!-- margin-top: calc(12vh + 50px); -->
                                    <v-btn flat icon large color="grey-darken-4" @click="$vuetify.goTo('#advertise-st-1', {duration: 1400, offset: -113, easing: 'easeOutQuad'})" style="margin-top: 180px; margin-right: 225px;">
                                        <v-icon x-large>keyboard_arrow_down</v-icon>
                                    </v-btn>
                                </v-layout>
                                
                                <!-- <p class="headline text-uppercase font-weight-light grey--text text--darken-3">Good memes to help your advertising.</p> -->
                            </v-flex>
                            <v-flex style="margin-top: 320px; margin-right: 23px;">
                                <h1 class="display-4 text-xs-right grey--text text--darken-3">Genius.</h1>
                                <p class="headline font-weight-light text-xs-left mt-3 grey--text text--darken-3" style="max-width: 18vw; position: absolute; left: calc(40vw - 360px);">From analytics to targetted advertising, we have tailored plans for every need.</p>
                                <v-layout>
                                    <v-spacer></v-spacer>
                                    <v-btn flat icon large color="grey-darken-4" @click="$vuetify.goTo('.phone-container', {duration: 1400, offset: -350, easing: 'easeOutQuad'})" style="margin-top: 385px; margin-right: 190px;">
                                        <v-icon x-large>keyboard_arrow_down</v-icon>
                                    </v-btn>
                                </v-layout>
                            </v-flex>
                            <v-flex class="phone-container" v-if="$vuetify.breakpoint.lgAndUp">
                                <v-layout justify-end align-center>
                                    <div class="phone-slider-wrapper">
                                        <div class="adv-slider">
                                            <div class="adv-slide">
                                                <!-- <img src="http://via.placeholder.com/337x594"> -->
                                                <v-layout style="background-color: #eee;" align-center fill-height column>
                                                    <v-flex xs10 class="mt-3">
                                                        <p class="display-2 text-xs-center font-weight-medium">The Cool Plan</p>
                                                        <v-img style="border-radius: 10px;" height="70%" src="img/coral-pattern.jpg"></v-img>
                                                        <p class="title grey--text font-weight-regular text--darken-2 text-xs-center mt-4">Perfect for this, this, and that.</p>
                                                    </v-flex>
                                                    <v-spacer></v-spacer>
                                                    <v-flex xs1 class="mb-4">
                                                        <v-btn large round to="/plans/splash-screen" depressed color="primary">Buy</v-btn>
                                                    </v-flex>
                                                </v-layout>
                                                
                                            </div>
                                            <div class="adv-slide">
                                                <!-- <img src="http://via.placeholder.com/337x594"> -->
                                                <v-layout style="background-color: #eee;" align-center fill-height column>
                                                    <v-flex xs10 class="mt-3">
                                                        <p class="display-2 text-xs-center font-weight-medium">Get Rich Plan</p>
                                                        <v-img style="border-radius: 10px;" height="70%" src="img/coral-pattern.jpg"></v-img>
                                                        <p class="title grey--text font-weight-regular text--darken-2 text-xs-center mt-4">Awesome for this but not for that.</p>
                                                    </v-flex>
                                                    <v-spacer></v-spacer>
                                                    <v-flex xs1 class="mb-4">
                                                        <v-btn large round depressed color="primary">Buy</v-btn>
                                                    </v-flex>
                                                </v-layout>
                                            </div>
                                            <div class="adv-slide">
                                                <!-- <img src="http://via.placeholder.com/337x594"> -->
                                                <v-layout style="background-color: #eee;" align-center fill-height column>
                                                    <v-flex xs10 class="mt-3">
                                                        <p class="display-2 text-xs-center font-weight-medium">Splash Screen</p>
                                                        <v-img style="border-radius: 10px;" height="70%" src="img/coral-pattern.jpg"></v-img>
                                                        <p class="title grey--text font-weight-regular text--darken-2 text-xs-center mt-4">Get your feet wet with a splash!</p>
                                                    </v-flex>
                                                    <v-spacer></v-spacer>
                                                    <v-flex xs1 class="mb-4">
                                                        <v-btn large round depressed color="primary">Buy</v-btn>
                                                    </v-flex>
                                                </v-layout>
                                            </div>
                                        </div>
                                    </div>
                                </v-layout>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <v-flex xs2 class="mr-4">
                        <v-layout row wrap style="max-width: 10vw; height: calc(100% - 40vh); margin-top: 36vh;">
                            <v-flex xs6>
                                <v-layout column justify-space-between>
                                    <v-flex>
                                        <v-divider color="grey"></v-divider>
                                        <v-divider color="grey"></v-divider>
                                        <v-divider color="grey"></v-divider>
                                    </v-flex>
                                    <v-flex style="margin-top: 720px;">
                                        <v-divider color="grey"></v-divider>
                                        <v-divider color="grey"></v-divider>
                                        <v-divider color="grey"></v-divider>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                            <v-flex xs6>
                                <v-divider vertical color="grey"></v-divider>
                                <v-divider vertical color="grey"></v-divider>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    
                </v-layout>
            </v-flex>
            <v-flex xs12 lg6 class="advertise-content">
                <div class="">
                    <v-img src="https://images.unsplash.com/photo-1552960562-daf630e9278b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&q=100" style="height: calc(100vh - 64px);"></v-img>
                    <div class="pa-5">
                        <h1 id="advertise-st-1" class="display-2 text-xs-left font-weight-light mb-5">a reliable solution.</h1>
                        <v-img class="hidden-md-and-down" style="margin-left: 7.5vw; height: 100%; width: 100%;" src="https://i.imgur.com/BBvqNHV.png"></v-img>
                        <v-img class="hidden-lg-and-up" src="https://i.imgur.com/BBvqNHV.png"></v-img>
                        <v-icon size="40" color="primary" class="icon__flip mt-2">format_quote</v-icon>
                        <v-icon size="40" color="primary" class="mt-2">format_quote</v-icon>
                        <blockquote class="font-weight-light text-xs-center headline px-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum maiores.</blockquote>
                        <br>
                        <span style="margin-left: 20%;" class="font-weight-light">-- Some Reviewer, CEO of Memes Corp.</span>
                    </div>
                    <div class="pa-5 hidden-md-and-down">
                        <h1 class="display-2 text-xs-left font-weight-light mb-5">checkit fam.</h1>
                        <div class="text-xs-center" style="margin-top: 250px; position: relative; z-index: 99;">
                            <p class="display-1 mb-5">Touchbase is a faster way to interact.</p>
                            <!-- <v-layout justify-center style="max-width: 30vw;">
                                <v-flex>
                                    <v-divider dark inset></v-divider>
                                    <v-divider dark inset></v-divider>
                                    <v-divider dark inset></v-divider>
                                </v-flex>
                            </v-layout> -->
                            <span class="font-weight-light text-xs-center headline">It is truly memes.</span>
                        </div>
                    </div>

                    <!-- <div id="phone-container" v-if="$vuetify.breakpoint.mdAndDown">
                        <v-layout justify-center align-center>
                            <div class="phone-slider-wrapper">
                                <div class="adv-slider">
                                    <div class="adv-slide">
                                        <v-layout style="background-color: #eee;" align-center fill-height column>
                                            <v-flex xs10 class="mt-3">
                                                <p class="display-2 text-xs-center font-weight-medium">The Cool Plan</p>
                                                <v-img style="border-radius: 10px;" height="70%" src="img/coral-pattern.jpg"></v-img>
                                                <p class="title grey--text font-weight-regular text--darken-2 text-xs-center mt-4">Perfect for this, this, and that.</p>
                                            </v-flex>
                                            <v-spacer></v-spacer>
                                            <v-flex xs1 class="mb-4">
                                                <v-btn large round depressed color="primary">Buy Now</v-btn>
                                            </v-flex>
                                        </v-layout>
                                        
                                    </div>
                                    <div class="adv-slide">
                                        <v-layout style="background-color: #eee;" align-center fill-height column>
                                            <v-flex xs10 class="mt-3">
                                                <p class="display-2 text-xs-center font-weight-medium">Get Rich Plan</p>
                                                <v-img style="border-radius: 10px;" height="70%" src="img/coral-pattern.jpg"></v-img>
                                                <p class="title grey--text font-weight-regular text--darken-2 text-xs-center mt-4">Awesome for this but not for that.</p>
                                            </v-flex>
                                            <v-spacer></v-spacer>
                                            <v-flex xs1 class="mb-4">
                                                <v-btn large round depressed color="primary">Buy Now</v-btn>
                                            </v-flex>
                                        </v-layout>
                                    </div>
                                    <div class="adv-slide">
                                        <v-layout style="background-color: #eee;" align-center fill-height column>
                                            <v-flex xs10 class="mt-3">
                                                <p class="display-2 text-xs-center font-weight-medium">Splash Screen</p>
                                                <v-img style="border-radius: 10px;" height="70%" src="img/coral-pattern.jpg"></v-img>
                                                <p class="title grey--text font-weight-regular text--darken-2 text-xs-center mt-4">Get your feet wet with a splash!</p>
                                            </v-flex>
                                            <v-spacer></v-spacer>
                                            <v-flex xs1 class="mb-4">
                                                <v-btn large round depressed color="primary">Buy Now</v-btn>
                                            </v-flex>
                                        </v-layout>
                                    </div>
                                </div>
                            </div>
                        </v-layout>
                    </div> -->

                </div>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import $ from "jquery";
import slick from 'slick-carousel';
import 'slick-carousel/slick/slick.css';

export default {
    name: 'Advertise',
    data() {
        return {
            isPotentialAdvertiser: false,
            potentialLoading: false,
        }
    },
    methods: {
        potentialFunc() {
            setTimeout(() => {
                this.potentialLoading = true
            }, 1000)
            this.potentialLoading = false
        },
        phoneScroll(e) {
            console.log(e)
            console.log(e.target)
            console.log('memes')
        }
    },
    mounted() {
        const slider = $('.adv-slider')
        slider.slick({
            arrows: false,
            dots: false,
        })

        // let that = this

        // const phoneContainer = $('.phone-wrapper')

        slider.on('wheel', (function(e) {
            e.preventDefault()
            let i = slider.slick('slickCurrentSlide') + 1
            // console.log(i)
            if (e.originalEvent.deltaY < 0) {
                if (i > 1) {
                    // $(this).slick('slickPrev')
                    slider.slick('slickPrev')
                }
                else {
                    // console.log('elsee!!!!!!')
                    // exit func or switch scroll back to main page
                    // that.$vuetify.goTo(1800, {duration: 1400, offset: -113, easing: 'easeOutQuad'})
                    // $('html').animate({
                    //     scrollTop: 1100
                    // }, 800)
                }
            } else {
                if (i < 3) {
                    // $(this).slick('slickNext')
                    slider.slick('slickNext')
                }
                else {
                    // console.log('22elsee!!!!!!')

                    // exit func or switch scroll back to main page
                    // $('html').animate({
                    //     scrollTop: 2400
                    // }, 800)

                }
            }
        }))
        // const phone = document.getElementById('phone-container')
        // phone.onscroll = this.phoneScroll
    },
}
</script>

<style lang="scss" scoped>

.phone-container {
    margin-top: 600px;
    margin-right: 10%;
    // margin-top: 1760px; 
    // width: 100vw;
    // height: 35vh;
    // padding-right: 50%;
    // position: absolute;
    // left: 0;
    // right: 0;
    // background-color: rgba(10, 10, 10, 0.3);
    //z-index: 999;
}

.adv-slide {
    width: 100%;
    height: 594px;
}

.adv-slider {
    width: 337px;
    // width: 100vw;
    margin-right: 50%;
    height: 594px;
    margin-left: 27px;
    margin-top: 98px;
}

.advertise-main {
    width: 100vw;
    position: relative;
    height: 5000px;
    overflow: auto;
    /* z-index: 2; */
}

.advertise-content {
    background-color: white;
}

.icon__flip {
    -moz-transform: scale(-1);
    -o-transform: scale(-1);
    -webkit-transform: scale(-1);
    transform: scale(-1);
    filter: FlipVH;
    -ms-filter: "FlipVH";
    margin-right: 89%;
}

/* .advertise-left {
    width: 50vw;
} */

#wrapper {
    overflow-x: hidden;
}

#wrapper:before {
    background-attachment: fixed;
    background-color: #ffccb3;
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 920 1750' x='0px' y='0px'%3E %3Cpath style='fill: rgba(255, 114, 86, 0.25)' d='M889.72,1137.55l-2.91-0.75l-364.39,282.94l-0.7-0.9l-0.51,0.11l-94.77-451.5l-32.51-15.75l-16.73-8.11l0,0.68 l-1.46,0l0-1.39l-1.89-0.92l-112.41-54.47l-0.29,1.03l-1.41-0.37l0.37-1.31l-34.14-16.54l-98.56-47.76l-0.59,0.81l-1.16-0.88 l0.42-0.57L11.43,766.33l-0.25,0.2l-0.9-1.15l102.87-79.98l0.08-0.1l0.02,0.02l116.68-90.72l-0.18-0.34l1.3-0.66l0.05,0.09 l100.5-78.14l-0.07-0.32l0.65-0.14l42.3-32.89l-0.15-54.54l-0.59,0.29l-0.64-1.31l1.23-0.6l-0.01-4.54l-0.33-122.47l-0.99,0.18 l-0.28-1.43l1.27-0.23l-0.4-147.49l-0.87-0.16l0.28-1.43l0.58,0.1l-0.35-127.48l-0.13-0.06l0.64-1.31L489.97,76.8l0.73,0.19 l-0.04,0.14l132.63,65.11l0.33-0.45l1.16,0.88l-0.16,0.22l114.21,56.07l0.45-0.35l0.72,0.93l47.89,23.51l2.76-1.36l0.56,4.61 l-3.32-1.63L571.52,330.88L375.95,482.93l0.66,239.95l51.12,243.57l222.53,107.83l236.23,60.93l2.27-1.77 M375.8,425.34l17.25-8.47 l36.13-127.75l-53.73,9.66L375.8,425.34z M551,241.05l38.19-52.2l-123.83-22.27l-34.13,120.68l98.99-17.81L551,241.05z M532.3,269.09l151.34-27.22l37.63-29.25l-130.48-23.47L532.3,269.09z M303.38,733.9l-2.36-4.48l-44.18-83.78L182.5,747.25 l40.78,36.46l52.69,47.11L303.38,733.9z M277.18,831.91l56.95,50.93L375.69,920l-0.13-49.23l-71.19-135L277.18,831.91z M303.96,731.86l41.93-148.25l-9.74-46.39L257.8,644.33L303.96,731.86z M304.94,733.73l9.55,18.12l61.05,115.78l-0.39-144.6 l-16.9-80.53l-11.71-55.81L304.94,733.73z M375.21,211.79l0.23,85.51l54.17-9.74l34.29-121.23l-88.87-15.98L375.21,211.79z M430.78,288.83l-17.88,63.21L394.81,416l44.01-21.6l90.15-123.23L430.78,288.83z M287.76,898.62l87.99,42.64l-0.05-19.29 l-91.37-81.71l-7.59-6.78l-14.88,52.59L287.76,898.62z M174.26,843.62l86.26,41.8l15-53.03l-93.89-83.95l-53.34,72.91L174.26,843.62 z M113.18,687.22L12.71,765.33l55.69,26.99l58.56,28.38l53.58-73.24l-34.83-31.14L113.18,687.22z M230.62,595.92l-116.27,90.4 l63.02,56.36l4.03,3.61l74.67-102.08l-7.47-14.17L230.62,595.92z M331.94,517.15l-100.15,77.86l25.25,47.88l78.71-107.59l-1.71-8.14 L331.94,517.15z M333.22,516.15l2.02,9.64l1.66,7.92l34.65-47.37L333.22,516.15z M337.31,535.63l9.43,44.95l26.67-94.3 L337.31,535.63z M347.39,583.66l27.74,132.16l-0.62-228.04L347.39,583.66z M374.7,21.83l0.35,127.02l89.27,16.06l24.61-87 L374.7,21.83z M490.25,78.56l-22.26,78.7l-2.24,7.91l124.39,22.37l10.23-13.99l22.04-30.12L490.25,78.56z M623.74,144.09 l-12.29,16.8l-19.71,26.95l131.07,23.58l14.73-11.45L623.74,144.09z M739,200.67l-13.3,10.34l-0.96,0.74l58.14,10.46L739,200.67z M723.19,212.96l-25.33,19.69l-11.14,8.66l97.03-17.45L723.19,212.96z M782.89,225.5l-98.64,17.74l-107.06,83.23L782.89,225.5z M631.68,282.26l49.48-38.47l-150.1,27l-89.41,122.22l129.1-63.37L631.68,282.26z M565.06,334.05l-125.28,61.5l-45.94,62.8 l-14.96,20.44L565.06,334.05z M425.31,412.87l11.65-15.93l-42.69,20.96l-13.66,48.3l-3.58,12.67L425.31,412.87z M392.51,418.76 l-16.71,8.2l0.01,4.72l0.12,45.68L392.51,418.76z M377.21,941.96l21.37,10.36l24.14,11.7l-45.56-40.74L377.21,941.96z M377.15,921.31l34.83,31.15l12.57,11.24l-47.53-90.14L377.15,921.31z M376.63,730.07l0.38,140.33l48.29,91.59L376.63,730.07z M806.29,1197.48l75.8-58.86l-28.56,11.47l-25.6,10.28l14.96,7.25l-0.64,1.31l-16.16-7.83l-124.76,50.1l40.56,36.27L806.29,1197.48z M522.43,1146.18l58.88,111.66l52.71-21.17l64.61-25.95l-75.11-67.17L522.43,1146.18z M621.92,1142.14l-115.78-103.53l-46.8-12.07 l62.33,118.2l7.06-0.18L621.92,1142.14z M700.14,1210.12l124.19-49.87l-42.89-20.78l-155.8,4.04L700.14,1210.12z M679.7,1295.77 l61.03-47.39l-40.9-36.57l-117.85,47.32l42.09,79.82L679.7,1295.77z M522.48,1417.85l1.83-1.42l98.6-76.56l-42.28-80.19 l-84.25,33.83L522.48,1417.85z M496.08,1292.06l83.87-33.68l-59.14-112.16l-55.04,1.43L496.08,1292.06z M465.46,1146.2l54.58-1.42 l-62.61-118.74l-18.03-4.65l0.36-1.41l16.74,4.32l-27.63-52.4L465.46,1146.2z M458.42,1024.79l45.35,11.7l-74.14-66.29 L458.42,1024.79z M431.46,969.87l75.38,67.41l136.26,35.15L431.46,969.87z M649.76,1075.65l-140.54-36.25l114.83,102.68l154.53-4.01 L649.76,1075.65z M656.92,1077.5l124.84,60.5l51.97-1.35l47.7-1.24L656.92,1077.5z M784.62,1139.38l41.54,20.13l56.45-22.67 L784.62,1139.38z'/%3E %3C/svg%3E");
    background-position: -50% 10%;
    background-repeat: repeat-y;
    background-size: 75% auto;
    content: '';
    display: block;
    height: 100%;
    left: 0;
    position: absolute;
    top: 0;
    width: 50vw;
}

// .phone-slider-wrapper {
//     background-image: url(https://i.imgur.com/4ARGzfk.png);
//     background-size: contain;
//     background-repeat: no-repeat;
//     width: 100%;
//     max-width: 500px;
//     height: 85vh;
//     max-height: 1000px;
// }

.phone-slider-wrapper {
    background-image: url(https://i.imgur.com/4ARGzfk.png);
    background-size: contain;
    background-repeat: no-repeat;
    width: 400px;
    height: 800px;
    position: absolute;
    margin-top: 180px;
}

</style>