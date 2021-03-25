import graphene
import json

from apps.users.models import User
from apps.accounts.models import Account
from apps.accounts import mutations
from apps.accounts.obj_types import AccountType
from apps.links.models import ToushLink


class Query(object):
    # TODO: DO THE PRIVACY FOR RETURNING ACCOUNTS
    own_account = graphene.Field(AccountType, service=graphene.String(required=True))
    own_accounts = graphene.List(AccountType)
    accounts = graphene.List(AccountType, username=graphene.String(required=True))
    toush_accounts = graphene.List(AccountType, short_url=graphene.String(required=True))

    # basically this thing gets an account for the current user 
    # based off the name of service
    #i.e. (service: "Facebook") and then return that account obj
    @staticmethod
    def resolve_own_account(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user.accounts.get(service=kwargs.get('service'))
        # else:
        #     return "Please login to do that"

    # same thing but returns all accounts for signed in user
    @staticmethod
    def resolve_own_accounts(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user.accounts.all()
        # else:
        #     return "Please login to do that"

    @staticmethod
    def resolve_accounts(cls, info, **kwargs):
        username = kwargs.get('username')
        user = User.objects.get(username=username)
        if user.settings.privacy_accounts == 'a' or user == current_user:
            return user.accounts.all()
        else:
            return ['private']

    @staticmethod
    def resolve_toush_accounts(cls, info, **kwargs):
        short_url = kwargs.get('short_url')
        # user = User.objects.get(username=username)
        #print(short_url)
        try:
            url = ToushLink.objects.get(short_url__exact=short_url)
            user = url.item.user
        except ToushLink.DoesNotExist:
            raise KeyError("invalid shortlink")
        if user.settings.privacy_accounts in 'as' or user == info.context.user:
            accounts_list = url.item.accounts_list["services"]
            account_list = user.accounts.filter(service__in=accounts_list)
            return account_list
        else:
            return ['private']

class Mutation(object):
    link_account = mutations.LinkAccount.Field()
    # unlink_account = mutations.UnlinkAccount.Field()