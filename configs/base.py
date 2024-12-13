import os
import sys
from datetime import timedelta
from configs.settings import *  # noqa

# language and timezone
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

ALLOWED_HOSTS = ['*']

# support app in apps
sys.path.append(f'{BASE_DIR}/apps')

# Third Party
INSTALLED_APPS += [
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'drf_yasg',
    'django_celery_beat',
    'django_celery_results',
]

# User Apps
INSTALLED_APPS += [
    'account',
    'access',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'djDance.urls'

AUTH_USER_MODEL = 'account.MyUser'

STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
STATIC_URL = 'static/'

# whitenoise
WHITENOISE_KEEP_ONLY_HASHED_FILES = True
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# DJANGO REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'utils.drf.pagination.CommonPageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1'],
    'VERSION_PARAM': 'version',
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=11),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER": "account.serializers.MyTokenObtainPairSerializer",
    "AUTH_TOKEN_CLASSES": [
        'account.authentication.CustonAccessToken',
    ],
}

LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(filename)s %(lineno)d %(funcName)s %(process)d %(thread)d %(message)s \n',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': LOGGING_LEVEL,
        'propagate': True,
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': LOGGING_LEVEL,
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': LOGGING_LEVEL,
            'propagate': True,
        },
        'django.server': {
            'handlers': ['console'],
            'level': LOGGING_LEVEL,
            'propagate': True,
        }
    }
}

# COR Headers
# !!! Change '*' to your domain in Production
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = ['http://*', 'https://*']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://']
