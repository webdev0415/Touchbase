// changed = graphene.List(graphene.String, required=True)
// interest_tags = graphene.List(graphene.String, required=False)

// username = graphene.String(required=True)
// first_name = graphene.String(required=False)
// last_name = graphene.String(required=False)
// email = graphene.String(required=False)

// occupation = graphene.String(required=False)
// bio = graphene.String(required=False)
// education = graphene.String(required=False)
// location = graphene.String(required=False)
// website = graphene.String(required=False)
// contact_phone = graphene.String(required=False)
// contact_email = graphene.String(required=False)


import gql from 'graphql-tag'

export const EDIT_PROFILE_MUTATION = gql`
mutation editProfile (
    $changed: [String]!,
    $interestTags: [String]!,
    $username: String!,
    $firstName: String!,
    $lastName: String!,
    $email: String!,
    $occupation: String!,
    $education: String!,
    $location: String!,
    $website: String!,
    $contactPhone: String!,
    $contactEmail: String!,
    $bio: String!,
    $file: String!,
    ) {
        editProfile (
            changed: $changed,
            interestTags: $interestTags,
            username: $username,
            firstName: $firstName,
            lastName: $lastName,
            email: $email,
            occupation: $occupation,
            education: $education,
            location: $location,
            website: $website,
            contactPhone: $contactPhone,
            contactEmail: $contactEmail,
            bio: $bio,
            file: $file,
        ) {
            errors
            success
        }
}
`