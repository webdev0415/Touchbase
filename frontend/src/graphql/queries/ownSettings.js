// 1
import gql from 'graphql-tag'

// 2
export const OWN_SETTINGS_QUERY = gql`
query {
    ownSettings {
        accountType
        haspSPF
        notifsEnable
        notifsFollows
        notifsUpdates
        notifsNewAccount
        sponsoredRelevant
        privateProfile
        haspBusiness
        haspCelebrity
        privateProfile
        privacyFollows
        privacyAccounts
        user {
            username
            firstName
            lastName
            email
            profilePic
        }
    }
}
`