import graphene
from graphene_django import DjangoObjectType
from apps.analytics.models import SiteVisit, ProfileVisit

class SiteVisitType(DjangoObjectType):
    """ site visit type object """

    class Meta:
        model = SiteVisit

class ProfileVisitType(DjangoObjectType):
    """ profile visit type object """

    class Meta:
        model = ProfileVisit