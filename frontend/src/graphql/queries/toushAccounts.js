// 1
import gql from 'graphql-tag'

// 2
export const TOUSH_ACCOUNTS_QUERY = gql`
    query ($shortUrl: String!) {
        toushAccounts (shortUrl: $shortUrl) {
            url
            created
            service
            identifier
        }
    }
`