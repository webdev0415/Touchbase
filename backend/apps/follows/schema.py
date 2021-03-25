import graphene

from django.conf import settings

from apps.follows.models import Follow
from apps.users.obj_types import UserType
from apps.users.models import User
from apps.follows import mutations

#hook this up to project level schema.py

class Query(object):
    # followers = graphene.Field(FollowType)
    # following = graphene.Field(FollowType)
    own_followers = graphene.List(UserType)
    own_following = graphene.List(UserType)
    followers = graphene.List(UserType, username=graphene.String(required=True))
    following = graphene.List(UserType, username=graphene.String(required=True))
    follower_count = graphene.Int(username=graphene.String(required=True))
    following_count = graphene.Int(username=graphene.String(required=True))
    is_following = graphene.Boolean(un_follower=graphene.String(required=True), un_followee=graphene.String(required=True))

    @staticmethod
    def resolve_own_followers(self, info):
         if info.context.user.is_authenticated:
            user = info.context.user
            return Follow.objects.followers(user)
        
    @staticmethod
    def resolve_own_following(self, info):
         if info.context.user.is_authenticated:
            user = info.context.user
            return Follow.objects.following(user)

    @staticmethod
    def resolve_followers(self, info, username):
        # is_private
         if info.context.user.is_authenticated:
            current_user = info.context.user
            user = User.objects.get(username=username)
            if user.settings.privacy_follows == 'a' or user == current_user:
                return Follow.objects.followers(user)
            elif user.settings.privacy_follows == 's':
                if Follow.objects.follows(current_user, user):
                    return Follow.objects.followers(user)
                else:
                    return ['private']
            else:
                return ['private']

        
    @staticmethod
    def resolve_following(self, info, username):
        # is_private
         if info.context.user.is_authenticated:
            current_user = info.context.user
            user = User.objects.get(username=username)
            if user.settings.privacy_follows == 'a' or user == current_user:
                return Follow.objects.following(user)
            elif user.settings.privacy_follows == 's':
                if Follow.objects.follows(current_user, user):
                    return Follow.objects.following(user)
                else:
                    return ['private']
            else:
                return ['private']

    @staticmethod
    def resolve_follower_count(self, info, username):
        user = User.objects.get(username=username)
        return Follow.objects.follower_count(user)
    
    @staticmethod
    def resolve_following_count(self, info, username):
        user = User.objects.get(username=username)
        return Follow.objects.following_count(user)

    @staticmethod
    def resolve_is_following(self, info, un_follower, un_followee):
        follower = User.objects.get(username=un_follower)
        followee = User.objects.get(username=un_followee)
        return Follow.objects.follows(follower, followee)

    # @staticmethod
    # def resolve_followers(cls, info, **kwargs):
        
    
    # @staticmethod
    # def resolve_following(cls, info, **kwargs):
    #     if info.context.user.is_authenticated:
    #         user = info.context.user
    #         return Follow.objects.following(user)

class Mutation(object):
    follow = mutations.AddFollow.Field()
    unfollow = mutations.Unfollow.Field()

    