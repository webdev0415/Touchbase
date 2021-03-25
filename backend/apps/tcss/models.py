from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.conf import settings

from apps.users.models import User
from apps.cliques.models import Clique

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

def get_follow_default():
    return {
        'candidates': [
            {
                'username': 'memes', # username of user
                'first_name': 'memeR', # username of user
                'last_name': 'remeM', # username of user
                'snippet': 'Cool guy with cool memes!...' # snippet of bio/occupation/education,
                # reason why you are seeing this user
            }
        ]
    }

def get_explore_default():
    return {
        'items': [
            {
                'type': 'brand', # media type
                'img': True, # does it have img. If type is brand, use square and large profile pic
                'src': '/img/avatar-1.png', # img src, in this case would be profile pic link
                'content': { # the content for that particular type, like pdj
                    'username': 'memesco',
                    'first_name': 'memesco',
                    'last_name': 'llc',
                    'message': 'selling memes since 1957!'
                },
                'interest_tags': [
                    'memes',
                    'comedy',
                    'funny stuff',
                ]
            },
        ]
    }

# TCSSRecord - past Tcss objects

# TCSS
class TCSS(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tcss'
    )
    created = models.DateTimeField(auto_now_add=True) 

    # PUT IN FOREIGN KEYS!! USR OBJECTS

    # wtf = JSONField(default=get_follow_default, null=True)
    #  user_id | id (of tcss)
    # ---------+----
    #       27 |  7
    # SELECT tcss_id, user_id FROM tcss_tcss_wtf WHERE tcss_id IN (SELECT id FROM tcss_tcss WHERE user_id = 27) AND user_id = 27;
    # INSERT INTO tcss_tcss_wtf (tcss_id, user_id) VALUES (7, 27);
    wtf = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='wtf_set',
    )

    # PUT IN FOREIGN KEYS!! USR, BRAND, CLIQUE OBJECTS
    # exp = JSONField(default=get_explore_default, null=True)
    exp_people = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='exp_people_set',
    )
    exp_cliques = models.ManyToManyField(
        Clique,
        related_name='exp_cliques_set',
    )
    # exp_brands = models.ManyToManyField(
    #     Brand,
    #     related_name='exp_brands_set',
    # )
