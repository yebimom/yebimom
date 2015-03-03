from yebimom.settings.settings import *
import os


INSTALLED_APPS += (
    # Django 3rd Party Modules ( installed via pip )
    'django_nose',
    'django_extensions',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SECRET_KEY = os.environ['SECRET_KEY']
