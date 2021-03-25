import gql from 'graphql-tag'

export const EDIT_SETTINGS_MUTATION = gql`
mutation editSettings (
    $accountType: String, $notifsEnable: Boolean,
    $notifsFollows: Boolean, $notifsNewAccount: Boolean,
    $notifsUpdates: Boolean, $sponsoredRelevant: Boolean,
    $privateProfile: Boolean, $privacyFollows: String,
    $privacyAccounts: String
) {
    editSettings (
        accountType: $accountType, notifsEnable: $notifsEnable,
        notifsFollows: $notifsFollows, notifsNewAccount: $notifsNewAccount,
        notifsUpdates: $notifsUpdates, sponsoredRelevant: $sponsoredRelevant,
        privateProfile: $privateProfile, privacyFollows: $privacyFollows,
        privacyAccounts: $privacyAccounts
    ) {
        success
        errors
    }
}
`