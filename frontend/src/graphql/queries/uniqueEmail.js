import gql from 'graphql-tag'

export const UNIQUE_EMAIL_QUERY = gql`
    query ($email: String!) {
        uniqueEmail (email: $email)
    }
`