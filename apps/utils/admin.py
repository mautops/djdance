from django.utils.html import format_html
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


class MyMPTTModelAdmin(MPTTModelAdmin):
    list_display_links = ['mptt_indent_field']

    @admin.display(boolean=False, description='title')
    def mptt_indent_field(self, instance):
        return format_html('<div style="text-indent:{}px">{}</div>', instance.level * 20, "↳ " + instance.title)

    def get_queryset(self, request):
        # 使用 select_related 和 prefetch_related 优化查询
        qs = super().get_queryset(request)
        return qs.select_related('parent').prefetch_related('children')
