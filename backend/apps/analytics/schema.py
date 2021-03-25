import graphene

from apps.analytics.models import SiteVisit, ProfileVisit
from apps.analytics import mutations

class Mutation(object):
    create_site_visit = mutations.CreateSiteVisit.Field()
    create_profile_visit = mutations.CreateProfileVisit.Field()