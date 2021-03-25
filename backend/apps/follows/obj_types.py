import graphene
from graphene_django import DjangoObjectType
from apps.follows.models import (
    Follow
)

class FollowType(DjangoObjectType):
    """ Follow type object """

    class Meta:
        model = Follow
        only_fields = [
            'id',
            'follower',
            'followee',
            'created'
        ]
    
    