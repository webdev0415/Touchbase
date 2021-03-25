from graphene_django import DjangoObjectType
from apps.payments.models import Transaction

class TransactionType(DjangoObjectType):
    """ Transaction type object """

    class Meta:
        model = Transaction
        only_fields = [
            "billing_state",
            "billing_city",
            "billing_country",
            "billing_first_name",
            "billing_last_name",
            "billing_phone",
            "billing_email",
            "price_total",
            "payment_status",
            "modified",
            "created",
            "user",
        ]