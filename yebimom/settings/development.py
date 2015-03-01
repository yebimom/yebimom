from yebimom.settings.settings import *


INSTALLED_APPS += (
    # Django 3rd Party Modules ( installed via pip )
    'django_nose',
    'django_extensions',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
