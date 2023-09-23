from rest_framework import routers
from rest_framework.routers import SimpleRouter
from django.urls import include, path
from . import views


router = SimpleRouter()
router.register(r'channels', views.ChannalViewSet, basename='channal')

app_name = 'channal'
urlpatterns = [
    path('', include(router.urls))
] + router.urls