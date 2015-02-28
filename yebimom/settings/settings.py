"""
Django settings for yebimom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from yebimom.settings.partials.database import *
from yebimom.settings.partials.static import *
from yebimom.settings.partials.application import *
from yebimom.settings.partials.development import *
from yebimom.settings.partials.international import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
