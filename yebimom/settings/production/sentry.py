from yebimom.settings.settings import *
import os

# Set DSN value
RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DSN'],
}

# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)
