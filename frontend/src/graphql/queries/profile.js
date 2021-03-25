// 1
import gql from 'graphql-tag'



// NOTE: SECURITY: REMOVE EMAIL UNDER USER FROM HERE
// 2
export const FULL_PROFILE_QUERY = gql`
    query {
        ownProfile {
            user {
                username
                firstName
                lastName
                profilePic
                email
                id
            }
            bio
            interestTags
            website
            viewCount
            location
            education
            isCompany
            isVerified
            isBusiness
            isDeveloper
            isCelebrity
            occupation
            contactPhone
            contactEmail
        }
    }
`

