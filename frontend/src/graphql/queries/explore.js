import gql from 'graphql-tag'

export const EXPLORE_QUERY = gql`
    query ($page: Int) {
        explore (page: $page) {
            people {
                id
                username
                firstName
                lastName
                profilePic
            }
            cliques {
                id
                name
                caption
                thumbnail
                created
                cliqueTags
                viewCount
            }
            brands {
                name
                caption
            }
        }
    }
`