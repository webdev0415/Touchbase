// 1
import gql from 'graphql-tag'

// 2
export const ALL_FOLLOWING_QUERY = gql`
    query ($username: String!) {
      following(username: $username) {
          username
          firstName
          lastName
          profilePic
      }
    }
`