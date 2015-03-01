import os
from yebimom.settings.partials.application import BASE_DIR, PROJECT_ROOT


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Serving the site and your static files from the same server
# https://docs.djangoproject.com/en/1.7/howto/static-files/deployment/#serving-the-site-and-your-static-files-from-the-same-server
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


# This setting defines the additional locations the staticfiles app will
# traverse if the FileSystemFinder finder is enabled
# https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(PROJECT_ROOT, 'components'),
)
