from django.contrib import admin
from apps.links.models import ToushLink, ToushItem, Visitor

# Register your models here.

admin.site.register(ToushLink)
admin.site.register(ToushItem)
admin.site.register(Visitor)