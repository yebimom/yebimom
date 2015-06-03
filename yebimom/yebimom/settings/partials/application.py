# Application definition

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.template.base import add_to_builtins

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

INSTALLED_APPS = (
    # Django 3rd Party Modules ( must set before django.contrib.admin )
    'grappelli',
    'modeltranslation',

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
    'rosetta',
    'pipeline',
    'corsheaders',
    'notifications',

    # Yebimom Apps
    'users',
    'centers',
    'events',
    'reviews',
    'managements',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
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

# Grapelli admin settings
GRAPPELLI_ADMIN_TITLE = 'Yebimom'

ROOT_URLCONF = 'yebimom.urls'

WSGI_APPLICATION = 'yebimom.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

HASHIDS_USER_PROFILE_SALT = os.environ['HASHIDS_USER_PROFILE_SALT']
HASHIDS_CENTER_SALT = os.environ['HASHIDS_CENTER_SALT']

SITE_ID = 1

GOOGLE_ANALYTICS_TRACKING_ID = os.environ['GOOGLE_ANALYTICS_TRACKING_ID']
NAVER_OPENAPI_MAP_API_KEY = os.environ['NAVER_OPENAPI_MAP_API_KEY']

# django cors headers

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)


# Mailgun Email delivery & authentication
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.environ['MAILGUN_ACCESS_KEY']
MAILGUN_SERVER_NAME = os.environ['MAILGUN_SERVER_NAME']


# API store SMS delivery
API_STORE_SMS_KEY = os.environ['API_STORE_SMS_KEY']
API_STORE_SMS_BASE_URL = os.environ['API_STORE_SMS_BASE_URL']
SMS_SEND_PHONE = os.environ['SMS_SEND_PHONE']


# Amazon Web Services ( AWS )
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

AWS_S3_CUSTOM_DOMAIN = 'cdn.yebimom.com'
AWS_S3_URL_PROTOCOL = 'https'


# Load template tags to All template
add_to_builtins('django.templatetags.i18n')
