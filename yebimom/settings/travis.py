# -*- coding: utf-8 -*-

from yebimom.settings.development import *

"""
개발환경에서는 로컬 폴더를 File Storage, Staticfiles Storage 로 사용한다.
다만, 트래비스에서 테스트가 통과하면, ./manage.py collectstatic 명령어를 통해서
실제 CDN ( S3 + CloudFront )에 데이터가 업로드 되어야한다.
"""

# https://docs.djangoproject.com/en/1.7/ref/settings/#default-file-storage
# https://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


# Setting for AWS

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
