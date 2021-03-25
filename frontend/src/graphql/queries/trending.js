import gql from 'graphql-tag'

export const TRENDING_QUERY = gql`
    query ($count: Int, $skip: Int) {
        trending (count: $count, skip: $skip) {
            id
            profilePic
            username
            firstName
            lastName
        }
    }
`