import graphene
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from apps.tcss.models import TCSS
from django.db.models import DateTimeField

class TCSSType(DjangoObjectType):
    """ TCSS type object """

    class Meta:
        model = TCSS
        only_fields = [
            'wtf',
            'exp_people',
            'exp_cliques',
        ]