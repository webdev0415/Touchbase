import gql from 'graphql-tag'

export const UNIQUE_USERNAME_QUERY = gql`
    query ($username: String!) {
        uniqueUsername (username: $username)
    }
`