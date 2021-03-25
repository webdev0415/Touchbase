from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.accounts.account_list import url_c_list
from apps.users.models import SPFServiceID

# TODO: make Account manager, make link_account method
#  """ Create 'user' linked 'service' ('url') relationship """
# copy paste the array account stuff from old codebase

def create_url(service, identifier):
    for key in url_c_list:
        if service in url_c_list[key]:
            if key == 'subdomain':
                return f'https://{identifier}.{service}'
            if key == 'whatsapp':
                return f'https://api.whatsapp.com/send?phone={identifier}'
                return f'https://{identifier}.{service}'
            if key == 'oauth':
                if service == 'youtube.com':
                    return f'https://www.youtube.com/channel/{identifier}'
                elif service == 'steamcommunity.com':
                    return f'https://steamcommunity.com/profiles/{identifier}'
            if key == 'username':
                pass
            if key == 'wechat':
                pass
            if key == 'nameandnumber':
                pass
            if key == 'url':
                pass
            return f'https://{service}{key}{identifier}'

class AccountManager(models.Manager):
    """ Account manager for extra methods """

    def link_account(self, user, service, identifier, oauth, spf_identifier, share_spf):
        """ Link an account """
        if oauth and spf_identifier and not identifier:
            url = create_url(service, spf_identifier)
            spfsid, created = SPFServiceID.objects.get_or_create(user=user)
            if service == 'youtube.com':
                spfsid.youtube = spf_identifier
                spfsid.save()
            elif service == 'steamcommunity.com':
                spfsid.steam = spf_identifier
                spfsid.save()
            relation, created = Account.objects.get_or_create(
                user=user, 
                service=service,
                defaults={
                    'identifier': spf_identifier,
                    'url': url,
                    'oauth': oauth,
                    's_spf': share_spf
                }
            )
            return True

        else:
            url = create_url(service, identifier)
            relation, created = Account.objects.get_or_create(
                user=user, 
                service=service,
                defaults={
                    'identifier': identifier,
                    'url': url,
                    'oauth': False
                }
            )

            # can return relation
            return True

    # make dedicated unlink_account
    # do a check for truthyness of removed
            # if removed is true, return success false
            # and say "account already removed"

class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='accounts',
        on_delete=models.CASCADE
    )

    url = models.URLField(max_length=200, default='')
    oauth = models.BooleanField(default=False)
    # identifier is just the username on that site
    identifier = models.CharField(max_length=100, default='')
    created = models.DateTimeField(verbose_name='Registered at', auto_now_add=timezone.now)
    service = models.CharField(max_length=100, default='')
    s_spf = models.BooleanField(default=True)

    # bools for is removed and is private 
    # if private, do the same privacy checking in profile object type
    # if removed it should not touch the frontend
    # is_private = models.BooleanField(default=False)
    # is_removed = models.BooleanField(default=False)

    objects = AccountManager()

    # class Meta:
    #     verbose_name = _('Linked Account Relationship')
    #     verbose_name_plural = _('Linked Account Relationships')

    def __str__(self):
        return "%s has %s linked" % (self.user, self.service)


