import gql from 'graphql-tag'

export const UNFOLLOW_USER_MUTATION = gql`
mutation unfollowUser ($usernameFollowee: String!) {
  unfollow(usernameFollowee: $usernameFollowee) {
      success
      errors
  }
}
`