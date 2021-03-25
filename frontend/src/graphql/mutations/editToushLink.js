import gql from 'graphql-tag'

export const EDIT_TOUSHLINK_MUTATION = gql`
mutation editToushLink (
    $changed: [String]!,
    $toushString: String!,
    $message: String!,
    $customLink: String!,
    $linkToProfile: Boolean!,
    $username: Boolean!,
    $firstName: Boolean!,
    $lastName: Boolean!,
    $contactPhone: Boolean!,
    $contactEmail: Boolean!,
    $accountsList: JSONString!,
    ) {
        editToushLink (
            toushString: $toushString,
            changed: $changed,
            message: $message,
            customLink: $customLink,
            linkToProfile: $linkToProfile,
            username: $username,
            firstName: $firstName,
            lastName: $lastName,
            contactPhone: $contactPhone,
            contactEmail: $contactEmail,
            accountsList: $accountsList
        ) {
            errors
            success
        }
}
`