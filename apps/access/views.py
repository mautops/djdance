from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from access.authentications import TokenAuthentication
from access.models import DataSource, AccessToken
from access.serializers import DataSourceSerializer, AccessTokenSerializer


class DataSourceViewSet(ModelViewSet):
    queryset = DataSource.objects.all()

    authentication_classes = [TokenAuthentication,
                              BasicAuthentication, SessionAuthentication]
    serializer_class = DataSourceSerializer


class AccessTokenViewSet(ModelViewSet):
    queryset = AccessToken.objects.all()

    authentication_classes = [TokenAuthentication,
                              BasicAuthentication, SessionAuthentication]
    serializer_class = AccessTokenSerializer
