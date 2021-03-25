import graphene
from apps.payments.models import Transaction
from apps.payments import mutations
from apps.payments.obj_types import TransactionType

class Query(object):
    own_transactions = graphene.List(TransactionType)

    @staticmethod
    def resolve_own_transactions(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user.payments.objects.all()

class Mutation(object):
    ptc = mutations.PTC.Field()




