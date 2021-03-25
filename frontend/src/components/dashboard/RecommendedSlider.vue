<!-- CustomComponent.vue -->
<template>
    <div class="swiper-container recommendedsSwiper">
        <v-layout row align-center class="swiper-wrapper pt-2">
            <!-- <v-list-tile class="swiper-slide"></v-list-tile>
            <v-list-tile class="swiper-slide">
                custom content here
                <h2>hello</h2>
            </v-list-tile> -->
            <v-flex class="swiper-slide px-2 grey--text text--darken-2 text-xs-center" v-for="person in recommendeds" :key="person.id">

                <v-avatar  :size="responsiveProfPic" color="primary" class="mb-1">
                    <img :src="person.profilePic"/>
                </v-avatar><br>
                <template v-if="$vuetify.breakpoint.mdAndUp">
                  <p @click="$router.push(person.username)" class="single-line-name subheading font-weight-light my-0 py-0">{{ person.firstName }} {{ person.lastName }}</p>
                  <span @click="$router.push(person.username)" class="font-weight-light">@{{ person.username }}</span>
                </template>
                <template v-else>
                  <p @click="$router.push(person.username)" class="single-line-name caption font-weight-light my-0 py-0">{{ person.firstName }} {{ person.lastName }}</p>
                </template>
                
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

let swiper;

export default {
  props: ["recommendeds", "usersPerPage", "page", "previousIndex"],
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
  },
  mounted() {
    let that = this
    const el = '.recommendedsSwiper'
    // Initialize Swiper
    // console.log(self.slidesPerView)
    swiper = new Swiper(el, {
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
          console.log('end slide changed', that.recommendeds.length - that.slidesPerView)
          that.$emit('sliderEnd', that.recommendeds.length - that.slidesPerView)
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

    // console.log(this.page, (this.usersPerPage * this.page) - 1)
    // if (this.page > 1) {
    //   swiper.slideTo((this.usersPerPage * this.page) - 1)
    // }
    if (this.previousIndex) {
      console.log('scrollTo', this.previousIndex)
      // NOTE: this is where it jumps to previous slide, make it show half of the next slide as well.
      // NOTE: figure out why explore items makes duplicates on trending load more
      swiper.slideTo(this.previousIndex - 1, 0)
    }
  },
  // watch: {
  //   recommendeds (newVal) {
  //     console.log('trending sees it:', newVal, swiper)
  //     // this.$forceUpdate()
  //     swiper.destroy()
  //     // swiper.updateSlides()
  //     // newVal.forEach(person => {
  //     //   swiper.appendSlide('')
  //     // })
  //   }
  // }
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
