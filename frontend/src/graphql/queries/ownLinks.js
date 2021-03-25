// 1
import gql from 'graphql-tag'

// 2
export const OWN_LINKS_QUERY = gql`
query {
  ownLinks {
    id
    created
    usageCount
    lifespan
    fullUrl
    expired
    shortUrl
    item {
        isToushFeed
        isToushProfile
        isToushEvents
        message
        linkToProfile
        username
        firstName
        lastName
        contactPhone
        contactEmail
        accountsList
    }
  }
}
`