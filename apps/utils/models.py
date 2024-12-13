"""自定义通用模型字段"""
import uuid
from django.conf import settings
from django.db import models
from django.contrib import admin
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class MyMPTTModel(MPTTModel):
    title = models.CharField(verbose_name='标题', max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class Meta:
        abstract = True

    class MPTTMeta:
        order_insertion_by = ['level', 'created']

    def __str__(self) -> str:
        return self.title

    @admin.display(boolean=True, description='Root')
    def is_root(self):
        return self.parent is None


def get_default_uuid() -> str:
    """生成uuid
    """
    return str(uuid.uuid4().hex)


class TokenModel(models.Model):
    """use token as primary key
    """
    token = models.CharField(
        verbose_name='秘钥 Token', default=get_default_uuid, max_length=32, auto_created=True, unique=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """use uuid as primary key
    """
    id = models.CharField(primary_key=True, auto_created=True, editable=False,
                          default=get_default_uuid, unique=True, max_length=32)

    class Meta:
        abstract = True


class OwnerModel(models.Model):
    """add owner field to model
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name='所有者', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class EnableModel(models.Model):
    """add is_enabled field to model
    """
    is_enabled = models.BooleanField(verbose_name='启用', default=True)

    class Meta:
        abstract = True


class DateTimeFramedModel(models.Model):
    """add start&end field to model, provide is_effective method
    """
    start = models.DateTimeField(verbose_name='start', null=True, blank=True)
    end = models.DateTimeField(verbose_name='end', null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def is_effective(self) -> bool:
        """
        检测时间窗口是否生效
        @return: bool
        """
        from datetime import datetime

        now = datetime.now()

        start = self.start or now
        end = self.end or now

        if start <= now <= end:
            return True
        return False


class TimeStampedModel(models.Model):
    """An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """
    # 兼容天舟云
    created = models.DateTimeField(verbose_name='created', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='modified', auto_now=True)

    class Meta:
        abstract = True


class TimeFramedModel(models.Model):
    """add start&end field to model, provide is_effective method
    """
    start = models.DateTimeField(
        verbose_name='开始', blank=True, null=True)
    end = models.DateTimeField(
        verbose_name='结束', blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def is_effective(self) -> bool:
        """
        检测时间窗口是否生效
        @return: bool
        """
        from time import time

        start = self.start or time()
        end = self.end or time()

        if start <= time() <= end:
            return True
        return False


class ExtraModel(models.Model):
    """add extra field to model
    """
    extra = models.TextField(verbose_name='额外数据', blank=True, null=True)

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    """add is_active field to model
    """
    is_active = models.BooleanField(verbose_name='是否启用', default=True)

    class Meta:
        abstract = True

    def delete(self, using=None, soft=True, *args, **kwargs):
        if soft:
            self.is_active = False
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)
