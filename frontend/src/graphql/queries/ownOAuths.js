// 1
import gql from 'graphql-tag'

// 2
export const OWN_OAUTHS_QUERY = gql`
query {
  ownOauthPosts {
    user {
        username
        firstName
        lastName
        profilePic
    }
    created
    service
    pdj
  }
}
`