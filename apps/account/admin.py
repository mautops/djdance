from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from account.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'cn_name', 'email', 'phone', 'wxid',
                    'is_staff', 'is_active', 'is_superuser', 'created', 'modified']
    fieldsets = [
        ('用户属性', {'fields': ('username', 'cn_name', 'email', 'phone', 'wxid')}),
        ('权限选择', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    ]
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'email', 'phone', 'cn_name']
    ordering = ['email']
    # add_form = UserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "phone", 'wxid', "password1", "password2"),
            },
        ),
    )


# admin.site.unregister(Group)
