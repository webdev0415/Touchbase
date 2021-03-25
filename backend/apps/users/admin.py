from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User, UserProfile, AccessData, OAuthPost, GlobalSPFLID, SPFServiceID, PublicChangeLog, UserSettings
from apps.users.forms import UserChangeForm, UserCreationForm

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True
    verbose_name = 'Profile'

class SettingsInline(admin.StackedInline):
    model = UserSettings
    can_delete = True
    verbose_name = 'Settings'

class PublicChangeLogInline(admin.StackedInline):
    model = PublicChangeLog
    can_delete = True
    verbose_name = 'Changelog'

class AccessDataInline(admin.StackedInline):
    model = AccessData
    can_delete = True
    verbose_name = 'Access Data'

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    inlines = (ProfileInline, SettingsInline, AccessDataInline, PublicChangeLogInline)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['full_name', 'email', 'username']
    fieldsets = [
        ['Auth', {'fields': ['username', 'password']}],
        ['Personal info', {'fields': ['last_name', 'first_name', 'profile_pic', 'language', 'country', 'birthday']}],
        ['Settings', {'fields': ['groups', 'is_admin', 'is_active', 'is_staff', 'is_superuser']}],
        ['Important dates', {'fields': ['last_login', 'registered_at']}],
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        [None, {'classes': ['wide'],
                'fields': ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']}],
    ]
    search_fields = ['email', 'username']
    ordering = ['email']
    readonly_fields = ['last_login', 'registered_at']


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# Unregister the Group model from admin.
admin.site.unregister(Group)

admin.site.register(OAuthPost)
admin.site.register(GlobalSPFLID)
admin.site.register(SPFServiceID)
