import graphene
from apps.analytics.models import SiteVisit, ProfileVisit
from apps.tcss.models import TCSS
from datetime import timedelta
from django.utils import timezone
# from apps.analytics.obj_types import SiteVisitType, ProfileVisitType

class CreateSiteVisit(graphene.Mutation):
    """ Mutation to add a site visit """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        page = graphene.String(required=True)

    def mutate(self, info, page):
        if info.context.user.is_authenticated:
            user = info.context.user
            if not TCSS.objects.filter(user=user).exists():
                if (timezone.now() - user.registered_at) > timedelta(1):
                    if ProfileVisit.objects.filter(viewer=user).count() > 3:
                        if SiteVisit.objects.filter(user=user).count() > 5:
                            TCSS.objects.create(user=user)
                            user.settings.has_tcss = True
                            user.settings.save()
                            # print(user.has_tcss)
            try:
                SiteVisit.objects.make_visit(user=user, page=page)
                return CreateSiteVisit(success=True)
            except:
                return CreateSiteVisit(success=False)
        else:
            return CreateSiteVisit(success=False, errors=['authenticate yo anonymous ass!'])


class CreateProfileVisit(graphene.Mutation):
    """ Mutation to add a profile visit """
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        viewee = graphene.String(required=True)

    def mutate(self, info, viewee):
        if info.context.user.is_authenticated:
            try:
                user = info.context.user
                # is it same user?
                if user.username != viewee:
                    ProfileVisit.objects.make_visit(viewer=user, viewee=viewee)
                    return CreateProfileVisit(success=True)
            except:
                return CreateProfileVisit(success=False)
        else:
            return CreateProfileVisit(success=False, errors=['authenticate yo anonymous ass!'])
