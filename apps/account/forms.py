from django.contrib.auth.forms import BaseUserCreationForm
from account.models import MyUser


class UserCreationForm(BaseUserCreationForm):
    # 用户创建表单
    class Meta:
        model = MyUser
        fields = '__all__'
