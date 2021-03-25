import gql from 'graphql-tag'

export const CREATE_PROFILEVISIT_MUTATION = gql`
mutation createProfileVisit ($viewee: String!) {
  createProfileVisit(viewee: $viewee) {
      success
      errors
  }
}
`