web: gunicorn --pythonpath yebimom/ --bind :5000 --workers=3 yebimom.wsgi
worker: celery --workdir=yebimom/ --app=yebimom.celery:app --concurrency=3 worker
flower: celery --workdir=yebimom/ --app=yebimom.celery:app flower
