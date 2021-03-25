import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  iconfont: 'md',
  // specify theme colors. Match with TB design guideline
  // primary will be the normal coral
  theme: {
    primary: '#FF7256',
    ogSuccess: '#4CAF50',
    success: '#22E09F',
    successTwo: '#00FF9A',
    info: '#99746D',
    error: '#F01F5E',
    primaryComp: '#FFF',
    alias: '#56B8FF',
    aliasAcc: '#3bd6bf',
  }
})
