import graphene
from apps.cliques.models import Clique
from apps.cliques.obj_types import CliqueType


class CreateClique(graphene.Mutation):
    """ Mutation to create a clique """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String(required=True)
        caption = graphene.String(required=True)
        file = graphene.String(required=True)

    def mutate(self, info, name, caption, file):
        if info.context.user.is_authenticated:
            try:
                Clique.objects.create_clique(info.context.user, name, file, caption)
            except:
                return CreateClique(success=False, errors=['idk man the server ain\'t workin rn 🤣'])
            
            return CreateClique(success=True)

class UpdateClique(graphene.Mutation):
    """ Mutation to update a clique """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String(required=False)
        caption = graphene.String(required=False)
        file = graphene.String(required=True)

    def mutate(self, info, name=None, file=None, caption=None):
        if info.context.user.is_authenticated:
            try:
                Clique.objects.update_clique(info.context.user, name, file, caption)
                return UpdateClique(success=True)
            except:
                return UpdateClique(success=False, errors=['idk man the server ain\'t workin rn 🤣'])


class JoinClique(graphene.Mutation):
    """ Mutation to join an clique """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        if info.context.user.is_authenticated:
            try:
                Clique.objects.join_clique(info.context.user, name)
                return JoinClique(success=True)
            except:
                return JoinClique(success=False, errors=['idk man the server ain\'t workin rn 🤣'])


class LeaveClique(graphene.Mutation):
    """ Mutation to leave an clique """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        if info.context.user.is_authenticated:
            try:
                Clique.objects.leave_clique(info.context.user, name)
                return LeaveClique(success=True)
            except:
                return LeaveClique(success=False, errors=['idk man the server ain\'t workin rn 🤣'])