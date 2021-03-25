<template>
    <div class="swiper-container filtersSwiper">
        <v-layout row align-center class="swiper-wrapper pt-2">
            <v-flex style="padding: 0 1%;" class="swiper-slide grey--text text--darken-2 text-xs-center" v-for="(filter, index) in filters" :key="index">
                <v-chip color="grey lighten-2" @click="selected.push(filter)" @input="selected.pop(filter)" :selected="selected.includes(filter)" :close="selected.includes(filter)" >{{ filter }}</v-chip>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import "swiper/dist/css/swiper.min.css"
import Swiper from 'swiper'

export default {
//   props: ["filters"],
  data() {
      return {
          selected: [],
      }
  },
  computed: {
    // slidesPerView() {
    //   switch (this.$vuetify.breakpoint.name) {
    //     case 'xs': return 6
    //     case 'sm': return 7
    //     case 'md': return 8
    //     case 'lg': return 9
    //     case 'xl': return 10
    //   }
    // },
    filters() {
        return this.$store.state.interestTagItems
    },
    responsiveProfPic() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return 70
        case 'sm': return 75
        case 'md': return 80
        case 'lg': return 85
        case 'xl': return 90
      }
    }
  },
  mounted() {
    let self = this
    const el = '.filtersSwiper'
    const swiper = new Swiper(el, {
      slidesPerView: 'auto',
      mousewheel: true,
      mousewheel: {
        sensitivity: 0.6,
      },
      freeMode: true,
      freeModeSticky: false,
      freeModeMomentumRatio: 0.4,
      grabCursor: true,
      direction: 'horizontal',
    })
  }
};
</script>

<style scoped>
.swiper-slide {
    width: auto;
}
</style>