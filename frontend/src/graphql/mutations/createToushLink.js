import gql from 'graphql-tag'

export const CREATE_TOUSHLINK_MUTATION = gql`
mutation createToushLink (
    $isToushEvents: Boolean!, 
    $isToushFeed: Boolean!,
    $isToushProfile: Boolean!,
    $message: String!,
    $link: String!,
    $lifespan: Int!,
    $maxCount: Int!,
    $customLink: String!,
    $linkToProfile: Boolean!,
    $username: Boolean!,
    $firstName: Boolean!,
    $lastName: Boolean!,
    $contactPhone: Boolean!,
    $contactEmail: Boolean!,
    $accountsList: JSONString!,
) {
  createToushLink (
    isToushEvents: $isToushEvents,
    isToushFeed: $isToushFeed,
    isToushProfile: $isToushProfile,
    message: $message,
    link: $link,
    lifespan: $lifespan,
    maxCount: $maxCount,
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