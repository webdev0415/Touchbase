from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.utils import timezone
from django.conf import settings

from apps.users.validators import TouchbaseUsernameValidator
from apps.users.models import User, get_it_default, IT_CHOICES

# tcss_follow will be the candidate list, 120 people is minimum and max, structured like this:
# {"it_1": [], "it_2"....., trending: [], viewed: []}

# Every user will have a minimum of 5 interest tags, so for every user:
# 
# "IT_N": it_count = 80, it_size = n, remainder gets subtracted from 80 and gets added to trending
# def divide(a, b):
    # q = 0
    # while a >= b:
    #    a -= b
    #    q += 1
    # return (q, a)
# q, r = divide(it_count, it_size)
# it_count -= r
# for each tag in it_tags, get top it_size users
#
# "VIEWED": In their ProfileVisits, get all profiles sorted by number of occurrence,
# max of 20. if less than 20, fill rest with trending. Evaluate before trending
# 
# "TRENDING": trending_count += r + (20 - viewed_count)
# get first trending_count users in trending list

class SiteVisitManager(models.Manager):
    """ Site Visit manager for CRUD of profile visits """
    def make_visit(self, user, page):
        SiteVisit.objects.create(user=user, page=page)

class ProfileVisitManager(models.Manager):
    """ Profile Visit manager for CRUD of profile visits """
    def make_visit(self, viewer, viewee):
        # get interest tags of viewee
        it = User.objects.get(username=viewee).profile.interest_tags
        ProfileVisit.objects.create(viewer=viewer, viewee=User.objects.get(username=viewee), interest_tags_viewee=it)

# SiteVisit
class SiteVisit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='site_visits',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True) 
    page = models.CharField(default='Home', max_length=32)

    objects = SiteVisitManager()


# ProfileVisit
class ProfileVisit(models.Model):
    viewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='profile_visits',
        on_delete=models.CASCADE
    )
    viewee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='viewees',
        on_delete=models.CASCADE
    )
    # viewee = models.CharField(
    #     max_length=45,
    #     validators=[TouchbaseUsernameValidator()],
    #     default="ifyouseethisusernamesomethingisverybroken"
    # )

    created = models.DateTimeField(auto_now_add=True) 

    # interest_tags of viewee
    interest_tags_viewee = ArrayField(models.CharField(max_length=32, default='', blank=True, choices=IT_CHOICES), default=get_it_default)

    objects = ProfileVisitManager()