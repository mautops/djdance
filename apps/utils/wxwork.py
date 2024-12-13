import os
import logging
from typing import Dict
import requests

logger = logging.getLogger(__name__)


class WxworkError(Exception):
    """企业微信异常"""


class Wxwork(object):
    BASE_URL = 'https://qyapi.weixin.qq.com/cgi-bin'

    def __init__(self, corp_id: str, secret: str, agent_id: str) -> None:
        self.corp_id = corp_id
        self.secret = secret
        self.agent_id = agent_id

    def get_access_token(self) -> str:
        """get access token

        Raises:
            WxworkError: get access token error

        Returns:
            str: access token
        """
        response = requests.get(url=f"{self.BASE_URL}/gettoken",
                                params={
                                    'corpid': self.corp_id,
                                    'corpsecret': self.secret
                                }).json()
        if response['errcode'] != 0 or response['errmsg'] != 'ok':
            raise WxworkError(
                f'get wxwork access token error: {response["errmsg"]}')
        access_token = response['access_token']
        logger.info(f'get wxwork access token success: {access_token}')
        return access_token

    def get_user_id(self, code: str) -> str:
        """get wxwork user id

        Args:
            code (str): wxwork code

        Raises:
            WxworkError: get user info error

        Returns:
            str: wxwork user id
        """
        access_token = self.get_access_token()
        response = requests.get(url=f"{self.BASE_URL}/auth/getuserinfo",
                                params={
                                    'access_token': access_token,
                                    'code': code
                                }).json()
        if response['errcode'] != 0 or response['errmsg'] != 'ok':
            raise WxworkError(
                f'get wxwork user id error: {response["errmsg"]}')
        logger.info(f'get wxwork user id success: {response}')
        return response['userid']

    def get_user(self, user_id: str) -> Dict:
        """get user by id

        Args:
            user_id (str): user id

        Returns:
            Dict: user info
        """
        access_token = self.get_access_token()
        response = requests.get(url=f"{self.BASE_URL}/user/get",
                                params={
                                    'access_token': access_token,
                                    'userid': user_id
                                }).json()
        if response['errcode'] != 0 or response['errmsg'] != 'ok':
            raise WxworkError(f'获取企业微信用户信息异常: {response["errmsg"]}')
        logger.info(f'获取企业微信用户信息成功: {response}')
        return response


wxwork = Wxwork(corp_id=os.environ.get('WECHAT_CORP_ID'),
                secret=os.environ.get('WECHAT_CORP_SECRET'),
                agent_id=os.environ.get('WECHAT_AGENT_ID'))
