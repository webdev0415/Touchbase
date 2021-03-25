from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db import IntegrityError
from django.contrib.postgres.fields import JSONField

from apps.users.models import UserProfile, User
from apps.links.utils import is_hash_taken

import random
from user_agents import parse
from datetime import datetime, timedelta

### implement ToushLink
### Link stuff from Github + analytics, statistics (view_count)

# def is_hash_taken(hash):
#     return True if ToushLink.objects.get(short_url=hash).exists() else False

# def get_random(): #### LENGTH OF LINK IS NOT RESTRICTED
#     length = getattr(settings, 'SHORTENER_LENGTH', 5)
#     # Removed l, I, 1
#     dictionary = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz234567890"

#     while True:
#         length += 1
#         hash = ''.join(random.choice(dictionary) for _ in range(length))

#         if not is_hash_taken(hash):
#             return hash

def get_random():
    length = getattr(settings, 'SHORTENER_LENGTH', 6)
    # Removed l, I, 1
    dictionary = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz234567890"

    for i in range(20):
        hash = ''.join(random.choice(dictionary) for _ in range(length))

        if not is_hash_taken(hash):
            return hash

class ToushLinkManager(models.Manager):
    """ Toush Link manager for CRUD of toush links """

    def make_link(self, user, link, link_to_profile, is_toush_events,
        is_toush_profile, is_toush_feed, username, first_name,
        last_name, contact_phone, contact_email, max_count, lifespan, message, custom_link, accounts_list):
        '''
        Make a Toush link
        '''
        # check if user allowed to save link
        try:
            # use user settings
            p = UserProfile.objects.get(user=user)
            enabled = p.toush_enabled
            max_links = p.toush_max_links
            max_concurrent = p.toush_max_concurrent_links
            lifespan = p.toush_default_lifespan if not lifespan else lifespan
            max_count = p.toush_default_max_uses if not max_count else max_count

            
            # username = user.username if username else ''
            # first_name = user.first_name if first_name else ''
            # last_name = user.last_name if last_name else ''
            # contact_email = p.contact_email if contact_email else ''
            # contact_phone = p.contact_phone if contact_phone else ''


        except UserProfile.DoesNotExist:
            # Use defaults from settings
            enabled = getattr(settings, 'SHORTENER_ENABLED', True)
            max_links = getattr(settings, 'SHORTENER_MAX_URLS', -1)
            max_concurrent = getattr(settings, 'SHORTENER_MAX_CONCURRENT', -1)
            lifespan = getattr(settings, 'SHORTENER_LIFESPAN', -1) if not lifespan else lifespan
            max_count = getattr(settings, 'SHORTENER_MAX_USES', -1) if not max_count else max_count

            # username = user.username if username else ''
            # first_name = user.first_name if first_name else ''
            # last_name = user.last_name if last_name else ''
            # contact_email = ''
            # contact_phone = ''

        # Ensure User is allowed to create
        if not enabled:
            raise PermissionError("not authorized to create toush links")

        # Expiry date, -1 to disable
        if lifespan != -1:
            expiry_date = timezone.now() + timedelta(hours=lifespan) ### an change to minutes here
        else:
            expiry_date = timezone.make_aware(timezone.datetime.max, timezone.get_default_timezone())

        # Ensure user has not met max_links quota
        if max_links != -1:
            if ToushItem.objects.filter(user=user).count() >= max_links:
                raise PermissionError("url quota exceeded")

        # Ensure user has not met concurrent urls quota
        if max_concurrent != -1:
            if ToushItem.objects.filter(user=user, toush_link__expired__gt=timezone.now()).count() >= max_concurrent:
                raise PermissionError("concurrent quota exceeded")
        
        if custom_link:
            try:
                item = ToushItem.objects.create(
                    user=user, is_toush_profile=is_toush_profile,
                    is_toush_events=is_toush_events, is_toush_feed=is_toush_feed,
                    username=username, first_name=first_name, last_name=last_name,
                    contact_phone=contact_phone, contact_email=contact_email,
                    message=message, link_to_profile=link_to_profile, toush_string=custom_link,
                    accounts_list=accounts_list

                )
                m = ToushLink.objects.create(item=item, full_url=link, short_url=custom_link, max_count=max_count, lifespan=lifespan, expired=expiry_date)
                #### IN OBJECT TYPE DEFINITION, EXCLUDE THE DATA/STATS FIELDS
                # so analytics don't leave server
            except IntegrityError:
                print('INTEGRITY ERROR - creating toush link with custom string')
        else:
            short = get_random()
            #### IN OBJECT TYPE DEFINITION, EXCLUDE THE DATA/STATS FIELDS
            # so analytics don't leave server
            item = ToushItem.objects.create(
                user=user, is_toush_profile=is_toush_profile,
                is_toush_events=is_toush_events, is_toush_feed=is_toush_feed,
                username=username, first_name=first_name, last_name=last_name,
                contact_phone=contact_phone, contact_email=contact_email,
                message=message, link_to_profile=link_to_profile, toush_string=short,
                accounts_list=accounts_list
            )
            ToushLink.objects.create(item=item, full_url=link, short_url=short, max_count=max_count, lifespan=lifespan, expired=expiry_date)
            return
    
    def expand(self, link, request):
        '''
        Expand a toush link
        '''

        try:
            url = ToushLink.objects.get(short_url__exact=link)
        except ToushLink.DoesNotExist:
            raise KeyError("invalid shortlink")

        # ensure we are within usage counts
        if url.max_count != -1:
            if url.max_count <= url.usage_count:
                raise PermissionError("max usages for link reached")

        # ensure we are within allowed datetime
        # print(timezone.now())
        # print(url.expired)
        if timezone.now() > url.expired:
            raise PermissionError("shortlink expired")


        url.usage_count += 1
        url.save()
        
        ### TO CONSERVE RESOURCES, CREATE VISITOR OBJECT AFTER THE CHECKS.
        ### VISITOR OBJECT ONLY MADE IF THE VISITOR "SEES" THE END PAGE
        user = request.user if request.user.username else None
        ip_addr_v4 = request.META['REMOTE_ADDR']
        ua_string = request.META['HTTP_USER_AGENT']
        user_agent = parse(ua_string)

        if user is not None:
            Visitor.objects.create(
                url=url,
                user=user, ip_addr_v4=ip_addr_v4, is_mobile=user_agent.is_mobile,
                is_tablet=user_agent.is_tablet, 
                is_touch_capable=user_agent.is_touch_capable,
                is_pc=user_agent.is_pc, is_bot=user_agent.is_bot,
                browser=user_agent.browser.family, 
                browser_version=user_agent.browser.version_string,
                os=user_agent.os.family, 
                os_version=user_agent.os.version_string,
                device=user_agent.device.family
            )
        else:
            Visitor.objects.create(
                url=url,
                ip_addr_v4=ip_addr_v4, is_mobile=user_agent.is_mobile,
                is_tablet=user_agent.is_tablet, 
                is_touch_capable=user_agent.is_touch_capable,
                is_pc=user_agent.is_pc, is_bot=user_agent.is_bot,
                browser=user_agent.browser.family, 
                browser_version=user_agent.browser.version_string,
                os=user_agent.os.family, 
                os_version=user_agent.os.version_string,
                device=user_agent.device.family
            )

        #### IN OBJECT TYPE DEFINITION, EXCLUDE THE DATA/STATS FIELDS
        # so analytics don't leave server
        return url


## can make variable? maybe it will run faster
def get_accounts_default():
    return {
        "services": []
    }

class ToushItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='toush_links',
        on_delete=models.CASCADE
    )
    accounts_list = JSONField(default=get_accounts_default)

    is_toush_profile = models.BooleanField(default=False)
    is_toush_feed = models.BooleanField(default=False)
    is_toush_events = models.BooleanField(default=False)

    toush_string = models.CharField(max_length=20, default='', unique=True)
    created = models.DateTimeField(verbose_name='Registered at', auto_now_add=timezone.now)

    username = models.BooleanField(default=False)
    first_name = models.BooleanField(default=False)
    last_name = models.BooleanField(default=False)
    profile_picture = models.BooleanField(default=False)
    banner = models.BooleanField(default=False) # imagefield
    color_scheme = models.BooleanField(default=False) # make this charfield with choices
    contact_phone = models.BooleanField(default=False)
    contact_email = models.BooleanField(default=False)
    message = models.CharField(max_length=128, default='', blank=True)
    link_to_profile = models.BooleanField(default=True)

    # feed_subselections

    def __str__(self):
        return f'{self.user.username} has link {self.toush_string}'


class ToushLink(models.Model):
    item = models.OneToOneField(ToushItem, related_name='toush_link', on_delete=models.CASCADE)
    # data = models.OneToOneField(ToushLinkData, related_name='toush_link_data', on_delete=models.CASCADE)
    full_url = models.CharField(max_length=256, default='')
    short_url = models.CharField(max_length=50, unique=True, db_index=True)
    usage_count = models.IntegerField(default=0) #
    max_count = models.IntegerField(default=-1) #
    lifespan = models.IntegerField(default=-1) #
    created = models.DateTimeField(auto_now_add=True) #
    expired = models.DateTimeField() #

    objects = ToushLinkManager()

    def __str__(self):
        return self.full_url

# class ToushLinkData(models.Model):
    

#     def __str__(self):
#         return self.usage_count


class Visitor(models.Model):
    url = models.ForeignKey(ToushLink, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    ip_addr_v4 = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    ip_addr_v6 = models.GenericIPAddressField(protocol='IPv6', blank=True, null=True)

    is_mobile = models.NullBooleanField(blank=True, null=True, default=None)
    is_tablet = models.NullBooleanField(blank=True, null=True, default=None)
    is_touch_capable = models.NullBooleanField(blank=True, null=True, default=None)
    is_pc = models.NullBooleanField(blank=True, null=True, default=None)
    is_bot = models.NullBooleanField(blank=True, null=True, default=None)

    browser = models.CharField(max_length=64, default='', blank=True)
    browser_version = models.CharField(max_length=64, default='', blank=True)

    os = models.CharField(max_length=64, default='', blank=True)
    os_version = models.CharField(max_length=128, default='', blank=True)

    device = models.CharField(max_length=128, default='', blank=True)

    def __str__(self):
        return str(self.user) if self.user else str(self.created)

