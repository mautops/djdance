from configs.base import *  # noqa

# !!! Uncomment this if you want to use Sentry
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration


# !!! Change to your secret key in Production
SECRET_KEY = os.environ.get('SECRET_KEY')

# !!! Close Debug Mode in Production
DEBUG = False

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', 5432),
        'OPTIONS': {
            'options': '-c search_path=public'
        }
    },
}

# !!! Uncomment this if you want to use Sentry
# sdn = os.environ.get("SENTRY_SDN")
# sentry_sdk.init(
#     dsn=f"https://{sdn}@sentry.xxx.com",        # !!!Change Sentry Server in Production
#     integrations=[DjangoIntegration()],
#     environment="product",
#     release="v0.0.1",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,

#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )
