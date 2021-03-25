import gql from 'graphql-tag'

export const SEND_TRANSACTION_MUTATION = gql`
mutation sendTransaction ($orderId: String!, $phone: String!) {
  ptc (orderId: $orderId, phone: $phone) {
    success
  }
}
`