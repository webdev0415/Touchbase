import gql from 'graphql-tag'

export const LOGIN_USER_MUTATION = gql`
mutation loginUser ($username: String!, $password: String!) {
  login (username: $username, password: $password) {
    token
    refreshToken
  }
}
`