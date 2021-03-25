// 1
import gql from 'graphql-tag'

// 2
export const PUBLIC_ACCOUNTS_QUERY = gql`
    query ($username: String!) {
        accounts (username: $username) {
            url
            created
            service
            identifier
        }
    }
`