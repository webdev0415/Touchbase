# profile models
# HAS NOT BEEN MIGRATED OR RECOGNIZED YET,
# NOT IN __INIT__.PY

### DO FOLLOWING AND FOLLOWERS

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.conf import settings
from django.utils import timezone

from apps.users.validators import phone_regex


IT_CHOICES = (
    ('All', 'All'),
    ('all', 'all'),
    ('3D printing', '3D printing'),
    ('Acting', 'Acting'),
    ('Art', 'Art'),
    ('Astrology', 'Astrology'),
    ('Astronomy', 'Astronomy'),
    ('Automobiles', 'Automobiles'),
    ('Business', 'Business'),
    ('Community', 'Community'),
    ('Computer programming', 'Computer programming'),
    ('Cooking', 'Cooking'),
    ('Couponing', 'Couponing'),
    ('DIY', 'DIY'),
    ('Dance', 'Dance'),
    ('Drawing', 'Drawing'),
    ('Electronics', 'Electronics'),
    ('Fashion', 'Fashion'),
    ('Film', 'Film'),
    ('Fitness And Exercise', 'Fitness And Exercise'),
    ('Gaming', 'Gaming'),
    ('Gardening', 'Gardening'),
    ('Graphic Design', 'Graphic Design'),
    ('Hiking', 'Hiking'),
    ('History', 'History'),
    ('Magic', 'Magic'),
    ('Mathematics', 'Mathematics'),
    ('Music', 'Music'),
    ('Painting', 'Painting'),
    ('Pets', 'Pets'),
    ('Philosophy', 'Philosophy'),
    ('Photography', 'Photography'),
    ('Playing musical instruments', 'Playing musical instruments'),
    ('Politics', 'Politics'),
    ('Programming', 'Programming'),
    ('Reading', 'Reading'),
    ('Role-play', 'Role-play'),
    ('Science', 'Science'),
    ('Singing', 'Singing'),
    ('Sports', 'Sports'),
    ('Stand-up comedy', 'Stand-up comedy'),
    ('Vacation', 'Vacation'),
    ('Writing', 'Writing'),
)

def get_pil_default():
    ### UI Things for displaying info concisely
    # ocedlo groups occupation, education, and location
    # fingv groups following, followers, and profile views
    # cont groups contact phone and contact email # list of item objects
    # changed up the json, see if still works
    return {
        "items": {
            "fingv": {
                "enabled": True,
                #"order": 1,
                "private": False
            },
            "ocedlo": {
                "enabled": True,
                #"order": 2,
                "private": False
            },
            "cont": {
                "enabled": True,
                #"order": 3,
                "private": False
            },
            "bio": {
                "enabled": True,
                #"order": 4,
                "private": False
            },
            "views": {
                "enabled": True,
                #"order": 5,
                "private": False
            }
        }
    }

def get_it_default():
    return [
        'All'
    ]


class UserProfileManager(models.Manager):
    """ Profile manager for extra methods """

    def add_view(self, profile):
        """ Add 1 view to view count """
        # print(profile.view_count, '~~~~', profile)
        profile.view_count += 1
        profile.save()


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    profile_items_layout = JSONField(default=get_pil_default)

    interest_tags = ArrayField(models.CharField(max_length=32, default='', blank=True, choices=IT_CHOICES), default=get_it_default)

    occupation = models.CharField(max_length=20, default='', blank=True)
    education = models.CharField(max_length=70, default='', blank=True)
    location = models.CharField(max_length=40, default='', blank=True)

    bio = models.CharField(max_length=200, default='Touchbase with me!', blank=True)
    website = models.URLField(max_length=100, default='http://touchbase.id', blank=True)

    contact_email = models.EmailField(verbose_name='Contact Email', max_length=255, default='', blank=True)
    contact_phone = models.CharField(validators=[phone_regex], max_length=17, default='', blank=True)

    view_count = models.IntegerField(default=0)

    is_verified = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    is_celebrity = models.BooleanField(default=False)

    ###### EVERYTHING BELOW HERE SHOULD BE MOVED TO SETTINGS

    # has_tcss = models.BooleanField(default=False)

    # views_privacy = models.BooleanField(default=True)

    # ### TOUSH STUFF # -1 means infinite # exclude in obj types or move to ToushProfileSettings
    # # can use toush_enabled to ban ppls
    # toush_enabled = models.BooleanField(default=True)
    # toush_max_links = models.IntegerField(default=-1)
    # toush_max_concurrent_links = models.IntegerField(default=100)
    # toush_default_lifespan = models.IntegerField(default=86400)
    # toush_default_max_uses = models.IntegerField(default=-1)

    # haspSPF = models.BooleanField(default=False)



    objects = UserProfileManager()

    def __str__(self):
        return str(self.user)


# NOTE: FOR PAGINATION, GET ALL ITEMS FOR A FIELD AND THEN GIVE SOME AT TIME
# INSTEAD OF GETTING AND GIVING SOME AT A TIME
class PublicChangeLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='changes',
        on_delete=models.CASCADE
    )
    # "statement": 'Added an account'
    # "service": 'touchbase' -- use tb logo and dont put semi colon
    # "username": 'memes'
    # "name": 'Hickory Doo'
    created = models.DateTimeField(auto_now_add=timezone.now)
    statement = models.CharField(max_length=32, default='', blank=True)
    service = models.CharField(max_length=100, default='', blank=True)
    # username = models.CharField(max_length=32, null=True)
    # name = models.CharField(max_length=128, null=True)
    def __str__(self):
        return str(self.user)