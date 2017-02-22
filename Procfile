web: gunicorn config.wsgi:application
worker: celery worker --app=canto.taskapp --loglevel=info
