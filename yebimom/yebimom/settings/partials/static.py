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
    os.path.join(PROJECT_ROOT, 'managements/components'),
)


# django-pipeline
# https://django-pipeline.readthedocs.org/en/latest/installation.html

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.closure.ClosureCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_CLOSURE_BINARY = '/usr/local/bin/closure-compiler'


PIPELINE_JS = {
    'vendor': {
        'source_filenames': (
            'js/underscore.min.js',
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
            'js/jquery-cookie.js',
            'js/bootstrap.min.js',
        ),
        'output_filename': 'js/vendor.min.js',
    },
    'yebimom': {
        'source_filenames': (
            'js/yebimom.js',
            'js/centers/*.js',
        ),
        'output_filename': 'js/yebimom.min.js'
    },
    'managements': {
        'source_filenames': (
            'managements/js/jquery-2.1.1.js',
            'managements/js/bootstrap.min.js',
            'managements/js/plugins/metisMenu/jquery.metisMenu.js',
            'managements/js/plugins/slimscroll/jquery.slimscroll.min.js',

            'managements/js/inspinia.js',
            'managements/js/plugins/pace/pace.min.js',

            'js/highcharts.min.js',
            'js/highcharts/data.min.js',
            'js/highcharts/exporting.min.js',
        ),
        'output_filename': 'js/managements.min.js'
    }
}

PIPELINE_CSS = {
    'vendor': {
        'source_filenames': (
            'css/bootstrap.min.css',
            'css/font-awesome.min.css',
            'css/jquery-ui-smoothness.min.css',
        ),
        'output_filename': 'css/vendor.min.css'
    },
    'yebimom': {
        'source_filenames': (
            'css/yebimom.css',
        ),
        'output_filename': 'css/yebimom.min.css'
    },
    'managements': {
        'source_filenames': (
            'managements/css/bootstrap.min.css',
            'managements/font-awesome/css/font-awesome.css',
            'managements/css/animate.css',
            'managements/css/style.css',
        ),
        'output_filename': 'css/managements.min.css'
    },
}
