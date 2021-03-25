from datetime import date
from uuid import uuid4

# django
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

# drf

# local
from apps.users.validators import TouchbaseUsernameValidator


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

    def _create_user(self, username, email, first_name, last_name, language, country, birthday, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(username=username,
                          email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name,
                          language=language,
                          country=country,
                          birthday=date(int(birthday.split('-')[0]), int(birthday.split('-')[1]), int(birthday.split('-')[2])), 
                          is_active=True,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          last_login=timezone.now(),
                          registered_at=timezone.now(),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, first_name=None, 
                    last_name=None, language=None, country=None, birthday=None, password=None, **extra_fields):
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(username, email, first_name, last_name, language, country, birthday, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, username, email, first_name, last_name, language, country, birthday,
                         password, **extra_fields):
        return self._create_user(username, email, first_name, last_name, language, country, birthday, password, is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Username',
        max_length=45,
        unique=True,
        validators=[TouchbaseUsernameValidator()],
        error_messages={
            'unique':"A user with that username already exists.",
        },
        default="ifyouseethisusernamesomethingisverybroken"
    )

    email = models.EmailField(verbose_name='Email', unique=True, max_length=255)

    first_name = models.CharField(
        verbose_name='First name',
        max_length=30,
        default='A wonderful first name'
    )

    last_name = models.CharField(
        verbose_name='Last name',
        max_length=30,
        default='A beautiful last name'
    )

    country = models.CharField(max_length=64, default='A country on earth')
    language = models.CharField(max_length=64, default='A country on earth')
    birthday = models.DateField(default=date.today)

    ### DO spaces, url here
    profile_pic = models.URLField(max_length=200, default='https://tbdev.nyc3.cdn.digitaloceanspaces.com/m/blank-face.png', verbose_name='profile_pic')

    token = models.UUIDField(verbose_name='Token', default=uuid4, editable=False)

    is_admin = models.BooleanField(verbose_name='Admin', default=False)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    registered_at = models.DateTimeField(verbose_name='Registered at', auto_now_add=timezone.now)

    # Should probably add created and modified fields for search engine ordering purposes

    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    ### HELPER FUNCTIONS ###

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    full_name.fget.short_description = 'Full name'

    @property
    def short_name(self):
        return f'{self.last_name} {self.first_name[0]}.'
    short_name.fget.short_description = 'Short name'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name

    def __str__(self):
        return str(self.full_name)

