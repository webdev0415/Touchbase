import graphene
from apps.accounts.models import Account
from apps.accounts.account_list import OAF_supported
from apps.accounts.obj_types import AccountType
from apps.users.models import PublicChangeLog

class LinkAccount(graphene.Mutation):
    """ Mutation to link an account """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        identifier = graphene.String(required=False)
        service = graphene.String(required=True)
        spf_identifier = graphene.String(required=False)
        share_spf = graphene.Boolean(required=True)

    def mutate(self, info, identifier, service, spf_identifier, share_spf):
        if info.context.user.is_authenticated:
            user = info.context.user
            oauth = True if service in OAF_supported else False
            identifier = identifier if identifier else ''
            spf_identifier = spf_identifier if spf_identifier else ''
            # print(oauth, spf_identifier)
            Account.objects.link_account(user=user, service=service, identifier=identifier, oauth=oauth, spf_identifier=spf_identifier, share_spf=share_spf)
            PublicChangeLog.objects.create(user=user, service=service, statement='')
            return LinkAccount(success=True)

        return LinkAccount(success=False)

class UnlinkAccount(graphene.Mutation):
    """ Mutation to unlink an account """
    success = graphene.Boolean()
    #add proper errors lol
    errors = graphene.List(graphene.String)

    class Arguments:
        service = graphene.String(required=True)

    def mutate(self, info, service):
        if info.context.user.is_authenticated:
            user = info.context.user
            # use unlink_account
            user.accounts.filter(service=service).delete()
            return UnlinkAccount(success=True)

        return UnlinkAccount(success=False)