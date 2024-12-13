from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from access.models import AccessToken, DataSource


class TokenAuthentication(BaseAuthentication):
    """ 验证项目绑定账号的 Token 是否有效 """
    keyword = 'token'

    def get_token(self, request):
        """
        从 http 请求头或 POST 数据中获取认证秘钥
        todo 待添加从 post 数据获取秘钥
        """
        # 从 URL 获取 Token 信息
        token = request.query_params.get(self.keyword)
        if token:
            return token

        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            raise AuthenticationFailed(
                'no Authenticate Token found in headers')

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise AuthenticationFailed(msg)

        return token

    def authenticate(self, request):
        token = self.get_token(request)

        try:
            token = AccessToken.objects.get(token=token)
        except AccessToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

        if not token.owner.is_active:
            raise AuthenticationFailed('User inactive or deleted.')

        try:
            if token.is_effective and token.is_active:
                return token.owner, token
            else:
                raise AuthenticationFailed('token not belong to this project')
        except (DataSource.DoesNotExist, DataSource.MultipleObjectsReturned):
            raise AuthenticationFailed(
                'no project registered or project registered more then one')
