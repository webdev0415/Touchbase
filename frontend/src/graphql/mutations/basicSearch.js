import gql from 'graphql-tag'

export const BASIC_SEARCH_MUTATION = gql`
mutation basicSearch ($term: String!) {
  basicSearch(term: $term) {
    results {
      username
      profilePic
      firstName
      lastName
    }
  }
}
`