import graphene
from graphene_django.debug import DjangoDebug

import apps.users.schema
import apps.follows.schema
import apps.accounts.schema
import apps.links.schema
import apps.payments.schema
import apps.analytics.schema
import apps.tcss.schema
import apps.cliques.schema


class Query(apps.users.schema.Query, apps.follows.schema.Query,
            apps.accounts.schema.Query, apps.links.schema.Query,
            apps.payments.schema.Query, apps.tcss.schema.Query,
            apps.cliques.schema.Query,
            graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='debug')


class Mutation(apps.users.schema.Mutation, apps.follows.schema.Mutation,
               apps.accounts.schema.Mutation, apps.links.schema.Mutation,
               apps.payments.schema.Mutation, apps.analytics.schema.Mutation,
               apps.cliques.schema.Mutation,
               graphene.ObjectType):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
