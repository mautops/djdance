import re
from typing import Any, Dict, AnyStr
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from account.models import MyUser
from urllib.parse import urljoin, quote


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        data['status'] = 'ok'
        data['state'] = 'drfjwt'
        return data


class MessageActionSerializer(serializers.Serializer):
    message = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'cn_name', 'email',
                  'phone', 'avatar']

    def get_avatar(self, obj: MyUser) -> str:
        base = 'https://api.multiavatar.com/'
        return urljoin(base, f'{quote(obj.email)}.png')


class SyncUserSerializer(serializers.Serializer):
    # 使用Serializer校验机制，但使用自定义方法校验字段值，通过设置default用于标识字段非必填项
    username = serializers.CharField(
        allow_blank=True, allow_null=True, required=False)
    cn_name = serializers.CharField(
        allow_blank=True, allow_null=True, required=False)
    phone = serializers.CharField(
        allow_blank=True, allow_null=True, required=False)
    email = serializers.CharField(
        allow_blank=True, allow_null=True, required=False)
    wx = serializers.CharField(
        allow_blank=True, allow_null=True, required=False)
    roles = serializers.CharField(
        allow_blank=True, allow_null=True, required=False, default=None)

    def validate_email(self, value: AnyStr):
        """校验 email 字段是否为有效电子邮件地址

        Args:
            value (AnyStr): 传递email参数

        Returns:
            value (AnyStr): 返回email参数
        """
        # 正则表达式匹配更复杂的电子邮件格式，如果需要的话
        email_pattern = re.compile(
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not email_pattern.match(value):
            raise ValueError("email 字段不是有效的电子邮件地址")
        return value

    def validate_phone(self, value: AnyStr):
        """校验 phone 字段是否符合自定义的电话号码格式

        Args:
            value (AnyStr): 传递phone参数

        Returns:
            value (AnyStr): 返回phone参数
        """
        phone_pattern = re.compile(r'^\d{11}$')
        if not phone_pattern.match(value):
            raise ValueError("phone 字段不符合电话号码格式")
        return value

    def validate(self, data):
        """校验所有必须的字段是否存在。

        Args:
            data (Dict): 传递参数

        Returns:
            data (Dict): 返回参数
        """
        # 确保所有非 default=None 的字段都有值
        missing_fields = [
            field for field in self.fields if self.fields[field].default and not data.get(field)]

        if missing_fields:
            raise ValueError(f"缺少必要的字段: {', '.join(missing_fields)}")
        return data
