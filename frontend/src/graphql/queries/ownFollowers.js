// 1
import gql from 'graphql-tag'

// 2
export const OWN_FOLLOWERS_QUERY = gql`
    query {
      ownFollowers {
          username
          firstName
          lastName
          profilePic
      }
    }
`