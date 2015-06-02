from yebimom.settings import *
import os


DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [".yebimom.com", ]


INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)


# https://docs.djangoproject.com/en/1.7/ref/settings/#default-file-storage
# https://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'yebimom.storage.S3PipelineManifestStorage'

STATIC_URL = 'https://cdn.yebimom.com/'


RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DSN'],
}
