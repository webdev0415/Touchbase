// import { ApolloClient } from 'apollo-client'
// import { split, from } from 'apollo-link'
// import { createUploadLink } from 'apollo-upload-client'
// import { InMemoryCache } from 'apollo-cache-inmemory'
// import { getMainDefinition } from 'apollo-utilities'
// import { createPersistedQueryLink } from 'apollo-link-persisted-queries'
// import { setContext } from 'apollo-link-context'
// import { withClientState } from 'apollo-link-state'
// import { createNetworkInterface } from 'apollo-client'

// // Create the apollo client
// export function createApolloClient ({
//   // Client ID if using multiple Clients
//   clientId = 'defaultClient',
//   // URL to the HTTP API
//   httpEndpoint,
//   // Token used in localstorage
//   tokenName = 'apollo-token',
//   // Enable this if you use Query persisting with Apollo Engine
//   persisting = false,
//   // Custom starting link.
//   // If you want to replace the default HttpLink, set `defaultHttpLink` to false
//   link = null,
//   // If true, add the default HttpLink.
//   // Disable it if you want to replace it with a terminating link using `link` option.
//   defaultHttpLink = true,
//   // Options for the default HttpLink
//   httpLinkOptions = {},
//   // Custom Apollo cache implementation (default is apollo-cache-inmemory)
//   cache = null,
//   // Options for the default cache
//   inMemoryCacheOptions = {},
//   // Additional Apollo client options
//   apollo = {},
//   // apollo-link-state options
//   clientState = null,
//   // Function returning Authorization header token
//   getAuth = defaultGetAuth,
//   // Local Schema
//   typeDefs = undefined,
//   // Local Resolvers
//   resolvers = undefined,
//   // Hook called when you should write local state in the cache
//   onCacheInit = undefined,
// }) {

//   // Apollo cache
//   if (!cache) {
//     cache = new InMemoryCache(inMemoryCacheOptions)
//   }

//   const httpLink = createUploadLink({
//       uri: httpEndpoint,
//       ...httpLinkOptions,
//   })

//   if (!link) {
//       link = httpLink
//   } else if (defaultHttpLink) {
//       link = from([link, httpLink])
//   }

//   // HTTP Auth header injection
//   authLink = setContext((_, { headers }) => {
//       const authorization = getAuth(tokenName)
//       const authorizationHeader = authorization ? { authorization } : {}
//       return {
//       headers: {
//           ...headers,
//           ...authorizationHeader,
//       },
//       }
//   })

//   // Concat all the http link parts
//   link = authLink.concat(link)

//   // On the server, we don't want WebSockets and Upload links

//   // If on the client, recover the injected state
//   if (typeof window !== 'undefined') {
//     // eslint-disable-next-line no-underscore-dangle
//     const state = window.__APOLLO_STATE__
//     if (state && state[clientId]) {
//       // Restore state
//       cache.restore(state[clientId])
//     }
//   }

//   if (!disableHttp) {
//     if (persisting) {
//       link = createPersistedQueryLink().concat(link)
//     }
//   }

//   if (clientState) {
//     console.warn(`clientState is deprecated, see https://vue-cli-plugin-apollo.netlify.com/guide/client-state.html`)
//     stateLink = withClientState({
//       cache,
//       ...clientState,
//     })
//     link = from([stateLink, link])
//   }

//   const networkInterface = createNetworkInterface([
//     uri: 'http://192.168.0.26'
//   ])

//   networkInterface.use([{
//     apply
//   }])

//   const apolloClient = new ApolloClient({
//     link,
//     cache,
//     typeDefs,
//     resolvers,
//     ...apollo,
//   })

//   // Re-write the client state defaults on cache reset
//   if (stateLink) {
//     apolloClient.onResetStore(stateLink.writeDefaults)
//   }

//   if (onCacheInit) {
//     onCacheInit(cache)
//     apolloClient.onResetStore(() => {
//       onCacheInit(cache)
//     })
//   }

//   return {
//     apolloClient,
//     stateLink,
//   }
// }

// function defaultGetAuth (tokenName) {
//   if (typeof window !== 'undefined') {
//     // get the authentication token from local storage if it exists
//     const token = window.localStorage.getItem(tokenName)
//     // return the headers to the context so httpLink can read them
//     return token ? `Bearer ${token}` : ''
//   }
// }