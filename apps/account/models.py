from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from model_utils.models import TimeStampedModel
from utils.models import UUIDModel


# Create your models here.
class EmailUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel, UUIDModel):
    # 属性管理
    username = models.CharField(max_length=32, unique=True, verbose_name='用户名')
    cn_name = models.CharField(
        verbose_name='中文名称', max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    email = models.EmailField(max_length=64, unique=True, verbose_name='邮箱地址')
    wxid = models.CharField(max_length=32, unique=True, verbose_name='微信号')

    # 状态管理
    is_staff = models.BooleanField(default=True, verbose_name='工作人员')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')

    objects = EmailUserManager()
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone', 'wxid']

    class Meta:
        ordering = ['-created']
        verbose_name_plural = verbose_name = '1 - 🙍‍♂️ 用户模型'

    def __str__(self):
        return self.email

    def get_full_name(self) -> str:
        return self.cn_name or self.username

    def get_short_name(self) -> str:
        return self.username
