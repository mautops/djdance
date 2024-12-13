from rest_framework.serializers import ModelSerializer
from access.models import DataSource, AccessToken


class DataSourceSerializer(ModelSerializer):
    class Meta:
        model = DataSource
        fields = '__all__'


class AccessTokenSerializer(ModelSerializer):
    class Meta:
        model = AccessToken
        fields = '__all__'
