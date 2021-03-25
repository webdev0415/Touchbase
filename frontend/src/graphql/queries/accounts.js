// 1
import gql from 'graphql-tag'

// 2
export const ALL_ACCOUNTS_QUERY = gql`
    query {
        ownAccounts {
            url
            created
            service
            identifier
        }
    }
`