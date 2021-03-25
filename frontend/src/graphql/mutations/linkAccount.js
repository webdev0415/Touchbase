import gql from 'graphql-tag'

export const LINK_ACCOUNT_MUTATION = gql`
mutation linkAccount ($identifier: String!, $service: String!, $spfIdentifier: String!, $shareSPF: Boolean!) {
  linkAccount (identifier: $identifier, service: $service, shareSpf: $shareSPF, spfIdentifier: $spfIdentifier) {
    success
  }
}
`