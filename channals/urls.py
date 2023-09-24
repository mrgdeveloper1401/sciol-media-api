from rest_framework import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import include, path
from . import views


# router = SimpleRouter()
router = DefaultRouter()
router.register(r'channels', views.ChannalViewSet)

app_name = 'channals'
urlpatterns = [
    path('', include(router.urls))
] + router.urls