import graphene

from apps.links.models import ToushLink, ToushItem
from apps.links import mutations
from apps.links.obj_types import ToushLinkType


class Query(object):
    expand = graphene.Field(ToushLinkType, short_url=graphene.String(required=True), edit=graphene.Boolean(required=False))
    ownLinks = graphene.List(ToushLinkType)

    @staticmethod
    def resolve_expand(cls, info, short_url, edit):
        request = info.context
        return ToushLink.objects.expand(short_url, request, edit)

    @staticmethod
    def resolve_ownLinks(cls, info):
        if info.context.user.is_authenticated:
            user = info.context.user
            return ToushLink.objects.filter(item__user=user).all()
        # NOTE: return auth error if user doesnt already recieve one
        # else:
        #     return ["Please login to do that."]

class Mutation(object):
    create_toush_link = mutations.CreateToushLink.Field()
    delete_toush = mutations.DeleteToush.Field()
    edit_toush_link = mutations.EditToushLink.Field()