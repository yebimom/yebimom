from yebimom.settings.settings import *
import os


# partials/development.py

DEBUG = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [".herokuapp.com", ".yebimom.com"]


# partials/static.py

# Serving static files from a cloud service or CDN
# https://docs.djangoproject.com/en/1.7/howto/static-files/deployment/#serving-static-files-from-a-cloud-service-or-cdn
STATIC_URL = 'https://cdn.yebimom.com/'


# https://docs.djangoproject.com/en/1.7/ref/settings/#default-file-storage
# https://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


# Setting for AWS

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']


# sentry

# Set DSN value
RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DSN'],
}

# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)
