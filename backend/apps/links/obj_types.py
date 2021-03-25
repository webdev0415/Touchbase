import graphene
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from apps.links.models import ToushLink, ToushItem
from django.db.models import DateTimeField

@convert_django_field.register(DateTimeField)
def convert_datetimefield(field, registry=None):
    return graphene.String()

class ToushItemType(DjangoObjectType):
    """ Type for Toush Item """

    def resolve_created(self, info):
        return self.created.strftime('%Y-%m-%d %H:%M')

    class Meta:
        model = ToushItem

class ToushLinkType(DjangoObjectType):
    """ Type for Toush Link """

    def resolve_created(self, info):
        return self.created.strftime('%Y-%m-%d %H:%M')

    def resolve_expired(self, info):
        # %Y-%m-%d %H:%M%z
        return self.expired.strftime('%Y-%m-%d %H:%M')

    class Meta:
        model = ToushLink
        # exclude_fields = [
        #     'max_count',
        #     'lifespan',
        # ]

