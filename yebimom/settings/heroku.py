from yebimom.settings.settings import *


# partials/development.py

DEBUG = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [".herokuapp.com", ".yebimom.com"]


# partials/static.py

# Serving static files from a cloud service or CDN
# https://docs.djangoproject.com/en/1.7/howto/static-files/deployment/#serving-static-files-from-a-cloud-service-or-cdn
STATIC_URL = '/static/'
# STATIC_URL = 'https://cdn.yebimom.com/'
