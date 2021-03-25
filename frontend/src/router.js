import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import Explore from '@/components/Explore'
// import ApolloTest from '@/views/ApolloTest'
import Login from '@/components/Login'
import Signup from '@/components/Signup'
import MyProfile from '@/components/me/MyProfile'
// import Accounts from '@/components/me/Accounts'
import Settings from '@/components/me/Settings'
import Profile from '@/components/Profile'
import Advertise from '@/components/Advertise'
import Links from '@/components/me/Links'
import EditLink from '@/components/me/EditLink'
import EditProfile from '@/components/me/EditProfile'
import SplashScreen from '@/components/plans/SplashScreen'
import Following from '@/components/me/Following'
import Followers from '@/components/me/Followers'
import OwnFollowing from '@/components/me/OwnFollowing'
import OwnFollowers from '@/components/me/OwnFollowers'
import Support from '@/components/Support'
import FAQ from '@/components/FAQ'



const routes = [
  {
    path: '/',
    component: Home,
    name: 'Home'
  },
  {
    path: '/advertise',
    component: Advertise,
    name: 'Advertise'
  },
  {
    path: '/support',
    component: Support,
    name: 'Support'
  },
  {
    path: '/faq',
    component: FAQ,
    name: 'FAQ'
  },
  {
    path: '/plans/splash-screen',
    component: SplashScreen,
    name: 'SplashScreen'
  },
  {
    path: '/login',
    component: Login,
    name: 'Login'
  },
  {
    path: '/signup',
    component: Signup,
    name: 'Signup'
  },
  {
    path: '/me',
    component: MyProfile,
    name: 'MyProfile'
  },
  {
    path: '/me/edit',
    component: EditProfile,
    name: 'EditProfile'
  },
  {
    path: '/:username/following',
    component: Following,
    name: 'Following'
  },
  {
    path: '/:username/followers',
    component: Followers,
    name: 'Followers'
  },
  {
    path: '/following',
    component: OwnFollowing,
    name: 'OwnFollowing'
  },
  {
    path: '/followers',
    component: OwnFollowers,
    name: 'OwnFollowers'
  },
  {
    path: '/links',
    component: Links, // change to Link settings component
    name: 'Links'
  },
  {
    path: '/links/:toushString/edit',
    component: EditLink,
    name: 'EditLink'
  },
  // {
  //   path: '/accounts',
  //   component: Accounts, // change to Link settings component
  //   name: 'Accounts'
  // },
  {
    path: '/settings',
    component: Settings, // change to Link settings component
    name: 'Settings'
  },
  // {
  //   path: '/saved',
  //   component: MyProfile, // idk
  //   name: 'Saved'
  // },

  {
    path: '/explore',
    component: Explore,
    name: 'Explore'
  },
  {
    path: '/alias',
    component: Home,
    name: 'Alias'
  },
  {
    path: '/themes',
    component: Home,
    name: 'Themes'
  },
  {
    path: '/sitemap',
    component: Home,
    name: 'Sitemap'
  },
  {
    path: '/legal',
    component: Home,
    name: 'Legal'
  },

  // {
  //   path: '/?redirect=:',
  //   component: Toush,
  //   name: 'Toush'
  // },

  {
    path: '/:username',
    component: Profile,
    name: 'Profile',
    //props: true //(route) => ({ query: route.params.username })
  }
  // {
  //   path: '/apollo-test',
  //   component: ApolloTest,
  //   name: 'ApolloTest'
  // },
]

Vue.use(Router)
const router = new Router({
  // scroll behavior. preserve scrolling pos of last page
  // or if it doesn't exist, keep it at the top.
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  },
  mode: 'history',
  routes
})

export default router
