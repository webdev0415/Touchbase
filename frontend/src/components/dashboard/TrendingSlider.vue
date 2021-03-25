<!-- CustomComponent.vue -->
<template>
    <div class="swiper-container recommendedsSwiper">
        <v-layout row align-center class="swiper-wrapper pt-2">
            <!-- <v-list-tile class="swiper-slide"></v-list-tile>
            <v-list-tile class="swiper-slide">
                custom content here
                <h2>hello</h2>
            </v-list-tile> -->
            <v-flex @click="$router.push(person.username)" class="swiper-slide px-2 grey--text text--darken-2 text-xs-center" v-for="person in recommendeds" :key="person.id">

                <v-avatar :size="responsiveProfPic" color="primary" class="mb-1">
                    <img src="img/avatar-2.png"/>
                </v-avatar><br>
                <p :style="{ fontSize: fontSize + 'px' }" class="single-line-name font-weight-light my-0 py-0">{{ person.firstName }} {{ person.lastName }}</p>
                <span class="font-weight-light">@{{ person.username }}</span>
            </v-flex>
        </v-layout>
        <!-- <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div> -->
        <!-- <v-icon class="swiper-next hidden-sm-and-down">arrow_right</v-icon>
        <v-icon class="swiper-prev hidden-sm-and-down">arrow_left</v-icon> -->
    </div>
</template>

<script>
import "swiper/dist/css/swiper.min.css"
// import { Swiper } from "swiper/dist/js/swiper.esm.js" 
import Swiper from 'swiper'

export default {
  props: ["recommendeds"],
  computed: {
    slidesPerView() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return 4
        case 'sm': return 5
        case 'md': return 6
        case 'lg': return 7
        case 'xl': return 8
      }
    },
    responsiveProfPic() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return 65
        case 'sm': return 75
        case 'md': return 80
        case 'lg': return 85
        case 'xl': return 90
      }
    },
    fontSize() {
      if (this.$vuetify.breakpoint.smAndDown) return 14
      return 16
    }
  },
  mounted() {
    // move trending query to this file and make a copy called TrendingSlider.vue
    console.log(this.recommendeds)
    let that = this
    const el = '.recommendedsSwiper'
    // Initialize Swiper
    const swiper = new Swiper(el, {
      slidesPerView: that.slidesPerView,
      // cssWidthAndHeight: true,
      // visibilityFullFit: true,
      // autoResize: true,
      mousewheel: true,
      mousewheel: {
        sensitivity: 0.6,
      },
      // spaceBetween: 100,
      // observer: true,
      freeMode: true,
      freeModeSticky: false,
      freeModeMomentumRatio: 0.4,
      grabCursor: true,
      direction: 'horizontal',
      on: {
        reachEnd: () => {
          console.log('end slide changed')
          that.$emit('trendingEnd')
        }
      }
      // observeParents: true,
      // initialSlide: 1,
      // resistanceRatio: 0,
      // speed: 150
      // navigation: {
      //     nextEl: '.swiper-button-next',
      //     prevEl: '.swiper-button-prev',
      // },
    })

    // Event will be fired after transition
    
    // console.log(swiper.activeIndex)
  }
}
</script>

<style>
.swiper-prev,
.swiper-next {
  position: absolute;
  top: 50%;
  margin-top: -22px;
  z-index: 10;
  /* cursor: pointer; */
  /* background-size: 27px 44px; */
  /* background-position: center; */
  /* background-repeat: no-repeat; */
}

.swiper-prev {
    left: 10px;
    right: auto;
}

.swiper-next {
    right: 10px;
    left: auto;
}

.swiper-container {
  max-width: 100%;
}

.single-line-name {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
