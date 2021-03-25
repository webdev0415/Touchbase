import gql from 'graphql-tag'

export const FOLLOW_USER_MUTATION = gql`
mutation followUser ($usernameFollowee: String!) {
  follow(usernameFollowee: $usernameFollowee) {
      success
      errors
  }
}
`