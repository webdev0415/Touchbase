from django.contrib import admin

# Register your models here.
from apps.analytics.models import ProfileVisit, SiteVisit

admin.site.register(ProfileVisit)
admin.site.register(SiteVisit)