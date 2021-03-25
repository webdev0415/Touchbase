import gql from 'graphql-tag'

export const REGISTER_USER_MUTATION = gql`
mutation registerUser ($username: String!, $email: String!, $firstName: String!, $lastName: String!, $language: String!, $country: String!, $birthday: String!, $password: String!, $file: String!) {
    register (username: $username, email: $email, firstName: $firstName, lastName: $lastName, language: $language, country: $country, birthday: $birthday, password: $password, file: $file) {
        success
        errors
    }
    login (username: $username, password: $password) {
        token
        refreshToken
    }
}
`