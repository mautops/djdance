from django.db import models
from access.constants import DSTYPES
from utils.models import ActiveModel, DateTimeFramedModel, OwnerModel, TimeStampedModel, UUIDModel, TokenModel


class DataSource(TimeStampedModel, ActiveModel, UUIDModel):
    title = models.CharField(
        verbose_name='数据源', max_length=50, db_comment='用户自定义的')
    label = models.CharField(verbose_name='标示符', max_length=50, unique=True)
    type = models.CharField(verbose_name='类型', max_length=32, choices=DSTYPES)

    class Meta:
        verbose_name_plural = verbose_name = '1 - 🫧 数据源管理'

    def __str__(self):
        return self.title


class AccessToken(TimeStampedModel, DateTimeFramedModel, ActiveModel, OwnerModel, UUIDModel, TokenModel):
    title = models.CharField(
        verbose_name='秘钥名称', max_length=50, db_comment='秘钥名称')
    ds = models.ForeignKey(DataSource, verbose_name='数据源',
                           on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = '2 - 🔑 密钥认证'

    def __str__(self):
        return self.title
