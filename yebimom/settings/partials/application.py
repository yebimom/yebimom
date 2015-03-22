# Application definition

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)


INSTALLED_APPS = (
    # Django Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # Django 3rd Party Modules ( installed via pip )
    'social.apps.django_app.default',
    'storages',
    'imagekit',
    'rest_framework',
    'robots',

    # Yebimom Apps
    'users',
    'centers',
    'events',
    'reviews'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # Django Default
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    # Django Customs
    "django.core.context_processors.request",

    # Python Social Auth Custom TEMPLATE_CONTEXT_PROCESSORS
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',

    # Yebimom Customs
    'yebimom.context_processors.google_analytics',
)

ROOT_URLCONF = 'yebimom.urls'

WSGI_APPLICATION = 'yebimom.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

HASHIDS_USER_PROFILE_SALT = os.environ['HASHIDS_USER_PROFILE_SALT']
HASHIDS_CENTER_SALT = os.environ['HASHIDS_CENTER_SALT']

SITE_ID = 1

GOOGLE_ANALYTICS_TRACKING_ID = os.environ['GOOGLE_ANALYTICS_TRACKING_ID']
