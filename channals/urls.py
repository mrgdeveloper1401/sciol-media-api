from rest_framework import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import include, path
from . import views


# router = SimpleRouter()
router = DefaultRouter()
router.register(r'channel', views.ChannalViewSet, basename='channal')


urlpatterns = [
    path('v1/', include(router.urls))
] + router.urls