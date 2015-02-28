from yebimom.settings.settings import *
import dj_database_url


# Parse database configuration from $DATABASE_URL
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
