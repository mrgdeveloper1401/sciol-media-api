from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include
from . import views


router = DefaultRouter
router.register('ufollow', views.RelationUserViewSet, basename='unf')

urlpatterns = [
    path('', include(router.urls)),
    
] + router.urls
