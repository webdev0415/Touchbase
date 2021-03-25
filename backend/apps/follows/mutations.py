import graphene
from apps.users.models import User
from apps.follows.models import Follow

class AddFollow(graphene.Mutation):
    """ Mutation to follow a user """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        #username_follower = graphene.String(required=True)
        username_followee = graphene.String(required=True)

    def mutate(self, info, username_followee):
        erl = []

        # add follower
        if info.context.user.is_authenticated:
            follower = info.context.user
        #follower = User.objects.get(username=username_follower)
        try:
            followee = User.objects.get(username=username_followee)
        except User.DoesNotExist:
            erl.append('userDoesNotExist')
            
        try:
            Follow.objects.add_follower(follower, followee)
        except:
            erl.append('couldNotFollow')
        # print(erl)
        if len(erl) > 0:
            return AddFollow(success=False, errors=erl)
        else:
            return AddFollow(success=True, errors=erl)

class Unfollow(graphene.Mutation):
    """ Mutation to unfollow a user """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    
    class Arguments:
        username_followee = graphene.String(required=True)

    def mutate(self, info, username_followee):
        erl = []

        # remove follower
        if info.context.user.is_authenticated:
            follower = info.context.user

        try:
            followee = User.objects.get(username=username_followee)
        except User.DoesNotExist:
            erl.append('userDoesNotExist')
        
        try:
            Follow.objects.remove_follower(follower, followee)
        except:
            erl.append('couldNotUnfollow')

        if len(erl) > 0:
            return Unfollow(success=False, errors=erl)
        else:
            return Unfollow(success=True, errors=erl)