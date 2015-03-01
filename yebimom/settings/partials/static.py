import os
from yebimom.settings.partials.application import BASE_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Serving the site and your static files from the same server
# https://docs.djangoproject.com/en/1.7/howto/static-files/deployment/#serving-the-site-and-your-static-files-from-the-same-server
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
