// 1
import gql from 'graphql-tag'

// 2
export const OWN_CHANGES_QUERY = gql`
    query {
      publicChanges {
          service
          statement
          created
          user {
              username
              firstName
              lastName
              profilePic
          }
      }
    }
`