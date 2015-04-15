# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
import os
from yebimom.settings.partials.application import BASE_DIR
from django.utils.translation import ugettext_lazy as _


LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('ko', _('Korean')),
    ('en', _('English')),
    ('zh-cn', _('Simplified Chinese')),
    ('zh-tw', _('Traditional Chinese')),
)
