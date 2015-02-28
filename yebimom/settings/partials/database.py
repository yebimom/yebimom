import dj_database_url


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config()
