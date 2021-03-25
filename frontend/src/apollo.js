import Vue from 'vue'
import VueApollo from 'vue-apollo'
import { createApolloClient } from 'vue-cli-plugin-apollo/graphql-client'

import { ApolloClient } from 'apollo-client'
// import { HttpLink } from 'apollo-link-http'
import { createUploadLink } from 'apollo-upload-client'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { onError } from 'apollo-link-error'
import { ApolloLink } from 'apollo-link'

Vue.use(VueApollo)

const cache = new InMemoryCache()

// NOTE TODO:
// THIS CODE DOESN'T APPLY TO MUTATIONS
// IN MUTATIONS, MANUALLY RECALL THE THIS.SUBMIT METHOD IN .CATCH(ERR)
// new: maybe mutation needs additional param and operation is just null rn
const link = ApolloLink.from([
  onError(({ graphQLErrors, networkError, operation, forward }) => {
    return forward(operation)
    // if (graphQLErrors) {
    //   graphQLErrors.forEach( ({ message, locations, path }) => {
    //     if (message === 'tokensRefreshed') {
    //       return forward(operation)
    //     } else if (message.includes('authenticate') && message.includes('ass')) {
    //       location.href = '/login'
    //     } else if ((message.includes('please') || message.includes('must')) && (message.includes('authenticate') || message.includes('login'))) {
    //       location.href = '/login'
    //     } else {
    //       console.log(`[GraphQL memes error]: Message: ${message}, Location: ${locations}, Path: ${path}`)
    //     }
    //   })
    // }
    // if (networkError) console.log(`[Network memes error]: ${networkError}`)
  }),
  createUploadLink()
  // new HttpLink({
  //   uri: '/graphql',
  //   credentials: 'same-origin'
  // })
])

// if (typeof window !== 'undefined') {
//   // eslint-disable-next-line no-underscore-dangle
//   const state = window.__APOLLO_STATE__
//   if (state && state[clientId]) {
//     // Restore state
//     cache.restore(state[clientId])
//   }
// }

const apolloClient = new ApolloClient({
  link,
  cache,
})

// Call this in the Vue app file
export function createProvider () {
  // Create vue apollo provider
  const apolloProvider = new VueApollo({
    defaultClient: apolloClient,
    defaultOptions: {
      $query: {
        loadingKey: 'loading',
        fetchPolicy: 'no-cache'
      }
    },
    errorHandler (error) {
      // eslint-disable-next-line no-console
      // console.log('%cError', 'background: red; color: white; padding: 2px 4px; border-radius: 3px; font-weight: bold;', error.message)
      // error.message
    }
  })

  return apolloProvider
}

// Manually call this when user log in
export async function onLogin (apolloClient, username) {
  localStorage.setItem('jwt-token', 'true')
  localStorage.setItem('username', username)
  try {
    await apolloClient.resetStore()
  } catch (e) {
    console.log('%cError on cache reset (login)', 'color: orange;', e.message)
  }
}

// Manually call this when user log out
export async function onLogout (apolloClient) {
  // TODO: delete auth cookies
  localStorage.removeItem('jwt-token')
  localStorage.removeItem('username')
  try {
    await apolloClient.resetStore()
  } catch (e) {
    console.log('%cError on cache reset (logout)', 'color: orange;', e.message)
  }
}


