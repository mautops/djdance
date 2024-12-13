from django.contrib import admin
from access.models import DataSource, AccessToken


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'label', 'type', 'created', 'modified']
    list_filter = ['is_active']
    search_fields = ['title', 'label']
    fieldsets = [
        ('属性字段', {'fields': ('title', 'label', 'type')}),
        ('状态字段', {'fields': ('is_active',)}),
    ]


@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ['title', 'ds', 'token', 'owner', 'is_active',
                    'start', 'end', 'created', 'modified']
    list_filter = ['is_active', ]
    search_fields = ['title', 'token']
    autocomplete_fields = ['ds', 'owner']
    fieldsets = [
        ('属性字段', {'fields': ('token', 'title')}),
        ('选择字段', {'fields': ('owner', 'ds')}),
        ('生效时间', {'fields': ('start', 'end')}),
        ('状态字段', {'fields': ('is_active',)}),
    ]
