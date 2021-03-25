import graphene
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from apps.accounts.models import Account
from django.db.models import DateTimeField

@convert_django_field.register(DateTimeField)
def convert_datetimefield(field, registry=None):
    return graphene.String()

class AccountType(DjangoObjectType):
    """ User type object """

    def resolve_created(self, info):
        return self.created.strftime('%Y-%m-%d %H:%M%z')

    class Meta:
        model = Account