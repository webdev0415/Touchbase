import graphene
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from django.db.models import DateTimeField

from apps.users.models import (
    User,
    UserProfile,
    UserSettings,
    OAuthPost,
    PublicChangeLog
)

@convert_django_field.register(DateTimeField)
def convert_datetimefield(field, registry=None):
    return graphene.String()

class UserType(DjangoObjectType):
    """ User type object """

    # def resolve_profile_pic(self, info):
    #     return f'{settings.AWS_STORAGE_BUCKET_NAME}.{settings.AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com/{settings.MEDIAFILES_LOCATION}/{user.token}.jpeg'

    class Meta:
        model = User
        only_fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'language',
            'country',
            'birthday',
            'registered_at',
            'profile_pic'
        ]

class OAuthPostType(DjangoObjectType):
    """ OAuthPost type object """
    class Meta:
        model = OAuthPost

class PublicChangeLogType(DjangoObjectType):
    """ changelog type object """

    def resolve_created(self, info):
        return self.created.strftime('%Y-%m-%d %H:%M')

    class Meta:
        model = PublicChangeLog

class UserSettingsType(DjangoObjectType):
    """ settings type object """

    class Meta:
        model = UserSettings
        only_fields = [
            'user',
            'views_privacy',
            'account_type',
            'notifs_enable',
            'notifs_follows',
            'notifs_new_account',
            'notifs_updates',
            'sponsored_relevant',
            'privacy_accounts',
            'privacy_follows',
            'private_profile',
            'haspSPF',
            'hasp_business',
            'hasp_celebrity'
        ]

def are_views_private(user):
    if UserProfile.objects.get(user=user).views_privacy:
        return False
    else:
        return True

# def private_resolver(cls, attname, default_value, root, info, **args):
#     user = info.context.user

    #
    #return getattr(root, attname, default_value)

#https://github.com/graphql-python/graphene/issues/798#issuecomment-405031847
# using objects

#asyncio executor
# https://github.com/graphql-python/graphene/issues/609

def is_private_field(field, user):
    profile = UserProfile.objects.get(user=user)
    #print(profile)
    profile_data = profile.profile_items_layout
    #print(profile_data)
    if profile_data["items"][field]["private"]:
        return False
    elif not profile_data["items"][field]["private"]:
        return True

class UserProfileType(DjangoObjectType):
    #### DISALLOW TOUSH_ SETTINGS LINKS
    """ Profile type object """
    # https://github.com/graphql-python/graphene/issues/105
    # IsPrivate scalar, returns None if field is private.
    # figure out how to do. Same as current solution
    # but way more DRY
    # bio = graphene.Field(IsPrivate)
    
    # def resolve_occupation(self, info):
    #     user = info.context.user
    #     field = 'ocedlo'
    #     if is_private_field(field, user):
    #         #log to console
    #         #print(self.occupation)
    #         return self.occupation
    #     else:
    #         return ""

    # def resolve_education(self, info):
    #     user = info.context.user
    #     field = 'ocedlo'
    #     if is_private_field(field, user):
    #         return self.education
    #     else:
    #         return ""

    # def resolve_location(self, info):
    #     user = info.context.user
    #     field = 'ocedlo'
    #     if is_private_field(field, user):
    #         return self.location
    #     else:
    #         return ""

    # def resolve_bio(self, info):
    #     user = info.context.user
    #     field = 'bio'
    #     if is_private_field(field, user):
    #         return self.bio
    #     else:
    #         return ""

    # def resolve_contact_email(self, info):
    #     user = info.context.user
    #     field = 'cont'
    #     if is_private_field(field, user):
    #         return self.contact_email
    #     else:
    #         return ""

    # def resolve_contact_phone(self, info):
    #     user = info.context.user
    #     field = 'cont'
    #     if is_private_field(field, user):
    #         return self.contact_phone
    #     else:
    #         return ""

    class Meta:
        model = UserProfile

