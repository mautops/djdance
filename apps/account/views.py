import logging
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from account.models import MyUser
from account.serializers import UserSerializer
from utils.constants import ACTION_RESPONSE, ACTION_CLOSE


logger = logging.getLogger(__name__)


class UserViewSet(ModelViewSet):
    """用户模型操作"""
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username', 'email', 'phone']

    @action(methods=['GET'], detail=False, url_path='current')
    def get_current_user(self, request, **kwargs):
        """获取当前登录用户"""
        if not request.user or request.user.is_anonymous:
            return Response({"data": None}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(request.user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def logout(self, request, *args, **kwargs):
        logout(request)  # 用户登出
        response = HttpResponseRedirect('/')
        response.delete_cookie(key='JWT')
        return response
