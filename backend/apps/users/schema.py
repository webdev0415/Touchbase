import graphene
import requests
import apps.graphql_jwt

from apps.users.models import User, UserProfile, OAuthPost, UserSettings
from apps.users import mutations
from apps.users.obj_types import UserType, UserProfileType, OAuthPostType, PublicChangeLogType, UserSettingsType


class Query(object):
    user = graphene.Field(UserType)
    unique_username = graphene.Boolean(username=graphene.String(required=True))
    unique_email = graphene.Boolean(email=graphene.String(required=True))
    test_canada = graphene.JSONString()
    # users = graphene.List(UserType)
    own_profile = graphene.Field(UserProfileType) # id=graphene.Int(required=False)
    own_settings = graphene.Field(UserSettingsType)
    profile = graphene.Field(UserProfileType, username=graphene.String(required=True))
    # NOTE: pro feature: accept number of posts or time range to filter
    own_oauth_posts = graphene.List(OAuthPostType)
    public_changes = graphene.List(PublicChangeLogType)

    @staticmethod
    def resolve_test_canada(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            u = info.context.user
            p, created = UserProfile.objects.get_or_create(user=u)

            result = requests.post('http://canada/all', json={"it": ['business', 'music', 'health']})
            res = {'events': None}
            res['events'] = result.json()["message"]
            return res
        # else:
        #     return "{'error': 'Please login to do that' }"

    @staticmethod
    def resolve_user(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            user = info.context.user
            return user # kwargs.get('id')
        # else:
        #     return "Please login to do that"

    @staticmethod
    def resolve_unique_username(cls, info, username, **kwargs):
        return not User.objects.filter(username=username).exists()
    
    @staticmethod
    def resolve_unique_email(cls, info, email, **kwargs):
        return not User.objects.filter(email=email).exists()

    @staticmethod
    def resolve_public_changes(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            user = info.context.user
            changelog = []
            for person in info.context.user.following.following(info.context.user):
                # sort by created on frontend
                changelog.extend(person.changes.all())
            # print(changelog)
            return changelog
            

    # @staticmethod
    # def resolve_users(cls, info, **kwargs): #paginate this
    #     return User.objects.all()

    @staticmethod
    def resolve_own_settings(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            user = info.context.user
            settings = UserSettings.objects.get(user=user)
            return settings

    @staticmethod
    def resolve_own_profile(cls, info, **kwargs):
        # if info.context.user.is_authenticated:
        #     request_username = info.context.user.username
        #     user = User.objects.get(username=request_username)
        #     print(user)
        #     return UserProfile.objects.get(id=13)
        if info.context.user.is_authenticated:
            user = info.context.user
             ##################### NOTE: REMOVE GET OR CREATE FOR PROD ################################
            profile, created = UserProfile.objects.get_or_create(user=user)
            return profile
        # else:
        #     return "Please login to do that"
    
    @staticmethod
    def resolve_profile(cls, info, username, **kwargs):
        if info.context.user.is_authenticated:
            current_user = info.context.user
        user = User.objects.get(username=username)
        ##################### NOTE: REMOVE GET OR CREATE FOR PROD ################################
        profile, created = UserProfile.objects.get_or_create(user=user)
        if not username == current_user.username:
            UserProfile.objects.add_view(profile=profile)
            UserSettings.objects.add_tri_count(user=user)
        return profile

    @staticmethod
    def resolve_own_oauth_posts(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            posts = []
            for person in info.context.user.following.following(info.context.user):
                settings, created = UserSettings.objects.get_or_create(user=person)
                # NOTE: pages like /home that MUST be hard refreshed
                # should instead just refresh on arrival instead!!

                 ##################### NOTE: REMOVE GET OR CREATE FOR PROD ################################
                #  if person.settings.haspSPF
                if settings.haspSPF:
                    # print(person.username, '~~~', person.OAuthPosts.all().order_by('-id')[:5])
                    posts.extend(list(person.OAuthPosts.all().order_by('-id')[:5]))
            # return info.context.user.OAuthPosts.all()
            #implement a system where each post has a set created field
            # if different services have different created/timestamp fields, 
            # iterate and normalize so they are all the same name and same depth of iteration
            # so frontend can proeprly sort and iterate
            # print(posts)
            return posts


class Mutation(object):
    login = mutations.CustomObtainJSONWebToken.Field()
    verify_token = apps.graphql_jwt.Verify.Field()
    refresh_token = apps.graphql_jwt.Refresh.Field()
    logout = apps.graphql_jwt.Revoke.Field()
    # logout = mutations.Logout.Field()
    sign_out_all = mutations.SignOutAllDevices.Field()

    register = mutations.Register.Field()
    reset_password = mutations.ResetPassword.Field()
    reset_password_confirm = mutations.ResetPasswordConfirm.Field()
    basic_search = mutations.BasicSearch.Field()
    edit_profile = mutations.EditProfile.Field()
    edit_settings = mutations.EditSettings.Field()
