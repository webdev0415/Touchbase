import gql from 'graphql-tag'

export const SIGN_OUT_ALL_MUTATION = gql`
mutation {
    signOutAll {
        success
    }
}
`