import gql from 'graphql-tag'

export const WHO_TO_FOLLOW_QUERY = gql`
    query ($count: Int, $skip: Int, $default: Boolean) {
        wtf (count: $count, skip: $skip, default: $default) {
            id
            profilePic
            username
            firstName
            lastName
        }
    }
`