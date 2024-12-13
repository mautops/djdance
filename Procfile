web: gunicorn
beat: celery -A djDance beat -l DEBUG
worker: celery -A djDance worker -l INFO