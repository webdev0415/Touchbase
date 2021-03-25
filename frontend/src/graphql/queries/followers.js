// 1
import gql from 'graphql-tag'

// 2
export const ALL_FOLLOWERS_QUERY = gql`
    query ($username: String!) {
      followers(username: $username) {
          username
          firstName
          lastName
          profilePic
      }
    }
`