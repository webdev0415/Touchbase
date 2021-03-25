<template>
<v-layout row fill-height align-center justify-center v-if="$apollo.loading">
    <v-progress-circular class="text-xs-center" indeterminate color="primary"></v-progress-circular>
</v-layout>

<v-layout v-else row class="px-4" justify-center fill-height>
    <v-flex xs12 sm8 md7 lg5>
        <v-form ref="editProfileForm" lazy-validation>
            <v-layout column align-center class="pb-5">
                <v-flex>
                    <p class="display-1 font-weight-regular grey--text text--darken-2 mt-4">
                        <span>Edit</span>
                        <span class="mx-2">My</span>
                        <span>Profile</span>
                    </p>
                    <!-- <p class="display-2 text-uppercase font-weight-light grey--text text--darken-1 mt-3">
                        <span>E<span class="display-1">dit</span></span>
                        <span class="mx-4">M<span class="display-1">y</span></span>
                        <span>P<span class="display-1">rofile</span></span>
                    </p> -->
                </v-flex>
                <!-- @click = image upload -->
                <v-flex @click="editImage = true" v-if="!editImage" style="cursor: pointer;" class="mt-4">
                    <v-badge color="grey darken-3" overlap>
                        <v-icon dark slot="badge">close</v-icon>
                        <img class="elevation-3" style="border-radius: 10px; max-height: 400px; max-width: 400px;" :src="profilePic"></img>
                    </v-badge>
                    <p class="text-xs-center font-weight-light subheading grey--text text--darken-1 mt-1">Click to change</p>
                </v-flex>
                <v-flex v-else class="mt-4">
                    <img-inputer v-if="!cropping && !cropped" icon="img" class="mb-1" accept="image/*" :maxSize="1024" @onExceed="exceedHandler" @onChange="fileChange"
                        no-mask no-multiple-text="Only one image" exceed-size-text="Too large! File size must be below "
                        placeholder="Drag and drop or click to browse" style="background-color: rgba(255, 255, 255, 0.25); max-height: 100%; max-width: 100%;"
                    />
                    <template
                        v-if="cropping && !cropped"
                    >
                        <Cropper
                        ref="cropper"
                        :stencil-props="{
                            aspectRatio: 1
                        }"
                        classname="crop-img"
                        :src="file"
                        />
                        <v-layout row>
                        <v-btn @click="resetImage" block color="black" flat>
                            <v-icon>close</v-icon>
                        </v-btn>
                        <v-btn @click="crop" block color="black" flat>
                            <v-icon>check</v-icon>
                        </v-btn>
                        </v-layout>
                    </template>
                    <!-- <img-inputer v-if="cropped" class="mb-1" no-mask readonly :imgSrc="fileUrl"
                        placeholder="Drag and drop a picture or click to browse" style="background-color: rgba(0, 0, 0, 0.15);"
                    /> -->
                    <v-badge v-if="cropped" color="grey darken-3" overlap>
                        <v-icon style="cursor: pointer;" @click="resetImage" dark slot="badge">close</v-icon>
                        <img class="elevation-3" style="border-radius: 10px; max-height: 400px; max-width: 400px;" :src="fileUrl"></img>
                    </v-badge>
                    <p class="text-xs-center font-weight-light subheading grey--text text--darken-1 mt-1">Save to finish updating</p>
                </v-flex>

                <v-flex style="width: 100%;" class="mb-3 mt-2">
                    <span class="text-uppercase grey--text mt-1">Profile</span>
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <v-icon color="alias" class="ml-3 pb-2">help</v-icon>
                    </v-layout>
                    <p v-if="feedback" class="red--text my-2 text-xs-center">Something went wrong. Double check the form please.</p>
                    <p v-if="feedbackEmpty" class="red--text my-2 text-xs-center">Please make an edit before saving.</p>
                </v-flex>
                <v-flex style="width: 100%;">
                    <v-layout row wrap>
                        <v-flex xs12 md6 :class="pRight">
                            <v-text-field
                                outline
                                label="Username"
                                :hint="`@${ownProfile.user.username} | Changing will sign you out`"
                                v-model="editUsername"
                                persistent-hint
                                prepend-inner-icon="person"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 md6 :class="pLeft">
                            <v-text-field
                                outline
                                label="Email"
                                :hint="`${ownProfile.user.email}`"
                                v-model="editEmail"
                                persistent-hint
                                prepend-inner-icon="mail"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 class="my-4">
                            <v-chip text-color="white" class="verified-chip subheading" color="aliasAcc" @click="$router.push('/plans/verified')">
                                <v-avatar
                                    color="white"
                                >
                                    <img style="height: 40px; width: 40px;" src="/img/avatar-2.png" alt="profile picture">
                                </v-avatar>
                                
                                <span class="ml-2">{{ editFirstName }} {{ editLastName }}</span>
                                <!-- <v-icon class="mr-2">close</v-icon> -->
                                <div style="position: absolute; left: 37%;">
                                    <span class="mr-2">Get the Verified Tag</span>
                                    <v-icon>verified_user</v-icon>
                                </div>
                                
                                <v-icon class="mr-3" style="position: absolute; right: 0;">exit_to_app</v-icon>
                            </v-chip>
                        </v-flex>
                        <v-flex xs12 md6 :class="pRight">
                            <v-text-field
                                outline
                                label="First Name"
                                :hint="`${ownProfile.user.firstName}`"
                                v-model="editFirstName"
                                persistent-hint
                                prepend-inner-icon="list"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 md6 :class="pLeft">
                            <v-text-field
                                outline
                                label="Last Name"
                                :hint="`${ownProfile.user.lastName}`"
                                v-model="editLastName"
                                persistent-hint
                                prepend-inner-icon="list"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 class="mt-3">
                            <v-select
                                :items="interestTagItems"
                                v-model="editInterestTags"
                                outline
                                multiple
                                chips
                                single-line
                                :height="`${Math.ceil(editInterestTags.length / 6.5) * 38}px`"
                                small-chips
                                hint="Interest Tags"
                                persistent-hint
                                prepend-inner-icon="view_carousel"
                            >
                                <template slot="label">
                                    <span class="pl-2">Interest Tags</span>
                                </template>
                                
                            </v-select>
                        </v-flex>
                    </v-layout>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-4 mb-3">
                    <span class="text-uppercase grey--text mt-1">Info</span>
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <v-icon color="alias" class="ml-3 pb-2">help</v-icon>
                    </v-layout>
                </v-flex>
                <v-flex style="width: 100%;">
                    <v-layout row wrap>
                        <v-flex xs12 md6 :class="pRight">
                            <v-text-field
                                outline
                                label="Location"
                                :hint="`${ownProfile.location}`"
                                v-model="editLocation"
                                persistent-hint
                                prepend-inner-icon="location_on"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 md6 :class="pLeft">
                            <v-text-field
                                outline
                                label="Occupation"
                                :hint="`${ownProfile.occupation}`"
                                v-model="editOccupation"
                                persistent-hint
                                prepend-inner-icon="work"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 class="my-4">
                            <v-text-field
                                outline
                                label="Biography"
                                :hint="`${ownProfile.bio}`"
                                v-model="editBio"
                                persistent-hint
                                prepend-inner-icon="comment"
                                counter="128"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 md6 :class="pRight">
                            <v-text-field
                                outline
                                label="Education"
                                :hint="`${ownProfile.education}`"
                                v-model="editEducation"
                                persistent-hint
                                prepend-inner-icon="school"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 md6 :class="pLeft">
                            <v-text-field
                                outline
                                label="Website"
                                :hint="`${ownProfile.website}`"
                                v-model="editWebsite"
                                persistent-hint
                                prepend-inner-icon="link"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex class="py-2" xs12>
                            
                        </v-flex>
                        <v-flex xs12 md6 :class="pRight">
                            <v-text-field
                                outline
                                label="Contact Email"
                                :hint="`${ownProfile.contactEmail}`"
                                v-model="editContactEmail"
                                persistent-hint
                                prepend-inner-icon="mail"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 md6 :class="pLeft">
                            <v-text-field
                                outline
                                label="Contact Phone"
                                :hint="`${ownProfile.contactPhone}`"
                                v-model="editContactPhone"
                                persistent-hint
                                prepend-inner-icon="phone"
                                counter="32"
                            ></v-text-field>
                        </v-flex>
                    </v-layout>
                </v-flex>
                <v-flex style="width: 100%;" class="mt-5 mb-3">
                    <span class="text-uppercase grey--text mt-1">Privacy</span>
                    <v-layout row align-center>
                        <v-divider class="mt-1 mb-3"></v-divider>
                        <v-icon color="alias" class="ml-3 pb-2">help</v-icon>
                    </v-layout>
                </v-flex>
                <v-flex class="mb-5">
                    <v-btn large flat to="/settings#privacy" class="animated-box in font-weight-medium subheading" color="primary">Go To Settings</v-btn>
                </v-flex>
                
            </v-layout>
        </v-form>
        
    </v-flex>
    <v-btn @click="edit()" color="primary" fixed bottom right style="height: 50px;">
        <span class="mr-2">Save</span>
        <v-icon>check</v-icon>
    </v-btn>
</v-layout>
</template>

<script>
import { Cropper } from 'vue-advanced-cropper'
import { onLogout } from '@/apollo'
import { FULL_PROFILE_QUERY } from '@/graphql/queries/profile'
import { EDIT_PROFILE_MUTATION } from '@/graphql/mutations/editProfile'
import { mapMutations } from 'vuex'

export default {
    name: 'EditProfile',
    components: {
        Cropper
    },
    data() {
        return {
            username: 'memes',
            ownProfile: {},
            editLoading: false,
            editImage: false,
            feedback: false,
            feedbackEmpty: false,
            feedbackQuery: false,
            editInterestTags: [],
            editUsername: '',
            editEmail: '',
            editFirstName: '',
            editLastName: '',
            editLocation: '',
            editOccupation: '',
            editBio: '',
            editEducation: '',
            editWebsite: '',
            editContactEmail: '',
            editContactPhone: '',
            profilePic: '',
            cropping: false,
            cropped: false,
            file: null,
            fileUrl: null,
        }
    },
    computed: {
        saveBtn() {
            if (this.$vuetify.breakpoint.smAndDown) {
                // return { 'mb-5': true, 'elevation-3': true }
                return { 'elevation-3': true }
            } else {
                return { 'elevation-3': true }
            }
        },
        interestTagItems() {
            return this.$store.state.interestTagItems
        },
        responsiveDimProfPic() {
            switch (this.$vuetify.breakpoint.name) {
                case 'xs': return 120
                case 'sm': return 130
                case 'md': return 140
                case 'lg': return 150
                case 'xl': return 160
            }
        },
        pRight() {
            if (this.$vuetify.breakpoint.mdAndUp) {
                return {
                    'pr-2': true
                }
            }
        },
        pLeft() {
            if (this.$vuetify.breakpoint.mdAndUp) {
                return {
                    'pl-2': true
                }
            }
        }
    },
    methods: {
        ...mapMutations([
            'unsetToken'
        ]),
        resetImage() {
            this.cropping = false
            this.cropped = false
            this.file = null
            this.fileUrl = null
        },
        crop() {
            const { coordinates, canvas, } = this.$refs.cropper.getResult()
            this.fileUrl = canvas.toDataURL('image/jpeg', 0.8)
            this.cropping = false
            this.cropped = true
        },
        fileChange(file, name) {
            console.log("File --> ", file)
            console.log("FileName -->", name)
            let r = new FileReader()
            r.onload = (e) => {
                this.file = e.target.result
                this.cropping = true
            }
            r.readAsDataURL(file)
        },
        onErr(err, file) {
            console.log("​onErr -> file", file);
            console.log("​onErr -> err", err);
        },
        exceedHandler(file) {
            console.warn("onExceed -> file", file);
        },
        logout() {
            this.unsetToken()
            onLogout(this.$apollo.provider.defaultClient)
            .then(() => {
                location.href = '/'
            })
        },
        edit() {
            if (this.$refs.editProfileForm.validate()) {
                this.editLoading = true

                let changed = []

                if (this.editInterestTags != this.ownProfile.interestTags) changed.push('interest_tags')
                if (this.editUsername != this.ownProfile.user.username) changed.push('username')
                if (this.editEmail != this.ownProfile.user.email) changed.push('email')
                if (this.editFirstName != this.ownProfile.user.firstName) changed.push('first_name')
                if (this.editLastName != this.ownProfile.user.lastName) changed.push('last_name')
                if (this.editLocation != this.ownProfile.location) changed.push('location')
                if (this.editOccupation != this.ownProfile.occupation) changed.push('occupation')
                if (this.editBio != this.ownProfile.bio) changed.push('bio')
                if (this.editEducation != this.ownProfile.education) changed.push('education')
                if (this.editWebsite != this.ownProfile.website) changed.push('website')
                if (this.editContactEmail != this.ownProfile.contactEmail) changed.push('contact_email')
                if (this.editContactPhone != this.ownProfile.contactPhone) changed.push('contact_phone')
                if (this.fileUrl) changed.push('profile_pic')


                const interestTags = this.editInterestTags
                const username = this.editUsername
                const email = this.editEmail
                const firstName = this.editFirstName
                const lastName = this.editLastName
                const location = this.editLocation
                const occupation = this.editOccupation
                const bio = this.editBio
                const education = this.editEducation
                const website = this.editWebsite
                const contactEmail = this.editContactEmail
                const contactPhone = this.editContactPhone
                const file = this.fileUrl

                if (changed.length > 0) {
                    this.$apollo.mutate({
                        mutation: EDIT_PROFILE_MUTATION,
                        variables: {
                            changed,
                            interestTags,
                            username,
                            email,
                            firstName,
                            lastName,
                            location,
                            occupation,
                            bio,
                            education,
                            website,
                            contactEmail,
                            contactPhone,
                            file
                        }
                    }).then(result => {
                        if (result.data.editProfile.success) {
                            this.editLoading = false
                            if (changed.includes('username')) {
                                this.logout()
                            } else {
                                this.$router.push({ name: 'MyProfile'})
                            }
                            
                        } else {
                            this.editLoading = false
                            this.feedback = true
                            console.log(result.data.editProfile.errors)
                        }
                    }).catch(err => {
                        console.log(err)
                        this.editLoading = false
                        this.feedback = true
                    })
                } else {
                    this.editLoading = false
                    this.feedbackEmpty = true
                }
                
            }
        }
    },
    apollo: {
        ownProfile: {
            query: FULL_PROFILE_QUERY,
            result({ data, loading }) {
                if (!loading && data.ownProfile) {
                    if (data.ownProfile) {
                        this.editInterestTags = data.ownProfile.interestTags
                        this.editUsername = data.ownProfile.user.username
                        this.editEmail = data.ownProfile.user.email
                        this.editFirstName = data.ownProfile.user.firstName
                        this.editLastName = data.ownProfile.user.lastName
                        this.editLocation = data.ownProfile.location
                        this.editOccupation = data.ownProfile.occupation
                        this.editBio = data.ownProfile.bio
                        this.editEducation = data.ownProfile.education
                        this.editWebsite = data.ownProfile.website
                        this.editContactEmail = data.ownProfile.contactEmail
                        this.editContactPhone = data.ownProfile.contactPhone
                        this.profilePic = data.ownProfile.user.profilePic
                    }
                }
            },
            error(err) {
                console.log(err)
                this.feedbackQuery = true
            }
        },
    },

}
</script>

<style>

.verified-chip {
    width: 100%; 
    height: 40px; 
    cursor: pointer;
    /* box-shadow: 1px 2px 10px #22BDA6; */
}
</style>