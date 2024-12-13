from configs.base import *  # noqa


# 秘钥，请妥善保存
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

# 消息队列
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


# !!! Comments out DATABASES if DO NOT Use Devcontainer
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USERNAME', 'postgres'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': os.environ.get('DB_PORT', 5432),
#         'OPTIONS': {
#             'options': '-c search_path=public'  # db schema
#         }
#     },
# }
