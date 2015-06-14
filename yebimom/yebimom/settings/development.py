from yebimom.settings import *


INSTALLED_APPS += (
    # Django 3rd Party Modules ( installed via pip )
    'django_nose',
    'django_extensions',
    'debug_toolbar',
    'rest_framework_swagger',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
