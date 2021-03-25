// 1
import gql from 'graphql-tag'

// 2
export const IS_FOLLOWING_QUERY = gql`
    query isFollowingQuery ($unFollower: String!, $unFollowee: String!) {
        isFollowing (unFollower: $unFollower, unFollowee: $unFollowee)
    }
`