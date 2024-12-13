from django.urls import path, include
from rest_framework.routers import SimpleRouter
from access.views import DataSourceViewSet, AccessTokenViewSet


router = SimpleRouter(trailing_slash=False)
router.register('datasource', DataSourceViewSet)
router.register('access', AccessTokenViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
