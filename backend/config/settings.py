"""
Django settings for Touchbase project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ
from datetime import timedelta

ROOT_DIR = environ.Path(__file__) - 2

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# APP CONFIGURATION 
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'graphene_django',
    'django_extensions',
    'django_elasticsearch_dsl',
    'storages',
]

LOCAL_APPS = [
    'apps.users',
    'apps.follows',
    'apps.accounts',
    'apps.links',
    'apps.payments',
    'apps.analytics',
    'apps.tcss',
    'apps.cliques',
    # 'apps.push_notifications',
    'apps.graphql_jwt.refresh_token.apps.RefreshTokenConfig',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'apps.graphql_jwt.middleware.DjangoMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')

# DOMAINS
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
DOMAIN = env.str('DOMAIN')

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_PORT = env.int('EMAIL_PORT', default='1025')
EMAIL_HOST = env.str('EMAIL_HOST', default='mailhog')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ('Hioz LLC', 'mehar.web.develop@gmail.com'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': 5432,
    },
}

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# TODO: move all staticfiles to cdn as well
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_LOCATION = 's'
STATICFILES_STORAGE = 'storage.StaticStorage'
MEDIAFILES_LOCATION = 'm'
DEFAULT_FILE_STORAGE = 'storage.MediaStorage'

AWS_ACCESS_KEY_ID = env.str('SPACES_AK')
AWS_SECRET_ACCESS_KEY = env.str('SPACES_SECRET')
AWS_S3_REGION_NAME = env.str('SPACES_REGION')
AWS_STORAGE_BUCKET_NAME = env.str('SPACES_NAME')
AWS_S3_ENDPOINT_URL = f'https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
# AWS_LOCATION = 'm'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_SECURE_URLS = False

STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, STATICFILES_LOCATION)
STATIC_ROOT = 'static/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL = '/staticfiles/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS = [
#     str(ROOT_DIR('static')),
# ]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# MEDIA_ROOT = str(ROOT_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
# MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': STATICFILES_DIRS,
#         'OPTIONS': {
#             'debug': DEBUG,
#             'loaders': [
#                 'django.template.loaders.filesystem.Loader',
#                 'django.template.loaders.app_directories.Loader',
#             ],
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 # 'django.template.context_processors.i18n',
#                 # 'django.template.context_processors.media',
#                 # 'django.template.context_processors.static',
#                 # 'django.template.context_processors.tz',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CACHE SETTINGS
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}


# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'apps.graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'

# LOGGING STUFF



# GRAPHQL & GRAPHENE CONFIGURATION
# ------------------------------------------------------------------------------
GRAPHENE = {
    'SCHEMA': 'config.schema.schema',
}

if DEBUG:
    GRAPHENE['MIDDLEWARE'] = [
        'graphene_django.debug.DjangoDebugMiddleware',
        'apps.graphql_jwt.middleware.JSONWebTokenMiddleware'
    ]
else:
    GRAPHENE['MIDDLEWARE'] = [
        'apps.graphql_jwt.middleware.JSONWebTokenMiddleware'
    ]

GRAPHQL_JWT = {
    # 'JWT_EXPIRATION_DELTA': timedelta(days=30),
    'JWT_AUTH_HEADER': 'authorization',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=30),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}


# ELASTICSEARCH CONFIGURATION 
# ------------------------------------------------------------------------------
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'elasticsearch:9200'
    },
}


# SPF CONFIGURATION 
# ------------------------------------------------------------------------------
SPFL_ID = []


# PAYPAL ACCESS TOKEN
# ------------------------------------------------------------------------------
PAYPAL = {
    'ACCESS_TOKEN': '',
    'AT_HEADERS': {
        'Accept': 'application/json',
        'Accept-Language': 'en_US',
    },
    'AT_DATA': {
        'grant_type': 'client_credentials'
    },
    'AT_AUTH': (
        env.str('PAYPAL_CLIENT'), 
        env.str('PAYPAL_SECRET')
    ),
    'CLIENT': env.str('PAYPAL_CLIENT'),
    'SECRET': env.str('PAYPAL_SECRET'),
    'OAUTH_API': env.str('PAYPAL_OAUTH_API'),
    'ORDER_API': env.str('PAYPAL_ORDER_API'),
    'MERCHANT_ID': env.str('PAYPAL_MERCHANT_ID')
}


# PUSH NOTIFICATIONS
# ------------------------------------------------------------------------------
PUSH_NOTIFICATIONS_SETTINGS = {
    "FCM_API_KEY": "AAAAVfbvsk0:APA91bH8U85SBU1Ydi6HnmEQMzodYMbZf32ERZTj3utFhOCqJL0-fwJwx4ftPUz1YPFTiMMNZTvwJfsnYEOei8sefNL1gIo-fQ8ZfXiVhmsdAXCWkNkN-ai4Hkd5MdKHdGxdHKVx_kVf",
    # "APNS_CERTIFICATE": "/path/to/your/certificate.pem",
    # "APNS_TOPIC": "com.example.push_test",
    # "APNS_USE_SANDBOX": True
    # "WNS_PACKAGE_SECURITY_ID": "[your package security id, e.g: 'ms-app://e-3-4-6234...']",
    # "WNS_SECRET_KEY": "[your app secret key, e.g.: 'KDiejnLKDUWodsjmewuSZkk']",
    # "WP_PRIVATE_KEY": "/path/to/your/private.pem",
    # "WP_CLAIMS": {'sub': "mailto: development@example.com"}
}