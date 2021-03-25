// 1
import gql from 'graphql-tag'

// Don't use this for Edit Toush, make new query for that
export const RESOLVE_TOUSH_QUERY = gql`
query ($shortUrl: String!, $edit: Boolean) {
    expand(shortUrl: $shortUrl, edit: $edit) {
        created
        usageCount
        shortUrl
        lifespan
        expired
        item {
            accountsList
            username
            firstName
            lastName
            contactEmail
            contactPhone
            isToushProfile
            linkToProfile
            isToushFeed
            isToushEvents
            created
            message
            user {
                profilePic
                username
                firstName
                lastName
            }
        }
    }
}
`