import gql from 'graphql-tag'

export const CREATE_SITEVISIT_MUTATION = gql`
mutation createSiteVisit ($page: String!) {
  createSiteVisit(page: $page) {
      success
      errors
  }
}
`