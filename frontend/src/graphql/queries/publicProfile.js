// 1
import gql from 'graphql-tag'

export const PUBLIC_PROFILE_QUERY = gql `
    query ($username: String!) {
        profile (username: $username) {
            user {
                username
                firstName
                lastName
                id
                profilePic
            }
            bio
            website
            location
            education
            viewCount
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