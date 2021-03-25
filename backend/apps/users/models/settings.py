from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.conf import settings
from django.utils import timezone

# personal, business, celebrity
TYPE_CHOICES = (
    ('p', 'p'),
    ('b', 'b'),
    ('c', 'c')
)

# anyone, some, none
PRIVACY_CHOICES = (
    ('a', 'a'),
    ('s', 's'),
    ('n', 'n')
)

class UserSettingsManager(models.Manager):
    """ settings manager for extra methods """

    def add_tri_count(self, user):
        """ Add 1 view to tri count """
        settings = user.settings
        settings.tri_count += 1
        settings.save()


class UserSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='settings'
    )

    ###### EVERYTHING BELOW HERE SHOULD BE IN SETTINGS

    # trr = trending reset, tri = trending interval, tra = trending appearance
    tri_count = models.IntegerField(default=0)
    tra_count = models.IntegerField(default=0)

    has_tcss = models.BooleanField(default=False)

    views_privacy = models.BooleanField(default=False)

    # new stuff
    account_type = models.CharField(max_length=1, default='p', choices=TYPE_CHOICES)
    notifs_enable = models.BooleanField(default=True)
    notifs_follows = models.BooleanField(default=True)
    notifs_new_account = models.BooleanField(default=True)
    notifs_updates = models.BooleanField(default=True)
    sponsored_relevant = models.BooleanField(default=True)
    privacy_accounts = models.CharField(max_length=1, default='a', choices=PRIVACY_CHOICES)
    privacy_follows = models.CharField(max_length=1, default='a', choices=PRIVACY_CHOICES)
    private_profile = models.BooleanField(default=False)
    hasp_business = models.BooleanField(default=False)
    hasp_celebrity = models.BooleanField(default=False)

    ### TOUSH STUFF # -1 means infinite -- admin only, no frontend
    # can use toush_enabled to ban ppls
    toush_enabled = models.BooleanField(default=True)
    toush_max_links = models.IntegerField(default=-1)
    toush_max_concurrent_links = models.IntegerField(default=100)
    toush_default_lifespan = models.IntegerField(default=86400)
    toush_default_max_uses = models.IntegerField(default=-1)

    # NOTE: CHANGE haspSPF to hasp_spf
    haspSPF = models.BooleanField(default=False)


    objects = UserSettingsManager()

    def __str__(self):
        return str(self.user)
