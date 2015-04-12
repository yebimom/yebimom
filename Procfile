web: gunicorn --pythonpath yebimom/ yebimom.wsgi
worker: celery --workdir=yebimom/ --app=yebimom.celery:app worker
