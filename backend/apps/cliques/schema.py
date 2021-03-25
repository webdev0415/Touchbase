import graphene

from apps.cliques.models import Clique
from apps.cliques import mutations
from apps.cliques.obj_types import CliqueType


class Query(object):
    # own_clique = graphene.Field(CliqueType, name=graphene.String(required=True))
    own_cliques = graphene.List(CliqueType)
    clique = graphene.Field(CliqueType, name=graphene.String(required=True))

    # @staticmethod
    # def resolve_own_clique(cls, info, name):
    #     if info.context.user.is_authenticated:
    #         return info.context.user.cliques.get(name=name)

    @staticmethod
    def resolve_own_cliques(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user.cliques.all()

    @staticmethod
    def resolve_clique(cls, info, name):
        return Clique.objects.get(name=name)


class Mutation(object):
    create_clique = mutations.CreateClique.Field()
    update_clique = mutations.UpdateClique.Field()
    join_clique = mutations.JoinClique.Field()
    leave_clique = mutations.LeaveClique.Field()