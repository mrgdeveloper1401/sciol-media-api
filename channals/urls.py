from rest_framework import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import include, path
from . import views


# router = SimpleRouter()
router = DefaultRouter()
router.register(r'channels', views.ChannalViewSet, basename='channal')


urlpatterns = [
    path('', include(router.urls))
] + router.urls