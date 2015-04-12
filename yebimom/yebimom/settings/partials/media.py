import os
from yebimom.settings.partials.application import PROJECT_ROOT


# Media files ( Images, User Uploaded files )
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
