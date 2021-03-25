from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class AccessData(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_accessdata'
    )

    # stuff that gets updated on login
    last_login = models.DateTimeField(default=timezone.now, blank=True)
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
        return str(self.user)