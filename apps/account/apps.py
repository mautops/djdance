from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    label = 'account'
    verbose_name = '>>> 1. 用户认证'
