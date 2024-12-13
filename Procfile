web: gunicorn
beat: celery -A djDancer beat -l DEBUG
worker: celery -A djDancer worker -l INFO