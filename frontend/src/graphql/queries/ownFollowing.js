// 1
import gql from 'graphql-tag'

// 2
export const OWN_FOLLOWING_QUERY = gql`
    query {
      ownFollowing {
          username
          firstName
          lastName
          profilePic
      }
    }
`