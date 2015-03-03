import os
import dj_database_url


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL
    )
}
